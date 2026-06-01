#!/usr/bin/env python3
"""Diagnose candidate system archetypes from synthetic case descriptors."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
cases_path = ROOT / "data" / "synthetic_archetype_cases.csv"
archetypes_path = ROOT / "data" / "synthetic_archetypes.csv"
output_path = ROOT / "outputs" / "tables" / "archetype_diagnostic_summary.csv"

output_path.parent.mkdir(parents=True, exist_ok=True)

with archetypes_path.open(newline="", encoding="utf-8") as f:
    archetypes = {row["archetype_id"]: row for row in csv.DictReader(f)}

with cases_path.open(newline="", encoding="utf-8") as f:
    cases = list(csv.DictReader(f))

rows = []
for case in cases:
    archetype = archetypes[case["archetype_id"]]
    rows.append({
        "case_id": case["case_id"],
        "domain": case["domain"],
        "case_name": case["case_name"],
        "candidate_archetype": archetype["archetype_name"],
        "visible_symptom": case["visible_symptom"],
        "structural_hypothesis": case["structural_hypothesis"],
        "typical_leverage_point": archetype["typical_leverage_point"],
    })

with output_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {output_path}")
