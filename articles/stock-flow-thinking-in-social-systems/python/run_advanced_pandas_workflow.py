#!/usr/bin/env python3
"""
Optional advanced pandas workflow for ARTICLE_TITLE.

This script is intentionally separate from the dependency-light default workflows.
It uses pandas for richer scenario analysis, diagnostics, and exports when an
advanced environment is available. It fails gracefully with setup instructions
when pandas is not installed.
"""
from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

ARTICLE_SLUG = "stock-flow-thinking-in-social-systems"
ARTICLE_TITLE = "Stock Flow Thinking In Social Systems"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ROOT / "outputs" / "tables"
OUTPUT_FIGURES = ROOT / "outputs" / "figures"
DATA_DIR = ROOT / "data"


def has_module(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def require_pandas() -> None:
    if has_module("pandas"):
        return
    print("Optional dependency 'pandas' is not installed for this Python interpreter.")
    print("Standard-library workflows should still run. To enable this advanced workflow:")
    print("  cd ~/Downloads/systems-thinking-code")
    print("  ./scripts/setup_advanced_python_env.sh")
    print("  . .venv/bin/activate")
    print(f"  python articles/{ARTICLE_SLUG}/python/run_advanced_pandas_workflow.py")
    sys.exit(0)


def profile_for_slug(slug: str) -> dict[str, float | str]:
    text = slug.replace("-", " ")
    if any(token in text for token in ["resilience", "threshold", "regime", "collapse", "overshoot"]):
        return {
            "domain": "resilience_threshold",
            "primary_stock": "resilience_stock",
            "pressure_name": "system_pressure",
            "initial_stock": 78.0,
            "initial_pressure": 34.0,
            "pressure_growth": 2.25,
            "capacity_growth": 1.10,
            "burden_growth": 0.90,
        }
    if any(token in text for token in ["policy", "governance", "institution", "public"]):
        return {
            "domain": "policy_governance",
            "primary_stock": "public_trust_capacity",
            "pressure_name": "administrative_burden",
            "initial_stock": 64.0,
            "initial_pressure": 42.0,
            "pressure_growth": 1.55,
            "capacity_growth": 1.35,
            "burden_growth": 1.10,
        }
    if any(token in text for token in ["sustainability", "climate", "food", "water", "energy", "ecology", "urban"]):
        return {
            "domain": "sustainability",
            "primary_stock": "ecological_social_capacity",
            "pressure_name": "resource_pressure",
            "initial_stock": 82.0,
            "initial_pressure": 38.0,
            "pressure_growth": 1.95,
            "capacity_growth": 1.20,
            "burden_growth": 1.00,
        }
    if any(token in text for token in ["burnout", "organization", "learning", "memory", "mental"]):
        return {
            "domain": "organizational_learning",
            "primary_stock": "human_learning_capacity",
            "pressure_name": "workload_pressure",
            "initial_stock": 72.0,
            "initial_pressure": 45.0,
            "pressure_growth": 1.75,
            "capacity_growth": 1.25,
            "burden_growth": 1.20,
        }
    return {
        "domain": "general_systems",
        "primary_stock": "system_capacity",
        "pressure_name": "system_pressure",
        "initial_stock": 74.0,
        "initial_pressure": 40.0,
        "pressure_growth": 1.70,
        "capacity_growth": 1.20,
        "burden_growth": 1.00,
    }


def build_scenarios(pd):
    profile = profile_for_slug(ARTICLE_SLUG)
    scenarios = [
        {"scenario": "baseline_pressure", "redesign": 0.00, "learning": 0.20, "buffer": 0.10, "delay": 999},
        {"scenario": "delayed_response", "redesign": 0.12, "learning": 0.35, "buffer": 0.28, "delay": 14},
        {"scenario": "professional_redesign", "redesign": 0.32, "learning": 0.62, "buffer": 0.55, "delay": 5},
        {"scenario": "transformative_change", "redesign": 0.48, "learning": 0.78, "buffer": 0.68, "delay": 3},
    ]
    rows: list[dict[str, object]] = []
    for sc in scenarios:
        stock = float(profile["initial_stock"])
        pressure = float(profile["initial_pressure"])
        burden = 30.0
        for year in range(0, 31):
            active = year >= int(sc["delay"])
            redesign = float(sc["redesign"]) if active else 0.0
            learning = float(sc["learning"]) if active else float(sc["learning"]) * 0.25
            buffer = float(sc["buffer"]) if active else float(sc["buffer"]) * 0.15

            pressure = pressure + float(profile["pressure_growth"]) * (1.0 - redesign * 0.45)
            burden = max(0.0, burden + float(profile["burden_growth"]) - redesign * 3.2)
            recovery_gain = float(profile["capacity_growth"]) + learning * 4.1 + buffer * 2.7
            degradation = pressure * 0.045 + burden * 0.035
            stock = max(0.0, min(100.0, stock + recovery_gain - degradation))
            threshold_margin = stock - pressure
            vulnerability_index = max(0.0, min(100.0, 55.0 + burden * 0.35 + pressure * 0.18 - stock * 0.28))
            resilience_ratio = stock / max(pressure, 1.0)
            regime = (
                "shifted_regime" if threshold_margin <= 0 else
                "near_threshold" if threshold_margin <= 10 else
                "stressed_recoverable" if threshold_margin <= 25 else
                "resilient"
            )
            rows.append({
                "article_slug": ARTICLE_SLUG,
                "article_title": ARTICLE_TITLE,
                "domain_profile": profile["domain"],
                "scenario": sc["scenario"],
                "year": year,
                str(profile["primary_stock"]): round(stock, 3),
                str(profile["pressure_name"]): round(pressure, 3),
                "threshold_margin": round(threshold_margin, 3),
                "administrative_or_system_burden": round(burden, 3),
                "vulnerability_index": round(vulnerability_index, 3),
                "resilience_ratio": round(resilience_ratio, 4),
                "intervention_active": bool(active),
                "regime_classification": regime,
            })
    return pd.DataFrame(rows), profile


def main() -> int:
    require_pandas()
    import pandas as pd

    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    df, profile = build_scenarios(pd)
    primary_stock = str(profile["primary_stock"])
    pressure_name = str(profile["pressure_name"])

    summary = (
        df.groupby(["article_slug", "domain_profile", "scenario"], as_index=False)
        .agg(
            final_stock=(primary_stock, "last"),
            final_pressure=(pressure_name, "last"),
            minimum_threshold_margin=("threshold_margin", "min"),
            average_burden=("administrative_or_system_burden", "mean"),
            peak_vulnerability=("vulnerability_index", "max"),
            final_resilience_ratio=("resilience_ratio", "last"),
            years_near_threshold=("regime_classification", lambda s: int((s == "near_threshold").sum())),
            years_shifted=("regime_classification", lambda s: int((s == "shifted_regime").sum())),
        )
    )
    summary["professional_diagnostic"] = summary.apply(
        lambda row: "regime-shift risk" if row["years_shifted"] > 0 else
        "threshold warning" if row["years_near_threshold"] > 0 else
        "resilience maintained",
        axis=1,
    )

    df.to_csv(OUTPUT_TABLES / "advanced_pandas_scenario_timeseries.csv", index=False)
    summary.to_csv(OUTPUT_TABLES / "advanced_pandas_scenario_summary.csv", index=False)

    try:
        with pd.ExcelWriter(OUTPUT_TABLES / "advanced_pandas_workbook.xlsx") as writer:
            df.to_excel(writer, sheet_name="timeseries", index=False)
            summary.to_excel(writer, sheet_name="summary", index=False)
    except Exception as exc:  # optional openpyxl writer may be unavailable
        print(f"Excel export skipped: {exc}")

    if has_module("matplotlib"):
        import matplotlib.pyplot as plt
        pivot = df.pivot(index="year", columns="scenario", values="threshold_margin")
        ax = pivot.plot(figsize=(10, 5), linewidth=2)
        ax.axhline(0, linestyle="--", linewidth=1)
        ax.set_title(f"Advanced threshold margin scenarios: {ARTICLE_TITLE}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Threshold margin")
        fig = ax.get_figure()
        fig.tight_layout()
        fig.savefig(OUTPUT_FIGURES / "advanced_pandas_threshold_margin.png", dpi=160)
        plt.close(fig)

        pivot_stock = df.pivot(index="year", columns="scenario", values=primary_stock)
        ax2 = pivot_stock.plot(figsize=(10, 5), linewidth=2)
        ax2.set_title(f"Advanced system capacity scenarios: {ARTICLE_TITLE}")
        ax2.set_xlabel("Year")
        ax2.set_ylabel(primary_stock.replace("_", " ").title())
        fig2 = ax2.get_figure()
        fig2.tight_layout()
        fig2.savefig(OUTPUT_FIGURES / "advanced_pandas_system_capacity.png", dpi=160)
        plt.close(fig2)
    else:
        print("matplotlib not installed; advanced tables were exported without figures.")

    print("Advanced pandas workflow complete")
    print(summary.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
