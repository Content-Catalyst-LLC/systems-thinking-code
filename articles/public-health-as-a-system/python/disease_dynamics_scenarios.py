#!/usr/bin/env python3
"""Generate a focused disease-dynamics diagnostic table from the main public health model."""

from __future__ import annotations

import csv
from pathlib import Path
from public_health_system_model import load_scenarios, run_scenario

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables" / "disease_dynamics_diagnostics.csv"


def main() -> None:
    rows = []
    for scenario in load_scenarios():
        data = run_scenario(scenario)
        peak = max(data, key=lambda row: float(row["infected"]))
        rows.append(
            {
                "scenario": scenario.name,
                "peak_week": peak["week"],
                "peak_infected": peak["infected"],
                "peak_severe_cases": peak["severe_cases"],
                "final_recovered": data[-1]["recovered"],
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
