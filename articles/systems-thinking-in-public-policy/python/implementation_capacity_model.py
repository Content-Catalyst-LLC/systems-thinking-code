"""Implementation capacity model combining staffing, knowledge, data systems, memory, and authority."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
fields = ["staffing", "knowledge", "data_systems", "institutional_memory", "authority"]
rows = []
with (ROOT / "data" / "synthetic_implementation_capacity.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        score = sum(float(row[field]) for field in fields) / len(fields)
        rows.append({"agency": row["agency"], "implementation_capacity_score": round(score, 2), "lowest_capacity_component": min(fields, key=lambda k: float(row[k]))})
with (OUT / "implementation_capacity_summary.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["agency", "implementation_capacity_score", "lowest_capacity_component"])
    writer.writeheader(); writer.writerows(rows)
print(f"Wrote {OUT / 'implementation_capacity_summary.csv'}")
