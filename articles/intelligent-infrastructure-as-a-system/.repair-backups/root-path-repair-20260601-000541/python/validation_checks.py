#!/usr/bin/env python3
"""Validation checks for dependency-light intelligent infrastructure outputs."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
REQUIRED = [
    "intelligent_infrastructure_timeseries.csv",
    "intelligent_infrastructure_summary.csv",
    "asset_priority_diagnostics.csv",
    "cyber_physical_dependency_diagnostics.csv",
    "climate_resilience_diagnostics.csv",
]


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required outputs: " + ", ".join(missing))
    with (TABLES / "intelligent_infrastructure_timeseries.csv").open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Timeseries output is empty.")
    scenarios = {row["scenario"] for row in rows}
    if len(scenarios) < 4:
        raise ValueError("Expected at least four infrastructure scenarios.")
    for row in rows:
        for field in ["risk_score", "resilience_score", "cyber_physical_dependency"]:
            value = float(row[field])
            if not 0 <= value <= 100:
                raise ValueError(f"{field} outside 0-100 range: {value}")
    print("Validation passed.")


if __name__ == "__main__":
    main()
