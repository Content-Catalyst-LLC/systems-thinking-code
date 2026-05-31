"""Represent nested systems using parent-child relationships."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_system_entities.csv"


def load_entities() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_tree(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    children: dict[str, list[str]] = defaultdict(list)
    id_to_name = {row["entity_id"]: row["entity_name"] for row in rows}
    for row in rows:
        parent = row["parent_entity_id"]
        if parent:
            children[id_to_name[parent]].append(row["entity_name"])
    return dict(children)


def main() -> None:
    tree = build_tree(load_entities())
    print("Nested system relationships:")
    for parent, children in tree.items():
        print(f"{parent}: {', '.join(children)}")


if __name__ == "__main__":
    main()
