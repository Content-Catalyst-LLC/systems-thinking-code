#!/usr/bin/env python3
"""Boundary expansion analysis for externalized costs."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_boundary_costs.csv"
OUT = ROOT / "outputs" / "tables" / "boundary_expansion_analysis.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    out_rows = []
    for row in rows:
        internal = float(row["internal_cost"])
        external = float(row["externalized_cost"])
        out_rows.append({
            **row,
            "expanded_boundary_cost": round(internal + external, 2),
            "externalized_share": round(external / (internal + external), 3),
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
