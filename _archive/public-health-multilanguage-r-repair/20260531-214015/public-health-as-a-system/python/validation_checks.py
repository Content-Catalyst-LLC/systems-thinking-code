#!/usr/bin/env python3
"""Validation checks for public health systems outputs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
TIMESERIES = TABLES / "public_health_system_timeseries.csv"
REPORT = TABLES / "validation_report.txt"


def main() -> None:
    errors: list[str] = []
    if not TIMESERIES.exists():
        raise FileNotFoundError(f"Missing required timeseries file: {TIMESERIES}")

    with TIMESERIES.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            scenario = row["scenario"]
            week = row["week"]
            susceptible = float(row["susceptible"])
            infected = float(row["infected"])
            recovered = float(row["recovered"])
            trust = float(row["public_trust"])
            capacity = float(row["care_capacity"])
            stress = float(row["care_stress"])

            if susceptible < -0.001 or infected < -0.001 or recovered < -0.001:
                errors.append(f"Negative population stock in {scenario} week {week}.")
            if not 0.0 <= trust <= 100.0:
                errors.append(f"Trust outside 0-100 range in {scenario} week {week}.")
            if capacity <= 0.0:
                errors.append(f"Care capacity dropped to zero in {scenario} week {week}.")
            if stress < 0.0:
                errors.append(f"Care stress negative in {scenario} week {week}.")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", encoding="utf-8") as handle:
        if errors:
            handle.write("Validation failed.\n")
            for error in errors:
                handle.write(f"- {error}\n")
        else:
            handle.write("Validation passed.\n")
            handle.write("Population stocks, trust bounds, care capacity, and care stress checks completed.\n")

    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors))

    print("Validation passed.")


if __name__ == "__main__":
    main()
