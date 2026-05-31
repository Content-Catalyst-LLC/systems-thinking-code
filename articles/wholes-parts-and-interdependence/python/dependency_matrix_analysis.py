"""
Dependency matrix analysis for "Wholes, Parts, and Interdependence".

Uses only the Python standard library.
"""

from __future__ import annotations

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
PARTS_PATH = DATA_DIR / "synthetic_system_parts.csv"
EDGES_PATH = DATA_DIR / "synthetic_dependency_edges.csv"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_matrix(parts: list[dict[str, str]], edges: list[dict[str, str]]) -> list[list[float]]:
    ids = [part["part_id"] for part in parts]
    names_to_ids = {part["part_name"]: part["part_id"] for part in parts}
    index = {part_id: i for i, part_id in enumerate(ids)}
    matrix = [[0.0 for _ in ids] for _ in ids]

    for edge in edges:
        source = names_to_ids.get(edge["source"])
        target = names_to_ids.get(edge["target"])
        if source in index and target in index:
            matrix[index[source]][index[target]] = float(edge["weight"])

    return matrix


def dependency_scores(parts: list[dict[str, str]], matrix: list[list[float]]) -> list[tuple[str, float, float]]:
    scores = []
    for i, part in enumerate(parts):
        outgoing = sum(matrix[i])
        incoming = sum(row[i] for row in matrix)
        scores.append((part["part_name"], round(outgoing, 2), round(incoming, 2)))
    return scores


def main() -> None:
    parts = load_csv(PARTS_PATH)
    edges = load_csv(EDGES_PATH)
    matrix = build_matrix(parts, edges)

    print("part_name,outgoing_dependency,incoming_dependency")
    for name, outgoing, incoming in dependency_scores(parts, matrix):
        print(f"{name},{outgoing},{incoming}")


if __name__ == "__main__":
    main()
