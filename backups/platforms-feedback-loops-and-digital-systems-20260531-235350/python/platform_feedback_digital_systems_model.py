#!/usr/bin/env python3
"""Dependency-light platform feedback model.

This model represents digital platforms as feedback systems whose outcomes emerge
from engagement amplification, creator adaptation, moderation capacity,
platform dependency, governance readiness, public value, and trust.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ROOT / "outputs" / "tables"


@dataclass(frozen=True)
class PlatformScenario:
    name: str
    periods: int
    initial_engagement: float
    amplification_strength: float
    harm_sensitivity: float
    moderation_capacity: float
    appeal_quality: float
    creator_adaptation_rate: float
    friction_strength: float
    transparency_strength: float
    portability_strength: float
    public_value_weight: float
    dependency_pressure: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: PlatformScenario) -> list[dict[str, float | str | int]]:
    engagement = scenario.initial_engagement
    creator_metric_pressure = 35.0
    harmful_cascade_risk = 22.0
    moderation_backlog = 18.0
    user_trust = 72.0
    platform_dependency = 45.0
    public_value = 50.0
    rows: list[dict[str, float | str | int]] = []

    for period in range(scenario.periods + 1):
        engagement = clamp(
            engagement
            + scenario.amplification_strength * 4.8
            + creator_metric_pressure * 0.05
            - scenario.friction_strength * 2.6
            - harmful_cascade_risk * 0.025
        )

        creator_metric_pressure = clamp(
            creator_metric_pressure
            + scenario.creator_adaptation_rate * engagement * 0.06
            - scenario.public_value_weight * 1.4
            - scenario.transparency_strength * 0.8
        )

        harmful_cascade_risk = clamp(
            harmful_cascade_risk
            + scenario.amplification_strength * engagement * 0.045
            + creator_metric_pressure * 0.045
            - scenario.harm_sensitivity * 2.8
            - scenario.friction_strength * 2.2
            - scenario.public_value_weight * 1.1
        )

        flagged_content = harmful_cascade_risk * 0.70 + engagement * 0.18
        governance_capacity = scenario.moderation_capacity * 60.0 + scenario.appeal_quality * 20.0
        moderation_backlog = clamp(moderation_backlog + flagged_content * 0.10 - governance_capacity * 0.06)

        platform_dependency = clamp(
            platform_dependency
            + scenario.dependency_pressure * 3.2
            + engagement * 0.025
            - scenario.portability_strength * 2.6
            - scenario.transparency_strength * 0.7
        )

        governance_readiness = clamp(
            scenario.moderation_capacity * 24.0
            + scenario.appeal_quality * 20.0
            + scenario.transparency_strength * 22.0
            + scenario.friction_strength * 14.0
            + scenario.portability_strength * 10.0
        )

        user_trust = clamp(
            user_trust
            - harmful_cascade_risk * 0.08
            - moderation_backlog * 0.06
            - platform_dependency * 0.025
            + governance_readiness * 0.09
            + scenario.public_value_weight * 1.2
        )

        public_value = clamp(
            35.0
            + user_trust * 0.22
            + governance_readiness * 0.18
            + scenario.public_value_weight * 14.0
            - harmful_cascade_risk * 0.16
            - creator_metric_pressure * 0.08
            - platform_dependency * 0.05
        )

        platform_risk = clamp(
            harmful_cascade_risk * 0.30
            + moderation_backlog * 0.22
            + creator_metric_pressure * 0.14
            + platform_dependency * 0.12
            - governance_readiness * 0.18
            - public_value * 0.08
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "engagement_index": round(engagement, 3),
                "creator_metric_pressure": round(creator_metric_pressure, 3),
                "harmful_cascade_risk": round(harmful_cascade_risk, 3),
                "moderation_backlog": round(moderation_backlog, 3),
                "platform_dependency": round(platform_dependency, 3),
                "governance_readiness": round(governance_readiness, 3),
                "user_trust": round(user_trust, 3),
                "public_value_index": round(public_value, 3),
                "platform_risk_index": round(platform_risk, 3),
            }
        )

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows supplied for {path}")
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
        avg_risk = mean(float(row["platform_risk_index"]) for row in subset)
        max_cascade = max(float(row["harmful_cascade_risk"]) for row in subset)
        max_backlog = max(float(row["moderation_backlog"]) for row in subset)
        min_trust = min(float(row["user_trust"]) for row in subset)
        avg_public_value = mean(float(row["public_value_index"]) for row in subset)

        summary.append(
            {
                "scenario": scenario_name,
                "final_platform_risk_index": final["platform_risk_index"],
                "average_platform_risk_index": round(avg_risk, 3),
                "maximum_harmful_cascade_risk": round(max_cascade, 3),
                "maximum_moderation_backlog": round(max_backlog, 3),
                "minimum_user_trust": round(min_trust, 3),
                "average_public_value_index": round(avg_public_value, 3),
                "final_platform_dependency": final["platform_dependency"],
                "diagnostic": (
                    "high-risk extractive platform pathway"
                    if avg_risk >= 40 or max_cascade >= 65
                    else "moderate risk requiring governance redesign"
                    if avg_risk >= 26 or max_backlog >= 45
                    else "comparatively accountable platform pathway"
                ),
            }
        )

    return summary


def build_scenarios() -> list[PlatformScenario]:
    return [
        PlatformScenario(
            name="Engagement-maximizing platform",
            periods=36,
            initial_engagement=62.0,
            amplification_strength=0.88,
            harm_sensitivity=0.12,
            moderation_capacity=0.22,
            appeal_quality=0.14,
            creator_adaptation_rate=0.82,
            friction_strength=0.08,
            transparency_strength=0.10,
            portability_strength=0.08,
            public_value_weight=0.10,
            dependency_pressure=0.72,
        ),
        PlatformScenario(
            name="Overloaded moderation",
            periods=36,
            initial_engagement=58.0,
            amplification_strength=0.70,
            harm_sensitivity=0.24,
            moderation_capacity=0.18,
            appeal_quality=0.24,
            creator_adaptation_rate=0.62,
            friction_strength=0.18,
            transparency_strength=0.18,
            portability_strength=0.14,
            public_value_weight=0.22,
            dependency_pressure=0.62,
        ),
        PlatformScenario(
            name="Balanced governance",
            periods=36,
            initial_engagement=52.0,
            amplification_strength=0.48,
            harm_sensitivity=0.68,
            moderation_capacity=0.66,
            appeal_quality=0.58,
            creator_adaptation_rate=0.40,
            friction_strength=0.54,
            transparency_strength=0.62,
            portability_strength=0.48,
            public_value_weight=0.58,
            dependency_pressure=0.36,
        ),
        PlatformScenario(
            name="Public-value platform design",
            periods=36,
            initial_engagement=48.0,
            amplification_strength=0.34,
            harm_sensitivity=0.82,
            moderation_capacity=0.76,
            appeal_quality=0.74,
            creator_adaptation_rate=0.28,
            friction_strength=0.70,
            transparency_strength=0.78,
            portability_strength=0.70,
            public_value_weight=0.82,
            dependency_pressure=0.24,
        ),
    ]


def main() -> None:
    ensure_outputs()
    all_rows: list[dict[str, object]] = []
    for scenario in build_scenarios():
        all_rows.extend(run_scenario(scenario))

    summary_rows = summarize(all_rows)

    write_csv(OUTPUT_TABLES / "platform_feedback_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "platform_feedback_summary.csv", summary_rows)

    print("\nPlatform feedback scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: avg risk={row['average_platform_risk_index']}, "
            f"max cascade={row['maximum_harmful_cascade_risk']}, "
            f"diagnostic={row['diagnostic']}"
        )


if __name__ == "__main__":
    main()
