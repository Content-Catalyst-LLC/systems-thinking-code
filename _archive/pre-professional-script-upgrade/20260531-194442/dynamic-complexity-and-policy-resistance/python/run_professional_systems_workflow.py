#!/usr/bin/env python3
"""
Professional systems-thinking workflow for this article folder.

This script is designed to be useful beyond a classroom demo. It creates a
synthetic but realistic systems-analysis dataset, compares intervention
scenarios, runs validation checks, and exports tables/figures that can be
adapted by policy analysts, sustainability analysts, organizational researchers,
governance teams, resilience practitioners, and systems modelers.

Outputs:
- outputs/tables/professional_systems_scenario_timeseries.csv
- outputs/tables/professional_systems_scenario_summary.csv
- outputs/tables/professional_leverage_diagnostics.csv
- outputs/tables/professional_validation_report.csv
- outputs/figures/professional_outcome_trajectories.png (if matplotlib exists)
- outputs/figures/professional_stock_trajectories.png (if matplotlib exists)
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import csv
import json
import math
import statistics
from typing import Dict, Iterable, List


ARTICLE_DIR = Path(__file__).resolve().parents[1]
ARTICLE_SLUG = ARTICLE_DIR.name
ARTICLE_TITLE = ARTICLE_SLUG.replace("-", " ").title()

DATA_DIR = ARTICLE_DIR / "data"
OUTPUT_TABLES = ARTICLE_DIR / "outputs" / "tables"
OUTPUT_FIGURES = ARTICLE_DIR / "outputs" / "figures"
DOCS_DIR = ARTICLE_DIR / "docs"

for path in (DATA_DIR, OUTPUT_TABLES, OUTPUT_FIGURES, DOCS_DIR):
    path.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class TopicProfile:
    article_slug: str
    article_title: str
    primary_stock_label: str
    pressure_label: str
    burden_label: str
    outcome_label: str
    base_capacity: float
    base_trust: float
    base_memory: float
    base_stock: float
    demand_growth: float
    extraction_pressure: float
    regeneration_rate: float
    degradation_rate: float
    equity_gap: float
    policy_delay: int


@dataclass(frozen=True)
class Scenario:
    name: str
    policy_effort: float
    capacity_investment: float
    burden_reduction: float
    feedback_closure: float
    trust_repair: float
    memory_investment: float
    extraction_reduction: float
    rebound_risk: float
    equity_investment: float
    delay_override: int | None = None


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def slug_contains(*terms: str) -> bool:
    return any(term in ARTICLE_SLUG for term in terms)


def infer_topic_profile() -> TopicProfile:
    """Infer a practical article-specific model profile from the folder slug."""
    title = ARTICLE_TITLE

    if slug_contains("sustainability", "climate", "food-water-energy", "urban", "public-health", "ecological", "resilience"):
        return TopicProfile(
            article_slug=ARTICLE_SLUG,
            article_title=title,
            primary_stock_label="ecological and social resilience stock",
            pressure_label="resource and climate pressure",
            burden_label="transition and vulnerability burden",
            outcome_label="sustainable public value",
            base_capacity=52,
            base_trust=55,
            base_memory=48,
            base_stock=86,
            demand_growth=2.1,
            extraction_pressure=7.5,
            regeneration_rate=0.030,
            degradation_rate=4.6,
            equity_gap=26,
            policy_delay=5,
        )

    if slug_contains("policy", "governance", "institutions", "institutional"):
        return TopicProfile(
            article_slug=ARTICLE_SLUG,
            article_title=title,
            primary_stock_label="public trust and institutional capacity stock",
            pressure_label="administrative and political pressure",
            burden_label="administrative burden",
            outcome_label="public value outcome",
            base_capacity=49,
            base_trust=52,
            base_memory=46,
            base_stock=78,
            demand_growth=1.8,
            extraction_pressure=5.2,
            regeneration_rate=0.024,
            degradation_rate=3.8,
            equity_gap=31,
            policy_delay=4,
        )

    if slug_contains("burnout", "organizations", "learning", "mental-models", "memory"):
        return TopicProfile(
            article_slug=ARTICLE_SLUG,
            article_title=title,
            primary_stock_label="organizational learning and human capacity stock",
            pressure_label="workload and coordination pressure",
            burden_label="hidden labor and rework burden",
            outcome_label="organizational learning outcome",
            base_capacity=47,
            base_trust=50,
            base_memory=44,
            base_stock=74,
            demand_growth=2.3,
            extraction_pressure=6.8,
            regeneration_rate=0.022,
            degradation_rate=4.9,
            equity_gap=24,
            policy_delay=3,
        )

    if slug_contains("stocks", "flows", "simulation", "scenario", "sensitivity", "dynamic", "causal"):
        return TopicProfile(
            article_slug=ARTICLE_SLUG,
            article_title=title,
            primary_stock_label="system stock and dynamic capacity",
            pressure_label="dynamic complexity pressure",
            burden_label="model uncertainty and intervention burden",
            outcome_label="system performance outcome",
            base_capacity=51,
            base_trust=50,
            base_memory=49,
            base_stock=82,
            demand_growth=1.9,
            extraction_pressure=6.0,
            regeneration_rate=0.026,
            degradation_rate=4.2,
            equity_gap=21,
            policy_delay=4,
        )

    if slug_contains("feedback", "delay", "overshoot", "collapse", "resistance"):
        return TopicProfile(
            article_slug=ARTICLE_SLUG,
            article_title=title,
            primary_stock_label="feedback-sensitive system stock",
            pressure_label="delay and overshoot pressure",
            burden_label="correction and adaptation burden",
            outcome_label="stabilized system outcome",
            base_capacity=48,
            base_trust=49,
            base_memory=47,
            base_stock=80,
            demand_growth=2.2,
            extraction_pressure=6.4,
            regeneration_rate=0.023,
            degradation_rate=4.7,
            equity_gap=23,
            policy_delay=6,
        )

    return TopicProfile(
        article_slug=ARTICLE_SLUG,
        article_title=title,
        primary_stock_label="core system capacity stock",
        pressure_label="system pressure",
        burden_label="implementation burden",
        outcome_label="system outcome",
        base_capacity=50,
        base_trust=50,
        base_memory=45,
        base_stock=80,
        demand_growth=2.0,
        extraction_pressure=6.0,
        regeneration_rate=0.025,
        degradation_rate=4.0,
        equity_gap=25,
        policy_delay=4,
    )


def scenario_catalog() -> List[Scenario]:
    return [
        Scenario(
            name="Baseline / current structure",
            policy_effort=22,
            capacity_investment=0.35,
            burden_reduction=0.20,
            feedback_closure=0.22,
            trust_repair=0.10,
            memory_investment=0.25,
            extraction_reduction=0.00,
            rebound_risk=0.08,
            equity_investment=0.10,
        ),
        Scenario(
            name="Pressure-only intervention",
            policy_effort=38,
            capacity_investment=0.25,
            burden_reduction=0.05,
            feedback_closure=0.18,
            trust_repair=-0.25,
            memory_investment=0.10,
            extraction_reduction=0.05,
            rebound_risk=0.18,
            equity_investment=0.05,
        ),
        Scenario(
            name="Capacity-building intervention",
            policy_effort=30,
            capacity_investment=1.35,
            burden_reduction=0.85,
            feedback_closure=0.48,
            trust_repair=0.50,
            memory_investment=0.85,
            extraction_reduction=0.18,
            rebound_risk=0.06,
            equity_investment=0.55,
        ),
        Scenario(
            name="Structural redesign",
            policy_effort=34,
            capacity_investment=1.85,
            burden_reduction=1.35,
            feedback_closure=0.70,
            trust_repair=0.80,
            memory_investment=1.25,
            extraction_reduction=0.35,
            rebound_risk=0.02,
            equity_investment=0.90,
        ),
    ]


def simulate(profile: TopicProfile, scenario: Scenario, years: int = 30) -> List[Dict[str, float | str | bool]]:
    delay = scenario.delay_override if scenario.delay_override is not None else profile.policy_delay

    capacity = profile.base_capacity
    trust = profile.base_trust
    memory = profile.base_memory
    stock = profile.base_stock
    equity_gap = profile.equity_gap
    burden = 38 + (profile.equity_gap * 0.18)
    pressure = 42 + profile.demand_growth

    rows: List[Dict[str, float | str | bool]] = []

    for year in range(years + 1):
        active = year >= delay
        demand = 42 + (profile.demand_growth * year)

        effort = scenario.policy_effort if active else 0
        feedback_gain = scenario.feedback_closure if active else 0.05
        capacity_investment = scenario.capacity_investment if active else 0.10
        burden_reduction = scenario.burden_reduction if active else 0.0
        memory_investment = scenario.memory_investment if active else 0.05
        trust_repair = scenario.trust_repair if active else 0.0
        equity_investment = scenario.equity_investment if active else 0.0
        extraction_reduction = scenario.extraction_reduction if active else 0.0
        rebound_risk = scenario.rebound_risk if active else 0.0

        extraction = profile.extraction_pressure * (1.0 - extraction_reduction) * (1.0 + rebound_risk)
        degradation = profile.degradation_rate * (1.0 - (extraction_reduction * 0.55))
        regeneration = stock * profile.regeneration_rate * (1.0 + (capacity / 250.0))

        stock = clamp(stock + regeneration - extraction - degradation, 0, 120)

        pressure = clamp(
            pressure
            + (demand * 0.018)
            + (burden * 0.025)
            - (capacity * 0.020)
            - (feedback_gain * 1.1),
            0,
            100,
        )

        burden = clamp(
            burden
            + (pressure * 0.045)
            + (equity_gap * 0.020)
            - burden_reduction
            - (capacity * 0.010)
            - (feedback_gain * 0.8),
            0,
            100,
        )

        capacity = clamp(
            capacity
            + capacity_investment
            + (memory * 0.010)
            + (feedback_gain * 0.80)
            - (pressure * 0.020)
            - (burden * 0.012),
            0,
            100,
        )

        memory = clamp(
            memory
            + memory_investment
            + (feedback_gain * 1.35)
            - (pressure * 0.010)
            - (burden * 0.006),
            0,
            100,
        )

        equity_gap = clamp(equity_gap - equity_investment + (burden * 0.004), 0, 100)

        trust = clamp(
            trust
            + trust_repair
            + (feedback_gain * 1.35)
            + (capacity * 0.018)
            - (burden * 0.030)
            - (equity_gap * 0.025)
            - (pressure * 0.010),
            0,
            100,
        )

        resilience_index = clamp(
            0.26 * capacity
            + 0.22 * trust
            + 0.20 * memory
            + 0.22 * stock
            + 0.10 * (100 - burden),
            0,
            100,
        )

        outcome = clamp(
            0.28 * capacity
            + 0.22 * trust
            + 0.18 * memory
            + 0.17 * stock
            + 0.10 * effort
            + 0.05 * (100 - equity_gap)
            - 0.14 * burden,
            0,
            100,
        )

        overshoot_pressure = max(0.0, extraction + degradation - regeneration)
        risk_index = clamp(
            0.36 * pressure
            + 0.26 * burden
            + 0.18 * equity_gap
            + 0.12 * overshoot_pressure
            + 0.08 * (100 - resilience_index),
            0,
            100,
        )

        rows.append(
            {
                "article_slug": profile.article_slug,
                "article_title": profile.article_title,
                "year": year,
                "scenario": scenario.name,
                "active_intervention": active,
                "primary_stock_label": profile.primary_stock_label,
                "pressure_label": profile.pressure_label,
                "burden_label": profile.burden_label,
                "outcome_label": profile.outcome_label,
                "demand_index": round(demand, 3),
                "capacity_index": round(capacity, 3),
                "trust_index": round(trust, 3),
                "institutional_memory_index": round(memory, 3),
                "system_stock_index": round(stock, 3),
                "burden_index": round(burden, 3),
                "equity_gap_index": round(equity_gap, 3),
                "pressure_index": round(pressure, 3),
                "feedback_closure": round(feedback_gain, 3),
                "resilience_index": round(resilience_index, 3),
                "risk_index": round(risk_index, 3),
                "outcome_index": round(outcome, 3),
                "overshoot_pressure": round(overshoot_pressure, 3),
            }
        )

    return rows


def write_csv(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    rows = list(rows)
    if not rows:
        raise ValueError(f"No rows supplied for {path}")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    scenarios = sorted({str(r["scenario"]) for r in rows})
    summary: List[Dict[str, object]] = []

    for scenario in scenarios:
        srows = [r for r in rows if r["scenario"] == scenario]
        final = srows[-1]
        outcome_values = [float(r["outcome_index"]) for r in srows]
        risk_values = [float(r["risk_index"]) for r in srows]
        burden_values = [float(r["burden_index"]) for r in srows]
        trust_values = [float(r["trust_index"]) for r in srows]
        stock_values = [float(r["system_stock_index"]) for r in srows]

        summary.append(
            {
                "article_slug": ARTICLE_SLUG,
                "scenario": scenario,
                "final_outcome_index": round(float(final["outcome_index"]), 3),
                "final_risk_index": round(float(final["risk_index"]), 3),
                "final_capacity_index": round(float(final["capacity_index"]), 3),
                "final_trust_index": round(float(final["trust_index"]), 3),
                "final_memory_index": round(float(final["institutional_memory_index"]), 3),
                "final_stock_index": round(float(final["system_stock_index"]), 3),
                "average_outcome_index": round(statistics.mean(outcome_values), 3),
                "average_risk_index": round(statistics.mean(risk_values), 3),
                "average_burden_index": round(statistics.mean(burden_values), 3),
                "minimum_trust_index": round(min(trust_values), 3),
                "minimum_stock_index": round(min(stock_values), 3),
                "years_risk_above_70": sum(1 for v in risk_values if v > 70),
                "years_stock_below_50": sum(1 for v in stock_values if v < 50),
            }
        )

    return summary


def leverage_diagnostics(summary_rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    by_name = {str(row["scenario"]): row for row in summary_rows}
    baseline = by_name.get("Baseline / current structure")
    if baseline is None:
        raise ValueError("Missing baseline scenario")

    diagnostics: List[Dict[str, object]] = []
    for name, row in by_name.items():
        if name == "Baseline / current structure":
            continue
        outcome_delta = float(row["final_outcome_index"]) - float(baseline["final_outcome_index"])
        risk_delta = float(row["final_risk_index"]) - float(baseline["final_risk_index"])
        trust_delta = float(row["final_trust_index"]) - float(baseline["final_trust_index"])
        memory_delta = float(row["final_memory_index"]) - float(baseline["final_memory_index"])

        diagnostics.append(
            {
                "article_slug": ARTICLE_SLUG,
                "comparison": f"{name} vs baseline",
                "outcome_delta": round(outcome_delta, 3),
                "risk_delta": round(risk_delta, 3),
                "trust_delta": round(trust_delta, 3),
                "memory_delta": round(memory_delta, 3),
                "professional_interpretation": interpret_leverage(outcome_delta, risk_delta, trust_delta, memory_delta),
            }
        )
    return diagnostics


def interpret_leverage(outcome_delta: float, risk_delta: float, trust_delta: float, memory_delta: float) -> str:
    if outcome_delta > 15 and risk_delta < -10 and trust_delta > 5:
        return "High-leverage redesign: improves outcomes, lowers risk, and strengthens trust."
    if outcome_delta > 8 and risk_delta <= 0:
        return "Useful intervention: improves outcomes without increasing modeled risk."
    if outcome_delta > 0 and risk_delta > 8:
        return "Fragile improvement: outcome improves but risk also rises; inspect burden, trust, and equity effects."
    if memory_delta > 6 and trust_delta > 4:
        return "Learning-oriented improvement: strengthens institutional memory and trust."
    return "Low or uncertain leverage: intervention does not clearly improve system behavior."


def validation_report(rows: List[Dict[str, object]], summary_rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    checks: List[Dict[str, object]] = []

    expected_scenarios = 4
    observed_scenarios = len({str(r["scenario"]) for r in rows})
    expected_years = 31

    checks.append(
        {
            "article_slug": ARTICLE_SLUG,
            "check": "scenario_count",
            "status": "pass" if observed_scenarios == expected_scenarios else "fail",
            "detail": f"Observed {observed_scenarios}; expected {expected_scenarios}.",
        }
    )

    year_counts = {}
    for scenario in sorted({str(r["scenario"]) for r in rows}):
        year_counts[scenario] = len([r for r in rows if r["scenario"] == scenario])

    checks.append(
        {
            "article_slug": ARTICLE_SLUG,
            "check": "year_count_per_scenario",
            "status": "pass" if all(v == expected_years for v in year_counts.values()) else "fail",
            "detail": json.dumps(year_counts, sort_keys=True),
        }
    )

    bounded_columns = [
        "capacity_index",
        "trust_index",
        "institutional_memory_index",
        "system_stock_index",
        "burden_index",
        "equity_gap_index",
        "pressure_index",
        "resilience_index",
        "risk_index",
        "outcome_index",
    ]
    out_of_bounds = []
    for r in rows:
        for col in bounded_columns:
            value = float(r[col])
            if value < 0 or value > 120:
                out_of_bounds.append((r["scenario"], r["year"], col, value))

    checks.append(
        {
            "article_slug": ARTICLE_SLUG,
            "check": "bounded_indices",
            "status": "pass" if not out_of_bounds else "fail",
            "detail": "All modeled indices are within expected range." if not out_of_bounds else str(out_of_bounds[:5]),
        }
    )

    by_scenario = {str(row["scenario"]): row for row in summary_rows}
    baseline = by_scenario.get("Baseline / current structure")
    redesign = by_scenario.get("Structural redesign")
    if baseline and redesign:
        improves = float(redesign["final_outcome_index"]) >= float(baseline["final_outcome_index"])
        checks.append(
            {
                "article_slug": ARTICLE_SLUG,
                "check": "redesign_outcome_not_worse_than_baseline",
                "status": "pass" if improves else "warning",
                "detail": f"Baseline final outcome={baseline['final_outcome_index']}; redesign final outcome={redesign['final_outcome_index']}.",
            }
        )

    return checks


def write_metadata(profile: TopicProfile) -> None:
    metadata = {
        "article_slug": profile.article_slug,
        "article_title": profile.article_title,
        "workflow_type": "professional systems-thinking diagnostic workflow",
        "primary_stock_label": profile.primary_stock_label,
        "pressure_label": profile.pressure_label,
        "burden_label": profile.burden_label,
        "outcome_label": profile.outcome_label,
        "notes": [
            "Synthetic data is generated for reproducible professional demonstration.",
            "The workflow is intended for adaptation by analysts, researchers, public-sector teams, sustainability practitioners, and organizational systems professionals.",
            "Replace synthetic assumptions with observed data, stakeholder evidence, and domain-specific validation before using for real decisions.",
        ],
    }
    (DOCS_DIR / "professional_workflow_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def try_write_figures(rows: List[Dict[str, object]]) -> None:
    try:
        import matplotlib.pyplot as plt  # type: ignore
    except Exception as exc:
        (OUTPUT_FIGURES / "matplotlib_not_available.txt").write_text(
            f"matplotlib was not available, so figures were not generated.\n{exc}\n",
            encoding="utf-8",
        )
        return

    scenarios = sorted({str(r["scenario"]) for r in rows})

    for column, filename, ylabel in [
        ("outcome_index", "professional_outcome_trajectories.png", "Outcome index"),
        ("system_stock_index", "professional_stock_trajectories.png", "System stock index"),
        ("risk_index", "professional_risk_trajectories.png", "Risk index"),
    ]:
        plt.figure(figsize=(10, 6))
        for scenario in scenarios:
            srows = [r for r in rows if r["scenario"] == scenario]
            years = [int(r["year"]) for r in srows]
            values = [float(r[column]) for r in srows]
            plt.plot(years, values, label=scenario, linewidth=2)
        plt.title(f"{ARTICLE_TITLE}: {ylabel} by Scenario")
        plt.xlabel("Year")
        plt.ylabel(ylabel)
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUTPUT_FIGURES / filename, dpi=160)
        plt.close()


def main() -> None:
    profile = infer_topic_profile()
    scenarios = scenario_catalog()

    rows: List[Dict[str, object]] = []
    for scenario in scenarios:
        rows.extend(simulate(profile, scenario))

    summary_rows = summarize(rows)
    leverage_rows = leverage_diagnostics(summary_rows)
    validation_rows = validation_report(rows, summary_rows)

    write_csv(OUTPUT_TABLES / "professional_systems_scenario_timeseries.csv", rows)
    write_csv(OUTPUT_TABLES / "professional_systems_scenario_summary.csv", summary_rows)
    write_csv(OUTPUT_TABLES / "professional_leverage_diagnostics.csv", leverage_rows)
    write_csv(OUTPUT_TABLES / "professional_validation_report.csv", validation_rows)
    write_metadata(profile)
    try_write_figures(rows)

    failure_count = sum(1 for r in validation_rows if r["status"] == "fail")
    if failure_count:
        raise SystemExit(f"Validation failed for {ARTICLE_SLUG}; inspect professional_validation_report.csv")

    print(f"Professional systems workflow complete for: {ARTICLE_TITLE}")
    print(f"Tables: {OUTPUT_TABLES}")
    print(f"Figures: {OUTPUT_FIGURES}")


if __name__ == "__main__":
    main()
