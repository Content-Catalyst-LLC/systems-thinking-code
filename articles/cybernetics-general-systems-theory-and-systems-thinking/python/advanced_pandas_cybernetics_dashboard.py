#!/usr/bin/env python3
"""
Optional advanced workflow for cybernetics and systems diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/cybernetics-general-systems-theory-and-systems-thinking")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "cybernetics_systems_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_cybernetics_systems_workflows.py first."
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
            average_variety_gap=("variety_gap", "mean"),
            average_regulation=("regulation_quality", "mean"),
            average_accountability=("accountability_index", "mean"),
            average_learning=("learning_capacity", "mean"),
            average_trust=("trust_index", "mean"),
            average_absolute_error=("error_signal", lambda s: s.abs().mean()),
        )
        .merge(final[["scenario", "system_state", "response_variety", "regulation_quality"]], on="scenario", how="left")
        .rename(columns={
            "system_state": "final_system_state",
            "response_variety": "final_response_variety",
            "regulation_quality": "final_regulation_quality",
        })
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_cybernetics_systems_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_cybernetics_systems_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("system_state", "System state", "advanced_system_state.png"),
        ("error_signal", "Error signal", "advanced_error_signal.png"),
        ("control_action", "Control action", "advanced_control_action.png"),
        ("response_variety", "Response variety", "advanced_response_variety.png"),
        ("variety_gap", "Variety gap", "advanced_variety_gap.png"),
        ("regulation_quality", "Regulation quality", "advanced_regulation_quality.png"),
        ("accountability_index", "Accountability index", "advanced_accountability.png"),
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
