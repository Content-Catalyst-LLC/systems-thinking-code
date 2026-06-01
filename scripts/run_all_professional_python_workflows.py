#!/usr/bin/env python3
"""Run professional Python workflows across every article directory."""
from pathlib import Path
import subprocess
import sys
repo = Path(__file__).resolve().parents[1]
failures = []
for article in sorted((repo / "articles").iterdir()):
    if not article.is_dir():
        continue
    workflow = article / "python" / "run_professional_workflow.py"
    if not workflow.exists():
        failures.append((article.name, "missing python workflow"))
        continue
    print(f"\n=== Python professional workflow: {article.name} ===")
    result = subprocess.run([sys.executable, str(workflow)], cwd=str(article))
    if result.returncode != 0:
        failures.append((article.name, f"exit {result.returncode}"))
if failures:
    print("\nFailures:")
    for slug, detail in failures:
        print(f"- {slug}: {detail}")
    raise SystemExit(1)
print("\nAll professional Python workflows completed successfully.")
