"""Rebound-effect model for efficiency scenarios."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
with (ROOT / "data" / "synthetic_policy_scenarios.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        efficiency_gain = max(0.0, 4.0 - float(row["extraction_rate"])) / 4.0
        rebound_strength = float(row["rebound_strength"])
        rows.append({"scenario": row["scenario"], "efficiency_gain": round(efficiency_gain, 3), "rebound_strength": rebound_strength, "net_reduction": round(efficiency_gain * (1.0 - rebound_strength), 3)})
with (OUT / "rebound_effect_summary.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["scenario", "efficiency_gain", "rebound_strength", "net_reduction"]); writer.writeheader(); writer.writerows(rows)
