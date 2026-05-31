"""Policy-resistance simulation for dynamic complexity examples.

Uses synthetic scenario parameters to show how intended policy effects can be
offset by compensating feedback, implementation lag, and boundary costs.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "synthetic_scenarios.csv"
OUT = ROOT / "outputs" / "tables" / "policy_resistance_summary.csv"


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    scenario_name: str
    policy_strength: float
    compensation_strength: float
    implementation_lag: int
    boundary_cost_weight: float


def load_scenarios(path: Path = DATA) -> list[Scenario]:
    with path.open(newline="") as f:
        return [
            Scenario(
                row["scenario_id"],
                row["scenario_name"],
                float(row["policy_strength"]),
                float(row["compensation_strength"]),
                int(row["implementation_lag"]),
                float(row["boundary_cost_weight"]),
            )
            for row in csv.DictReader(f)
        ]


def simulate(s: Scenario, months: int = 24) -> list[dict[str, float | int | str]]:
    outcome = 50.0
    boundary_cost = 0.0
    rows: list[dict[str, float | int | str]] = []
    for month in range(1, months + 1):
        active_policy = s.policy_strength if month > s.implementation_lag else 0.0
        compensation = s.compensation_strength * max(0.0, outcome - 50.0) / 50.0
        boundary_cost += s.boundary_cost_weight * active_policy * 0.7
        outcome += 3.0 * active_policy - 2.2 * compensation - 0.35 * boundary_cost
        rows.append(
            {
                "scenario_id": s.scenario_id,
                "scenario_name": s.scenario_name,
                "month": month,
                "active_policy": round(active_policy, 3),
                "compensation": round(compensation, 3),
                "boundary_cost": round(boundary_cost, 3),
                "system_outcome": round(outcome, 3),
            }
        )
    return rows


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, float | int | str]] = []
    for scenario in load_scenarios():
        rows.extend(simulate(scenario))
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
