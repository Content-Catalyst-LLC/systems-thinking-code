#!/usr/bin/env python3
"""
Dependency-light professional workflow for Peter Senge and the learning organization.

Purpose:
- Simulate learning loops, defensive routines, mental model inquiry, shared vision,
  team learning, institutional memory, trust, and adaptive performance.
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
class LearningScenario:
    name: str
    periods: int
    feedback_quality: float
    psychological_safety: float
    mental_model_inquiry: float
    shared_vision_strength: float
    team_learning_quality: float
    systems_thinking_practice: float
    leadership_support: float
    performance_pressure: float
    blame_tendency: float
    turnover_pressure: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: LearningScenario) -> list[dict[str, object]]:
    learning_stock = 34.0
    institutional_memory = 42.0
    trust_stock = 48.0
    defensive_routines = scenario.blame_tendency * 60.0
    adaptive_capacity = 36.0
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        feedback_use = clamp(
            scenario.feedback_quality * 28.0
            + scenario.psychological_safety * 24.0
            + scenario.leadership_support * 16.0
            - defensive_routines * 0.20
        )

        inquiry_strength = clamp(
            scenario.mental_model_inquiry * 24.0
            + scenario.team_learning_quality * 18.0
            + scenario.systems_thinking_practice * 22.0
            - scenario.performance_pressure * 10.0
        )

        shared_alignment = clamp(
            scenario.shared_vision_strength * 28.0
            + trust_stock * 0.18
            + scenario.leadership_support * 14.0
            - defensive_routines * 0.12
        )

        defensive_routines = clamp(
            defensive_routines
            + scenario.performance_pressure * 2.4
            + scenario.blame_tendency * 2.8
            - scenario.psychological_safety * 3.0
            - scenario.mental_model_inquiry * 1.8
            - scenario.leadership_support * 1.5
        )

        learning_flow = clamp(
            feedback_use * 0.22
            + inquiry_strength * 0.24
            + scenario.team_learning_quality * 4.0
            + scenario.systems_thinking_practice * 4.5
            - defensive_routines * 0.08
        )

        forgetting_flow = clamp(
            scenario.turnover_pressure * 5.5
            + defensive_routines * 0.06
            + max(0.0, 50.0 - trust_stock) * 0.04
        )

        learning_stock = clamp(learning_stock + learning_flow - forgetting_flow)

        institutional_memory = clamp(
            institutional_memory
            + learning_flow * 0.35
            + scenario.leadership_support * 1.2
            - scenario.turnover_pressure * 3.2
        )

        trust_stock = clamp(
            trust_stock
            + feedback_use * 0.14
            + shared_alignment * 0.10
            + scenario.psychological_safety * 1.7
            - defensive_routines * 0.10
        )

        adaptive_capacity = clamp(
            adaptive_capacity
            + learning_stock * 0.05
            + institutional_memory * 0.04
            + scenario.systems_thinking_practice * 2.4
            + scenario.team_learning_quality * 2.0
            - defensive_routines * 0.08
        )

        organizational_performance = clamp(
            adaptive_capacity * 0.28
            + learning_stock * 0.22
            + trust_stock * 0.18
            + shared_alignment * 0.14
            + institutional_memory * 0.12
            - defensive_routines * 0.16
        )

        learning_capacity_score = clamp(
            scenario.systems_thinking_practice * 18.0
            + scenario.mental_model_inquiry * 16.0
            + scenario.shared_vision_strength * 16.0
            + scenario.team_learning_quality * 18.0
            + learning_stock * 0.22
            + institutional_memory * 0.12
            - defensive_routines * 0.14
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "feedback_use_index": round(feedback_use, 3),
                "inquiry_strength": round(inquiry_strength, 3),
                "shared_alignment": round(shared_alignment, 3),
                "defensive_routines_index": round(defensive_routines, 3),
                "learning_stock": round(learning_stock, 3),
                "institutional_memory_stock": round(institutional_memory, 3),
                "trust_stock": round(trust_stock, 3),
                "adaptive_capacity": round(adaptive_capacity, 3),
                "organizational_performance": round(organizational_performance, 3),
                "learning_capacity_score": round(learning_capacity_score, 3),
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
        avg_learning = mean(float(row["learning_capacity_score"]) for row in subset)
        avg_defensiveness = mean(float(row["defensive_routines_index"]) for row in subset)
        avg_performance = mean(float(row["organizational_performance"]) for row in subset)

        if float(final["learning_capacity_score"]) >= 65 and float(final["defensive_routines_index"]) <= 30:
            diagnostic = "learning organization pathway"
        elif avg_defensiveness >= 50:
            diagnostic = "defensive routines suppress organizational learning"
        elif avg_learning >= 50:
            diagnostic = "partial learning capacity with structural constraints"
        else:
            diagnostic = "low learning capacity"

        summary.append(
            {
                "scenario": scenario_name,
                "final_learning_capacity_score": final["learning_capacity_score"],
                "final_defensive_routines_index": final["defensive_routines_index"],
                "final_adaptive_capacity": final["adaptive_capacity"],
                "final_organizational_performance": final["organizational_performance"],
                "average_learning_capacity_score": round(avg_learning, 3),
                "average_defensive_routines_index": round(avg_defensiveness, 3),
                "average_organizational_performance": round(avg_performance, 3),
                "final_learning_stock": final["learning_stock"],
                "final_institutional_memory_stock": final["institutional_memory_stock"],
                "diagnostic": diagnostic,
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "feedback_use_index",
        "inquiry_strength",
        "shared_alignment",
        "defensive_routines_index",
        "learning_stock",
        "institutional_memory_stock",
        "trust_stock",
        "adaptive_capacity",
        "organizational_performance",
        "learning_capacity_score",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

    return errors


def build_scenarios() -> list[LearningScenario]:
    return [
        LearningScenario(
            name="Compliance culture",
            periods=48,
            feedback_quality=0.34,
            psychological_safety=0.30,
            mental_model_inquiry=0.24,
            shared_vision_strength=0.36,
            team_learning_quality=0.28,
            systems_thinking_practice=0.22,
            leadership_support=0.34,
            performance_pressure=0.68,
            blame_tendency=0.58,
            turnover_pressure=0.42,
        ),
        LearningScenario(
            name="Defensive performance culture",
            periods=48,
            feedback_quality=0.48,
            psychological_safety=0.24,
            mental_model_inquiry=0.30,
            shared_vision_strength=0.42,
            team_learning_quality=0.34,
            systems_thinking_practice=0.32,
            leadership_support=0.42,
            performance_pressure=0.86,
            blame_tendency=0.76,
            turnover_pressure=0.54,
        ),
        LearningScenario(
            name="Adaptive improvement culture",
            periods=48,
            feedback_quality=0.66,
            psychological_safety=0.60,
            mental_model_inquiry=0.58,
            shared_vision_strength=0.62,
            team_learning_quality=0.64,
            systems_thinking_practice=0.58,
            leadership_support=0.66,
            performance_pressure=0.50,
            blame_tendency=0.34,
            turnover_pressure=0.30,
        ),
        LearningScenario(
            name="Learning organization pathway",
            periods=48,
            feedback_quality=0.78,
            psychological_safety=0.78,
            mental_model_inquiry=0.76,
            shared_vision_strength=0.80,
            team_learning_quality=0.82,
            systems_thinking_practice=0.84,
            leadership_support=0.82,
            performance_pressure=0.42,
            blame_tendency=0.20,
            turnover_pressure=0.22,
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

    write_csv(OUTPUT_TABLES / "senge_learning_organization_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "senge_learning_organization_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Learning capacity, defensive routines, trust, memory, and adaptation outputs completed.\n",
        encoding="utf-8",
    )

    print("\nSenge learning organization scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: learning capacity={row['final_learning_capacity_score']}, "
            f"defensiveness={row['final_defensive_routines_index']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'senge_learning_organization_timeseries.csv'}")


if __name__ == "__main__":
    main()
