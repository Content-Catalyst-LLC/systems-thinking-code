"""
Structural cause mapping from synthetic causal edge data.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_causal_edges.csv"


def load_edges(path: Path = DATA_PATH) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize_causal_roles(edges: list[dict[str, str]]) -> Counter[str]:
    return Counter(edge["causal_role"] for edge in edges)


def incoming_causes(edges: list[dict[str, str]], target: str) -> list[dict[str, str]]:
    return [edge for edge in edges if edge["target"] == target]


def main() -> None:
    edges = load_edges()
    print("Causal role counts:")
    for role, count in summarize_causal_roles(edges).most_common():
        print(f"- {role}: {count}")

    print("\nIncoming causes for institutional_capacity:")
    for edge in incoming_causes(edges, "institutional_capacity"):
        print(f"- {edge['source']} ({edge['polarity']}, {edge['delay']} delay): {edge['relationship_note']}")


if __name__ == "__main__":
    main()
