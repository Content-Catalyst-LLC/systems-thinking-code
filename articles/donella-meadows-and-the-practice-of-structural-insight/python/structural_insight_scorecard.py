#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "meadows_structural_insight_timeseries.csv"
OUT = TABLES / "structural_insight_scorecard.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping structural insight scorecard; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        final = subset[-1]
        avg_score = mean(float(r["structural_insight_score"]) for r in subset)
        output.append({
            "scenario": scenario,
            "final_structural_insight_score": final["structural_insight_score"],
            "average_structural_insight_score": round(avg_score, 3),
            "final_resource_stock": final["resource_stock"],
            "final_trust_stock": final["trust_stock"],
            "final_resilience_capacity": final["resilience_capacity"],
            "score_class": "strong structural insight" if avg_score >= 60 else "partial structural insight" if avg_score >= 45 else "weak structural insight",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
