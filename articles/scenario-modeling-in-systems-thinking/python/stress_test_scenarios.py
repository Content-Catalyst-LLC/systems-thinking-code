#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"

def main() -> None:
    with (DATA / "synthetic_stress_tests.csv").open(newline="", encoding="utf-8") as f:
        tests = list(csv.DictReader(f))

    rows = []
    for row in tests:
        severity = float(row["severity"])
        resilience_score = max(0.0, 1.0 - severity)
        rows.append({
            "stress_id": row["stress_id"],
            "description": row["description"],
            "severity": severity,
            "illustrative_resilience_score": round(resilience_score, 3),
            "priority": "high" if severity >= 0.65 else "medium",
        })

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    out = OUTPUTS / "stress_test_summary.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
