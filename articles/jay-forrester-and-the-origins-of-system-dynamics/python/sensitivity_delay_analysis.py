#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "delay_assumption_sensitivity_notes.csv"


def main() -> None:
    path = RAW / "synthetic_delay_assumptions.csv"
    if not path.exists():
        print("Skipping delay sensitivity notes; missing synthetic_delay_assumptions.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []
    for row in rows:
        delay = int(row["delay_periods"])
        output.append({
            "delay_id": row["delay_id"],
            "delay_type": row["delay_type"],
            "delay_periods": delay,
            "affected_stock_or_flow": row["affected_stock_or_flow"],
            "sensitivity_class": "high" if delay >= 9 else "moderate" if delay >= 5 else "low",
            "risk_if_ignored": row["risk_if_ignored"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
