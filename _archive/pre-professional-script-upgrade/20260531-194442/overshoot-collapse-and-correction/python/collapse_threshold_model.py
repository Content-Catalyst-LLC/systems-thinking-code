"""Collapse-threshold model for synthetic systems stocks."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with (DATA / "system_stocks.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            stock = float(row["initial_level"])
            threshold = float(row["critical_threshold"])
            margin = stock - threshold
            rows.append({
                "stock_id": row["stock_id"],
                "stock_name": row["stock_name"],
                "domain": row["domain"],
                "initial_level": stock,
                "critical_threshold": threshold,
                "resilience_margin": round(margin, 3),
                "risk_band": "high" if margin < 0.20 else "moderate" if margin < 0.35 else "lower",
            })

    out_path = OUT / "collapse_threshold_summary.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
