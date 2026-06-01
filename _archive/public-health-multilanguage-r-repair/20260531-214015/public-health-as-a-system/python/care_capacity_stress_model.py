#!/usr/bin/env python3
"""Create care-capacity and overload diagnostics from public health scenario outputs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMESERIES = ROOT / "outputs" / "tables" / "public_health_system_timeseries.csv"
OUT = ROOT / "outputs" / "tables" / "care_capacity_stress_diagnostics.csv"


def main() -> None:
    if not TIMESERIES.exists():
        raise FileNotFoundError("Run public_health_system_model.py before care_capacity_stress_model.py")

    by_scenario: dict[str, list[dict[str, str]]] = {}
    with TIMESERIES.open("r", newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            by_scenario.setdefault(row["scenario"], []).append(row)

    rows = []
    for scenario, data in sorted(by_scenario.items()):
        peak_stress = max(float(row["care_stress"]) for row in data)
        overload_weeks = sum(float(row["care_stress"]) > 1.0 for row in data)
        min_capacity = min(float(row["care_capacity"]) for row in data)
        rows.append(
            {
                "scenario": scenario,
                "peak_care_stress": round(peak_stress, 3),
                "overload_weeks": overload_weeks,
                "minimum_care_capacity": round(min_capacity, 3),
                "capacity_diagnostic": "overload risk" if overload_weeks else "capacity maintained",
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
