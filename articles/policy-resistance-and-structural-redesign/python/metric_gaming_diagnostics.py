"""Metric gaming diagnostics for policy-resistance analysis."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
METRICS = ROOT / "data" / "raw" / "synthetic_metrics_targets.csv"
OUT = ROOT / "outputs" / "tables" / "metric_gaming_diagnostics.csv"

RISK_SCORE = {"low": 0.25, "medium": 0.55, "high": 0.85}
PROXY_SCORE = {"weak": 0.25, "partial": 0.55, "narrow": 0.40, "strong": 0.90}


def main() -> None:
    rows = []
    with METRICS.open(newline="") as f:
        for row in csv.DictReader(f):
            gaming = RISK_SCORE[row["gaming_risk"]]
            proxy = PROXY_SCORE[row["system_health_proxy"]]
            row["diagnostic_priority"] = round(gaming * (1 - proxy), 3)
            rows.append(row)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
