#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"

def main() -> None:
    with (DATA / "synthetic_scenario_assumptions.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    sensitivity_rows = []
    for row in rows:
        demand = float(row["demand_growth"])
        capacity = float(row["capacity_growth"])
        trust = float(row["trust_change"])
        shock = float(row["shock_multiplier"])
        sensitivity_rows.append({
            "scenario_id": row["scenario_id"],
            "demand_pressure_indicator": round(demand * shock - capacity, 4),
            "trust_direction": "improving" if trust > 0 else "declining" if trust < 0 else "stable",
            "sensitivity_priority": "high" if demand * shock - capacity > 0.04 else "medium",
        })

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    out = OUTPUTS / "scenario_sensitivity_workflow.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(sensitivity_rows[0].keys()))
        writer.writeheader()
        writer.writerows(sensitivity_rows)

    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
