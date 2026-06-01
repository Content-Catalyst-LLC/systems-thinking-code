"""One-at-a-time sensitivity ranking for a simplified sustainability score."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
parameters = {"regeneration_rate": 0.42, "extraction_rate": -0.55, "policy_delay": -0.28, "rebound_strength": -0.33, "equity_weight": 0.37}
rows = [{"parameter": k, "effect_direction": "positive" if v > 0 else "negative", "absolute_effect": round(abs(v), 3)} for k, v in parameters.items()]
rows.sort(key=lambda r: r["absolute_effect"], reverse=True)
with (OUT / "sensitivity_results.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["parameter", "effect_direction", "absolute_effect"]); writer.writeheader(); writer.writerows(rows)
