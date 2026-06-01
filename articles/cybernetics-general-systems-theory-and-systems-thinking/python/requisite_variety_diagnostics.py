#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "requisite_variety_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_variety_diagnostics.csv"
    if not path.exists():
        print("Skipping requisite variety diagnostics; missing synthetic_variety_diagnostics.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        gap = float(row["variety_gap"])
        output.append({
            "domain": row["domain"],
            "disturbance_variety": round(float(row["disturbance_variety"]), 3),
            "response_variety": round(float(row["response_variety"]), 3),
            "variety_gap": round(gap, 3),
            "gap_class": "high variety gap" if gap >= 0.30 else "moderate variety gap" if gap >= 0.10 else "contained variety gap",
            "diagnostic": row["diagnostic"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
