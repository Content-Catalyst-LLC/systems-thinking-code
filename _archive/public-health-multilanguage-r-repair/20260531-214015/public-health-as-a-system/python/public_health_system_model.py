#!/usr/bin/env python3
"""
Public health systems model.

Dependency-light professional workflow using only the Python standard library.
It compares scenarios for disease dynamics, care capacity, public trust,
health risk, prevention value, and intervention timing.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ROOT / "outputs" / "tables"
DATA_DIR = ROOT / "data"


@dataclass(frozen=True)
class PublicHealthScenario:
    name: str
    population: int
    initial_infected: int
    transmission_rate: float
    recovery_rate: float
    severe_case_rate: float
    care_capacity: float
    prevention_strength: float
    trust_initial: float
    trust_gain: float
    trust_loss_from_overload: float
    vulnerability_index: float
    intervention_start_week: int


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_scenarios(path: Path = DATA_DIR / "scenario_assumptions.csv") -> list[PublicHealthScenario]:
    scenarios: list[PublicHealthScenario] = []
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            scenarios.append(
                PublicHealthScenario(
                    name=row["scenario"],
                    population=int(row["population"]),
                    initial_infected=int(row["initial_infected"]),
                    transmission_rate=float(row["transmission_rate"]),
                    recovery_rate=float(row["recovery_rate"]),
                    severe_case_rate=float(row["severe_case_rate"]),
                    care_capacity=float(row["care_capacity"]),
                    prevention_strength=float(row["prevention_strength"]),
                    trust_initial=float(row["trust_initial"]),
                    trust_gain=float(row["trust_gain"]),
                    trust_loss_from_overload=float(row["trust_loss_from_overload"]),
                    vulnerability_index=float(row["vulnerability_index"]),
                    intervention_start_week=int(row["intervention_start_week"]),
                )
            )
    return scenarios


def run_scenario(scenario: PublicHealthScenario, weeks: int = 52) -> list[dict[str, object]]:
    susceptible = float(scenario.population - scenario.initial_infected)
    infected = float(scenario.initial_infected)
    recovered = 0.0
    trust = scenario.trust_initial
    care_capacity = scenario.care_capacity
    rows: list[dict[str, object]] = []

    for week in range(weeks + 1):
        intervention_active = week >= scenario.intervention_start_week
        prevention = scenario.prevention_strength if intervention_active else scenario.prevention_strength * 0.25

        if intervention_active:
            trust = clamp(trust + scenario.trust_gain)

        cooperation_effect = trust / 100.0
        effective_transmission = scenario.transmission_rate * (1.0 - prevention) * (1.0 - cooperation_effect * 0.30)

        new_infections = effective_transmission * susceptible * infected / scenario.population
        recoveries = scenario.recovery_rate * infected

        new_infections = min(new_infections, susceptible)
        recoveries = min(recoveries, infected)

        susceptible -= new_infections
        infected += new_infections - recoveries
        recovered += recoveries

        severe_cases = infected * scenario.severe_case_rate * (1.0 + scenario.vulnerability_index / 150.0)
        care_stress = severe_cases / max(care_capacity, 1.0)

        if care_stress > 1.0:
            overload_penalty = (care_stress - 1.0) * scenario.trust_loss_from_overload
            trust = clamp(trust - overload_penalty)
            care_capacity = max(1.0, care_capacity - overload_penalty * 0.35)
        else:
            care_capacity = min(scenario.care_capacity * 1.25, care_capacity + 0.5)

        health_risk_index = clamp(
            infected / scenario.population * 100.0 * 2.5
            + care_stress * 20.0
            + scenario.vulnerability_index * 0.35
            - trust * 0.12
        )

        prevention_value_index = clamp(
            prevention * 45.0
            + trust * 0.25
            + max(0.0, 1.0 - care_stress) * 25.0
            - scenario.vulnerability_index * 0.10
        )

        rows.append(
            {
                "week": week,
                "scenario": scenario.name,
                "intervention_active": intervention_active,
                "susceptible": round(susceptible, 3),
                "infected": round(infected, 3),
                "recovered": round(recovered, 3),
                "new_infections": round(new_infections, 3),
                "severe_cases": round(severe_cases, 3),
                "care_capacity": round(care_capacity, 3),
                "care_stress": round(care_stress, 3),
                "public_trust": round(trust, 3),
                "health_risk_index": round(health_risk_index, 3),
                "prevention_value_index": round(prevention_value_index, 3),
            }
        )

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    scenarios = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []

    for scenario_name in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario_name]
        peak_infected = max(float(row["infected"]) for row in subset)
        peak_care_stress = max(float(row["care_stress"]) for row in subset)
        average_trust = mean(float(row["public_trust"]) for row in subset)
        average_risk = mean(float(row["health_risk_index"]) for row in subset)
        overload_weeks = sum(float(row["care_stress"]) > 1.0 for row in subset)
        final = subset[-1]

        summary.append(
            {
                "scenario": scenario_name,
                "peak_infected": round(peak_infected, 3),
                "peak_care_stress": round(peak_care_stress, 3),
                "overload_weeks": overload_weeks,
                "average_public_trust": round(average_trust, 3),
                "average_health_risk_index": round(average_risk, 3),
                "final_public_trust": final["public_trust"],
                "final_prevention_value_index": final["prevention_value_index"],
                "diagnostic": (
                    "system overload risk"
                    if overload_weeks >= 8
                    else "moderate public health stress"
                    if average_risk >= 35
                    else "comparatively resilient public health pathway"
                ),
            }
        )

    return summary


def main() -> None:
    scenarios = load_scenarios()
    all_rows: list[dict[str, object]] = []
    for scenario in scenarios:
        all_rows.extend(run_scenario(scenario))

    summary_rows = summarize(all_rows)
    write_csv(OUTPUT_TABLES / "public_health_system_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "public_health_system_summary.csv", summary_rows)

    print("\nPublic health system scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: peak infected={row['peak_infected']}, "
            f"peak care stress={row['peak_care_stress']}, "
            f"diagnostic={row['diagnostic']}"
        )


if __name__ == "__main__":
    main()
