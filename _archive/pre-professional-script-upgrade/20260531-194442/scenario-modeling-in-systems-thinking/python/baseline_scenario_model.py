#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"

@dataclass
class State:
    year: int
    scenario_id: str
    capacity: float
    demand: float
    trust: float
    risk: float

def load_assumptions() -> dict[str, dict[str, float]]:
    path = DATA / "synthetic_scenario_assumptions.csv"
    with path.open(newline="", encoding="utf-8") as f:
        rows = csv.DictReader(f)
        return {
            row["scenario_id"]: {
                "demand_growth": float(row["demand_growth"]),
                "capacity_growth": float(row["capacity_growth"]),
                "trust_change": float(row["trust_change"]),
                "shock_multiplier": float(row["shock_multiplier"]),
            }
            for row in rows
        }

def simulate(scenario_id: str, years: int = 10) -> list[State]:
    assumptions = load_assumptions()[scenario_id]
    state = State(0, scenario_id, 100.0, 95.0, 70.0, 30.0)
    results = [state]

    for year in range(1, years + 1):
        capacity = state.capacity * (1 + assumptions["capacity_growth"])
        demand = state.demand * (1 + assumptions["demand_growth"]) * assumptions["shock_multiplier"]
        pressure = max(demand - capacity, 0.0)
        trust = max(0.0, min(100.0, state.trust + assumptions["trust_change"] * 100 - pressure * 0.05))
        risk = max(0.0, min(100.0, state.risk + pressure * 0.08 - (capacity - demand) * 0.02))
        state = State(year, scenario_id, capacity, demand, trust, risk)
        results.append(state)

    return results

def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    rows = []
    for scenario_id in load_assumptions():
        rows.extend(simulate(scenario_id))

    out = OUTPUTS / "baseline_scenario_model_outputs.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["scenario_id", "year", "capacity", "demand", "trust", "risk"])
        for row in rows:
            writer.writerow([row.scenario_id, row.year, round(row.capacity, 2), round(row.demand, 2), round(row.trust, 2), round(row.risk, 2)])

    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
