"""
Part-whole network model.

This example maps dependency pathways among system parts.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_dependency_edges.csv"


def load_edges() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_graph(edges: list[dict[str, str]]) -> dict[str, list[str]]:
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
    graph = build_graph(load_edges())
    paths = find_paths(graph, "community_users", "funding_stream")

    print("Dependency pathways from community_users to funding_stream:")
    if not paths:
        print("No direct pathway found in this simplified synthetic graph.")
    for path in paths:
        print(" -> ".join(path))


if __name__ == "__main__":
    main()
