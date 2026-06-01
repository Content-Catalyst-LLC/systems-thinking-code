#!/usr/bin/env python3
"""Validate urban systems workflow outputs."""

from __future__ import annotations

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
TIMESERIES = TABLES / "urban_systems_timeseries.csv"
SUMMARY = TABLES / "urban_systems_summary.csv"

BOUNDED_FIELDS = [
    "transit_mode_share",
    "congestion_index",
    "housing_supply_index",
    "housing_cost_index",
    "transport_cost_index",
    "utility_cost_index",
    "affordability_index",
    "infrastructure_condition",
    "displacement_pressure",
    "climate_risk_index",
    "access_index",
    "urban_resilience_index",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required output: {path}")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = read_csv(TIMESERIES)
    summary = read_csv(SUMMARY)
    errors: list[str] = []

    if len(rows) < 100:
        errors.append(f"Expected at least 100 time-series rows; found {len(rows)}.")
    if len(summary) < 4:
        errors.append(f"Expected four scenario summaries; found {len(summary)}.")

    for row in rows:
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if not 0 <= value <= 100:
                errors.append(f"{field} outside 0-100 range for {row['scenario']} year {row['year']}: {value}")
        if float(row["road_capacity"]) <= 0:
            errors.append(f"Road capacity invalid for {row['scenario']} year {row['year']}.")

    diagnostics = {row["diagnostic"] for row in summary}
    if not diagnostics:
        errors.append("Missing diagnostic values in summary.")

    if errors:
        for error in errors:
            print(f"Validation error: {error}", file=sys.stderr)
        raise SystemExit(1)

    print("Validation passed.")


if __name__ == "__main__":
    main()
