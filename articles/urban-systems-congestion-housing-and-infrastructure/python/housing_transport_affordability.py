#!/usr/bin/env python3
"""Compute housing-transport-utility affordability diagnostics."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "urban_systems_timeseries.csv"
OUTPUT = TABLES / "housing_transport_affordability_diagnostics.csv"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing {INPUT}. Run urban_systems_model.py first.")
    with INPUT.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output: list[dict[str, object]] = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        final = subset[-1]
        average_total_burden = mean(
            float(row["housing_cost_index"]) * 0.45
            + float(row["transport_cost_index"]) * 0.35
            + float(row["utility_cost_index"]) * 0.20
            for row in subset
        )
        output.append({
            "scenario": scenario,
            "final_housing_cost_index": final["housing_cost_index"],
            "final_transport_cost_index": final["transport_cost_index"],
            "final_utility_cost_index": final["utility_cost_index"],
            "final_affordability_index": final["affordability_index"],
            "average_total_burden_index": round(average_total_burden, 3),
            "diagnostic": "affordability stress" if float(final["affordability_index"]) < 45 else "affordability comparatively stronger",
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
