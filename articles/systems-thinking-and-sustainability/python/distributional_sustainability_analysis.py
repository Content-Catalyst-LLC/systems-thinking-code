"""Distributional sustainability analysis using synthetic group impacts."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
with (ROOT / "data" / "synthetic_distributional_impacts.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        benefits = float(row["benefits"]); harms = float(row["harms"]); costs = float(row["transition_costs"])
        rows.append({"group": row["group"], "benefits": benefits, "harms": harms, "transition_costs": costs, "net_justice": round(benefits - harms - costs, 3)})
with (OUT / "distributional_justice_summary.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["group", "benefits", "harms", "transition_costs", "net_justice"]); writer.writeheader(); writer.writerows(rows)
