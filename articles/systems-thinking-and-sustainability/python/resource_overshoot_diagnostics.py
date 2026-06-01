"""Resource overshoot diagnostics for synthetic sustainability flows."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
with (ROOT / "data" / "synthetic_resource_flows.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        use = float(row["resource_use"]); capacity = float(row["regeneration_capacity"])
        rows.append({"year": row["year"], "resource_use": use, "regeneration_capacity": capacity, "overshoot": round(max(0.0, use - capacity), 3)})
with (OUT / "resource_overshoot_diagnostics.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["year", "resource_use", "regeneration_capacity", "overshoot"]); writer.writeheader(); writer.writerows(rows)
