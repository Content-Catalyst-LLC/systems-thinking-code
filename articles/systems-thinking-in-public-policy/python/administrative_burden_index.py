"""Administrative burden index using learning, compliance, psychological, digital, and appeal costs."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
with (ROOT / "data" / "synthetic_administrative_burden.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        costs = [float(row[k]) for k in ["learning_cost", "compliance_cost", "psychological_cost", "digital_cost", "appeal_burden"]]
        burden_index = sum(costs) / len(costs)
        rows.append({"group": row["group"], "burden_index": round(burden_index, 2), "highest_cost_component": max(["learning_cost", "compliance_cost", "psychological_cost", "digital_cost", "appeal_burden"], key=lambda k: float(row[k]))})
with (OUT / "administrative_burden_index.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["group", "burden_index", "highest_cost_component"])
    writer.writeheader(); writer.writerows(rows)
print(f"Wrote {OUT / 'administrative_burden_index.csv'}")
