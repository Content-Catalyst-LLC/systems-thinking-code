"""Compare unconstrained and constrained growth trajectories."""

from __future__ import annotations

import math
from pathlib import Path
import csv


def run(years: int = 25, initial: float = 100.0, rate: float = 0.13, capacity: float = 260.0):
    unconstrained = initial
    constrained = initial
    rows = []
    for year in range(years + 1):
        rows.append(
            {
                "year": year,
                "unconstrained_growth": round(unconstrained, 3),
                "constrained_growth": round(constrained, 3),
                "gap": round(unconstrained - constrained, 3),
            }
        )
        unconstrained = unconstrained * math.exp(rate)
        constrained = constrained + rate * constrained * (1 - constrained / capacity)
    return rows


def main() -> None:
    out = Path(__file__).resolve().parents[1] / "outputs" / "tables" / "constrained_growth_comparison.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = run()
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
