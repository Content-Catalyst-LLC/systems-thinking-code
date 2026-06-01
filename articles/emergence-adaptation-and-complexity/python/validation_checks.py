#!/usr/bin/env python3
"""Validation checks for dependency-light complexity outputs."""

from __future__ import annotations

import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TABLES = os.path.join(ROOT, "outputs", "tables")
REQUIRED = [
    "emergence_adaptation_complexity_timeseries.csv",
    "emergence_adaptation_complexity_summary.csv",
    "validation_report.txt",
]


def require_file(path: str) -> None:
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    if os.path.getsize(path) == 0:
        raise ValueError(f"File is empty: {path}")


def validate_timeseries(path: str) -> None:
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Timeseries file contains no rows.")
    scenarios = {row["scenario"] for row in rows}
    if len(scenarios) < 4:
        raise ValueError(f"Expected at least 4 scenarios; found {len(scenarios)}")
    for row in rows:
        for field in ["system_mean", "clustering_index", "diversity_index", "synchronization_index", "complexity_index"]:
            value = float(row[field])
            if value < -0.001 or value > 1.001:
                raise ValueError(f"{field} outside 0-1 range: {value}")


def main() -> None:
    for filename in REQUIRED:
        require_file(os.path.join(TABLES, filename))
    validate_timeseries(os.path.join(TABLES, "emergence_adaptation_complexity_timeseries.csv"))
    print("Validation passed.")


if __name__ == "__main__":
    main()
