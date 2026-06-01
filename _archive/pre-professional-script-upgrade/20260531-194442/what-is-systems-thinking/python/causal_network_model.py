"""
Simple causal-network model using synthetic edge data.

No external dependencies required.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_causal_edges.csv"


def load_edges(path: Path = DATA_PATH) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_adjacency(edges: list[dict[str, str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge["source"]].append(edge["target"])
    return dict(graph)


def find_paths(
    graph: dict[str, list[str]],
    start: str,
    end: str,
    path: list[str] | None = None,
    max_depth: int = 5,
) -> list[list[str]]:
    if path is None:
        path = [start]
    if start == end:
        return [path]
    if len(path) > max_depth:
        return []

    paths: list[list[str]] = []
    for node in graph.get(start, []):
        if node not in path:
            paths.extend(find_paths(graph, node, end, path + [node], max_depth))
    return paths


def main() -> None:
    edges = load_edges()
    graph = build_adjacency(edges)
    paths = find_paths(graph, "resource_flow", "response_delay")

    print("Causal paths from resource_flow to response_delay:")
    for path in paths:
        print(" -> ".join(path))


if __name__ == "__main__":
    main()
