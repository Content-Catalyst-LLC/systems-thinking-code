#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "model_risk_sensitivity.csv"


def main() -> None:
    path = RAW / "synthetic_model_risk.csv"
    if not path.exists():
        print("Skipping model risk sensitivity; missing synthetic_model_risk.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        severity = float(row["severity"])
        likelihood = float(row["likelihood"])
        risk_score = severity * likelihood * 100.0
        output.append({
            "risk_id": row["risk_id"],
            "risk_type": row["risk_type"],
            "severity": round(severity, 3),
            "likelihood": round(likelihood, 3),
            "risk_score": round(risk_score, 3),
            "risk_class": "high model risk" if risk_score >= 55 else "moderate model risk",
            "mitigation": row["mitigation"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
