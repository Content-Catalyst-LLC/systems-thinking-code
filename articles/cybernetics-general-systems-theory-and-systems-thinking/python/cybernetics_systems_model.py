#!/usr/bin/env python3
"""
Dependency-light professional workflow for cybernetics, general systems theory, and systems thinking.

Purpose:
- Simulate feedback control, requisite variety, open-system exchange, adaptation,
  delay, trust, accountability, and regulation quality.
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
class CyberneticScenario:
    name: str
    periods: int
    initial_state: float
    reference_goal: float
    disturbance_variety: float
    response_variety: float
    feedback_quality: float
    feedback_delay: int
    control_strength: float
    adaptation_rate: float
    openness: float
    accountability_quality: float
    trust_level: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def delayed_value(history: list[float], delay: int) -> float:
    if len(history) <= delay:
        return history[0]
    return history[-delay - 1]


def run_scenario(scenario: CyberneticScenario) -> list[dict[str, object]]:
    state = scenario.initial_state
    response_variety = scenario.response_variety * 100.0
    trust = scenario.trust_level * 100.0
    learning_capacity = 38.0
    state_history = [state]
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        observed_state = delayed_value(state_history, scenario.feedback_delay)
        error = scenario.reference_goal - observed_state

        variety_gap = clamp(scenario.disturbance_variety * 100.0 - response_variety)

        control_action = clamp(
            abs(error) * scenario.control_strength
            + scenario.feedback_quality * 8.0
            - variety_gap * 0.08
        )

        disturbance_pressure = clamp(
            scenario.disturbance_variety * 9.0
            + scenario.openness * 3.0
            + period * 0.03
        )

        environmental_exchange = scenario.openness * 2.5 - scenario.accountability_quality * 1.4

        correction_direction = 1.0 if error >= 0 else -1.0
        state = clamp(
            state
            + correction_direction * control_action * 0.18
            - disturbance_pressure * 0.20
            + environmental_exchange
        )

        response_variety = clamp(
            response_variety
            + scenario.adaptation_rate * 3.2
            + scenario.feedback_quality * 1.6
            + scenario.accountability_quality * 1.4
            - variety_gap * 0.04
        )

        learning_capacity = clamp(
            learning_capacity
            + scenario.feedback_quality * 1.8
            + scenario.adaptation_rate * 2.2
            + scenario.accountability_quality * 1.6
            - max(0.0, 45.0 - trust) * 0.04
        )

        trust = clamp(
            trust
            + scenario.accountability_quality * 1.9
            + scenario.feedback_quality * 1.0
            - variety_gap * 0.05
            - abs(error) * 0.03
        )

        regulation_quality = clamp(
            100.0
            - abs(scenario.reference_goal - state) * 0.55
            - variety_gap * 0.30
            + response_variety * 0.18
            + learning_capacity * 0.18
            + trust * 0.10
        )

        accountability_index = clamp(
            scenario.accountability_quality * 45.0
            + trust * 0.25
            + scenario.feedback_quality * 20.0
            - variety_gap * 0.15
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "system_state": round(state, 3),
                "observed_state": round(observed_state, 3),
                "reference_goal": round(scenario.reference_goal, 3),
                "error_signal": round(error, 3),
                "control_action": round(control_action, 3),
                "disturbance_pressure": round(disturbance_pressure, 3),
                "response_variety": round(response_variety, 3),
                "variety_gap": round(variety_gap, 3),
                "learning_capacity": round(learning_capacity, 3),
                "trust_index": round(trust, 3),
                "regulation_quality": round(regulation_quality, 3),
                "accountability_index": round(accountability_index, 3),
            }
        )

        state_history.append(state)

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
        avg_variety_gap = mean(float(row["variety_gap"]) for row in subset)
        avg_regulation = mean(float(row["regulation_quality"]) for row in subset)
        avg_accountability = mean(float(row["accountability_index"]) for row in subset)
        avg_error = mean(abs(float(row["error_signal"])) for row in subset)

        if avg_variety_gap <= 15 and avg_regulation >= 65 and avg_accountability >= 60:
            diagnostic = "accountable adaptive regulation"
        elif avg_variety_gap >= 35:
            diagnostic = "response variety insufficient for disturbance variety"
        elif avg_error >= 25:
            diagnostic = "feedback delay or weak regulation creates persistent error"
        else:
            diagnostic = "partial regulation with remaining systems risk"

        summary.append(
            {
                "scenario": scenario_name,
                "final_system_state": final["system_state"],
                "final_response_variety": final["response_variety"],
                "average_variety_gap": round(avg_variety_gap, 3),
                "average_regulation_quality": round(avg_regulation, 3),
                "average_accountability_index": round(avg_accountability, 3),
                "average_absolute_error": round(avg_error, 3),
                "final_learning_capacity": final["learning_capacity"],
                "final_trust_index": final["trust_index"],
                "diagnostic": diagnostic,
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "system_state",
        "observed_state",
        "reference_goal",
        "control_action",
        "disturbance_pressure",
        "response_variety",
        "variety_gap",
        "learning_capacity",
        "trust_index",
        "regulation_quality",
        "accountability_index",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

        error_value = float(row["error_signal"])
        if error_value < -120.001 or error_value > 120.001:
            errors.append(f"error_signal outside expected range in {row['scenario']} period {row['period']}: {error_value}")

    return errors


def build_scenarios() -> list[CyberneticScenario]:
    return [
        CyberneticScenario(
            name="Rigid control",
            periods=48,
            initial_state=46.0,
            reference_goal=70.0,
            disturbance_variety=0.72,
            response_variety=0.34,
            feedback_quality=0.34,
            feedback_delay=8,
            control_strength=0.46,
            adaptation_rate=0.18,
            openness=0.48,
            accountability_quality=0.22,
            trust_level=0.42,
        ),
        CyberneticScenario(
            name="Delayed feedback",
            periods=48,
            initial_state=46.0,
            reference_goal=70.0,
            disturbance_variety=0.66,
            response_variety=0.46,
            feedback_quality=0.42,
            feedback_delay=10,
            control_strength=0.62,
            adaptation_rate=0.26,
            openness=0.54,
            accountability_quality=0.34,
            trust_level=0.46,
        ),
        CyberneticScenario(
            name="Adaptive regulation",
            periods=48,
            initial_state=46.0,
            reference_goal=70.0,
            disturbance_variety=0.62,
            response_variety=0.62,
            feedback_quality=0.66,
            feedback_delay=4,
            control_strength=0.48,
            adaptation_rate=0.62,
            openness=0.58,
            accountability_quality=0.58,
            trust_level=0.58,
        ),
        CyberneticScenario(
            name="Accountable learning system",
            periods=48,
            initial_state=46.0,
            reference_goal=70.0,
            disturbance_variety=0.58,
            response_variety=0.70,
            feedback_quality=0.78,
            feedback_delay=3,
            control_strength=0.42,
            adaptation_rate=0.78,
            openness=0.64,
            accountability_quality=0.82,
            trust_level=0.66,
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

    write_csv(OUTPUT_TABLES / "cybernetics_systems_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "cybernetics_systems_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Feedback, variety, adaptation, regulation, trust, and accountability outputs completed.\n",
        encoding="utf-8",
    )

    print("\nCybernetics and systems scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: variety gap={row['average_variety_gap']}, "
            f"regulation quality={row['average_regulation_quality']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'cybernetics_systems_timeseries.csv'}")


if __name__ == "__main__":
    main()
