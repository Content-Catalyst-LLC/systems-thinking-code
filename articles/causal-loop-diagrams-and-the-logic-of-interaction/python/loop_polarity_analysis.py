#!/usr/bin/env python3
"""Calculate loop polarity from predefined loop edge sequences."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"


def load_edge_signs() -> Dict[str, int]:
    signs: Dict[str, int] = {}
    with (DATA / "synthetic_causal_edges.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            signs[row["edge_id"]] = 1 if row["polarity"] == "positive" else -1
    return signs


def main() -> None:
    signs = load_edge_signs()
    with (DATA / "synthetic_feedback_loops.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            product = 1
            edge_ids = row["edge_sequence"].split("|")
            for edge_id in edge_ids:
                product *= signs.get(edge_id, 1)
            calculated = "reinforcing" if product > 0 else "balancing"
            print(f"{row['loop_id']} | {row['loop_name']} | calculated={calculated} | expected={row['expected_polarity']}")


if __name__ == "__main__":
    main()
