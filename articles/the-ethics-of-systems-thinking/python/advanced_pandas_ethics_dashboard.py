#!/usr/bin/env python3
"""
Optional advanced workflow for ethical systems diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/the-ethics-of-systems-thinking")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "ethical_systems_thinking_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_ethical_systems_workflows.py first."
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
            average_ethical_score=("ethical_system_score", "mean"),
            average_cumulative_harm=("cumulative_harm", "mean"),
            average_accountability=("accountability_index", "mean"),
            average_boundary_ethics=("boundary_ethics_score", "mean"),
            average_model_risk=("model_risk", "mean"),
            average_repair_stock=("repair_stock", "mean"),
        )
        .merge(final[["scenario", "ethical_system_score", "cumulative_harm", "repair_stock"]], on="scenario", how="left")
        .rename(columns={
            "ethical_system_score": "final_ethical_system_score",
            "cumulative_harm": "final_cumulative_harm",
            "repair_stock": "final_repair_stock",
        })
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_ethics_systems_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_ethics_systems_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("boundary_ethics_score", "Boundary ethics score", "advanced_boundary_ethics.png"),
        ("accountability_index", "Accountability index", "advanced_accountability.png"),
        ("cumulative_harm", "Cumulative harm", "advanced_cumulative_harm.png"),
        ("repair_stock", "Repair stock", "advanced_repair_stock.png"),
        ("ethical_leverage", "Ethical leverage", "advanced_ethical_leverage.png"),
        ("model_risk", "Model risk", "advanced_model_risk.png"),
        ("ethical_system_score", "Ethical system score", "advanced_ethical_system_score.png"),
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
