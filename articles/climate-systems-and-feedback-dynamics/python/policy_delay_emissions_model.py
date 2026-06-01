#!/usr/bin/env python3
"""Compare cumulative emissions and warming penalties associated with policy delay."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "climate_feedback_scenario_timeseries.csv"
OUTPUT = TABLES / "policy_delay_emissions_diagnostics.csv"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing {INPUT}. Run climate_feedback_dynamics_model.py first.")

    with INPUT.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    scenarios = sorted({row["scenario"] for row in rows})
    baseline_rows = [row for row in rows if row["scenario"] == "Baseline high emissions"]
    baseline_cumulative = sum(float(row["emissions_gtco2"]) for row in baseline_rows)
    baseline_final_temp = float(baseline_rows[-1]["temperature_anomaly_c"])

    output_rows = []
    for scenario in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario]
        cumulative = sum(float(row["emissions_gtco2"]) for row in subset)
        final_temp = float(subset[-1]["temperature_anomaly_c"])
        output_rows.append(
            {
                "scenario": scenario,
                "cumulative_emissions_gtco2": round(cumulative, 3),
                "avoided_emissions_vs_baseline_gtco2": round(baseline_cumulative - cumulative, 3),
                "final_temperature_anomaly_c": round(final_temp, 3),
                "temperature_difference_vs_baseline_c": round(final_temp - baseline_final_temp, 3),
                "diagnostic": (
                    "baseline comparison" if scenario == "Baseline high emissions" else
                    "strong delay penalty remains" if final_temp > 2.0 else
                    "material improvement vs baseline"
                ),
            }
        )

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)

    print("Policy delay diagnostics written to", OUTPUT)


if __name__ == "__main__":
    main()
