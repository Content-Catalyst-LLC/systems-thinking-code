#!/usr/bin/env python3
"""Calculate reinforcing or balancing loop polarity from signed edges."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES = ROOT / "data" / "synthetic_signed_edges.csv"
LOOPS = ROOT / "data" / "synthetic_feedback_loops.csv"


def load_edge_signs() -> dict[str, int]:
    with EDGES.open(newline="", encoding="utf-8") as handle:
        return {row["edge_id"]: (1 if row["sign"] == "+" else -1) for row in csv.DictReader(handle)}


def polarity(edge_ids: list[str], edge_signs: dict[str, int]) -> tuple[int, str]:
    product = 1
    for edge_id in edge_ids:
        product *= edge_signs[edge_id]
    return product, "reinforcing" if product > 0 else "balancing"


def main() -> None:
    edge_signs = load_edge_signs()
    with LOOPS.open(newline="", encoding="utf-8") as handle:
        for loop in csv.DictReader(handle):
            edge_ids = loop["edge_sequence"].split("|")
            product, label = polarity(edge_ids, edge_signs)
            print(f"{loop['loop_id']} | {loop['loop_name']} | product={product} | {label}")


if __name__ == "__main__":
    main()
