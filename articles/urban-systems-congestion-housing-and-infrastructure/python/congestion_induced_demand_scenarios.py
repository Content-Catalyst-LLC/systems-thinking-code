#!/usr/bin/env python3
"""Generate congestion and induced-demand diagnostics from urban scenario outputs."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "urban_systems_timeseries.csv"
OUTPUT = TABLES / "congestion_induced_demand_diagnostics.csv"


def read_rows() -> list[dict[str, str]]:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing {INPUT}. Run urban_systems_model.py first.")
    with INPUT.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = read_rows()
    scenarios = sorted({row["scenario"] for row in rows})
    output: list[dict[str, object]] = []
    for scenario in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario]
        first, last = subset[0], subset[-1]
        demand_growth = float(last["vehicle_demand"]) - float(first["vehicle_demand"])
        capacity_growth = float(last["road_capacity"]) - float(first["road_capacity"])
        induced_pressure_ratio = demand_growth / capacity_growth if capacity_growth else 0.0
        output.append({
            "scenario": scenario,
            "initial_congestion_index": first["congestion_index"],
            "final_congestion_index": last["congestion_index"],
            "mean_congestion_index": round(mean(float(row["congestion_index"]) for row in subset), 3),
            "vehicle_demand_growth": round(demand_growth, 3),
            "road_capacity_growth": round(capacity_growth, 3),
            "induced_pressure_ratio": round(induced_pressure_ratio, 3),
            "diagnostic": "capacity absorbed by demand" if induced_pressure_ratio > 0.75 else "demand partly managed",
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
