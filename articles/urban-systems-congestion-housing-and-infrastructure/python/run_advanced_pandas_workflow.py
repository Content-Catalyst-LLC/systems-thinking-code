#!/usr/bin/env python3
"""Optional advanced pandas/matplotlib workflow for urban systems diagnostics.

The default workflows do not require external packages. This script is optional
and fails gracefully with setup instructions if advanced dependencies are absent.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as exc:
    print("Optional advanced dependencies are not installed.")
    print("Run from the article folder:")
    print("  python3 -m venv .venv")
    print("  . .venv/bin/activate")
    print("  pip install -r requirements-advanced.txt")
    print("Then rerun:")
    print("  python python/run_advanced_pandas_workflow.py")
    raise SystemExit(0) from exc


def ensure_default_outputs() -> None:
    if not (TABLES / "urban_systems_timeseries.csv").exists():
        subprocess.run([sys.executable, str(ROOT / "python" / "urban_systems_model.py")], cwd=str(ROOT), check=True)


def main() -> None:
    ensure_default_outputs()
    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(TABLES / "urban_systems_timeseries.csv")
    summary = (
        df.groupby("scenario")
        .agg(
            final_congestion_index=("congestion_index", "last"),
            final_affordability_index=("affordability_index", "last"),
            final_infrastructure_condition=("infrastructure_condition", "last"),
            final_displacement_pressure=("displacement_pressure", "last"),
            mean_access_index=("access_index", "mean"),
            mean_urban_resilience_index=("urban_resilience_index", "mean"),
        )
        .reset_index()
    )
    summary["diagnostic"] = summary.apply(
        lambda row: "high urban fragility"
        if row["mean_urban_resilience_index"] < 35 or row["final_infrastructure_condition"] < 30
        else "moderate stress requiring redesign"
        if row["final_congestion_index"] > 55 or row["final_affordability_index"] < 45
        else "comparatively resilient urban pathway",
        axis=1,
    )

    summary.to_csv(TABLES / "advanced_urban_systems_summary.csv", index=False)
    with pd.ExcelWriter(TABLES / "advanced_urban_systems_workbook.xlsx") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        summary.to_excel(writer, sheet_name="scenario_summary", index=False)

    for metric, title, y_label, filename in [
        ("congestion_index", "Congestion Trajectories", "Congestion index", "advanced_congestion_trajectories.png"),
        ("affordability_index", "Affordability Trajectories", "Affordability index", "advanced_affordability_trajectories.png"),
        ("infrastructure_condition", "Infrastructure Condition", "Infrastructure condition", "advanced_infrastructure_condition.png"),
        ("urban_resilience_index", "Urban Resilience", "Urban resilience index", "advanced_urban_resilience.png"),
    ]:
        ax = df.pivot(index="year", columns="scenario", values=metric).plot(figsize=(10, 6), linewidth=2)
        ax.set_title(title)
        ax.set_xlabel("Year")
        ax.set_ylabel(y_label)
        ax.grid(True, alpha=0.25)
        ax.figure.tight_layout()
        ax.figure.savefig(FIGURES / filename, dpi=150)
        plt.close(ax.figure)

    print("Advanced pandas urban workflow completed.")
    print(f"Wrote {TABLES / 'advanced_urban_systems_workbook.xlsx'}")


if __name__ == "__main__":
    main()
