#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"

REQUIRED = [
    "systems_thinking_age_complexity_timeseries.csv",
    "systems_thinking_age_complexity_summary.csv",
]

BOUNDED_FIELDS = [
    "complexity_pressure",
    "resilience_capacity",
    "feedback_amplification",
    "accountability_score",
    "harm_pressure",
    "resilience_stock",
    "learning_stock",
    "trust_stock",
    "accountability_memory",
    "harm_stock",
    "transformation_capacity",
    "systems_readiness_score",
]


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required output files: " + ", ".join(missing))

    rows = list(csv.DictReader((TABLES / "systems_thinking_age_complexity_timeseries.csv").open("r", encoding="utf-8")))
    if not rows:
        raise ValueError("Timeseries output has no data rows.")

    errors: list[str] = []
    for row in rows:
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors[:25]))

    print("Validation passed.")


if __name__ == "__main__":
    main()
