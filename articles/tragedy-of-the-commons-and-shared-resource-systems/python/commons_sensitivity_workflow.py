#!/usr/bin/env python3
"""Small sensitivity workflow for commons sustainability assumptions."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def final_stock(regen_rate: float, use: float, restoration: float, years: int = 25) -> float:
    stock = 1000.0
    capacity = 1400.0
    for _ in range(years):
        regen = regen_rate * stock * max(0.0, 1.0 - stock / capacity)
        stock = max(0.0, stock + regen + restoration - use)
    return stock


def main() -> None:
    rows = []
    for regen_rate in [0.12, 0.18, 0.22, 0.28]:
        for use in [80, 100, 120, 150]:
            for restoration in [0, 10, 25, 40]:
                rows.append(
                    {
                        "regeneration_rate": regen_rate,
                        "annual_use": use,
                        "restoration": restoration,
                        "final_stock": round(final_stock(regen_rate, use, restoration), 3),
                    }
                )
    output = OUT / "commons_sensitivity_results.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
