#!/usr/bin/env python3
"""Validation checks for the food-water-energy workflow outputs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"

REQUIRED = {
    "food_water_energy_nexus_timeseries.csv": [
        "year",
        "scenario",
        "groundwater_stock",
        "food_production_index",
        "water_security_index",
        "energy_security_index",
        "nexus_stress_index",
        "resilience_index",
    ],
    "food_water_energy_nexus_summary.csv": [
        "scenario",
        "final_groundwater_stock",
        "average_nexus_stress_index",
        "average_resilience_index",
        "diagnostic",
    ],
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    problems: list[str] = []
    for filename, required_columns in REQUIRED.items():
        path = TABLES / filename
        if not path.exists():
            problems.append(f"Missing output file: {path}")
            continue
        rows = read_rows(path)
        if not rows:
            problems.append(f"Output file has no rows: {path}")
            continue
        missing = [column for column in required_columns if column not in rows[0]]
        if missing:
            problems.append(f"{filename} missing columns: {', '.join(missing)}")
    timeseries = read_rows(TABLES / "food_water_energy_nexus_timeseries.csv") if (TABLES / "food_water_energy_nexus_timeseries.csv").exists() else []
    for row in timeseries:
        for column in ["groundwater_stock", "food_production_index", "water_security_index", "energy_security_index", "nexus_stress_index", "resilience_index"]:
            value = float(row[column])
            if value < 0:
                problems.append(f"Negative value in {column}: {value}")
    summary_path = TABLES / "validation_report.txt"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    if problems:
        summary_path.write_text("Validation failed:\n" + "\n".join(problems) + "\n", encoding="utf-8")
        raise SystemExit("\n".join(problems))
    summary_path.write_text("Validation passed. Required files, columns, and basic ranges are present.\n", encoding="utf-8")
    print("Validation passed.")


if __name__ == "__main__":
    main()
