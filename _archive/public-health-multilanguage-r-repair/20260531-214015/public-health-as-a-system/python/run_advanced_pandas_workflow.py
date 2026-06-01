#!/usr/bin/env python3
"""
Optional advanced public health workflow using pandas, matplotlib, and openpyxl.

This script is not part of the default smoke test. Install requirements first:
    pip install -r requirements-advanced.txt
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"


def require_packages() -> None:
    missing = []
    for package in ["pandas", "matplotlib", "openpyxl", "numpy"]:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    if missing:
        joined = ", ".join(missing)
        raise SystemExit(
            f"Missing optional advanced packages: {joined}\n"
            "Install them with:\n"
            "  python3 -m venv .venv\n"
            "  . .venv/bin/activate\n"
            "  pip install -r requirements-advanced.txt"
        )


def ensure_default_outputs() -> None:
    required = TABLES / "public_health_system_timeseries.csv"
    if not required.exists():
        subprocess.run([sys.executable, str(ROOT / "python" / "run_all_public_health_workflows.py")], check=True)


def main() -> None:
    require_packages()
    ensure_default_outputs()

    import pandas as pd
    import matplotlib.pyplot as plt

    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(TABLES / "public_health_system_timeseries.csv")

    summary = (
        df.groupby("scenario")
        .agg(
            peak_infected=("infected", "max"),
            peak_care_stress=("care_stress", "max"),
            average_public_trust=("public_trust", "mean"),
            average_health_risk=("health_risk_index", "mean"),
            final_prevention_value=("prevention_value_index", "last"),
        )
        .reset_index()
    )
    summary.to_csv(TABLES / "advanced_public_health_summary.csv", index=False)

    workbook_path = TABLES / "advanced_public_health_workbook.xlsx"
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="timeseries", index=False)
        summary.to_excel(writer, sheet_name="summary", index=False)

    for metric, title, filename in [
        ("infected", "Infection trajectories by scenario", "advanced_public_health_infections.png"),
        ("care_stress", "Care stress trajectories by scenario", "advanced_public_health_care_stress.png"),
        ("public_trust", "Public trust trajectories by scenario", "advanced_public_health_trust.png"),
        ("health_risk_index", "Health risk trajectories by scenario", "advanced_public_health_risk.png"),
    ]:
        fig, ax = plt.subplots(figsize=(10, 6))
        for scenario, subset in df.groupby("scenario"):
            ax.plot(subset["week"], subset[metric], label=scenario)
        ax.set_title(title)
        ax.set_xlabel("Week")
        ax.set_ylabel(metric.replace("_", " ").title())
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(FIGURES / filename, dpi=180)
        plt.close(fig)

    print(f"Advanced pandas workflow complete. Workbook: {workbook_path}")


if __name__ == "__main__":
    main()
