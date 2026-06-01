"""Distributional policy impact: benefits minus burdens and risks."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
with (ROOT / "data" / "synthetic_distributional_impacts.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        net = float(row["benefits"]) - float(row["burdens"]) - float(row["risks"])
        rows.append({"group": row["group"], "benefits": row["benefits"], "burdens": row["burdens"], "risks": row["risks"], "access_score": row["access_score"], "net_policy_impact": round(net, 2)})
with (OUT / "distributional_policy_impact.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["group", "benefits", "burdens", "risks", "access_score", "net_policy_impact"])
    writer.writeheader(); writer.writerows(rows)
print(f"Wrote {OUT / 'distributional_policy_impact.csv'}")
