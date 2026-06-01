#!/usr/bin/env python3
"""Run all dependency-light public health workflows."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "public_health_system_model.py",
    "validation_checks.py",
    "disease_dynamics_scenarios.py",
    "care_capacity_stress_model.py",
    "public_trust_health_feedback.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], check=True)
    print("\nAll dependency-light Python public health workflows completed.")


if __name__ == "__main__":
    main()
