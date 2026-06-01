#!/usr/bin/env python3

Run optional pandas/matplotlib advanced workflows across existing article folders.

This runner is intentionally optional. It does not replace the dependency-light
standard-library workflows. If pandas is unavailable, it prints setup instructions
and exits without marking the repository as failed.

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADVANCED_SCRIPTS = sorted(ROOT.glob("articles/*/python/run_advanced_pandas_workflow.py"))


def dependency_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def main() -> int:
    if not dependency_available("pandas"):
        print("Optional advanced dependency 'pandas' is not installed for this Python interpreter.")
        print("Standard-library workflows can still run.")
        print("To enable advanced workflows, run:")
        print("  cd ~/Downloads/systems-thinking-code")
        print("  ./scripts/setup_advanced_python_env.sh")
        print("  . .venv/bin/activate")
        print("  python scripts/run_all_advanced_pandas_workflows.py")
        return 0

    if not ADVANCED_SCRIPTS:
        print("No advanced pandas workflow scripts found under articles/*/python/.")
        return 0

    failures: list[tuple[str, int]] = []
    for script in ADVANCED_SCRIPTS:
        print(f"\n=== Running {script.relative_to(ROOT)} ===")
        result = subprocess.run([sys.executable, str(script)], cwd=str(script.parents[1]))
        if result.returncode != 0:
            failures.append((str(script.relative_to(ROOT)), result.returncode))

    if failures:
        print("\nAdvanced workflow failures:")
        for path, code in failures:
            print(f"  {path}: exit code {code}")
        return 1

    print("\nAll available advanced pandas workflows completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
