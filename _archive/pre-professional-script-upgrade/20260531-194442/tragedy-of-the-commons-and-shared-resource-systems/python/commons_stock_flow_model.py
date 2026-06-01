#!/usr/bin/env python3
"""Shared resource stock-flow model for commons systems."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def load_resources() -> list[dict[str, str]]:
    with (DATA / "synthetic_shared_resources.csv").open(newline="") as handle:
        return list(csv.DictReader(handle))


def simulate_resource(resource: dict[str, str], annual_use: float, years: int = 25) -> list[dict[str, float | str | int]]:
    stock = float(resource["initial_stock"])
    carrying_capacity = float(resource["carrying_capacity"])
    regen_rate = float(resource["regeneration_rate"])
    critical = float(resource["critical_threshold"])
    rows: list[dict[str, float | str | int]] = []
    for year in range(years + 1):
        regeneration = regen_rate * stock * max(0.0, 1.0 - stock / carrying_capacity)
        status = "critical" if stock < critical else "stable"
        rows.append(
            {
                "resource_id": resource["resource_id"],
                "resource_name": resource["resource_name"],
                "year": year,
                "stock": round(stock, 3),
                "annual_use": round(annual_use, 3),
                "regeneration": round(regeneration, 3),
                "status": status,
            }
        )
        stock = max(0.0, stock + regeneration - annual_use)
    return rows


def main() -> None:
    rows: list[dict[str, float | str | int]] = []
    for resource in load_resources():
        annual_use = float(resource["initial_stock"]) * 0.10
        rows.extend(simulate_resource(resource, annual_use))
    output = OUT / "commons_stock_flow_results.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
