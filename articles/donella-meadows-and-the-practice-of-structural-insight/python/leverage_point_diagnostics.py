#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "leverage_point_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_leverage_points.csv"
    if not path.exists():
        print("Skipping leverage diagnostics; missing synthetic_leverage_points.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        depth = int(row["relative_depth"])
        output.append({
            "leverage_id": row["leverage_id"],
            "leverage_name": row["leverage_name"],
            "leverage_level": row["leverage_level"],
            "relative_depth": depth,
            "example_intervention": row["example_intervention"],
            "diagnostic_question": row["diagnostic_question"],
            "structural_depth_class": "deep leverage" if depth >= 8 else "medium leverage" if depth >= 5 else "low leverage",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
