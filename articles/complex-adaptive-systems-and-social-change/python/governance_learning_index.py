#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "complex_adaptive_social_change_timeseries.csv"
OUT = TABLES / "governance_learning_index.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping governance learning index; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        final = subset[-1]
        avg_learning = mean(float(r["learning_capacity_index"]) for r in subset)
        avg_legitimacy = mean(float(r["legitimacy_index"]) for r in subset)
        index = avg_learning * 0.42 + avg_legitimacy * 0.34 + float(final["institutional_response_index"]) * 0.24
        output.append({
            "scenario": scenario,
            "governance_learning_index": round(index, 3),
            "average_learning_capacity": round(avg_learning, 3),
            "average_legitimacy": round(avg_legitimacy, 3),
            "final_institutional_response": final["institutional_response_index"],
            "diagnostic": "strong learning governance" if index >= 60 else "governance learning needs reinforcement",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
