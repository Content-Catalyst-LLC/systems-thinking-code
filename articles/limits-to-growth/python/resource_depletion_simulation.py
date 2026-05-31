"""Resource-stock simulation for limits-to-growth analysis."""

from __future__ import annotations

from pathlib import Path
import csv


def simulate(years: int = 30, stock: float = 1000.0, growth: float = 100.0):
    rows = []
    for year in range(years + 1):
        extraction = 0.08 * growth
        regeneration = 0.035 * stock
        stock = max(0.0, stock + regeneration - extraction)
        growth = growth + 0.12 * growth * (stock / 1000.0)
        rows.append(
            {
                "year": year,
                "resource_stock": round(stock, 3),
                "system_scale": round(growth, 3),
                "extraction": round(extraction, 3),
                "regeneration": round(regeneration, 3),
            }
        )
    return rows


def main() -> None:
    rows = simulate()
    out = Path(__file__).resolve().parents[1] / "outputs" / "tables" / "resource_depletion_simulation.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
