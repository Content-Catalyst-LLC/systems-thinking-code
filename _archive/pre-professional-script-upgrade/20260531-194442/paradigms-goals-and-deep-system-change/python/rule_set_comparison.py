#!/usr/bin/env python3
"""Compare rule sets: suspicion-based control vs accessible accountability."""

from __future__ import annotations

RULE_SETS = {
    "suspicion_based": {"burden": 0.75, "error_control": 0.7, "trust_repair": 0.1, "access": 0.45},
    "accessible_accountability": {"burden": 0.3, "error_control": 0.65, "trust_repair": 0.75, "access": 0.78},
}


def system_score(rules: dict[str, float]) -> float:
    return round(0.3 * rules["error_control"] + 0.3 * rules["access"] + 0.25 * rules["trust_repair"] - 0.25 * rules["burden"], 3)


def main() -> None:
    for name, rules in RULE_SETS.items():
        print(name, system_score(rules), rules)


if __name__ == "__main__":
    main()
