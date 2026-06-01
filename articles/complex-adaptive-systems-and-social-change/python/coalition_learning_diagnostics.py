#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "coalition_learning_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_learning_cycles.csv"
    if not path.exists():
        print("Skipping coalition learning diagnostics; missing synthetic_learning_cycles.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []
    cumulative_learning = 0.0

    for row in rows:
        score = (
            float(row["feedback_quality"]) * 0.32
            + float(row["participation_quality"]) * 0.30
            + float(row["institutional_memory"]) * 0.25
            + 0.13
        )
        cumulative_learning += score
        output.append({
            "cycle_id": row["cycle_id"],
            "period": row["period"],
            "learning_cycle_score": round(score * 100, 3),
            "cumulative_learning_signal": round(cumulative_learning * 100, 3),
            "adaptation_action": row["adaptation_action"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
