#!/usr/bin/env python3
"""Compare open-access depletion with cooperative governance."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def rows_from_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="") as handle:
        return list(csv.DictReader(handle))


def simulate(initial: float, capacity: float, regen_rate: float, use_multiplier: float, restoration: float, years: int = 25) -> list[float]:
    stock = initial
    series = []
    base_use = initial * 0.09 * use_multiplier
    for _ in range(years + 1):
        series.append(round(stock, 3))
        regeneration = regen_rate * stock * max(0.0, 1.0 - stock / capacity)
        stock = max(0.0, stock + regeneration + restoration * 0.20 - base_use)
    return series


def main() -> None:
    resources = {r["resource_id"]: r for r in rows_from_csv("synthetic_shared_resources.csv")}
    rules = rows_from_csv("synthetic_governance_rules.csv")
    output_rows = []
    for rule in rules:
        resource = resources[rule["resource_id"]]
        stocks = simulate(
            float(resource["initial_stock"]),
            float(resource["carrying_capacity"]),
            float(resource["regeneration_rate"]),
            float(rule["quota_multiplier"]),
            float(rule["restoration_investment"]),
        )
        for year, stock in enumerate(stocks):
            output_rows.append(
                {
                    "resource_id": resource["resource_id"],
                    "resource_name": resource["resource_name"],
                    "scenario": rule["scenario"],
                    "year": year,
                    "stock": stock,
                    "governance_quality": round(
                        (float(rule["monitoring_strength"]) + float(rule["sanction_strength"]) + float(rule["participation_score"])) / 3,
                        3,
                    ),
                }
            )
    output = OUT / "open_access_vs_governance_results.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
