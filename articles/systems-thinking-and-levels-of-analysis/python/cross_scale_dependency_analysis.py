"""Analyze cross-scale dependencies using synthetic relationship data."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_cross_scale_edges.csv"


def load_edges() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rank_dependencies(edges: list[dict[str, str]]) -> list[tuple[str, float]]:
    scores: dict[str, float] = {}
    for edge in edges:
        target = edge["target_entity"]
        scores[target] = scores.get(target, 0.0) + float(edge["strength"])
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


def main() -> None:
    print("entity,total_incoming_dependency_strength")
    for entity, score in rank_dependencies(load_edges()):
        print(f"{entity},{score:.2f}")


if __name__ == "__main__":
    main()
