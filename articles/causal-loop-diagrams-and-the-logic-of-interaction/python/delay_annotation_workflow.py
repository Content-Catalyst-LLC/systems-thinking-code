#!/usr/bin/env python3
"""Summarize delay annotations for causal-loop edges."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"


def main() -> None:
    with (DATA / "synthetic_delay_annotations.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print("Delay annotations")
    for row in rows:
        print(f"- {row['edge_id']}: {row['delay_type']} ({row['delay_steps']} steps) — {row['why_delay_matters']}")


if __name__ == "__main__":
    main()
