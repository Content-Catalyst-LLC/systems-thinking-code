#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "cybernetics_systems_timeseries.csv"
OUT = TABLES / "adaptive_regulation_scorecard.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping adaptive regulation scorecard; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_regulation = mean(float(r["regulation_quality"]) for r in subset)
        avg_learning = mean(float(r["learning_capacity"]) for r in subset)
        avg_accountability = mean(float(r["accountability_index"]) for r in subset)
        avg_variety_gap = mean(float(r["variety_gap"]) for r in subset)
        score = avg_regulation * 0.34 + avg_learning * 0.24 + avg_accountability * 0.28 - avg_variety_gap * 0.14
        output.append({
            "scenario": scenario,
            "adaptive_regulation_score": round(score, 3),
            "average_regulation_quality": round(avg_regulation, 3),
            "average_learning_capacity": round(avg_learning, 3),
            "average_accountability_index": round(avg_accountability, 3),
            "average_variety_gap": round(avg_variety_gap, 3),
            "diagnostic": "strong adaptive regulation" if score >= 60 else "adaptive regulation needs redesign",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
