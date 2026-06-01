"""
Boundary causal map.

A small adjacency-list example for boundary-related variables.
"""

from __future__ import annotations

GRAPH = {
    "narrow_boundary": ["excluded_stakeholders", "hidden_externalities"],
    "excluded_stakeholders": ["low_legitimacy", "missed_harms"],
    "hidden_externalities": ["false_efficiency", "future_risk"],
    "stakeholder_inclusion": ["better_problem_frame", "higher_legitimacy"],
    "expanded_time_horizon": ["maintenance_visibility", "intergenerational_accountability"],
}


def print_paths(start: str, path: list[str] | None = None) -> None:
    if path is None:
        path = [start]

    next_nodes = GRAPH.get(start, [])
    if not next_nodes:
        print(" -> ".join(path))
        return

    for node in next_nodes:
        print_paths(node, path + [node])


def main() -> None:
    print("Paths from narrow_boundary:")
    print_paths("narrow_boundary")
    print()
    print("Paths from stakeholder_inclusion:")
    print_paths("stakeholder_inclusion")


if __name__ == "__main__":
    main()
