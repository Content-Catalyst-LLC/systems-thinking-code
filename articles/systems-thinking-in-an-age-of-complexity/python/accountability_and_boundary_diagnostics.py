#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "accountability_boundary_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_accountability_indicators.csv"
    if not path.exists():
        print("Skipping accountability and boundary diagnostics; missing synthetic_accountability_indicators.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        baseline = float(row["baseline_score"])
        target = float(row["target_score"])
        gap = target - baseline
        output.append({
            "indicator_id": row["indicator_id"],
            "indicator_name": row["indicator_name"],
            "baseline_score": round(baseline, 3),
            "target_score": round(target, 3),
            "accountability_gap": round(gap, 3),
            "priority_class": "high priority" if gap >= 40 else "moderate priority",
            "notes": row["notes"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
