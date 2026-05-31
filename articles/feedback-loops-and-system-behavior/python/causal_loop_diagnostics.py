"""Causal-loop diagnostics from synthetic causal-edge data."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

EDGES_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_causal_edges.csv"
LOOPS_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_feedback_loops.csv"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def degree_summary(edges: list[dict[str, str]]) -> dict[str, dict[str, int]]:
    summary: dict[str, dict[str, int]] = defaultdict(lambda: {"in": 0, "out": 0})
    for edge in edges:
        summary[edge["source"]]["out"] += 1
        summary[edge["target"]]["in"] += 1
    return dict(summary)


def main() -> None:
    edges = load_csv(EDGES_PATH)
    loops = load_csv(LOOPS_PATH)

    print("Loop inventory:")
    for loop in loops:
        print(f"- {loop['loop_id']} | {loop['loop_name']} | {loop['loop_type']}")

    print("\nVariable degree summary:")
    for variable, counts in sorted(degree_summary(edges).items()):
        print(f"{variable}: in={counts['in']} out={counts['out']}")


if __name__ == "__main__":
    main()
