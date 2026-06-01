"""Carbon accumulation scenarios using synthetic emissions and removals."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
carbon_stock = 420.0
with (ROOT / "data" / "synthetic_resource_flows.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        year = int(row["year"]); emissions = float(row["emissions"]); removals = 30.0 + max(0, year - 2030) * 1.2
        carbon_stock += emissions / 20.0 - removals / 50.0
        rows.append({"year": year, "emissions": round(emissions, 3), "removals": round(removals, 3), "carbon_stock": round(carbon_stock, 3)})
with (OUT / "carbon_accumulation_scenarios.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["year", "emissions", "removals", "carbon_stock"]); writer.writeheader(); writer.writerows(rows)
