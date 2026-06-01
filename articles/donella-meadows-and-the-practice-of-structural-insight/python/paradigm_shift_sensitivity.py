#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "meadows_structural_insight_timeseries.csv"
OUT = TABLES / "paradigm_shift_sensitivity.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping paradigm shift sensitivity; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_leverage = mean(float(r["leverage_quality"]) for r in subset)
        avg_insight = mean(float(r["structural_insight_score"]) for r in subset)
        avg_overshoot = mean(float(r["overshoot_index"]) for r in subset)
        output.append({
            "scenario": scenario,
            "average_leverage_quality": round(avg_leverage, 3),
            "average_structural_insight_score": round(avg_insight, 3),
            "average_overshoot_index": round(avg_overshoot, 3),
            "diagnostic": "deep leverage signal" if avg_leverage >= 60 and avg_insight >= 60 else "leverage remains too shallow",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
