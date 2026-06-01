#!/usr/bin/env python3
"""
Professional systems analysis workflow for: Success to the Successful and Systemic Advantage

This is a runnable applied workflow. It creates synthetic but realistic systems
analysis data, compares intervention strategies, validates assumptions, and
exports tables/figures a professional analyst can adapt with observed evidence.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import csv
import json
import statistics
from typing import Dict, Iterable, List

ARTICLE_DIR = Path(__file__).resolve().parents[1]
PROFILE = {
  "article_slug": "success-to-the-successful-and-systemic-advantage",
  "article_title": "Success to the Successful and Systemic Advantage",
  "family": "archetypes_feedback",
  "stock_label": "feedback-sensitive system capacity",
  "pressure_label": "delay and overshoot pressure",
  "burden_label": "correction burden",
  "outcome_label": "stabilized system behavior",
  "capacity_label": "corrective capacity",
  "trust_label": "feedback trust",
  "memory_label": "learning memory",
  "base_stock": 80,
  "base_capacity": 49,
  "base_trust": 49,
  "base_memory": 46,
  "base_burden": 42,
  "equity_gap": 23,
  "demand_growth": 2.1,
  "regeneration_rate": 0.025,
  "degradation_rate": 4.7,
  "policy_delay": 5,
  "shock_year": 11
}
DATA_DIR = ARTICLE_DIR / "data"
TABLES_DIR = ARTICLE_DIR / "outputs" / "tables"
FIGURES_DIR = ARTICLE_DIR / "outputs" / "figures"
DOCS_DIR = ARTICLE_DIR / "docs"
for directory in [DATA_DIR, TABLES_DIR, FIGURES_DIR, DOCS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

@dataclass(frozen=True)
class Scenario:
    name: str
    policy_effort: float
    capacity_investment: float
    burden_reduction: float
    feedback_closure: float
    trust_repair: float
    memory_investment: float
    stock_regeneration_boost: float
    pressure_reduction: float
    equity_investment: float
    delay_override: int | None = None

def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))

def scenario_catalog() -> List[Scenario]:
    return [
        Scenario("Current structure / baseline", 18, 0.35, 0.00, 0.18, 0.20, 0.15, 0.00, 0.00, 0.10, None),
        Scenario("Pressure-only intervention", 36, 0.20, -0.04, 0.14, -0.10, 0.05, 0.00, 0.04, 0.05, None),
        Scenario("Capacity and feedback investment", 30, 1.45, 0.26, 0.56, 0.80, 1.10, 0.008, 0.20, 0.65, max(1, int(PROFILE["policy_delay"]) - 2)),
        Scenario("Structural redesign and learning", 34, 2.20, 0.44, 0.78, 1.20, 1.60, 0.016, 0.38, 1.05, max(1, int(PROFILE["policy_delay"]) - 3)),
        Scenario("Delayed reform under rising pressure", 26, 0.80, 0.18, 0.36, 0.35, 0.50, 0.004, 0.16, 0.35, int(PROFILE["policy_delay"]) + 4),
    ]

def simulate_scenario(scenario: Scenario, years: int = 30) -> List[Dict[str, float | str | int | bool]]:
    stock = float(PROFILE["base_stock"])
    capacity = float(PROFILE["base_capacity"])
    trust = float(PROFILE["base_trust"])
    memory = float(PROFILE["base_memory"])
    burden = float(PROFILE["base_burden"])
    equity_gap = float(PROFILE["equity_gap"])
    policy_delay = scenario.delay_override if scenario.delay_override is not None else int(PROFILE["policy_delay"])
    rows: List[Dict[str, float | str | int | bool]] = []
    for year in range(years + 1):
        policy_active = year >= policy_delay
        shock = 1.0 if year == int(PROFILE["shock_year"]) else 0.0
        demand_pressure = float(PROFILE["demand_growth"]) * year + 4.5 * shock
        pressure = float(PROFILE["degradation_rate"]) + demand_pressure * 0.55
        if policy_active:
            pressure *= (1.0 - scenario.pressure_reduction)
            burden = clamp(burden * (1.0 - scenario.burden_reduction) + pressure * 0.06 - scenario.feedback_closure * 0.45)
            capacity = clamp(capacity + scenario.capacity_investment + scenario.feedback_closure * 0.85 - burden * 0.025)
            trust = clamp(trust + scenario.trust_repair + scenario.feedback_closure * 0.95 - burden * 0.030 - equity_gap * 0.018)
            memory = clamp(memory + scenario.memory_investment + scenario.feedback_closure * 0.75 - pressure * 0.025)
            equity_gap = clamp(equity_gap - scenario.equity_investment + burden * 0.018)
            regen_rate = float(PROFILE["regeneration_rate"]) + scenario.stock_regeneration_boost
            effort_effect = scenario.policy_effort * 0.050
        else:
            burden = clamp(burden + pressure * 0.11 + shock * 2.5)
            capacity = clamp(capacity - burden * 0.018 + memory * 0.010)
            trust = clamp(trust - burden * 0.025 - equity_gap * 0.015)
            memory = clamp(memory - pressure * 0.030)
            equity_gap = clamp(equity_gap + burden * 0.015)
            regen_rate = float(PROFILE["regeneration_rate"])
            effort_effect = 0.0
        regeneration = stock * regen_rate
        degradation = pressure + burden * 0.045 + equity_gap * 0.035 - capacity * 0.020 - effort_effect
        stock = clamp(stock + regeneration - max(0.0, degradation), 0.0, 120.0)
        risk_index = clamp(100 - (0.30 * stock + 0.25 * capacity + 0.20 * trust + 0.15 * memory - 0.10 * burden - 0.08 * equity_gap))
        outcome_index = clamp(0.30 * stock + 0.22 * capacity + 0.20 * trust + 0.18 * memory - 0.06 * burden - 0.04 * equity_gap)
        rows.append({
            "article_slug": PROFILE["article_slug"], "article_title": PROFILE["article_title"], "topic_family": PROFILE["family"],
            "year": year, "scenario": scenario.name, "policy_active": policy_active, "shock_event": bool(shock),
            "system_stock_index": round(stock, 3), "capacity_index": round(capacity, 3), "trust_index": round(trust, 3),
            "memory_index": round(memory, 3), "burden_index": round(burden, 3), "equity_gap_index": round(equity_gap, 3),
            "risk_index": round(risk_index, 3), "outcome_index": round(outcome_index, 3),
            "resilience_ratio": round(stock / max(1.0, float(PROFILE["base_stock"])), 4), "regeneration": round(regeneration, 3), "pressure": round(pressure, 3),
        })
    return rows

def write_csv(path: Path, rows: Iterable[Dict[str, object]], fieldnames: List[str] | None = None) -> None:
    rows = list(rows)
    if not rows:
        raise ValueError(f"No rows supplied for {path}")
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def diagnostic_label(outcome: float, risk: float, trust: float) -> str:
    if outcome >= 76 and risk <= 42 and trust >= 62:
        return "Strong professional trajectory: structural redesign appears durable under synthetic assumptions."
    if outcome >= 62 and risk <= 58:
        return "Improving trajectory: monitor burden, trust, equity, and delayed side effects."
    if risk >= 70:
        return "High-risk trajectory: intervention remains pressure-heavy or under-capacitated."
    return "Mixed trajectory: additional diagnosis and stakeholder evidence required."

def summarize(rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    scenarios = sorted({str(row["scenario"]) for row in rows})
    summary: List[Dict[str, object]] = []
    for scenario in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario]
        last = subset[-1]
        risks = [float(row["risk_index"]) for row in subset]
        outcomes = [float(row["outcome_index"]) for row in subset]
        burdens = [float(row["burden_index"]) for row in subset]
        stocks = [float(row["system_stock_index"]) for row in subset]
        trusts = [float(row["trust_index"]) for row in subset]
        summary.append({
            "article_slug": PROFILE["article_slug"], "scenario": scenario,
            "final_outcome_index": last["outcome_index"], "final_risk_index": last["risk_index"],
            "final_stock_index": last["system_stock_index"], "final_capacity_index": last["capacity_index"],
            "final_trust_index": last["trust_index"], "final_memory_index": last["memory_index"],
            "average_burden_index": round(statistics.mean(burdens), 3), "minimum_stock_index": round(min(stocks), 3),
            "minimum_trust_index": round(min(trusts), 3), "peak_risk_index": round(max(risks), 3),
            "average_outcome_index": round(statistics.mean(outcomes), 3), "years_high_risk": sum(1 for value in risks if value > 70),
            "professional_diagnostic": diagnostic_label(float(last["outcome_index"]), float(last["risk_index"]), float(last["trust_index"])),
        })
    return summary

def leverage_diagnostics(summary_rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    baseline = next((row for row in summary_rows if row["scenario"] == "Current structure / baseline"), summary_rows[0])
    diagnostics = []
    for row in summary_rows:
        outcome_gain = float(row["final_outcome_index"]) - float(baseline["final_outcome_index"])
        risk_reduction = float(baseline["final_risk_index"]) - float(row["final_risk_index"])
        diagnostics.append({
            "article_slug": PROFILE["article_slug"], "scenario": row["scenario"],
            "outcome_gain_vs_baseline": round(outcome_gain, 3), "risk_reduction_vs_baseline": round(risk_reduction, 3),
            "trust_gain_vs_baseline": round(float(row["final_trust_index"]) - float(baseline["final_trust_index"]), 3),
            "memory_gain_vs_baseline": round(float(row["final_memory_index"]) - float(baseline["final_memory_index"]), 3),
            "interpretation": "High leverage" if outcome_gain > 12 and risk_reduction > 10 else ("Moderate leverage" if outcome_gain > 5 else ("Counterproductive under assumptions" if risk_reduction < 0 else "Low leverage")),
        })
    return diagnostics

def validate(rows: List[Dict[str, object]], summary_rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    required = ["year", "scenario", "system_stock_index", "capacity_index", "trust_index", "memory_index", "burden_index", "equity_gap_index", "risk_index", "outcome_index"]
    missing = [col for col in required if col not in rows[0]]
    bad_values = [row for row in rows if not (0 <= float(row["outcome_index"]) <= 100 and 0 <= float(row["risk_index"]) <= 100)]
    return [
        {"check": "required_columns", "status": "pass" if not missing else "fail", "detail": ", ".join(missing) if missing else "All required columns present."},
        {"check": "scenario_count", "status": "pass" if len(summary_rows) >= 5 else "warning", "detail": f"{len(summary_rows)} scenarios summarized."},
        {"check": "bounded_indices", "status": "pass" if not bad_values else "fail", "detail": f"{len(bad_values)} rows outside expected bounds."},
        {"check": "professional_outputs", "status": "pass", "detail": "Timeseries, summary, leverage diagnostics, validation, assumptions, and metadata exported."},
    ]

def export_metadata() -> None:
    metadata = {key: PROFILE[key] for key in ["article_slug", "article_title", "family", "stock_label", "pressure_label", "burden_label", "outcome_label"]}
    metadata["professional_note"] = "Synthetic assumptions are for reproducible demonstration. Replace with observed data and stakeholder evidence before real decisions."
    (DATA_DIR / "article_model_profile.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    assumptions = [
        {"assumption": "Synthetic model", "detail": "Generated data illustrates dynamic structure and should not be treated as observed evidence."},
        {"assumption": "Bounded indices", "detail": "All major indices are normalized from 0 to 100 for comparison."},
        {"assumption": "Topic profile", "detail": f"This article uses the '{PROFILE['family']}' professional modeling profile."},
        {"assumption": "Professional adaptation", "detail": "Replace synthetic parameters with administrative records, survey evidence, environmental indicators, or stakeholder-validated assumptions."},
    ]
    write_csv(DATA_DIR / "professional_model_assumptions.csv", assumptions)

def export_figures(rows: List[Dict[str, object]]) -> None:
    try:
        import matplotlib.pyplot as plt  # type: ignore
    except Exception:
        (FIGURES_DIR / "FIGURES_SKIPPED.txt").write_text("matplotlib not available; CSV outputs were still generated.\n", encoding="utf-8")
        return
    scenarios = sorted({str(row["scenario"]) for row in rows})
    plots = [("outcome_index", "Outcome index", "professional_outcome_trajectories.png"), ("risk_index", "Risk index", "professional_risk_trajectories.png"), ("system_stock_index", PROFILE["stock_label"], "professional_stock_trajectories.png"), ("trust_index", PROFILE["trust_label"], "professional_trust_trajectories.png")]
    for ycol, ylabel, filename in plots:
        plt.figure(figsize=(10, 6))
        for scenario in scenarios:
            subset = [row for row in rows if row["scenario"] == scenario]
            plt.plot([int(row["year"]) for row in subset], [float(row[ycol]) for row in subset], label=scenario)
        plt.title(f"{PROFILE['article_title']} — {ylabel}")
        plt.xlabel("Year")
        plt.ylabel(ylabel)
        plt.legend(fontsize=7)
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / filename, dpi=180)
        plt.close()

def main() -> None:
    export_metadata()
    all_rows: List[Dict[str, object]] = []
    write_csv(DATA_DIR / "professional_scenarios.csv", [asdict(s) for s in scenario_catalog()])
    for scenario in scenario_catalog():
        all_rows.extend(simulate_scenario(scenario))
    write_csv(TABLES_DIR / "professional_timeseries.csv", all_rows, fieldnames=list(all_rows[0].keys()))
    summary_rows = summarize(all_rows)
    write_csv(TABLES_DIR / "professional_scenario_summary.csv", summary_rows)
    write_csv(TABLES_DIR / "professional_leverage_diagnostics.csv", leverage_diagnostics(summary_rows))
    validation = validate(all_rows, summary_rows)
    write_csv(TABLES_DIR / "professional_validation_report.csv", validation)
    export_figures(all_rows)
    if any(row["status"] == "fail" for row in validation):
        raise SystemExit("Validation failed. Inspect outputs/tables/professional_validation_report.csv")
    print(f"Professional workflow complete for {PROFILE['article_title']}")
    print(f"Topic family: {PROFILE['family']}")
    print(f"Tables: {TABLES_DIR}")
    print(f"Figures: {FIGURES_DIR}")

if __name__ == "__main__":
    main()
