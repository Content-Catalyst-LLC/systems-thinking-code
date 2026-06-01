#!/usr/bin/env python3
"""Paradigm scenario model.

The same starting system is evaluated under different paradigms. This example is
not predictive; it demonstrates how goals and assumptions change trajectories.
"""

from __future__ import annotations

PARADIGMS = {
    "growth": {"revenue": 0.9, "resilience": 0.2, "burden": 0.15, "external_cost_visibility": 0.2},
    "stewardship": {"revenue": 0.45, "resilience": 0.9, "burden": 0.7, "external_cost_visibility": 0.9},
    "dignity": {"revenue": 0.4, "resilience": 0.65, "burden": 0.95, "external_cost_visibility": 0.85},
}


def evaluate(paradigm: str) -> dict[str, float]:
    p = PARADIGMS[paradigm]
    visible_success = 0.5 * p["revenue"] + 0.3 * p["resilience"] + 0.2 * p["burden"]
    hidden_cost = (1 - p["external_cost_visibility"]) * (0.5 * p["revenue"] + 0.2)
    whole_system_score = visible_success - hidden_cost
    return {
        "visible_success": round(visible_success, 3),
        "hidden_cost": round(hidden_cost, 3),
        "whole_system_score": round(whole_system_score, 3),
    }


def main() -> None:
    for name in PARADIGMS:
        print(name, evaluate(name))


if __name__ == "__main__":
    main()
