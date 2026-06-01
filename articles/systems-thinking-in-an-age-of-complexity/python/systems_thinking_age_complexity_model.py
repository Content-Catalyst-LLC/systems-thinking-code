#!/usr/bin/env python3
"""
Dependency-light professional workflow for Systems Thinking in an Age of Complexity.

Purpose:
- Simulate complexity pressure, feedback amplification, resilience, learning,
  accountability, harm accumulation, boundary inclusion, and transformation capacity.
- Use only Python standard library.
- Write outputs relative to the article root, no matter where the script is launched.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ARTICLE_ROOT / "outputs" / "tables"


@dataclass
class ComplexityScenario:
    name: str
    periods: int
    interdependence: float
    feedback_intensity: float
    delay_pressure: float
    adaptation_rate: float
    uncertainty: float
    redundancy: float
    modularity: float
    learning_capacity: float
    trust: float
    response_variety: float
    boundary_inclusion: float
    accountability: float
    harm_exposure: float
    ethical_leverage: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: ComplexityScenario) -> list[dict[str, object]]:
    resilience_stock = 35.0
    trust_stock = scenario.trust * 55.0
    learning_stock = scenario.learning_capacity * 50.0
    harm_stock = scenario.harm_exposure * 45.0
    accountability_memory = scenario.accountability * 40.0
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        complexity_pressure = clamp(
            scenario.interdependence * 22.0
            + scenario.feedback_intensity * 22.0
            + scenario.delay_pressure * 18.0
            + scenario.adaptation_rate * 16.0
            + scenario.uncertainty * 22.0
        )

        resilience_capacity = clamp(
            scenario.redundancy * 18.0
            + scenario.modularity * 16.0
            + learning_stock * 0.22
            + trust_stock * 0.16
            + scenario.response_variety * 20.0
        )

        feedback_amplification = clamp(
            scenario.feedback_intensity * 24.0
            + scenario.interdependence * 16.0
            + scenario.delay_pressure * 14.0
            - resilience_capacity * 0.16
            - accountability_memory * 0.10
        )

        accountability_score = clamp(
            scenario.accountability * 28.0
            + scenario.boundary_inclusion * 22.0
            + accountability_memory * 0.20
            + trust_stock * 0.10
            + scenario.ethical_leverage * 16.0
        )

        harm_pressure = clamp(
            scenario.harm_exposure * 22.0
            + max(0.0, complexity_pressure - resilience_capacity) * 0.26
            + feedback_amplification * 0.16
            + max(0.0, 55.0 - accountability_score) * 0.20
            - scenario.ethical_leverage * 6.0
        )

        learning_flow = clamp(
            scenario.learning_capacity * 4.0
            + scenario.accountability * 3.2
            + scenario.boundary_inclusion * 2.8
            + trust_stock * 0.04
            - harm_pressure * 0.05
        )

        resilience_stock = clamp(
            resilience_stock
            + resilience_capacity * 0.08
            + learning_flow * 0.30
            - complexity_pressure * 0.05
            - harm_pressure * 0.04
        )

        learning_stock = clamp(
            learning_stock
            + learning_flow * 0.36
            + accountability_score * 0.06
            - scenario.delay_pressure * 1.2
        )

        trust_stock = clamp(
            trust_stock
            + accountability_score * 0.07
            + scenario.boundary_inclusion * 2.0
            + scenario.ethical_leverage * 1.6
            - harm_stock * 0.05
        )

        accountability_memory = clamp(
            accountability_memory
            + accountability_score * 0.08
            + scenario.ethical_leverage * 1.7
            - harm_pressure * 0.04
        )

        harm_stock = clamp(
            harm_stock
            + harm_pressure * 0.22
            - accountability_score * 0.08
            - scenario.ethical_leverage * 2.2
        )

        transformation_capacity = clamp(
            scenario.ethical_leverage * 26.0
            + learning_stock * 0.20
            + accountability_score * 0.22
            + resilience_stock * 0.16
            + scenario.boundary_inclusion * 14.0
            - harm_stock * 0.12
        )

        systems_readiness_score = clamp(
            resilience_stock * 0.22
            + learning_stock * 0.22
            + trust_stock * 0.16
            + accountability_score * 0.20
            + transformation_capacity * 0.24
            - complexity_pressure * 0.12
            - harm_stock * 0.16
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "complexity_pressure": round(complexity_pressure, 3),
                "resilience_capacity": round(resilience_capacity, 3),
                "feedback_amplification": round(feedback_amplification, 3),
                "accountability_score": round(accountability_score, 3),
                "harm_pressure": round(harm_pressure, 3),
                "resilience_stock": round(resilience_stock, 3),
                "learning_stock": round(learning_stock, 3),
                "trust_stock": round(trust_stock, 3),
                "accountability_memory": round(accountability_memory, 3),
                "harm_stock": round(harm_stock, 3),
                "transformation_capacity": round(transformation_capacity, 3),
                "systems_readiness_score": round(systems_readiness_score, 3),
            }
        )

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
    summary: list[dict[str, object]] = []

    for scenario_name in sorted({str(row["scenario"]) for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario_name]
        final = subset[-1]
        avg_complexity = mean(float(row["complexity_pressure"]) for row in subset)
        avg_readiness = mean(float(row["systems_readiness_score"]) for row in subset)
        avg_harm = mean(float(row["harm_stock"]) for row in subset)
        avg_accountability = mean(float(row["accountability_score"]) for row in subset)

        if float(final["systems_readiness_score"]) >= 65 and float(final["harm_stock"]) <= 35:
            diagnostic = "accountable transformation pathway"
        elif avg_complexity >= 65 and avg_readiness <= 45:
            diagnostic = "complexity exceeds institutional response capacity"
        elif avg_harm >= 55:
            diagnostic = "high harm accumulation requiring boundary and repair redesign"
        elif avg_accountability >= 55:
            diagnostic = "partial readiness with remaining complexity risk"
        else:
            diagnostic = "fragmented or brittle systems capacity"

        summary.append(
            {
                "scenario": scenario_name,
                "final_systems_readiness_score": final["systems_readiness_score"],
                "final_complexity_pressure": final["complexity_pressure"],
                "final_harm_stock": final["harm_stock"],
                "final_resilience_stock": final["resilience_stock"],
                "final_learning_stock": final["learning_stock"],
                "final_accountability_score": final["accountability_score"],
                "final_transformation_capacity": final["transformation_capacity"],
                "average_complexity_pressure": round(avg_complexity, 3),
                "average_systems_readiness_score": round(avg_readiness, 3),
                "average_harm_stock": round(avg_harm, 3),
                "diagnostic": diagnostic,
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "complexity_pressure",
        "resilience_capacity",
        "feedback_amplification",
        "accountability_score",
        "harm_pressure",
        "resilience_stock",
        "learning_stock",
        "trust_stock",
        "accountability_memory",
        "harm_stock",
        "transformation_capacity",
        "systems_readiness_score",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

    return errors


def build_scenarios() -> list[ComplexityScenario]:
    return [
        ComplexityScenario(
            name="Fragmented reaction",
            periods=48,
            interdependence=0.82,
            feedback_intensity=0.76,
            delay_pressure=0.74,
            adaptation_rate=0.34,
            uncertainty=0.80,
            redundancy=0.24,
            modularity=0.28,
            learning_capacity=0.26,
            trust=0.30,
            response_variety=0.30,
            boundary_inclusion=0.24,
            accountability=0.26,
            harm_exposure=0.78,
            ethical_leverage=0.18,
        ),
        ComplexityScenario(
            name="Optimized brittle system",
            periods=48,
            interdependence=0.76,
            feedback_intensity=0.70,
            delay_pressure=0.62,
            adaptation_rate=0.46,
            uncertainty=0.68,
            redundancy=0.28,
            modularity=0.34,
            learning_capacity=0.42,
            trust=0.42,
            response_variety=0.42,
            boundary_inclusion=0.36,
            accountability=0.38,
            harm_exposure=0.62,
            ethical_leverage=0.30,
        ),
        ComplexityScenario(
            name="Adaptive learning system",
            periods=48,
            interdependence=0.70,
            feedback_intensity=0.62,
            delay_pressure=0.52,
            adaptation_rate=0.66,
            uncertainty=0.60,
            redundancy=0.58,
            modularity=0.60,
            learning_capacity=0.68,
            trust=0.62,
            response_variety=0.68,
            boundary_inclusion=0.64,
            accountability=0.66,
            harm_exposure=0.42,
            ethical_leverage=0.58,
        ),
        ComplexityScenario(
            name="Accountable transformation pathway",
            periods=48,
            interdependence=0.68,
            feedback_intensity=0.58,
            delay_pressure=0.46,
            adaptation_rate=0.78,
            uncertainty=0.56,
            redundancy=0.72,
            modularity=0.72,
            learning_capacity=0.80,
            trust=0.74,
            response_variety=0.80,
            boundary_inclusion=0.82,
            accountability=0.82,
            harm_exposure=0.30,
            ethical_leverage=0.84,
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

    write_csv(OUTPUT_TABLES / "systems_thinking_age_complexity_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "systems_thinking_age_complexity_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Complexity, resilience, learning, accountability, harm, and transformation outputs completed.\n",
        encoding="utf-8",
    )

    print("\nSystems thinking in an age of complexity scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: readiness={row['final_systems_readiness_score']}, "
            f"harm={row['final_harm_stock']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'systems_thinking_age_complexity_timeseries.csv'}")


if __name__ == "__main__":
    main()
