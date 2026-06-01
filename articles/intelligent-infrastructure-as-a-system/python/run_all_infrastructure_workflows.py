#!/usr/bin/env python3
"""Run all dependency-light Python workflows for this article."""

from __future__ import annotations
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "intelligent_infrastructure_system_model.py",
    "asset_risk_priority_diagnostics.py",
    "cyber_physical_dependency_model.py",
    "climate_resilience_indicators.py",
    "validation_checks.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], cwd=str(ROOT), check=True)
    print("\nAll dependency-light Python intelligent infrastructure workflows completed.")


if __name__ == "__main__":
    main()
