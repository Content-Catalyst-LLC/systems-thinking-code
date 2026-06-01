#!/usr/bin/env python3
"""Dependency-light urban systems scenario model.

Models congestion, induced demand, housing-transport affordability,
infrastructure condition, displacement pressure, access, climate risk, and
urban resilience across scenarios.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ROOT / "outputs" / "tables"


@dataclass(frozen=True)
class UrbanScenario:
    name: str
    initial_travel_demand: float
    road_capacity: float
    transit_capacity: float
    housing_supply_index: float
    housing_cost_index: float
    household_income_index: float
    infrastructure_condition: float
    maintenance_investment: float
    transit_investment: float
    affordable_housing_investment: float
    climate_stress: float
    displacement_pressure: float
    policy_start_year: int
    induced_demand_factor: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: UrbanScenario, years: int = 30) -> list[dict[str, object]]:
    travel_demand = scenario.initial_travel_demand
    road_capacity = scenario.road_capacity
    transit_capacity = scenario.transit_capacity
    housing_supply = scenario.housing_supply_index
    housing_cost = scenario.housing_cost_index
    infrastructure_condition = scenario.infrastructure_condition
    displacement_pressure = scenario.displacement_pressure
    rows: list[dict[str, object]] = []

    for year in range(years + 1):
        policy_active = year >= scenario.policy_start_year

        maintenance = scenario.maintenance_investment if policy_active else scenario.maintenance_investment * 0.25
        transit_investment = scenario.transit_investment if policy_active else scenario.transit_investment * 0.20
        affordable_housing = scenario.affordable_housing_investment if policy_active else scenario.affordable_housing_investment * 0.20

        if "road" in scenario.name.lower():
            road_capacity += 1.2
            travel_demand += scenario.induced_demand_factor * 2.1
        else:
            road_capacity += 0.15
            travel_demand += 0.65

        transit_capacity = clamp(transit_capacity + transit_investment * 0.18 - scenario.climate_stress * 0.25)
        transit_mode_share = clamp(12.0 + transit_capacity * 0.35 - housing_cost * 0.04 + affordable_housing * 0.10)

        vehicle_demand = max(0.0, travel_demand * (1.0 - transit_mode_share / 100.0))
        congestion_index = clamp((vehicle_demand / max(road_capacity, 1.0)) * 55.0)

        housing_supply = clamp(housing_supply + affordable_housing * 0.16 + transit_investment * 0.04)
        housing_cost = clamp(
            housing_cost
            + displacement_pressure * 0.18
            + congestion_index * 0.025
            - housing_supply * 0.045
            - affordable_housing * 0.22
        )

        transport_cost = clamp(20.0 + congestion_index * 0.35 - transit_mode_share * 0.18)
        utility_cost = clamp(18.0 + scenario.climate_stress * 20.0 - infrastructure_condition * 0.05)
        affordability_index = clamp(
            scenario.household_income_index - housing_cost * 0.45 - transport_cost * 0.35 - utility_cost * 0.20
        )

        infrastructure_condition = clamp(
            infrastructure_condition
            + maintenance * 0.22
            - 1.55
            - scenario.climate_stress * 1.35
            - congestion_index * 0.012
        )

        displacement_pressure = clamp(
            displacement_pressure
            + transit_investment * 0.04
            + housing_cost * 0.03
            - affordable_housing * 0.18
        )

        climate_risk_index = clamp(
            scenario.climate_stress * 60.0
            + (100.0 - infrastructure_condition) * 0.25
            + (100.0 - affordability_index) * 0.12
        )

        access_index = clamp(
            100.0
            - congestion_index * 0.30
            + transit_mode_share * 0.32
            + affordability_index * 0.18
            + infrastructure_condition * 0.12
            - displacement_pressure * 0.12
        )

        urban_resilience_index = clamp(
            access_index * 0.30
            + affordability_index * 0.25
            + infrastructure_condition * 0.25
            + transit_mode_share * 0.10
            - climate_risk_index * 0.10
        )

        rows.append({
            "year": year,
            "scenario": scenario.name,
            "policy_active": policy_active,
            "travel_demand": round(travel_demand, 3),
            "vehicle_demand": round(vehicle_demand, 3),
            "road_capacity": round(road_capacity, 3),
            "transit_capacity": round(transit_capacity, 3),
            "transit_mode_share": round(transit_mode_share, 3),
            "congestion_index": round(congestion_index, 3),
            "housing_supply_index": round(housing_supply, 3),
            "housing_cost_index": round(housing_cost, 3),
            "transport_cost_index": round(transport_cost, 3),
            "utility_cost_index": round(utility_cost, 3),
            "affordability_index": round(affordability_index, 3),
            "infrastructure_condition": round(infrastructure_condition, 3),
            "displacement_pressure": round(displacement_pressure, 3),
            "climate_risk_index": round(climate_risk_index, 3),
            "access_index": round(access_index, 3),
            "urban_resilience_index": round(urban_resilience_index, 3),
        })

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
        final = subset[-1]
        avg_congestion = mean(float(row["congestion_index"]) for row in subset)
        avg_affordability = mean(float(row["affordability_index"]) for row in subset)
        min_infrastructure = min(float(row["infrastructure_condition"]) for row in subset)
        max_displacement = max(float(row["displacement_pressure"]) for row in subset)
        avg_resilience = mean(float(row["urban_resilience_index"]) for row in subset)

        summary.append({
            "scenario": scenario_name,
            "final_congestion_index": final["congestion_index"],
            "final_affordability_index": final["affordability_index"],
            "final_infrastructure_condition": final["infrastructure_condition"],
            "final_displacement_pressure": final["displacement_pressure"],
            "average_congestion_index": round(avg_congestion, 3),
            "average_affordability_index": round(avg_affordability, 3),
            "minimum_infrastructure_condition": round(min_infrastructure, 3),
            "maximum_displacement_pressure": round(max_displacement, 3),
            "average_urban_resilience_index": round(avg_resilience, 3),
            "diagnostic": (
                "high urban fragility" if avg_resilience < 35 or min_infrastructure < 30 else
                "moderate stress requiring redesign" if avg_congestion > 55 or avg_affordability < 45 else
                "comparatively resilient urban pathway"
            ),
        })

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "transit_mode_share",
        "congestion_index",
        "housing_supply_index",
        "housing_cost_index",
        "transport_cost_index",
        "utility_cost_index",
        "affordability_index",
        "infrastructure_condition",
        "displacement_pressure",
        "climate_risk_index",
        "access_index",
        "urban_resilience_index",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 100.001:
                errors.append(f"{field} outside 0-100 range in {row['scenario']} year {row['year']}.")
        if float(row["road_capacity"]) <= 0:
            errors.append(f"Road capacity dropped to zero in {row['scenario']} year {row['year']}.")

    return errors


def build_scenarios() -> list[UrbanScenario]:
    return [
        UrbanScenario(
            name="Road expansion baseline",
            initial_travel_demand=82.0,
            road_capacity=70.0,
            transit_capacity=36.0,
            housing_supply_index=44.0,
            housing_cost_index=64.0,
            household_income_index=68.0,
            infrastructure_condition=62.0,
            maintenance_investment=3.0,
            transit_investment=2.0,
            affordable_housing_investment=2.0,
            climate_stress=0.24,
            displacement_pressure=42.0,
            policy_start_year=4,
            induced_demand_factor=1.0,
        ),
        UrbanScenario(
            name="Deferred maintenance",
            initial_travel_demand=80.0,
            road_capacity=68.0,
            transit_capacity=34.0,
            housing_supply_index=43.0,
            housing_cost_index=62.0,
            household_income_index=66.0,
            infrastructure_condition=58.0,
            maintenance_investment=1.0,
            transit_investment=1.5,
            affordable_housing_investment=2.0,
            climate_stress=0.30,
            displacement_pressure=44.0,
            policy_start_year=12,
            induced_demand_factor=0.55,
        ),
        UrbanScenario(
            name="Transit housing coordination",
            initial_travel_demand=80.0,
            road_capacity=68.0,
            transit_capacity=38.0,
            housing_supply_index=46.0,
            housing_cost_index=62.0,
            household_income_index=68.0,
            infrastructure_condition=62.0,
            maintenance_investment=5.0,
            transit_investment=9.0,
            affordable_housing_investment=8.0,
            climate_stress=0.22,
            displacement_pressure=40.0,
            policy_start_year=4,
            induced_demand_factor=0.35,
        ),
        UrbanScenario(
            name="Integrated resilient urbanism",
            initial_travel_demand=78.0,
            road_capacity=67.0,
            transit_capacity=42.0,
            housing_supply_index=50.0,
            housing_cost_index=58.0,
            household_income_index=72.0,
            infrastructure_condition=66.0,
            maintenance_investment=8.0,
            transit_investment=10.0,
            affordable_housing_investment=11.0,
            climate_stress=0.18,
            displacement_pressure=34.0,
            policy_start_year=3,
            induced_demand_factor=0.25,
        ),
    ]


def main() -> None:
    ensure_outputs()
    all_rows: list[dict[str, object]] = []
    for scenario in build_scenarios():
        all_rows.extend(run_scenario(scenario))

    validation_errors = validate(all_rows)
    if validation_errors:
        raise ValueError("Validation failed:\n" + "\n".join(validation_errors))

    summary_rows = summarize(all_rows)
    write_csv(OUTPUT_TABLES / "urban_systems_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "urban_systems_summary.csv", summary_rows)

    with (OUTPUT_TABLES / "validation_report.txt").open("w", encoding="utf-8") as handle:
        handle.write("Validation passed.\n")
        handle.write("Urban bounded indicators, capacity checks, and scenario outputs completed.\n")

    print("\nUrban systems scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: final congestion={row['final_congestion_index']}, "
            f"final affordability={row['final_affordability_index']}, "
            f"diagnostic={row['diagnostic']}"
        )


if __name__ == "__main__":
    main()
