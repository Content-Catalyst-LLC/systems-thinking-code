#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "senge_learning_organization_timeseries.csv"
OUT = TABLES / "learning_capacity_sensitivity.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping learning capacity sensitivity; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_learning = mean(float(r["learning_capacity_score"]) for r in subset)
        avg_defensive = mean(float(r["defensive_routines_index"]) for r in subset)
        avg_feedback = mean(float(r["feedback_use_index"]) for r in subset)
        final = subset[-1]
        output.append({
            "scenario": scenario,
            "average_learning_capacity_score": round(avg_learning, 3),
            "average_defensive_routines_index": round(avg_defensive, 3),
            "average_feedback_use_index": round(avg_feedback, 3),
            "final_adaptive_capacity": final["adaptive_capacity"],
            "diagnostic": "learning loop dominates" if avg_learning > avg_defensive else "defensive loop dominates",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
