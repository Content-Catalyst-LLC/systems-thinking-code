#!/usr/bin/env python3
"""
Optional advanced workflow for Meadows structural insight diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/donella-meadows-and-the-practice-of-structural-insight")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "meadows_structural_insight_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_meadows_structural_insight_workflows.py first."
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
            average_resource=("resource_stock", "mean"),
            minimum_resource=("resource_stock", "min"),
            average_overshoot=("overshoot_index", "mean"),
            average_leverage=("leverage_quality", "mean"),
            average_structural_insight=("structural_insight_score", "mean"),
            average_trust=("trust_stock", "mean"),
            average_resilience=("resilience_capacity", "mean"),
        )
        .merge(final[["scenario", "resource_stock", "structural_insight_score"]], on="scenario", how="left")
        .rename(columns={
            "resource_stock": "final_resource",
            "structural_insight_score": "final_structural_insight",
        })
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_meadows_structural_insight_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_meadows_structural_insight_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("resource_stock", "Resource stock", "advanced_resource_stock.png"),
        ("overshoot_index", "Overshoot index", "advanced_overshoot.png"),
        ("leverage_quality", "Leverage quality", "advanced_leverage_quality.png"),
        ("trust_stock", "Trust stock", "advanced_trust.png"),
        ("resilience_capacity", "Resilience capacity", "advanced_resilience.png"),
        ("structural_insight_score", "Structural insight score", "advanced_structural_insight.png"),
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
