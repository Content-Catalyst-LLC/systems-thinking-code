"""Feedback-loop closure diagnostics for policy learning."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
with (ROOT / "data" / "synthetic_feedback_signals.csv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        received = float(row["received"])
        acted = float(row["acted_upon"])
        embedded = float(row["embedded"])
        rows.append({"signal_id": row["signal_id"], "source": row["source"], "signal_type": row["signal_type"], "closure_rate": round(acted / received, 3), "embedding_rate": round(embedded / received, 3)})
with (OUT / "feedback_closure_diagnostics.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["signal_id", "source", "signal_type", "closure_rate", "embedding_rate"])
    writer.writeheader(); writer.writerows(rows)
print(f"Wrote {OUT / 'feedback_closure_diagnostics.csv'}")
