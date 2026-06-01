#!/usr/bin/env python3
"""Optional advanced pandas/matplotlib workflow.

This script exits gracefully if pandas/matplotlib/openpyxl are not installed.
It is intentionally not required by the default smoke test.
"""

from __future__ import annotations

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TABLES = os.path.join(ROOT, "outputs", "tables")
FIGURES = os.path.join(ROOT, "outputs", "figures")


def main() -> None:
    try:
        import pandas as pd  # type: ignore
        import matplotlib.pyplot as plt  # type: ignore
    except Exception as exc:
        print("Advanced dependencies are not installed. Skipping optional pandas workflow.")
        print("Install with: python3 -m pip install pandas matplotlib openpyxl")
        print(f"Import detail: {exc}")
        return

    os.makedirs(FIGURES, exist_ok=True)
    input_path = os.path.join(TABLES, "emergence_adaptation_complexity_timeseries.csv")
    if not os.path.exists(input_path):
        raise FileNotFoundError("Run the default Python workflow before the advanced workflow.")

    df = pd.read_csv(input_path)
    summary = df.groupby("scenario").agg(
        average_complexity=("complexity_index", "mean"),
        peak_complexity=("complexity_index", "max"),
        final_synchronization=("synchronization_index", "last"),
        final_diversity=("diversity_index", "last"),
    ).reset_index()
    summary.to_csv(os.path.join(TABLES, "advanced_pandas_complexity_summary.csv"), index=False)
    try:
        summary.to_excel(os.path.join(TABLES, "advanced_pandas_complexity_workbook.xlsx"), index=False)
    except Exception as exc:
        print(f"Excel export skipped: {exc}")

    ax = None
    for scenario, part in df.groupby("scenario"):
        ax = part.plot(x="period", y="complexity_index", label=scenario, ax=ax)
    if ax is not None:
        ax.set_title("Complexity index trajectories")
        ax.set_xlabel("Period")
        ax.set_ylabel("Complexity index")
        fig = ax.get_figure()
        fig.tight_layout()
        fig.savefig(os.path.join(FIGURES, "advanced_pandas_complexity_trajectories.png"), dpi=160)
        plt.close(fig)
    print("Optional advanced pandas workflow completed.")


if __name__ == "__main__":
    main()
