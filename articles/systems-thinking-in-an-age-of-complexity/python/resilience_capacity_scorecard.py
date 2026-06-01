#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "resilience_capacity_scorecard.csv"


def main() -> None:
    path = RAW / "synthetic_resilience_capacity.csv"
    if not path.exists():
        print("Skipping resilience capacity scorecard; missing synthetic_resilience_capacity.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        score = (
            float(row["redundancy"]) * 20.0
            + float(row["modularity"]) * 18.0
            + float(row["learning_capacity"]) * 24.0
            + float(row["response_variety"]) * 22.0
            + float(row["trust"]) * 16.0
        )
        output.append({
            "domain": row["domain"],
            "resilience_capacity_score": round(score, 3),
            "redundancy": row["redundancy"],
            "modularity": row["modularity"],
            "learning_capacity": row["learning_capacity"],
            "response_variety": row["response_variety"],
            "trust": row["trust"],
            "diagnostic": row["diagnostic"],
            "priority_class": "high redesign priority" if score < 55 else "strengthen and monitor",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
