#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "transformation_leverage_scenarios.csv"


def main() -> None:
    path = RAW / "synthetic_transformation_levers.csv"
    if not path.exists():
        print("Skipping transformation leverage scenarios; missing synthetic_transformation_levers.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        score = (
            float(row["goal_change"]) * 28.0
            + float(row["rule_change"]) * 24.0
            + float(row["information_flow_change"]) * 22.0
            + float(row["power_change"]) * 26.0
        )
        output.append({
            "lever_id": row["lever_id"],
            "lever_name": row["lever_name"],
            "transformation_leverage_score": round(score, 3),
            "goal_change": row["goal_change"],
            "rule_change": row["rule_change"],
            "information_flow_change": row["information_flow_change"],
            "power_change": row["power_change"],
            "diagnostic": "deep leverage candidate" if score >= 70 else "moderate leverage candidate",
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
