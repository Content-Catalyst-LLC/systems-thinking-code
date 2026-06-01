#!/usr/bin/env python3
"""
Optional advanced pandas workflow for food-water-energy systems.

This script fails gracefully if optional dependencies are missing. Install with:
  python3 -m venv .venv
  . .venv/bin/activate
  pip install -r requirements-advanced.txt
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
    print("Optional advanced dependency missing:", exc)
    print("Install optional dependencies with: pip install -r requirements-advanced.txt")
    raise SystemExit(0)


def ensure_default_outputs() -> None:
    if not (TABLES / "food_water_energy_nexus_timeseries.csv").exists():
        subprocess.run([sys.executable, str(ROOT / "python" / "run_all_nexus_workflows.py")], cwd=ROOT, check=True)


def main() -> None:
    ensure_default_outputs()
    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(TABLES / "food_water_energy_nexus_timeseries.csv")
    summary = (
        df.groupby("scenario")
        .agg(
            final_groundwater_stock=("groundwater_stock", "last"),
            final_food_production_index=("food_production_index", "last"),
            final_water_security_index=("water_security_index", "last"),
            final_energy_security_index=("energy_security_index", "last"),
            average_nexus_stress_index=("nexus_stress_index", "mean"),
            average_resilience_index=("resilience_index", "mean"),
            minimum_groundwater_stock=("groundwater_stock", "min"),
        )
        .reset_index()
    )
    summary["diagnostic"] = pd.cut(
        summary["average_nexus_stress_index"],
        bins=[-1, 40, 60, 101],
        labels=["comparatively resilient pathway", "moderate stress requiring redesign", "high nexus fragility"],
    )
    summary.to_csv(TABLES / "advanced_nexus_summary.csv", index=False)
    with pd.ExcelWriter(TABLES / "advanced_nexus_workbook.xlsx") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        summary.to_excel(writer, sheet_name="scenario_summary", index=False)
    for metric, title, filename in [
        ("groundwater_stock", "Groundwater stock trajectories", "advanced_groundwater_stock.png"),
        ("nexus_stress_index", "Nexus stress trajectories", "advanced_nexus_stress.png"),
        ("resilience_index", "Nexus resilience trajectories", "advanced_resilience.png"),
    ]:
        ax = df.pivot(index="year", columns="scenario", values=metric).plot(figsize=(10, 6), title=title)
        ax.set_xlabel("Year")
        ax.set_ylabel(metric.replace("_", " ").title())
        ax.figure.tight_layout()
        ax.figure.savefig(FIGURES / filename, dpi=200)
        plt.close(ax.figure)
    print("Advanced pandas workflow completed.")


if __name__ == "__main__":
    main()
