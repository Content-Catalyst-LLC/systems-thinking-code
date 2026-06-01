#!/usr/bin/env python3
"""Run professional systems workflows across all existing article folders."""

from pathlib import Path
import subprocess
import sys

repo = Path(__file__).resolve().parents[1]
articles = repo / "articles"
workflow_name = "run_professional_systems_workflow.py"

if not articles.exists():
    raise SystemExit(f"Missing articles directory: {articles}")

article_dirs = sorted([p for p in articles.iterdir() if p.is_dir()])
if not article_dirs:
    raise SystemExit("No article directories found.")

failures = []
for article_dir in article_dirs:
    workflow = article_dir / "python" / workflow_name
    if not workflow.exists():
        failures.append((article_dir.name, "missing workflow"))
        continue
    print(f"\n=== Python workflow: {article_dir.name} ===")
    result = subprocess.run([sys.executable, str(workflow)], cwd=str(article_dir))
    if result.returncode != 0:
        failures.append((article_dir.name, f"exit {result.returncode}"))

if failures:
    print("\nFailures:")
    for slug, detail in failures:
        print(f"- {slug}: {detail}")
    raise SystemExit(1)

print("\nAll professional Python workflows completed successfully.")
