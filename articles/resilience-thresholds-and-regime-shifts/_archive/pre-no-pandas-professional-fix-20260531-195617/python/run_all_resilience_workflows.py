#!/usr/bin/env python3
"""Run all professional Python workflows for the resilience article."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "resilience_threshold_regime_model.py",
    "early_warning_indicator_analysis.py",
    "hysteresis_recovery_diagnostics.py",
    "adaptive_capacity_scenarios.py",
    "resilience_sensitivity_analysis.py",
    "distributional_vulnerability_model.py",
    "export_resilience_outputs.py",
    "validation_checks.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], check=True)
    print("\nAll Python resilience workflows completed successfully.")


if __name__ == "__main__":
    main()
