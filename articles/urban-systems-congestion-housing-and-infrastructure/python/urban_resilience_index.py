#!/usr/bin/env python3
"""Summarize urban resilience and rank scenarios across system dimensions."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "urban_systems_timeseries.csv"
OUTPUT = TABLES / "urban_resilience_rankings.csv"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing {INPUT}. Run urban_systems_model.py first.")
    with INPUT.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output: list[dict[str, object]] = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        final = subset[-1]
        composite = mean(
            float(row["urban_resilience_index"]) * 0.40
            + float(row["access_index"]) * 0.20
            + float(row["affordability_index"]) * 0.20
            + float(row["infrastructure_condition"]) * 0.20
            for row in subset
        )
        output.append({
            "scenario": scenario,
            "final_urban_resilience_index": final["urban_resilience_index"],
            "final_access_index": final["access_index"],
            "final_affordability_index": final["affordability_index"],
            "final_infrastructure_condition": final["infrastructure_condition"],
            "mean_composite_resilience_score": round(composite, 3),
        })

    output.sort(key=lambda row: float(row["mean_composite_resilience_score"]), reverse=True)
    for idx, row in enumerate(output, start=1):
        row["rank"] = idx

    fieldnames = ["rank"] + [key for key in output[0].keys() if key != "rank"]
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
