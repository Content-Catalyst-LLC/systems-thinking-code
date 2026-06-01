#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for the intelligent infrastructure article.

The core workflow must run first because the R workflow expects
outputs/tables/intelligent_infrastructure_timeseries.csv.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

# Core file first. Remaining files run only when present.
SCRIPTS = [
    "intelligent_infrastructure_system_model.py",
    "asset_risk_priority_diagnostics.py",
    "predictive_maintenance_scenarios.py",
    "cyber_physical_dependency_model.py",
    "climate_resilience_indicators.py",
    "validation_checks.py",
]


def main() -> None:
    for script in SCRIPTS:
        script_path = PYTHON_DIR / script
        if not script_path.exists():
            print(f"Skipping missing optional workflow: {script}")
            continue
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(script_path)], cwd=str(ARTICLE_ROOT), check=True)

    expected = ARTICLE_ROOT / "outputs" / "tables" / "intelligent_infrastructure_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python intelligent infrastructure workflows completed.")


if __name__ == "__main__":
    main()
