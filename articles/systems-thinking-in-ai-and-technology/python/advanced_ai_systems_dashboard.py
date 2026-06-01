"""Optional advanced pandas/matplotlib layer for AI systems outputs.

This script is optional. It fails gracefully when pandas, matplotlib, or openpyxl
are not installed.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except Exception as exc:  # pragma: no cover
    print("Optional advanced dependencies are missing.")
    print("Install them with: python3 -m pip install -r requirements-advanced.txt")
    print(f"Details: {exc}")
    sys.exit(0)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    ts = pd.read_csv(TABLES / "ai_technology_systems_timeseries.csv")
    summary = pd.read_csv(TABLES / "ai_technology_systems_summary.csv")

    for metric in ["ai_system_risk", "governance_readiness", "public_trust", "false_positive_gap"]:
        ax = None
        for scenario, group in ts.groupby("scenario"):
            ax = group.plot(x="period", y=metric, label=scenario, ax=ax, linewidth=2)
        ax.set_title(metric.replace("_", " ").title())
        ax.set_xlabel("Period")
        ax.set_ylabel(metric.replace("_", " ").title())
        fig = ax.get_figure()
        fig.tight_layout()
        fig.savefig(FIGURES / f"advanced_{metric}.png", dpi=160)
        plt.close(fig)

    try:
        with pd.ExcelWriter(TABLES / "ai_technology_systems_advanced_workbook.xlsx") as writer:
            ts.to_excel(writer, sheet_name="timeseries", index=False)
            summary.to_excel(writer, sheet_name="summary", index=False)
    except Exception as exc:
        print(f"Excel workbook skipped: {exc}")

    print("Optional advanced AI systems dashboard complete.")

if __name__ == "__main__":
    main()
