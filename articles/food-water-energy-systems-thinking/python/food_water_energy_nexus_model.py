#!/usr/bin/env python3
"""
Professional dependency-light food-water-energy nexus model.

This script uses only the Python standard library. It generates synthetic but
realistic scenario outputs for groundwater stock, irrigation withdrawal,
pumping energy, soil health, food production, water security, energy security,
nexus stress, and resilience.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
import json
import os
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
DATA = ROOT / "data"

@dataclass(frozen=True)
class NexusScenario:
    name: str
    initial_groundwater: float
    annual_recharge: float
    irrigation_withdrawal: float
    water_efficiency_gain: float
    initial_soil_health: float
    soil_regeneration: float
    energy_price_index: float
    renewable_energy_share: float
    climate_stress: float
    vulnerability_index: float
    policy_start_year: int


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def ensure_dirs() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)


def scenarios() -> list[NexusScenario]:
    return [
        NexusScenario(
            name="Baseline depletion",
            initial_groundwater=1000.0,
            annual_recharge=28.0,
            irrigation_withdrawal=55.0,
            water_efficiency_gain=0.00,
            initial_soil_health=62.0,
            soil_regeneration=0.5,
            energy_price_index=1.1,
            renewable_energy_share=0.15,
            climate_stress=0.18,
            vulnerability_index=52.0,
            policy_start_year=999,
        ),
        NexusScenario(
            name="Drought stress",
            initial_groundwater=1000.0,
            annual_recharge=20.0,
            irrigation_withdrawal=62.0,
            water_efficiency_gain=0.05,
            initial_soil_health=58.0,
            soil_regeneration=0.4,
            energy_price_index=1.3,
            renewable_energy_share=0.18,
            climate_stress=0.32,
            vulnerability_index=62.0,
            policy_start_year=8,
        ),
        NexusScenario(
            name="Efficiency only",
            initial_groundwater=1000.0,
            annual_recharge=28.0,
            irrigation_withdrawal=55.0,
            water_efficiency_gain=0.24,
            initial_soil_health=62.0,
            soil_regeneration=0.8,
            energy_price_index=1.05,
            renewable_energy_share=0.32,
            climate_stress=0.18,
            vulnerability_index=48.0,
            policy_start_year=5,
        ),
        NexusScenario(
            name="Regenerative resilience",
            initial_groundwater=1000.0,
            annual_recharge=34.0,
            irrigation_withdrawal=50.0,
            water_efficiency_gain=0.30,
            initial_soil_health=66.0,
            soil_regeneration=2.4,
            energy_price_index=0.95,
            renewable_energy_share=0.68,
            climate_stress=0.16,
            vulnerability_index=34.0,
            policy_start_year=3,
        ),
    ]


def run_scenario(scenario: NexusScenario, years: int = 30) -> list[dict[str, object]]:
    groundwater = scenario.initial_groundwater
    soil_health = scenario.initial_soil_health
    rows: list[dict[str, object]] = []

    for year in range(years + 1):
        policy_active = year >= scenario.policy_start_year
        efficiency = scenario.water_efficiency_gain if policy_active else 0.0
        regeneration = scenario.soil_regeneration if policy_active else scenario.soil_regeneration * 0.25
        renewable_share = scenario.renewable_energy_share if policy_active else scenario.renewable_energy_share * 0.40

        climate_multiplier = 1.0 + scenario.climate_stress
        effective_withdrawal = scenario.irrigation_withdrawal * climate_multiplier * (1.0 - efficiency)
        groundwater = max(0.0, groundwater + scenario.annual_recharge - effective_withdrawal)

        depletion_ratio = 1.0 - groundwater / max(scenario.initial_groundwater, 1.0)
        pumping_head_penalty = max(0.0, depletion_ratio) * 0.65
        pumping_energy = effective_withdrawal * (1.0 + pumping_head_penalty)
        fossil_energy_exposure = pumping_energy * (1.0 - renewable_share)

        soil_health = clamp(
            soil_health + regeneration - scenario.climate_stress * 2.0 - effective_withdrawal * 0.015,
            0.0,
            100.0,
        )

        water_security = clamp((groundwater / scenario.initial_groundwater) * 100.0)
        food_production = clamp(
            35.0
            + water_security * 0.25
            + soil_health * 0.35
            - scenario.climate_stress * 22.0
            - scenario.energy_price_index * fossil_energy_exposure * 0.015
        )
        energy_security = clamp(
            100.0
            - fossil_energy_exposure * 0.25
            - scenario.energy_price_index * 10.0
            + renewable_share * 20.0
        )
        nexus_stress = clamp(
            (100.0 - food_production) * 0.30
            + (100.0 - water_security) * 0.30
            + (100.0 - energy_security) * 0.20
            + scenario.climate_stress * 60.0 * 0.10
            + scenario.vulnerability_index * 0.10
        )
        resilience_index = clamp(
            100.0 - nexus_stress + soil_health * 0.10 + renewable_share * 10.0 - depletion_ratio * 20.0
        )

        rows.append(
            {
                "year": year,
                "scenario": scenario.name,
                "policy_active": policy_active,
                "groundwater_stock": round(groundwater, 3),
                "effective_withdrawal": round(effective_withdrawal, 3),
                "pumping_energy": round(pumping_energy, 3),
                "fossil_energy_exposure": round(fossil_energy_exposure, 3),
                "soil_health": round(soil_health, 3),
                "food_production_index": round(food_production, 3),
                "water_security_index": round(water_security, 3),
                "energy_security_index": round(energy_security, 3),
                "nexus_stress_index": round(nexus_stress, 3),
                "resilience_index": round(resilience_index, 3),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    scenario_names = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []
    for name in scenario_names:
        subset = [row for row in rows if row["scenario"] == name]
        final = subset[-1]
        min_groundwater = min(float(row["groundwater_stock"]) for row in subset)
        avg_stress = mean(float(row["nexus_stress_index"]) for row in subset)
        avg_resilience = mean(float(row["resilience_index"]) for row in subset)
        years_high_stress = sum(float(row["nexus_stress_index"]) >= 60.0 for row in subset)
        diagnostic = (
            "high nexus fragility"
            if years_high_stress >= 10
            else "moderate stress requiring redesign"
            if avg_stress >= 40.0
            else "comparatively resilient pathway"
        )
        summary.append(
            {
                "scenario": name,
                "final_groundwater_stock": final["groundwater_stock"],
                "minimum_groundwater_stock": round(min_groundwater, 3),
                "final_food_production_index": final["food_production_index"],
                "final_water_security_index": final["water_security_index"],
                "final_energy_security_index": final["energy_security_index"],
                "average_nexus_stress_index": round(avg_stress, 3),
                "average_resilience_index": round(avg_resilience, 3),
                "years_high_stress": years_high_stress,
                "diagnostic": diagnostic,
            }
        )
    return summary


def write_synthetic_inputs() -> None:
    scenario_rows = [s.__dict__ for s in scenarios()]
    write_csv(DATA / "synthetic_policy_scenarios.csv", scenario_rows)
    # Lightweight indicator tables for downstream SQL/R examples.
    write_csv(
        DATA / "synthetic_resource_indicators.csv",
        [
            {"indicator": "groundwater_stock", "unit": "index", "system": "water"},
            {"indicator": "food_production_index", "unit": "index", "system": "food"},
            {"indicator": "energy_security_index", "unit": "index", "system": "energy"},
            {"indicator": "nexus_stress_index", "unit": "index", "system": "integrated"},
            {"indicator": "resilience_index", "unit": "index", "system": "integrated"},
        ],
    )


def main() -> None:
    ensure_dirs()
    write_synthetic_inputs()
    all_rows: list[dict[str, object]] = []
    for scenario in scenarios():
        all_rows.extend(run_scenario(scenario))
    summary_rows = summarize(all_rows)
    write_csv(TABLES / "food_water_energy_nexus_timeseries.csv", all_rows)
    write_csv(TABLES / "food_water_energy_nexus_summary.csv", summary_rows)
    with (TABLES / "food_water_energy_nexus_summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary_rows, handle, indent=2)
    print("\nFood-water-energy nexus scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: final groundwater={row['final_groundwater_stock']}, "
            f"avg stress={row['average_nexus_stress_index']}, diagnostic={row['diagnostic']}"
        )


if __name__ == "__main__":
    main()
