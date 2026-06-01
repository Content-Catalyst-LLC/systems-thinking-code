#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"

REQUIRED = [
    "complex_adaptive_social_change_timeseries.csv",
    "complex_adaptive_social_change_summary.csv",
]

BOUNDED_FIELDS = [
    "adoption_index",
    "trust_index",
    "resistance_index",
    "institutional_response_index",
    "movement_capacity_index",
    "learning_capacity_index",
    "legitimacy_index",
    "transformation_momentum",
]


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required output files: " + ", ".join(missing))

    rows = list(csv.DictReader((TABLES / "complex_adaptive_social_change_timeseries.csv").open("r", encoding="utf-8")))
    if not rows:
        raise ValueError("Timeseries output has no data rows.")

    errors: list[str] = []
    for row in rows:
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if value < -0.001 or value > 100.001:
                errors.append(f"{field} outside 0-100 range in {row['scenario']} period {row['period']}: {value}")

    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors[:25]))

    print("Validation passed.")


if __name__ == "__main__":
    main()
