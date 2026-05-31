#!/usr/bin/env python3
"""Compare stakeholder causal assumptions in a synthetic map."""
from __future__ import annotations

import csv
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"


def main() -> None:
    with (DATA / "synthetic_stakeholder_maps.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    confidence = Counter(row["confidence"] for row in rows)
    polarity = Counter(row["polarity"] for row in rows)
    print("Stakeholder causal assumptions")
    print("Confidence counts:", dict(confidence))
    print("Polarity counts:", dict(polarity))
    for row in rows:
        print(f"- {row['stakeholder_group']}: {row['causal_assumption']} ({row['polarity']}, {row['confidence']})")


if __name__ == "__main__":
    main()
