#!/usr/bin/env python3
"""
Optional advanced pandas/matplotlib climate workflow.

This script intentionally fails gracefully when optional dependencies are missing.
Install from the repository root with:

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r articles/climate-systems-and-feedback-dynamics/requirements-advanced.txt
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
except ModuleNotFoundError as exc:
    missing = exc.name
    print(f"Optional advanced dependency missing: {missing}")
    print("Run this from the repository root:")
    print("  python3 -m venv .venv")
    print("  . .venv/bin/activate")
    print("  python -m pip install -r articles/climate-systems-and-feedback-dynamics/requirements-advanced.txt")
    sys.exit(0)


def ensure_default_outputs() -> None:
    timeseries = TABLES / "climate_feedback_scenario_timeseries.csv"
    if not timeseries.exists():
        subprocess.run([sys.executable, str(ROOT / "python" / "run_all_climate_workflows.py")], cwd=str(ROOT), check=True)


def main() -> None:
    ensure_default_outputs()
    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(TABLES / "climate_feedback_scenario_timeseries.csv")

    summary = (
        df.groupby("scenario", as_index=False)
        .agg(
            final_co2_ppm=("co2_ppm", "last"),
            final_temperature_anomaly_c=("temperature_anomaly_c", "last"),
            maximum_temperature_anomaly_c=("temperature_anomaly_c", "max"),
            cumulative_emissions_gtco2=("emissions_gtco2", "sum"),
            average_risk_index=("risk_index", "mean"),
            peak_risk_index=("risk_index", "max"),
        )
        .sort_values("final_temperature_anomaly_c")
    )

    summary.to_csv(TABLES / "advanced_climate_pandas_summary.csv", index=False)

    workbook = TABLES / "advanced_climate_workbook.xlsx"
    with pd.ExcelWriter(workbook, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="timeseries")
        summary.to_excel(writer, index=False, sheet_name="summary")

    for metric, ylabel, filename, title in [
        ("emissions_gtco2", "Annual emissions (GtCO2)", "advanced_climate_emissions.png", "Emissions Trajectories"),
        ("co2_ppm", "Atmospheric CO2 (ppm)", "advanced_climate_co2_stock.png", "Atmospheric CO2 Stock"),
        ("temperature_anomaly_c", "Temperature anomaly (°C)", "advanced_climate_temperature.png", "Temperature Response"),
        ("risk_index", "Risk index", "advanced_climate_risk.png", "Climate Risk Index"),
    ]:
        fig, ax = plt.subplots(figsize=(10, 6))
        for scenario, group in df.groupby("scenario"):
            ax.plot(group["year"], group[metric], label=scenario, linewidth=2)
        ax.set_title(title)
        ax.set_xlabel("Year")
        ax.set_ylabel(ylabel)
        ax.legend(loc="best", fontsize=8)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(FIGURES / filename, dpi=160)
        plt.close(fig)

    print("Advanced pandas climate workflow completed.")
    print("Workbook:", workbook)


if __name__ == "__main__":
    main()
