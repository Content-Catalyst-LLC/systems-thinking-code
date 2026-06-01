#!/usr/bin/env python3
"""
Dependency-light professional workflow for complex adaptive systems and social change.

Purpose:
- Simulate social diffusion, adaptive agents, trust, resistance, institutional response,
  movement capacity, governance learning, legitimacy, and transformation momentum.
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
class SocialChangeScenario:
    name: str
    periods: int
    initial_adoption: float
    network_reach: float
    trust_level: float
    resource_capacity: float
    institutional_openness: float
    backlash_pressure: float
    learning_capacity: float
    participation_quality: float
    equity_alignment: float
    media_amplification: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: SocialChangeScenario) -> list[dict[str, object]]:
    adoption = scenario.initial_adoption
    trust = scenario.trust_level * 100.0
    resistance = scenario.backlash_pressure * 55.0
    institutional_response = scenario.institutional_openness * 35.0
    movement_capacity = scenario.resource_capacity * 45.0
    learning = scenario.learning_capacity * 45.0
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        diffusion_gain = (
            scenario.network_reach * adoption * (100.0 - adoption) / 100.0 * 0.075
            + scenario.media_amplification * 2.1
            + trust * 0.018
            + movement_capacity * 0.022
        )

        resistance_growth = (
            adoption * scenario.backlash_pressure * 0.042
            + scenario.media_amplification * scenario.backlash_pressure * 1.4
            - scenario.participation_quality * 1.2
            - scenario.equity_alignment * 1.0
        )

        resistance = clamp(resistance + resistance_growth - learning * 0.018)

        institutional_response = clamp(
            institutional_response
            + adoption * scenario.institutional_openness * 0.035
            + movement_capacity * 0.025
            + scenario.participation_quality * 1.1
            - resistance * 0.020
        )

        learning = clamp(
            learning
            + scenario.learning_capacity * 1.8
            + scenario.participation_quality * 1.4
            + institutional_response * 0.018
            - resistance * 0.010
        )

        trust = clamp(
            trust
            + institutional_response * 0.030
            + scenario.equity_alignment * 1.8
            + scenario.participation_quality * 1.4
            - resistance * 0.035
        )

        movement_capacity = clamp(
            movement_capacity
            + adoption * 0.025
            + trust * 0.020
            + scenario.resource_capacity * 1.5
            - resistance * 0.014
        )

        adoption = clamp(
            adoption
            + diffusion_gain
            + institutional_response * 0.018
            + learning * 0.016
            - resistance * 0.030
        )

        transformation_momentum = clamp(
            adoption * 0.28
            + trust * 0.18
            + institutional_response * 0.20
            + learning * 0.16
            + movement_capacity * 0.12
            + scenario.equity_alignment * 12.0
            - resistance * 0.22
        )

        legitimacy_index = clamp(
            trust * 0.32
            + scenario.participation_quality * 22.0
            + scenario.equity_alignment * 24.0
            + institutional_response * 0.18
            - resistance * 0.15
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "adoption_index": round(adoption, 3),
                "trust_index": round(trust, 3),
                "resistance_index": round(resistance, 3),
                "institutional_response_index": round(institutional_response, 3),
                "movement_capacity_index": round(movement_capacity, 3),
                "learning_capacity_index": round(learning, 3),
                "legitimacy_index": round(legitimacy_index, 3),
                "transformation_momentum": round(transformation_momentum, 3),
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
    scenarios = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []

    for scenario_name in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario_name]
        final = subset[-1]
        average_momentum = mean(float(row["transformation_momentum"]) for row in subset)
        peak_resistance = max(float(row["resistance_index"]) for row in subset)
        final_legitimacy = float(final["legitimacy_index"])
        final_adoption = float(final["adoption_index"])

        summary.append(
            {
                "scenario": scenario_name,
                "final_adoption_index": final_adoption,
                "final_legitimacy_index": final_legitimacy,
                "final_transformation_momentum": final["transformation_momentum"],
                "average_transformation_momentum": round(average_momentum, 3),
                "peak_resistance_index": round(peak_resistance, 3),
                "final_institutional_response_index": final["institutional_response_index"],
                "final_learning_capacity_index": final["learning_capacity_index"],
                "diagnostic": (
                    "transformational pathway"
                    if final_adoption >= 70 and final_legitimacy >= 60
                    else "contested change requiring deeper coalition and governance learning"
                    if peak_resistance >= 55
                    else "limited diffusion pathway"
                ),
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "adoption_index",
        "trust_index",
        "resistance_index",
        "institutional_response_index",
        "movement_capacity_index",
        "learning_capacity_index",
        "legitimacy_index",
        "transformation_momentum",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 100.001:
                errors.append(f"{field} outside 0-100 range in {row['scenario']} period {row['period']}: {value}")

    return errors


def main() -> None:
    ensure_outputs()

    scenarios = [
        SocialChangeScenario(
            name="Fragmented baseline",
            periods=48,
            initial_adoption=14.0,
            network_reach=0.32,
            trust_level=0.42,
            resource_capacity=0.30,
            institutional_openness=0.24,
            backlash_pressure=0.38,
            learning_capacity=0.28,
            participation_quality=0.30,
            equity_alignment=0.34,
            media_amplification=0.28,
        ),
        SocialChangeScenario(
            name="High backlash environment",
            periods=48,
            initial_adoption=18.0,
            network_reach=0.46,
            trust_level=0.38,
            resource_capacity=0.42,
            institutional_openness=0.30,
            backlash_pressure=0.78,
            learning_capacity=0.34,
            participation_quality=0.32,
            equity_alignment=0.36,
            media_amplification=0.64,
        ),
        SocialChangeScenario(
            name="Coalition learning strategy",
            periods=48,
            initial_adoption=18.0,
            network_reach=0.62,
            trust_level=0.54,
            resource_capacity=0.58,
            institutional_openness=0.52,
            backlash_pressure=0.42,
            learning_capacity=0.70,
            participation_quality=0.68,
            equity_alignment=0.66,
            media_amplification=0.48,
        ),
        SocialChangeScenario(
            name="Accountable transformation pathway",
            periods=48,
            initial_adoption=20.0,
            network_reach=0.70,
            trust_level=0.62,
            resource_capacity=0.68,
            institutional_openness=0.68,
            backlash_pressure=0.34,
            learning_capacity=0.82,
            participation_quality=0.82,
            equity_alignment=0.84,
            media_amplification=0.42,
        ),
    ]

    all_rows: list[dict[str, object]] = []
    for scenario in scenarios:
        all_rows.extend(run_scenario(scenario))

    validation_errors = validate(all_rows)
    if validation_errors:
        raise ValueError("Validation failed:\n" + "\n".join(validation_errors))

    summary_rows = summarize(all_rows)

    write_csv(OUTPUT_TABLES / "complex_adaptive_social_change_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "complex_adaptive_social_change_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Bounded indicators, adoption, resistance, legitimacy, learning, and transformation outputs completed.\n",
        encoding="utf-8",
    )

    print("\nComplex adaptive social change scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: final adoption={row['final_adoption_index']}, "
            f"momentum={row['final_transformation_momentum']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'complex_adaptive_social_change_timeseries.csv'}")


if __name__ == "__main__":
    main()
