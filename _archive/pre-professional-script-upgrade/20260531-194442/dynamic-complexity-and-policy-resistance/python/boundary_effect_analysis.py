"""Boundary-effect analysis for externalized policy costs."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
COSTS = ROOT / "data" / "raw" / "synthetic_boundary_costs.csv"
OUT = ROOT / "outputs" / "tables" / "boundary_effect_summary.csv"


def discount_adjusted_cost(relative_magnitude: float, delay_months: int, discount: float = 0.015) -> float:
    """Simple discounted cost; for teaching, not policy valuation."""
    return relative_magnitude / ((1 + discount) ** delay_months)


def main() -> None:
    rows = []
    with COSTS.open(newline="") as f:
        for row in csv.DictReader(f):
            mag = float(row["relative_magnitude"])
            delay = int(row["delay_months"])
            row["discount_adjusted_cost"] = round(discount_adjusted_cost(mag, delay), 3)
            rows.append(row)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
