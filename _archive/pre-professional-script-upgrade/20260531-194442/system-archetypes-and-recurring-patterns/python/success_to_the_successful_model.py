#!/usr/bin/env python3
"""Success-to-the-successful model: early advantage attracts future resources."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "success_to_the_successful_model.csv"
out.parent.mkdir(parents=True, exist_ok=True)

success_a = 52.0
success_b = 48.0
resource_pool = 20.0
rows = []

for t in range(25):
    total_success = success_a + success_b
    resource_a = resource_pool * success_a / total_success
    resource_b = resource_pool * success_b / total_success
    success_a += 0.28 * resource_a
    success_b += 0.28 * resource_b
    rows.append({"time": t, "success_a": round(success_a, 3), "success_b": round(success_b, 3), "resource_a": round(resource_a, 3), "resource_b": round(resource_b, 3)})

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
