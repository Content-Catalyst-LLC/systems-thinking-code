"""Analyze stock depletion and restoration balance."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with (DATA / "indicators.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            stock = float(row["stock_level"])
            buffer = float(row["buffer_level"])
            pressure = float(row["pressure"])
            rows.append({
                "month": row["month"],
                "domain": row["domain"],
                "pressure": pressure,
                "stock_level": stock,
                "buffer_level": buffer,
                "depletion_index": round((pressure + (1 - stock) + (1 - buffer)) / 3, 3),
            })
    out_path = OUT / "stock_depletion_analysis.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
