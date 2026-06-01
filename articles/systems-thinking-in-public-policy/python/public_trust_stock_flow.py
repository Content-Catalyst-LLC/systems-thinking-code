"""Public trust stock-flow model from synthetic reliability, fairness, accountability, burden, and opacity indicators."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
trust_stock = 50.0
rows = []
with (ROOT / "data" / "synthetic_trust_indicators.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        inflow = (float(row["reliability"]) + float(row["fairness"]) + float(row["accountability"])) / 150.0
        outflow = (float(row["burden"]) + float(row["opacity"])) / 180.0
        trust_stock = max(0, min(100, trust_stock + inflow - outflow))
        rows.append({"year": row["year"], "trust_stock": round(trust_stock, 3), "trust_inflow": round(inflow, 3), "trust_outflow": round(outflow, 3)})
with (OUT / "public_trust_stock_flow.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["year", "trust_stock", "trust_inflow", "trust_outflow"])
    writer.writeheader(); writer.writerows(rows)
print(f"Wrote {OUT / 'public_trust_stock_flow.csv'}")
