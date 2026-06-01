#!/usr/bin/env python3
"""
Professional dependency-light climate systems workflow.

Models carbon stocks, simplified radiative forcing, temperature response,
ocean heat uptake, feedback amplification, vulnerability, and adaptation risk.

This is a synthetic systems-thinking model for scenario analysis and education.
It is not an official climate projection tool.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
import math
from pathlib import Path
from statistics import mean
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ROOT / "outputs" / "tables"
OUTPUT_REPORTS = ROOT / "outputs" / "reports"


@dataclass(frozen=True)
class ClimateScenario:
    name: str
    initial_co2_ppm: float
    annual_emissions_gtco2: float
    emissions_decline_rate: float
    natural_sink_fraction: float
    policy_delay_years: int
    water_vapor_feedback: float
    ice_albedo_feedback: float
    carbon_cycle_feedback: float
    adaptation_capacity: float
    vulnerability_index: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    OUTPUT_REPORTS.mkdir(parents=True, exist_ok=True)


def co2_forcing(co2_ppm: float, reference_ppm: float = 280.0) -> float:
    """Approximate CO2 radiative forcing in W/m²."""
    if co2_ppm <= 0 or reference_ppm <= 0:
        raise ValueError("CO2 concentration and reference concentration must be positive.")
    return 5.35 * math.log(co2_ppm / reference_ppm)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: ClimateScenario, years: int = 80) -> list[dict[str, object]]:
    """Run a simplified climate scenario over a fixed time horizon."""
    co2_ppm = scenario.initial_co2_ppm
    emissions = scenario.annual_emissions_gtco2
    ocean_heat_index = 0.0
    temperature_anomaly = 1.2
    rows: list[dict[str, object]] = []

    for year in range(years + 1):
        policy_active = year >= scenario.policy_delay_years

        if policy_active:
            emissions *= 1.0 - scenario.emissions_decline_rate
        else:
            emissions *= 1.005

        # Approximation for scenario demonstration only:
        # about 7.8 GtCO2 corresponds to 1 ppm CO2 before sink adjustment.
        gross_ppm_addition = emissions / 7.8

        # Sink stress weakens natural sink effectiveness as warming rises.
        sink_stress = min(0.25, max(0.0, (temperature_anomaly - 1.5) * 0.04))
        effective_sink_fraction = max(0.10, scenario.natural_sink_fraction - sink_stress)
        net_ppm_addition = gross_ppm_addition * (1.0 - effective_sink_fraction)

        # Carbon-cycle feedback adds extra concentration pressure as warming rises.
        feedback_ppm = max(0.0, temperature_anomaly - 1.0) * scenario.carbon_cycle_feedback * 0.08
        co2_ppm += net_ppm_addition + feedback_ppm

        forcing = co2_forcing(co2_ppm)
        feedback_multiplier = (
            1.0
            + scenario.water_vapor_feedback
            + scenario.ice_albedo_feedback
            + scenario.carbon_cycle_feedback
        )

        # Ocean heat uptake delays and stores response.
        ocean_heat_index += forcing * 0.035
        ocean_delay_term = ocean_heat_index * 0.006

        target_temperature = 0.78 * forcing * feedback_multiplier
        temperature_anomaly += 0.10 * (target_temperature - temperature_anomaly) + ocean_delay_term

        hazard_index = min(100.0, temperature_anomaly * 24.0)
        exposure_index = 55.0
        residual_vulnerability = max(0.0, scenario.vulnerability_index - scenario.adaptation_capacity * 0.35)
        risk_index = clamp(hazard_index * exposure_index * residual_vulnerability / 10000.0)

        rows.append(
            {
                "year": year,
                "scenario": scenario.name,
                "policy_active": policy_active,
                "emissions_gtco2": round(emissions, 3),
                "co2_ppm": round(co2_ppm, 3),
                "forcing_wm2": round(forcing, 3),
                "temperature_anomaly_c": round(temperature_anomaly, 3),
                "ocean_heat_index": round(ocean_heat_index, 3),
                "effective_sink_fraction": round(effective_sink_fraction, 3),
                "hazard_index": round(hazard_index, 3),
                "residual_vulnerability": round(residual_vulnerability, 3),
                "risk_index": round(risk_index, 3),
            }
        )

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows available for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    scenarios = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []

    for scenario in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario]
        final = subset[-1]
        max_temp = max(float(row["temperature_anomaly_c"]) for row in subset)
        cumulative_emissions = sum(float(row["emissions_gtco2"]) for row in subset)
        average_risk = mean(float(row["risk_index"]) for row in subset)
        first_year_above_2c = next(
            (int(row["year"]) for row in subset if float(row["temperature_anomaly_c"]) >= 2.0),
            None,
        )

        summary.append(
            {
                "scenario": scenario,
                "final_co2_ppm": final["co2_ppm"],
                "final_temperature_anomaly_c": final["temperature_anomaly_c"],
                "maximum_temperature_anomaly_c": round(max_temp, 3),
                "cumulative_emissions_gtco2": round(cumulative_emissions, 3),
                "average_risk_index": round(average_risk, 3),
                "first_year_above_2c": "" if first_year_above_2c is None else first_year_above_2c,
                "diagnostic": (
                    "high warming and adaptation risk"
                    if max_temp >= 2.5
                    else "threshold warning"
                    if max_temp >= 2.0
                    else "lower-risk transition pathway"
                ),
            }
        )

    return summary


def default_scenarios() -> list[ClimateScenario]:
    return [
        ClimateScenario(
            name="Baseline high emissions",
            initial_co2_ppm=420.0,
            annual_emissions_gtco2=40.0,
            emissions_decline_rate=0.000,
            natural_sink_fraction=0.45,
            policy_delay_years=999,
            water_vapor_feedback=0.18,
            ice_albedo_feedback=0.07,
            carbon_cycle_feedback=0.06,
            adaptation_capacity=20.0,
            vulnerability_index=62.0,
        ),
        ClimateScenario(
            name="Delayed transition",
            initial_co2_ppm=420.0,
            annual_emissions_gtco2=40.0,
            emissions_decline_rate=0.025,
            natural_sink_fraction=0.45,
            policy_delay_years=20,
            water_vapor_feedback=0.18,
            ice_albedo_feedback=0.07,
            carbon_cycle_feedback=0.06,
            adaptation_capacity=35.0,
            vulnerability_index=58.0,
        ),
        ClimateScenario(
            name="Rapid mitigation",
            initial_co2_ppm=420.0,
            annual_emissions_gtco2=40.0,
            emissions_decline_rate=0.060,
            natural_sink_fraction=0.47,
            policy_delay_years=5,
            water_vapor_feedback=0.16,
            ice_albedo_feedback=0.05,
            carbon_cycle_feedback=0.04,
            adaptation_capacity=50.0,
            vulnerability_index=48.0,
        ),
        ClimateScenario(
            name="Justice-centered transition",
            initial_co2_ppm=420.0,
            annual_emissions_gtco2=40.0,
            emissions_decline_rate=0.065,
            natural_sink_fraction=0.48,
            policy_delay_years=3,
            water_vapor_feedback=0.16,
            ice_albedo_feedback=0.05,
            carbon_cycle_feedback=0.035,
            adaptation_capacity=68.0,
            vulnerability_index=38.0,
        ),
    ]


def validate_rows(rows: Iterable[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    required = {"year", "scenario", "emissions_gtco2", "co2_ppm", "temperature_anomaly_c", "risk_index"}
    for i, row in enumerate(rows):
        missing = required - set(row)
        if missing:
            issues.append(f"row {i}: missing columns {sorted(missing)}")
        if float(row.get("co2_ppm", 0)) <= 0:
            issues.append(f"row {i}: CO2 ppm must be positive")
        if float(row.get("emissions_gtco2", -1)) < 0:
            issues.append(f"row {i}: emissions should not be negative in this demonstration model")
    return issues


def write_validation_report(rows: list[dict[str, object]], summary_rows: list[dict[str, object]]) -> None:
    issues = validate_rows(rows)
    report = OUTPUT_REPORTS / "climate_workflow_validation_report.md"
    lines = [
        "# Climate Workflow Validation Report",
        "",
        f"Rows generated: {len(rows)}",
        f"Scenarios generated: {len(summary_rows)}",
        f"Validation issues: {len(issues)}",
        "",
    ]
    if issues:
        lines.append("## Issues")
        lines.extend(f"- {issue}" for issue in issues)
    else:
        lines.append("No structural validation issues detected in the synthetic workflow outputs.")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_outputs()
    all_rows: list[dict[str, object]] = []
    for scenario in default_scenarios():
        all_rows.extend(run_scenario(scenario))

    summary_rows = summarize(all_rows)
    write_csv(OUTPUT_TABLES / "climate_feedback_scenario_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "climate_feedback_scenario_summary.csv", summary_rows)
    write_validation_report(all_rows, summary_rows)

    print("\nClimate feedback scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: final temp={row['final_temperature_anomaly_c']}°C, "
            f"cumulative emissions={row['cumulative_emissions_gtco2']} GtCO2, "
            f"diagnostic={row['diagnostic']}"
        )


if __name__ == "__main__":
    main()
