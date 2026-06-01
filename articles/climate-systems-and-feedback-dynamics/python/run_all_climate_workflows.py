#!/usr/bin/env python3
"""Run all default dependency-light climate systems workflows."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "climate_feedback_dynamics_model.py",
    "climate_vulnerability_risk_index.py",
    "policy_delay_emissions_model.py",
]


def main() -> None:
    for script in SCRIPTS:
        path = ROOT / "python" / script
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(path)], cwd=str(ROOT), check=True)
    print("\nDefault climate workflows completed successfully.")


if __name__ == "__main__":
    main()
