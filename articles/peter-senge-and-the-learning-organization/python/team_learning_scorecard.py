#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "team_learning_scorecard.csv"


def main() -> None:
    path = RAW / "synthetic_feedback_events.csv"
    if not path.exists():
        print("Skipping team learning scorecard; missing synthetic_feedback_events.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []
    cumulative_revision = 0.0

    for row in rows:
        score = (
            float(row["feedback_quality"]) * 0.38
            + float(row["psychological_safety"]) * 0.34
            + float(row["decision_revision"]) * 0.28
        ) * 100.0
        cumulative_revision += float(row["decision_revision"])
        output.append({
            "event_id": row["event_id"],
            "period": row["period"],
            "event_type": row["event_type"],
            "team_learning_score": round(score, 3),
            "cumulative_decision_revision_signal": round(cumulative_revision, 3),
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
