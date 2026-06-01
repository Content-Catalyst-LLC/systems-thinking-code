#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "resilience_feedback_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_resilience_indicators.csv"
    if not path.exists():
        print("Skipping resilience diagnostics; missing synthetic_resilience_indicators.csv")
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
            "domain": row["domain"],
            "baseline_score": round(baseline, 3),
            "target_score": round(target, 3),
            "resilience_gap": round(gap, 3),
            "priority_class": "high priority" if gap >= 35 else "moderate priority" if gap >= 20 else "watch",
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
