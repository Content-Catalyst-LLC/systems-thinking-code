"""Synthetic inequality accumulation model for group-level stock trajectories."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def trajectory(group: str, wealth: float, inflow: float, outflow: float, months: int = 36) -> list[dict[str, float | str]]:
    rows = []
    for month in range(months + 1):
        rows.append({"group": group, "month": month, "wealth_stock": round(wealth, 2), "inflow": inflow, "outflow": outflow})
        wealth = max(0, wealth + inflow - outflow + 0.01 * wealth)
    return rows


if __name__ == "__main__":
    rows = []
    rows.extend(trajectory("higher_asset_baseline", 80_000, 2200, 1100))
    rows.extend(trajectory("lower_asset_high_burden", 4_000, 1200, 1150))
    path = OUT / "inequality_accumulation_trajectories.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")
