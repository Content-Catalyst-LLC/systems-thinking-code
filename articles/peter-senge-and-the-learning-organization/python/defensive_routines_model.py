#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "defensive_routines_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_defensive_routines.csv"
    if not path.exists():
        print("Skipping defensive routines diagnostics; missing synthetic_defensive_routines.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        intensity = float(row["intensity"])
        output.append({
            "routine_id": row["routine_id"],
            "routine_type": row["routine_type"],
            "intensity": round(intensity, 3),
            "learning_risk": row["learning_risk"],
            "suppression_score": round(intensity * 100, 3),
            "possible_countermeasure": row["possible_countermeasure"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
