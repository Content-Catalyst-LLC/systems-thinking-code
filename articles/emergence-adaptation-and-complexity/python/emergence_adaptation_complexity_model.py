#!/usr/bin/env python3
"""Dependency-light emergence, adaptation, and complexity model.

This script simulates adaptive agents whose states evolve through local interaction,
institutional guidance, noise, diversity preservation, and shock response.
It uses only the Python standard library and writes reproducible CSV outputs.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
import os
import random
from statistics import mean, pstdev

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_TABLES = os.path.join(ROOT, "outputs", "tables")


@dataclass(frozen=True)
class ComplexityScenario:
    name: str
    agents: int
    periods: int
    interaction_strength: float
    adaptation_rate: float
    noise: float
    institutional_guidance: float
    diversity_floor: float
    shock_period: int
    shock_strength: float


def ensure_outputs() -> None:
    os.makedirs(OUTPUT_TABLES, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def initialize_agents(count: int, seed: int) -> list[float]:
    rng = random.Random(seed)
    return [rng.random() for _ in range(count)]


def neighbor_average(values: list[float], index: int, radius: int = 2) -> float:
    count = len(values)
    neighbors = [values[(index + offset) % count] for offset in range(-radius, radius + 1) if offset != 0]
    return mean(neighbors)


def compute_clustering(values: list[float]) -> float:
    distances = [abs(values[i] - values[(i + 1) % len(values)]) for i in range(len(values))]
    return clamp(1.0 - mean(distances))


def compute_diversity(values: list[float]) -> float:
    return clamp(pstdev(values) * 3.0)


def compute_synchronization(values: list[float]) -> float:
    return clamp(1.0 - compute_diversity(values))


def compute_complexity_index(clustering: float, diversity: float, synchronization: float) -> float:
    # Complexity is highest between total disorder and total sameness.
    balance = 1.0 - abs(synchronization - 0.5) * 2.0
    return clamp(0.35 * clustering + 0.35 * diversity + 0.30 * balance)


def run_scenario(scenario: ComplexityScenario, seed: int = 42) -> list[dict[str, object]]:
    rng = random.Random(seed)
    values = initialize_agents(scenario.agents, seed)
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        clustering = compute_clustering(values)
        diversity = compute_diversity(values)
        synchronization = compute_synchronization(values)
        complexity_index = compute_complexity_index(clustering, diversity, synchronization)
        system_mean = mean(values)

        rows.append({
            "period": period,
            "scenario": scenario.name,
            "system_mean": round(system_mean, 4),
            "clustering_index": round(clustering, 4),
            "diversity_index": round(diversity, 4),
            "synchronization_index": round(synchronization, 4),
            "complexity_index": round(complexity_index, 4),
            "minimum_agent_state": round(min(values), 4),
            "maximum_agent_state": round(max(values), 4),
        })

        shock = scenario.shock_strength if period == scenario.shock_period else 0.0
        new_values: list[float] = []
        for i, current in enumerate(values):
            local_signal = neighbor_average(values, i)
            adaptive_target = (
                scenario.interaction_strength * local_signal
                + (1.0 - scenario.interaction_strength) * scenario.institutional_guidance
            )
            random_noise = rng.uniform(-scenario.noise, scenario.noise)
            updated = current + scenario.adaptation_rate * (adaptive_target - current) + random_noise - shock
            if scenario.diversity_floor > 0:
                updated = updated * (1.0 - scenario.diversity_floor) + rng.random() * scenario.diversity_floor
            new_values.append(clamp(updated))
        values = new_values

    return rows


def write_csv(path: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    scenarios = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []

    for scenario_name in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario_name]
        final = subset[-1]
        peak_complexity = max(float(row["complexity_index"]) for row in subset)
        average_complexity = mean(float(row["complexity_index"]) for row in subset)
        final_synchronization = float(final["synchronization_index"])
        final_diversity = float(final["diversity_index"])
        diagnostic = (
            "over-synchronized fragile pattern" if final_synchronization > 0.85 else
            "high volatility and weak coherence" if final_diversity > 0.85 else
            "adaptive complex pattern"
        )
        summary.append({
            "scenario": scenario_name,
            "final_complexity_index": final["complexity_index"],
            "peak_complexity_index": round(peak_complexity, 4),
            "average_complexity_index": round(average_complexity, 4),
            "final_clustering_index": final["clustering_index"],
            "final_diversity_index": final_diversity,
            "final_synchronization_index": final_synchronization,
            "diagnostic": diagnostic,
        })

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "system_mean",
        "clustering_index",
        "diversity_index",
        "synchronization_index",
        "complexity_index",
        "minimum_agent_state",
        "maximum_agent_state",
    ]
    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 1.001:
                errors.append(f"{field} outside 0-1 range in {row['scenario']} period {row['period']}: {value}")
    return errors


def build_scenarios() -> list[ComplexityScenario]:
    return [
        ComplexityScenario("Weak interaction baseline", 120, 60, 0.20, 0.12, 0.035, 0.55, 0.04, 999, 0.00),
        ComplexityScenario("Strong local conformity", 120, 60, 0.82, 0.28, 0.015, 0.55, 0.01, 999, 0.00),
        ComplexityScenario("Adaptive diversity", 120, 60, 0.55, 0.22, 0.030, 0.58, 0.10, 32, 0.10),
        ComplexityScenario("Guided resilient adaptation", 120, 60, 0.46, 0.18, 0.022, 0.62, 0.08, 32, 0.06),
    ]


def main() -> None:
    ensure_outputs()
    all_rows: list[dict[str, object]] = []
    for index, scenario in enumerate(build_scenarios()):
        all_rows.extend(run_scenario(scenario, seed=42 + index))

    validation_errors = validate(all_rows)
    if validation_errors:
        raise ValueError("Validation failed:\n" + "\n".join(validation_errors))

    summary_rows = summarize(all_rows)
    write_csv(os.path.join(OUTPUT_TABLES, "emergence_adaptation_complexity_timeseries.csv"), all_rows)
    write_csv(os.path.join(OUTPUT_TABLES, "emergence_adaptation_complexity_summary.csv"), summary_rows)

    with open(os.path.join(OUTPUT_TABLES, "validation_report.txt"), "w", encoding="utf-8") as handle:
        handle.write("Validation passed.\n")
        handle.write("Bounded indicators, complexity metrics, and scenario outputs completed.\n")

    print("\nEmergence, adaptation, and complexity scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: final complexity={row['final_complexity_index']}, "
            f"peak complexity={row['peak_complexity_index']}, diagnostic={row['diagnostic']}"
        )


if __name__ == "__main__":
    main()
