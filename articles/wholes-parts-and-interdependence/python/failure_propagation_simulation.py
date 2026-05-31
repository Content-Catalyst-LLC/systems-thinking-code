"""
Failure propagation simulation for a simplified interdependent system.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
EDGES_PATH = DATA_DIR / "synthetic_dependency_edges.csv"


def load_edges() -> list[dict[str, str]]:
    with EDGES_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_weighted_graph(edges: list[dict[str, str]]) -> dict[str, list[tuple[str, float]]]:
    graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for edge in edges:
        graph[edge["source"]].append((edge["target"], float(edge["weight"])))
    return dict(graph)


def propagate_failure(start: str, shock: float, steps: int = 4, damping: float = 0.65) -> dict[str, float]:
    graph = build_weighted_graph(load_edges())
    stress = {start: shock}
    frontier = {start: shock}

    for _ in range(steps):
        next_frontier: dict[str, float] = {}
        for node, node_stress in frontier.items():
            for target, weight in graph.get(node, []):
                transmitted = node_stress * weight * damping
                next_frontier[target] = next_frontier.get(target, 0.0) + transmitted
                stress[target] = stress.get(target, 0.0) + transmitted
        frontier = next_frontier

    return {node: round(value, 2) for node, value in sorted(stress.items())}


def main() -> None:
    result = propagate_failure("funding_stream", shock=25.0)
    print("part,accumulated_stress")
    for part, value in result.items():
        print(f"{part},{value}")


if __name__ == "__main__":
    main()
