#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "five_disciplines_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_five_disciplines.csv"
    if not path.exists():
        print("Skipping five disciplines diagnostics; missing synthetic_five_disciplines.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        baseline = float(row["baseline_score"])
        target = float(row["target_score"])
        gap = target - baseline
        output.append({
            "discipline_id": row["discipline_id"],
            "discipline_name": row["discipline_name"],
            "baseline_score": round(baseline, 3),
            "target_score": round(target, 3),
            "development_gap": round(gap, 3),
            "priority_class": "high priority" if gap >= 38 else "moderate priority" if gap >= 25 else "watch",
            "diagnostic_question": row["diagnostic_question"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
