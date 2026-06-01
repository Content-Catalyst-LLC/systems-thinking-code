#!/usr/bin/env python3
"""
Optional advanced workflow for Forrester-style system dynamics diagnostics.

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
    print("  cd ~/Downloads/systems-thinking-code/articles/jay-forrester-and-the-origins-of-system-dynamics")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    sys.exit(0)


def require_core_output() -> Path:
    path = TABLES_DIR / "forrester_system_dynamics_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run python/run_all_forrester_system_dynamics_workflows.py first."
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
            average_backlog=("backlog_stock", "mean"),
            average_resistance=("resistance_index", "mean"),
            average_performance=("system_performance", "mean"),
            average_trust=("trust_stock", "mean"),
            average_learning=("institutional_learning_stock", "mean"),
            maximum_corrective_action=("corrective_action", "max"),
        )
        .merge(final[["scenario", "backlog_stock", "capacity_stock", "system_performance"]], on="scenario", how="left")
        .rename(columns={
            "backlog_stock": "final_backlog",
            "capacity_stock": "final_capacity",
            "system_performance": "final_performance",
        })
    )

    scenario_summary.to_csv(TABLES_DIR / "advanced_system_dynamics_dashboard.csv", index=False)

    workbook_path = TABLES_DIR / "advanced_forrester_system_dynamics_dashboard.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        scenario_summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, label, filename in [
        ("backlog_stock", "Backlog stock", "advanced_backlog.png"),
        ("capacity_stock", "Capacity stock", "advanced_capacity.png"),
        ("resistance_index", "Policy resistance index", "advanced_resistance.png"),
        ("trust_stock", "Trust stock", "advanced_trust.png"),
        ("institutional_learning_stock", "Institutional learning stock", "advanced_learning.png"),
        ("system_performance", "System performance", "advanced_performance.png"),
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
