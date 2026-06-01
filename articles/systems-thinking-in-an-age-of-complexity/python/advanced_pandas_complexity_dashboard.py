#!/usr/bin/env python3
"""
Optional advanced workflow for systems thinking in an age of complexity.

Requires:
  pandas
  matplotlib
  openpyxl

Install with:
  python -m pip install -r requirements-advanced.txt

The default repository does not require these dependencies. This script fails
gracefully with setup instructions when optional packages are missing.
"""

from __future__ import annotations

from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES_DIR = ARTICLE_ROOT / "outputs" / "tables"
FIGURES_DIR = ARTICLE_ROOT / "outputs" / "figures"

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ModuleNotFoundError as exc:
    print("Missing optional advanced dependency:", exc.name)
    print("Run:")
    print("  cd ~/Downloads/systems-thinking-code/articles/systems-thinking-in-an-age-of-complexity")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "systems_thinking_age_complexity_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_age_complexity_workflows.py first."
        )
    return path


def main() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(require_core_output())

    final = df.sort_values(["scenario", "period"]).groupby("scenario", as_index=False).tail(1)
    scenario_summary = (
        df.groupby("scenario", as_index=False)
        .agg(
            average_complexity_pressure=("complexity_pressure", "mean"),
            average_readiness=("systems_readiness_score", "mean"),
            average_harm=("harm_stock", "mean"),
            average_resilience=("resilience_stock", "mean"),
            average_learning=("learning_stock", "mean"),
            average_accountability=("accountability_score", "mean"),
            average_transformation=("transformation_capacity", "mean"),
        )
        .merge(
            final[["scenario", "systems_readiness_score", "harm_stock", "transformation_capacity"]],
            on="scenario",
            how="left",
        )
        .rename(
            columns={
                "systems_readiness_score": "final_systems_readiness_score",
                "harm_stock": "final_harm_stock",
                "transformation_capacity": "final_transformation_capacity",
            }
        )
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_complexity_systems_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_complexity_systems_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("complexity_pressure", "Complexity pressure", "advanced_complexity_pressure.png"),
        ("resilience_capacity", "Resilience capacity", "advanced_resilience_capacity.png"),
        ("feedback_amplification", "Feedback amplification", "advanced_feedback_amplification.png"),
        ("accountability_score", "Accountability score", "advanced_accountability.png"),
        ("harm_stock", "Harm stock", "advanced_harm_stock.png"),
        ("learning_stock", "Learning stock", "advanced_learning_stock.png"),
        ("transformation_capacity", "Transformation capacity", "advanced_transformation_capacity.png"),
        ("systems_readiness_score", "Systems readiness score", "advanced_systems_readiness.png"),
    ]:
        plt.figure(figsize=(11, 6))
        for scenario, subset in df.groupby("scenario"):
            plt.plot(subset["period"], subset[metric], linewidth=2, label=scenario)
        plt.title(label + " by Scenario")
        plt.xlabel("Period")
        plt.ylabel(label)
        plt.legend()
        plt.grid(True, alpha=0.25)
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / filename, dpi=150)
        plt.close()

    print("Advanced dashboard complete.")
    print(f"Wrote {workbook_path}")


if __name__ == "__main__":
    main()
