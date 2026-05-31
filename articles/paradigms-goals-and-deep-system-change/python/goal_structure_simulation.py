#!/usr/bin/env python3
"""Goal-structure simulation for paradigms, goals, and deep system change.

This script compares simple synthetic trajectories under different operating goals.
It is intentionally transparent and lightweight so readers can inspect every assumption.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class GoalScenario:
    name: str
    throughput_weight: float
    access_weight: float
    dignity_weight: float
    burden_penalty: float
    harm_penalty: float


def step(state: dict[str, float], scenario: GoalScenario) -> dict[str, float]:
    """Advance a toy system one time step under a goal structure."""
    throughput_push = 0.05 * scenario.throughput_weight
    access_repair = 0.07 * scenario.access_weight
    dignity_repair = 0.06 * scenario.dignity_weight
    burden_change = 0.04 * scenario.throughput_weight - 0.07 * scenario.burden_penalty
    harm_change = 0.03 * scenario.throughput_weight - 0.06 * scenario.harm_penalty

    return {
        "throughput": min(1.0, max(0.0, state["throughput"] + throughput_push)),
        "access": min(1.0, max(0.0, state["access"] + access_repair - 0.02 * state["burden"])),
        "dignity": min(1.0, max(0.0, state["dignity"] + dignity_repair - 0.03 * state["harm"])),
        "burden": min(1.0, max(0.0, state["burden"] + burden_change)),
        "harm": min(1.0, max(0.0, state["harm"] + harm_change)),
    }


def score(state: dict[str, float]) -> float:
    """Composite systems score: high access/dignity/throughput, low burden/harm."""
    return round((state["throughput"] + state["access"] + state["dignity"] + (1 - state["burden"]) + (1 - state["harm"])) / 5, 3)


def run_scenario(scenario: GoalScenario, years: int = 6) -> list[dict[str, object]]:
    state = {"throughput": 0.70, "access": 0.52, "dignity": 0.42, "burden": 0.60, "harm": 0.50}
    rows: list[dict[str, object]] = []
    for year in range(years + 1):
        rows.append({"scenario": scenario.name, "year": year, **{k: round(v, 3) for k, v in state.items()}, "score": score(state)})
        state = step(state, scenario)
    return rows


def main() -> None:
    scenarios = [
        GoalScenario("narrow_throughput", 1.0, 0.1, 0.05, 0.1, 0.1),
        GoalScenario("access_and_dignity", 0.45, 0.9, 0.85, 0.8, 0.9),
        GoalScenario("resilience_and_repair", 0.35, 0.65, 0.7, 0.85, 0.95),
    ]
    rows: list[dict[str, object]] = []
    for scenario in scenarios:
        rows.extend(run_scenario(scenario))

    out = OUTPUT_DIR / "goal_structure_simulation.csv"
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
