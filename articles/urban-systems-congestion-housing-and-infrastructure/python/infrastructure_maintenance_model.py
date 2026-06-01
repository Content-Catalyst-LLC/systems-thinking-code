#!/usr/bin/env python3
"""Assess infrastructure condition, maintenance backlog, and climate stress."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "urban_systems_timeseries.csv"
OUTPUT = TABLES / "infrastructure_maintenance_diagnostics.csv"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing {INPUT}. Run urban_systems_model.py first.")
    with INPUT.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output: list[dict[str, object]] = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        first, final = subset[0], subset[-1]
        min_condition = min(float(row["infrastructure_condition"]) for row in subset)
        condition_change = float(final["infrastructure_condition"]) - float(first["infrastructure_condition"])
        average_climate_risk = mean(float(row["climate_risk_index"]) for row in subset)
        output.append({
            "scenario": scenario,
            "initial_infrastructure_condition": first["infrastructure_condition"],
            "final_infrastructure_condition": final["infrastructure_condition"],
            "minimum_infrastructure_condition": round(min_condition, 3),
            "condition_change": round(condition_change, 3),
            "average_climate_risk_index": round(average_climate_risk, 3),
            "diagnostic": "maintenance backlog risk" if min_condition < 40 else "condition comparatively stable",
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
