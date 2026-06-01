#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "meadows_structural_insight_timeseries.csv"
OUT = TABLES / "overshoot_delay_diagnostics.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping overshoot delay diagnostics; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_delay_gap = mean(abs(float(r["resource_stock"]) - float(r["perceived_resource_stock"])) for r in subset)
        peak_overshoot = max(float(r["overshoot_index"]) for r in subset)
        min_resource = min(float(r["resource_stock"]) for r in subset)
        output.append({
            "scenario": scenario,
            "average_resource_perception_gap": round(avg_delay_gap, 3),
            "peak_overshoot_index": round(peak_overshoot, 3),
            "minimum_resource_stock": round(min_resource, 3),
            "diagnostic": "overshoot and delayed feedback risk" if peak_overshoot >= 35 or avg_delay_gap >= 20 else "overshoot risk comparatively contained",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
