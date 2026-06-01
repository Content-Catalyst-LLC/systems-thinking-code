#!/usr/bin/env python3
"""Optional advanced pandas/matplotlib workflow.

Run after the default Python workflow. This script is optional and fails gracefully
when pandas or matplotlib are not installed.
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
except ImportError as exc:
    print("Optional advanced dependencies are missing.")
    print("Install them with: python3 -m pip install -r requirements-advanced.txt")
    print(f"Details: {exc}")
    sys.exit(0)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    path = TABLES / "platform_feedback_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError("Run python/run_all_platform_workflows.py first.")

    df = pd.read_csv(path)
    summary = df.groupby("scenario", as_index=False).agg(
        average_risk=("platform_risk_index", "mean"),
        peak_cascade=("harmful_cascade_risk", "max"),
        final_dependency=("platform_dependency", "last"),
        minimum_trust=("user_trust", "min"),
        average_public_value=("public_value_index", "mean"),
    )
    summary.to_csv(TABLES / "advanced_platform_dashboard_summary.csv", index=False)

    for metric in [
        "platform_risk_index",
        "harmful_cascade_risk",
        "moderation_backlog",
        "platform_dependency",
        "user_trust",
        "public_value_index",
    ]:
        plt.figure(figsize=(10, 6))
        for scenario, subset in df.groupby("scenario"):
            plt.plot(subset["period"], subset[metric], label=scenario)
        plt.title(metric.replace("_", " ").title())
        plt.xlabel("Period")
        plt.ylabel(metric.replace("_", " ").title())
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(FIGURES / f"advanced_{metric}.png", dpi=160)
        plt.close()

    try:
        with pd.ExcelWriter(TABLES / "advanced_platform_workbook.xlsx") as writer:
            df.to_excel(writer, sheet_name="timeseries", index=False)
            summary.to_excel(writer, sheet_name="summary", index=False)
    except Exception as exc:  # openpyxl may be missing.
        print(f"Skipped Excel export: {exc}")

    print("Advanced pandas/matplotlib platform workflow completed.")


if __name__ == "__main__":
    main()
