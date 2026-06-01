#!/usr/bin/env python3
"""Run all dependency-light Python workflows for the platform systems article."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "platform_feedback_digital_systems_model.py",
    "validation_checks.py",
    "engagement_amplification_scenarios.py",
    "moderation_capacity_model.py",
    "platform_dependency_index.py",
    "public_value_governance_score.py",
]


def main() -> None:
    for script in SCRIPTS:
        path = ROOT / "python" / script
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(path)], cwd=str(ROOT), check=True)
    print("\nAll dependency-light Python platform workflows completed.")


if __name__ == "__main__":
    main()
