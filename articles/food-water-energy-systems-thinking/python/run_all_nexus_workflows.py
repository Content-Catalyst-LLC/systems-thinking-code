#!/usr/bin/env python3
"""Run dependency-light food-water-energy workflows."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "food_water_energy_nexus_model.py",
    "validation_checks.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], cwd=ROOT, check=True)
    print("\nAll dependency-light Python food-water-energy workflows completed.")


if __name__ == "__main__":
    main()
