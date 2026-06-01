#!/usr/bin/env python3
"""Create displacement risk and access trade-off diagnostics."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "urban_systems_timeseries.csv"
OUTPUT = TABLES / "displacement_access_diagnostics.csv"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing {INPUT}. Run urban_systems_model.py first.")
    with INPUT.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output: list[dict[str, object]] = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        final = subset[-1]
        max_displacement = max(float(row["displacement_pressure"]) for row in subset)
        avg_access = mean(float(row["access_index"]) for row in subset)
        avg_affordability = mean(float(row["affordability_index"]) for row in subset)
        output.append({
            "scenario": scenario,
            "final_displacement_pressure": final["displacement_pressure"],
            "maximum_displacement_pressure": round(max_displacement, 3),
            "average_access_index": round(avg_access, 3),
            "average_affordability_index": round(avg_affordability, 3),
            "diagnostic": "anti-displacement safeguards needed" if max_displacement > 55 else "displacement pressure comparatively contained",
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
