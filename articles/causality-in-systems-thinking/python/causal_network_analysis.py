"""
Causal network analysis with standard-library graph traversal.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_causal_edges.csv"


def load_edges() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def adjacency(edges: list[dict[str, str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge["source"]].append(edge["target"])
    return dict(graph)


def find_paths(graph: dict[str, list[str]], start: str, end: str, path: list[str] | None = None) -> list[list[str]]:
    if path is None:
        path = [start]
    if start == end:
        return [path]
    if len(path) > 6:
        return []

    paths: list[list[str]] = []
    for node in graph.get(start, []):
        if node not in path:
            paths.extend(find_paths(graph, node, end, path + [node]))
    return paths


def main() -> None:
    graph = adjacency(load_edges())
    paths = find_paths(graph, "resource_flow", "public_trust")
    print("Causal paths from resource_flow to public_trust:")
    for path in paths:
        print(" -> ".join(path))


if __name__ == "__main__":
    main()
