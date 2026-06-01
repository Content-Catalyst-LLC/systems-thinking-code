#!/usr/bin/env python3
"""Optional advanced analytics layer using pandas, matplotlib, and openpyxl.

This script is intentionally optional. If dependencies are missing, it exits cleanly
with setup instructions and does not break the default smoke test.
"""

from __future__ import annotations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ModuleNotFoundError as exc:
    print("Optional advanced dependencies are not installed.")
    print("Run:")
    print("  cd ~/Downloads/systems-thinking-code/articles/intelligent-infrastructure-as-a-system")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements-advanced.txt")
    print("  python python/advanced_infrastructure_analytics.py")
    sys.exit(0)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    path = TABLES / "intelligent_infrastructure_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError("Run python/run_all_infrastructure_workflows.py first.")
    df = pd.read_csv(path)
    yearly = df.groupby(["scenario", "year"], as_index=False)[["risk_score", "resilience_score", "cyber_physical_dependency", "condition"]].mean()

    for metric in ["risk_score", "resilience_score", "cyber_physical_dependency", "condition"]:
        fig, ax = plt.subplots(figsize=(10, 6))
        for scenario, group in yearly.groupby("scenario"):
            ax.plot(group["year"], group[metric], label=scenario)
        ax.set_title(metric.replace("_", " ").title())
        ax.set_xlabel("Year")
        ax.set_ylabel(metric.replace("_", " ").title())
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(FIGURES / f"advanced_{metric}_trajectory.png", dpi=160)
        plt.close(fig)

    workbook = TABLES / "advanced_infrastructure_workbook.xlsx"
    with pd.ExcelWriter(workbook, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        yearly.to_excel(writer, sheet_name="yearly_means", index=False)
        pd.read_csv(TABLES / "intelligent_infrastructure_summary.csv").to_excel(writer, sheet_name="summary", index=False)
        pd.read_csv(TABLES / "asset_priority_diagnostics.csv").to_excel(writer, sheet_name="asset_priority", index=False)
    print(f"Wrote advanced workbook: {workbook}")
    print(f"Wrote advanced figures to: {FIGURES}")


if __name__ == "__main__":
    main()
