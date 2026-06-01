#!/usr/bin/env python3
"""
Dependency-light professional workflow for intelligent infrastructure systems analysis.

This script intentionally uses only the Python standard library. It writes all outputs
relative to the article root so it works whether called from Downloads, the repository
root, the article folder, or a workflow runner.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ARTICLE_ROOT / "outputs" / "tables"


@dataclass
class InfrastructureScenario:
    name: str
    years: int
    sensor_coverage: float
    sensor_reliability: float
    maintenance_funding: float
    workforce_capacity: float
    predictive_model_quality: float
    cyber_security_readiness: float
    vendor_dependency: float
    climate_stress: float
    equity_weight: float
    public_accountability: float


@dataclass
class Asset:
    asset_id: str
    category: str
    condition: float
    age: float
    service_criticality: float
    redundancy: float
    equity_priority: float
    climate_exposure: float
    cyber_dependency: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def build_assets() -> list[Asset]:
    return [
        Asset("bridge_north", "transport", 64.0, 42.0, 78.0, 35.0, 62.0, 44.0, 28.0),
        Asset("water_main_east", "water", 58.0, 55.0, 86.0, 25.0, 82.0, 52.0, 34.0),
        Asset("substation_7", "power", 70.0, 38.0, 92.0, 42.0, 70.0, 48.0, 66.0),
        Asset("transit_signal_core", "transport", 72.0, 24.0, 74.0, 48.0, 58.0, 36.0, 72.0),
        Asset("stormwater_pump_south", "stormwater", 54.0, 47.0, 88.0, 30.0, 76.0, 78.0, 44.0),
        Asset("cooling_center_grid_node", "public_facility", 68.0, 31.0, 80.0, 38.0, 88.0, 70.0, 52.0),
        Asset("air_quality_sensor_cluster", "environmental", 82.0, 12.0, 58.0, 55.0, 74.0, 62.0, 40.0),
        Asset("wastewater_lift_station", "wastewater", 60.0, 49.0, 84.0, 32.0, 68.0, 55.0, 46.0),
        Asset("public_broadband_hub", "digital", 76.0, 18.0, 72.0, 40.0, 80.0, 32.0, 84.0),
        Asset("hospital_access_corridor", "transport", 62.0, 36.0, 90.0, 28.0, 86.0, 46.0, 30.0),
    ]


def asset_failure_probability(asset: Asset, scenario: InfrastructureScenario) -> float:
    deterioration_pressure = (
        (100.0 - asset.condition) * 0.38
        + asset.age * 0.22
        + asset.climate_exposure * scenario.climate_stress * 0.18
        + asset.cyber_dependency * scenario.vendor_dependency * 0.08
    )

    intelligence_offset = (
        scenario.sensor_coverage * scenario.sensor_reliability * 16.0
        + scenario.predictive_model_quality * 10.0
        + scenario.maintenance_funding * 8.0
    )

    return clamp(deterioration_pressure - intelligence_offset)


def asset_consequence(asset: Asset, scenario: InfrastructureScenario) -> float:
    return clamp(
        asset.service_criticality * 0.38
        + (100.0 - asset.redundancy) * 0.24
        + asset.equity_priority * scenario.equity_weight * 0.22
        + asset.climate_exposure * scenario.climate_stress * 0.16
    )


def cyber_physical_dependency(asset: Asset, scenario: InfrastructureScenario) -> float:
    return clamp(
        asset.cyber_dependency * 0.50
        + scenario.vendor_dependency * 35.0
        + scenario.sensor_coverage * 12.0
        - scenario.cyber_security_readiness * 28.0
    )


def maintenance_action_score(asset: Asset, scenario: InfrastructureScenario, risk_score: float) -> float:
    capacity = scenario.maintenance_funding * 42.0 + scenario.workforce_capacity * 36.0
    decision_quality = scenario.predictive_model_quality * 18.0 + scenario.public_accountability * 14.0
    priority_signal = risk_score * 0.52 + asset.equity_priority * scenario.equity_weight * 0.18
    return clamp((capacity + decision_quality + priority_signal) / 2.2)


def run_scenario(scenario: InfrastructureScenario) -> list[dict[str, object]]:
    assets = build_assets()
    rows: list[dict[str, object]] = []

    for year in range(scenario.years + 1):
        for asset in assets:
            failure_probability = asset_failure_probability(asset, scenario)
            consequence = asset_consequence(asset, scenario)
            cyber_dependency = cyber_physical_dependency(asset, scenario)
            risk_score = clamp(failure_probability * 0.55 + consequence * 0.35 + cyber_dependency * 0.10)
            maintenance_score = maintenance_action_score(asset, scenario, risk_score)

            resilience_score = clamp(
                asset.condition * 0.22
                + asset.redundancy * 0.16
                + scenario.maintenance_funding * 18.0
                + scenario.workforce_capacity * 14.0
                + scenario.cyber_security_readiness * 12.0
                + scenario.public_accountability * 10.0
                - failure_probability * 0.14
                - cyber_dependency * 0.08
            )

            rows.append(
                {
                    "year": year,
                    "scenario": scenario.name,
                    "asset_id": asset.asset_id,
                    "category": asset.category,
                    "condition": round(asset.condition, 3),
                    "failure_probability": round(failure_probability, 3),
                    "failure_consequence": round(consequence, 3),
                    "cyber_physical_dependency": round(cyber_dependency, 3),
                    "risk_score": round(risk_score, 3),
                    "maintenance_action_score": round(maintenance_score, 3),
                    "resilience_score": round(resilience_score, 3),
                    "equity_priority": round(asset.equity_priority, 3),
                    "redundancy": round(asset.redundancy, 3),
                }
            )

            deterioration = 2.2 + scenario.climate_stress * asset.climate_exposure * 0.018
            improvement = maintenance_score * 0.045 + scenario.predictive_model_quality * 0.55
            asset.condition = clamp(asset.condition - deterioration + improvement)

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    scenarios = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []

    for scenario_name in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario_name]
        final_year = max(int(row["year"]) for row in subset)
        final_rows = [row for row in subset if int(row["year"]) == final_year]

        avg_risk = mean(float(row["risk_score"]) for row in final_rows)
        avg_resilience = mean(float(row["resilience_score"]) for row in final_rows)
        max_cyber_dependency = max(float(row["cyber_physical_dependency"]) for row in final_rows)
        high_risk_assets = sum(1 for row in final_rows if float(row["risk_score"]) >= 55)
        low_resilience_assets = sum(1 for row in final_rows if float(row["resilience_score"]) <= 45)

        summary.append(
            {
                "scenario": scenario_name,
                "final_average_risk_score": round(avg_risk, 3),
                "final_average_resilience_score": round(avg_resilience, 3),
                "maximum_cyber_physical_dependency": round(max_cyber_dependency, 3),
                "high_risk_asset_count": high_risk_assets,
                "low_resilience_asset_count": low_resilience_assets,
                "diagnostic": (
                    "high infrastructure fragility"
                    if high_risk_assets >= 4 or avg_resilience < 42
                    else "moderate risk requiring governance and maintenance redesign"
                    if avg_risk >= 42 or max_cyber_dependency >= 60
                    else "comparatively resilient intelligent infrastructure pathway"
                ),
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "condition",
        "failure_probability",
        "failure_consequence",
        "cyber_physical_dependency",
        "risk_score",
        "maintenance_action_score",
        "resilience_score",
        "equity_priority",
        "redundancy",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 100.001:
                errors.append(
                    f"{field} outside 0-100 range in {row['scenario']} "
                    f"{row['asset_id']} year {row['year']}: {value}"
                )

    return errors


def main() -> None:
    ensure_outputs()

    scenarios = [
        InfrastructureScenario(
            name="Reactive maintenance baseline",
            years=20,
            sensor_coverage=0.22,
            sensor_reliability=0.58,
            maintenance_funding=0.28,
            workforce_capacity=0.35,
            predictive_model_quality=0.16,
            cyber_security_readiness=0.32,
            vendor_dependency=0.42,
            climate_stress=0.48,
            equity_weight=0.35,
            public_accountability=0.30,
        ),
        InfrastructureScenario(
            name="Sensor-rich but underfunded",
            years=20,
            sensor_coverage=0.78,
            sensor_reliability=0.70,
            maintenance_funding=0.26,
            workforce_capacity=0.34,
            predictive_model_quality=0.54,
            cyber_security_readiness=0.36,
            vendor_dependency=0.72,
            climate_stress=0.50,
            equity_weight=0.38,
            public_accountability=0.34,
        ),
        InfrastructureScenario(
            name="Predictive maintenance strategy",
            years=20,
            sensor_coverage=0.72,
            sensor_reliability=0.78,
            maintenance_funding=0.64,
            workforce_capacity=0.62,
            predictive_model_quality=0.72,
            cyber_security_readiness=0.60,
            vendor_dependency=0.46,
            climate_stress=0.42,
            equity_weight=0.58,
            public_accountability=0.58,
        ),
        InfrastructureScenario(
            name="Accountable resilient infrastructure",
            years=20,
            sensor_coverage=0.70,
            sensor_reliability=0.82,
            maintenance_funding=0.76,
            workforce_capacity=0.74,
            predictive_model_quality=0.76,
            cyber_security_readiness=0.78,
            vendor_dependency=0.26,
            climate_stress=0.36,
            equity_weight=0.78,
            public_accountability=0.82,
        ),
    ]

    all_rows: list[dict[str, object]] = []
    for scenario in scenarios:
        all_rows.extend(run_scenario(scenario))

    validation_errors = validate(all_rows)
    if validation_errors:
        raise ValueError("Validation failed:\n" + "\n".join(validation_errors))

    summary_rows = summarize(all_rows)

    write_csv(OUTPUT_TABLES / "intelligent_infrastructure_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "intelligent_infrastructure_summary.csv", summary_rows)

    validation_report = OUTPUT_TABLES / "validation_report.txt"
    validation_report.write_text(
        "Validation passed.\n"
        "Bounded indicators, infrastructure risk scores, cyber-physical dependency, and resilience outputs completed.\n",
        encoding="utf-8",
    )

    print("\nIntelligent infrastructure scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: avg risk={row['final_average_risk_score']}, "
            f"avg resilience={row['final_average_resilience_score']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'intelligent_infrastructure_timeseries.csv'}")


if __name__ == "__main__":
    main()
