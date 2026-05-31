#!/usr/bin/env python3
"""Build a signed causal graph from synthetic causal-loop data."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"


def read_edges() -> List[dict]:
    with (DATA / "synthetic_causal_edges.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_adjacency(edges: List[dict]) -> Dict[str, List[Tuple[str, int, int]]]:
    graph: Dict[str, List[Tuple[str, int, int]]] = {}
    for edge in edges:
        sign = 1 if edge["polarity"].lower() == "positive" else -1
        delay = int(edge["delay_steps"])
        graph.setdefault(edge["source_variable"], []).append((edge["target_variable"], sign, delay))
    return graph


def main() -> None:
    graph = build_adjacency(read_edges())
    print("Signed causal graph adjacency list")
    for source, targets in sorted(graph.items()):
        for target, sign, delay in targets:
            label = "+" if sign > 0 else "-"
            delay_note = f", delay={delay}" if delay else ""
            print(f"- {source} --{label}{delay_note}--> {target}")


if __name__ == "__main__":
    main()
