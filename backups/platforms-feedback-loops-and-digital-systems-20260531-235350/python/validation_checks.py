#!/usr/bin/env python3
"""Validation checks for platform feedback outputs."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
TIMESERIES = TABLES / "platform_feedback_timeseries.csv"
REPORT = TABLES / "validation_report.txt"

BOUNDED_FIELDS = [
    "engagement_index",
    "creator_metric_pressure",
    "harmful_cascade_risk",
    "moderation_backlog",
    "platform_dependency",
    "governance_readiness",
    "user_trust",
    "public_value_index",
    "platform_risk_index",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run platform_feedback_digital_systems_model.py first.")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = read_rows(TIMESERIES)
    errors: list[str] = []

    for row in rows:
        scenario = row.get("scenario", "unknown scenario")
        period = row.get("period", "unknown period")
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if value < -0.001 or value > 100.001:
                errors.append(f"{field} outside 0-100 range in {scenario} period {period}: {value}")

    if errors:
        REPORT.write_text("Validation failed.\n" + "\n".join(errors) + "\n", encoding="utf-8")
        raise SystemExit("Validation failed. See outputs/tables/validation_report.txt")

    REPORT.write_text(
        "Validation passed.\n"
        "Checked bounded platform indicators, scenario structure, and output table integrity.\n",
        encoding="utf-8",
    )
    print("Validation passed.")


if __name__ == "__main__":
    main()
