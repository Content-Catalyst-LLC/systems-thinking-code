#!/usr/bin/env python3
"""
Optional advanced workflow for complex adaptive social change diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/complex-adaptive-systems-and-social-change")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "complex_adaptive_social_change_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_complex_adaptive_social_change_workflows.py first."
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
            average_momentum=("transformation_momentum", "mean"),
            peak_resistance=("resistance_index", "max"),
            average_legitimacy=("legitimacy_index", "mean"),
            average_learning=("learning_capacity_index", "mean"),
            average_trust=("trust_index", "mean"),
        )
        .merge(final[["scenario", "adoption_index", "transformation_momentum"]], on="scenario", how="left")
        .rename(columns={"adoption_index": "final_adoption", "transformation_momentum": "final_momentum"})
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_social_change_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_complex_adaptive_social_change_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("adoption_index", "Adoption index", "advanced_adoption.png"),
        ("resistance_index", "Resistance index", "advanced_resistance.png"),
        ("legitimacy_index", "Legitimacy index", "advanced_legitimacy.png"),
        ("learning_capacity_index", "Learning capacity index", "advanced_learning.png"),
        ("transformation_momentum", "Transformation momentum", "advanced_momentum.png"),
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
