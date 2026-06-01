#!/usr/bin/env python3
"""Run all professional resilience workflows without third-party dependencies."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "resilience_threshold_regime_model.py",
    "early_warning_indicator_analysis.py",
]


def main() -> None:
    for script in SCRIPTS:
        path = ROOT / "python" / script
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(path)], check=True)
    print("\nAll Python resilience workflows completed successfully.")


if __name__ == "__main__":
    main()
