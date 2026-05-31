#!/usr/bin/env python3
"""Detect simple feedback loops in a signed directed graph."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"

Edge = Tuple[str, int]


def load_graph() -> Dict[str, List[Edge]]:
    graph: Dict[str, List[Edge]] = defaultdict(list)
    with (DATA / "synthetic_causal_edges.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sign = 1 if row["polarity"] == "positive" else -1
            graph[row["source_variable"]].append((row["target_variable"], sign))
    return graph


def find_cycles(graph: Dict[str, List[Edge]], max_depth: int = 5) -> List[Tuple[List[str], int]]:
    cycles: List[Tuple[List[str], int]] = []
    nodes = sorted(graph.keys())
    for start in nodes:
        stack = [(start, [start], 1)]
        while stack:
            current, path, sign_product = stack.pop()
            if len(path) > max_depth:
                continue
            for nxt, sign in graph.get(current, []):
                if nxt == start and len(path) > 1:
                    cycles.append((path + [start], sign_product * sign))
                elif nxt not in path:
                    stack.append((nxt, path + [nxt], sign_product * sign))
    # canonicalize to avoid duplicate rotations in this small demo
    seen = set()
    unique: List[Tuple[List[str], int]] = []
    for path, sign in cycles:
        key = tuple(path)
        if key not in seen:
            seen.add(key)
            unique.append((path, sign))
    return unique


def main() -> None:
    cycles = find_cycles(load_graph())
    if not cycles:
        print("No closed loops detected in the synthetic edge list.")
        return
    for path, sign in cycles:
        polarity = "reinforcing" if sign > 0 else "balancing"
        print(f"{polarity}: {' -> '.join(path)}")


if __name__ == "__main__":
    main()
