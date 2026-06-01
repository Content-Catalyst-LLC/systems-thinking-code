#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "complex_adaptive_social_change_timeseries.csv"
OUT = TABLES / "transformation_momentum_scorecard.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping transformation scorecard; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        final = subset[-1]
        peak_momentum = max(float(r["transformation_momentum"]) for r in subset)
        avg_momentum = mean(float(r["transformation_momentum"]) for r in subset)
        output.append({
            "scenario": scenario,
            "final_momentum": final["transformation_momentum"],
            "peak_momentum": round(peak_momentum, 3),
            "average_momentum": round(avg_momentum, 3),
            "momentum_class": "transformational" if float(final["transformation_momentum"]) >= 60 else "emerging" if float(final["transformation_momentum"]) >= 40 else "fragile",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
