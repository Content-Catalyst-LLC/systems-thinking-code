"""
Structural causal map using synthetic edge data.

The goal is to connect repeated events to deeper structural relationships.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_causal_edges.csv"


def load_edges(path: Path = DATA_PATH) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_graph(edges: list[dict[str, str]]) -> dict[str, list[tuple[str, str]]]:
    graph: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for edge in edges:
        graph[edge["source"]].append((edge["target"], edge["polarity"]))
    return dict(graph)


def print_graph(graph: dict[str, list[tuple[str, str]]]) -> None:
    for source, targets in sorted(graph.items()):
        for target, polarity in targets:
            sign = "+" if polarity == "positive" else "-"
            print(f"{source} --({sign})--> {target}")


def main() -> None:
    edges = load_edges()
    graph = build_graph(edges)
    print_graph(graph)


if __name__ == "__main__":
    main()
