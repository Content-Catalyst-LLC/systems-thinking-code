#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"

REQUIRED = [
    "forrester_system_dynamics_timeseries.csv",
    "forrester_system_dynamics_summary.csv",
]

BOUNDED_FIELDS = [
    "capacity_stock",
    "corrective_action",
    "investment_flow",
    "service_flow",
    "resistance_index",
    "trust_stock",
    "institutional_learning_stock",
    "system_performance",
]


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required output files: " + ", ".join(missing))

    rows = list(csv.DictReader((TABLES / "forrester_system_dynamics_timeseries.csv").open("r", encoding="utf-8")))
    if not rows:
        raise ValueError("Timeseries output has no data rows.")

    errors: list[str] = []
    for row in rows:
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if value < -0.001 or value > 150.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")
        backlog = float(row["backlog_stock"])
        if backlog < -0.001 or backlog > 220.001:
            errors.append(f"backlog_stock outside expected range in {row['scenario']} period {row['period']}: {backlog}")

    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors[:25]))

    print("Validation passed.")


if __name__ == "__main__":
    main()
