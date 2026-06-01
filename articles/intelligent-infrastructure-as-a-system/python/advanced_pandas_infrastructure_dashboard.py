#!/usr/bin/env python3
"""
Optional advanced workflow for intelligent infrastructure diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/intelligent-infrastructure-as-a-system")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "intelligent_infrastructure_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_intelligent_infrastructure_workflows.py first."
        )
    return path


def main() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    path = require_core_output()
    df = pd.read_csv(path)

    yearly = (
        df.groupby(["scenario", "year"], as_index=False)
        .agg(
            average_risk_score=("risk_score", "mean"),
            average_resilience_score=("resilience_score", "mean"),
            average_cyber_dependency=("cyber_physical_dependency", "mean"),
            average_condition=("condition", "mean"),
        )
    )

    final_year = int(df["year"].max())
    final_assets = df[df["year"] == final_year].copy()
    final_assets["risk_rank"] = final_assets.groupby("scenario")["risk_score"].rank(
        method="dense", ascending=False
    )

    equity_priority = (
        final_assets.groupby(["scenario", "category"], as_index=False)
        .agg(
            mean_risk=("risk_score", "mean"),
            mean_resilience=("resilience_score", "mean"),
            mean_equity_priority=("equity_priority", "mean"),
            mean_cyber_dependency=("cyber_physical_dependency", "mean"),
        )
        .sort_values(["scenario", "mean_risk"], ascending=[True, False])
    )

    yearly.to_csv(TABLES_DIR / "advanced_yearly_infrastructure_dashboard.csv", index=False)
    final_assets.to_csv(TABLES_DIR / "advanced_final_asset_dashboard.csv", index=False)
    equity_priority.to_csv(TABLES_DIR / "advanced_equity_category_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_intelligent_infrastructure_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        yearly.to_excel(writer, sheet_name="yearly_indicators", index=False)
        final_assets.to_excel(writer, sheet_name="final_assets", index=False)
        equity_priority.to_excel(writer, sheet_name="equity_category", index=False)

    for metric, label, filename in [
        ("average_risk_score", "Average risk score", "advanced_risk_score.png"),
        ("average_resilience_score", "Average resilience score", "advanced_resilience_score.png"),
        ("average_cyber_dependency", "Average cyber-physical dependency", "advanced_cyber_dependency.png"),
        ("average_condition", "Average asset condition", "advanced_asset_condition.png"),
    ]:
        plt.figure(figsize=(11, 6))
        for scenario, subset in yearly.groupby("scenario"):
            plt.plot(subset["year"], subset[metric], linewidth=2, label=scenario)
        plt.title(label + " by Scenario")
        plt.xlabel("Year")
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
