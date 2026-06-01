#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "feedback_delay_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_feedback_signals.csv"
    if not path.exists():
        print("Skipping feedback delay diagnostics; missing synthetic_feedback_signals.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []
    for row in rows:
        quality = float(row["signal_quality"])
        delay = int(row["delay_periods"])
        noise = float(row["noise_level"])
        reliability = max(0.0, min(100.0, quality * 100.0 - delay * 3.0 - noise * 25.0))
        output.append({
            "signal_id": row["signal_id"],
            "signal_name": row["signal_name"],
            "delay_periods": delay,
            "noise_level": round(noise, 3),
            "feedback_reliability_score": round(reliability, 3),
            "affected_decision": row["affected_decision"],
            "diagnostic": "feedback likely too delayed or noisy" if reliability < 50 else "feedback usable with review",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
