#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "open_system_exchange_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_open_system_exchanges.csv"
    if not path.exists():
        print("Skipping open-system exchange diagnostics; missing synthetic_open_system_exchanges.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        risk = row["externality_risk"].lower()
        priority = "boundary critique required" if risk == "high" else "boundary review recommended"
        output.append({
            "exchange_id": row["exchange_id"],
            "system_domain": row["system_domain"],
            "input_flow": row["input_flow"],
            "output_flow": row["output_flow"],
            "externality_risk": row["externality_risk"],
            "boundary_question": row["boundary_question"],
            "diagnostic": priority,
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
