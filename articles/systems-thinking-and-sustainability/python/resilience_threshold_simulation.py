"""Resilience threshold simulation using synthetic resilience indicators."""
from pathlib import Path
import csv
from statistics import mean
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
fields = ["diversity", "redundancy", "learning", "trust", "equity", "adaptive_capacity"]
rows = []
with (ROOT / "data" / "synthetic_resilience_indicators.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        score = mean(float(row[field]) for field in fields)
        warning = "high" if score < 0.48 else "moderate" if score < 0.56 else "watch"
        rows.append({"system": row["system"], "resilience_score": round(score, 3), "threshold_warning": warning})
with (OUT / "resilience_threshold_summary.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["system", "resilience_score", "threshold_warning"]); writer.writeheader(); writer.writerows(rows)
