#!/usr/bin/env python3
"""
Optional advanced workflow for Senge learning organization diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/peter-senge-and-the-learning-organization")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "senge_learning_organization_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_senge_learning_organization_workflows.py first."
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
            average_learning_capacity=("learning_capacity_score", "mean"),
            average_defensive_routines=("defensive_routines_index", "mean"),
            average_feedback_use=("feedback_use_index", "mean"),
            average_trust=("trust_stock", "mean"),
            average_performance=("organizational_performance", "mean"),
            average_adaptive_capacity=("adaptive_capacity", "mean"),
        )
        .merge(final[["scenario", "learning_capacity_score", "defensive_routines_index", "adaptive_capacity"]], on="scenario", how="left")
        .rename(columns={
            "learning_capacity_score": "final_learning_capacity",
            "defensive_routines_index": "final_defensive_routines",
            "adaptive_capacity": "final_adaptive_capacity",
        })
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_senge_learning_organization_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_senge_learning_organization_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("feedback_use_index", "Feedback use index", "advanced_feedback_use.png"),
        ("inquiry_strength", "Inquiry strength", "advanced_inquiry.png"),
        ("shared_alignment", "Shared alignment", "advanced_shared_alignment.png"),
        ("defensive_routines_index", "Defensive routines index", "advanced_defensive_routines.png"),
        ("learning_stock", "Learning stock", "advanced_learning_stock.png"),
        ("institutional_memory_stock", "Institutional memory stock", "advanced_memory.png"),
        ("learning_capacity_score", "Learning capacity score", "advanced_learning_capacity.png"),
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
