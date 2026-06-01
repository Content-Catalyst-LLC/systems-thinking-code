#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"

REQUIRED = [
    "cybernetics_systems_timeseries.csv",
    "cybernetics_systems_summary.csv",
]

BOUNDED_FIELDS = [
    "system_state",
    "observed_state",
    "reference_goal",
    "control_action",
    "disturbance_pressure",
    "response_variety",
    "variety_gap",
    "learning_capacity",
    "trust_index",
    "regulation_quality",
    "accountability_index",
]


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required output files: " + ", ".join(missing))

    rows = list(csv.DictReader((TABLES / "cybernetics_systems_timeseries.csv").open("r", encoding="utf-8")))
    if not rows:
        raise ValueError("Timeseries output has no data rows.")

    errors: list[str] = []
    for row in rows:
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")
        error_value = float(row["error_signal"])
        if error_value < -120.001 or error_value > 120.001:
            errors.append(f"error_signal outside expected range in {row['scenario']} period {row['period']}: {error_value}")

    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors[:25]))

    print("Validation passed.")


if __name__ == "__main__":
    main()
