#!/usr/bin/env python3
"""Run all dependency-light Python workflows for the urban systems article."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "urban_systems_model.py",
    "validation_checks.py",
    "congestion_induced_demand_scenarios.py",
    "housing_transport_affordability.py",
    "infrastructure_maintenance_model.py",
    "displacement_risk_diagnostics.py",
    "urban_resilience_index.py",
    "export_urban_outputs.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], cwd=str(ROOT), check=True)
    print("\nAll dependency-light Python urban systems workflows completed.")


if __name__ == "__main__":
    main()
