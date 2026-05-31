#!/usr/bin/env python3
"""Construct a signed causal graph from synthetic edge data.

This example uses only the Python standard library so it can run in minimal environments.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES = ROOT / "data" / "synthetic_signed_edges.csv"


def load_edges(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_adjacency(edges: list[dict[str, str]]) -> dict[str, list[tuple[str, int, str]]]:
    adjacency: dict[str, list[tuple[str, int, str]]] = {}
    for edge in edges:
        source = edge["source_variable"]
        target = edge["target_variable"]
        sign = 1 if edge["sign"] == "+" else -1
        adjacency.setdefault(source, []).append((target, sign, edge["delay"]))
    return adjacency


def main() -> None:
    edges = load_edges(EDGES)
    adjacency = build_adjacency(edges)
    for source, targets in adjacency.items():
        print(source)
        for target, sign, delay in targets:
            marker = "+" if sign > 0 else "-"
            print(f"  {marker} -> {target} ({delay} delay)")


if __name__ == "__main__":
    main()
