#!/usr/bin/env python3
"""Metric sensitivity workflow.

Shows how changing metric weights can alter which scenario appears best.
"""

from __future__ import annotations

SCENARIOS = {
    "throughput_baseline": {"throughput": 0.9, "access": 0.45, "dignity": 0.3, "burden": 0.8},
    "dignity_reform": {"throughput": 0.72, "access": 0.78, "dignity": 0.82, "burden": 0.28},
    "resilience_repair": {"throughput": 0.68, "access": 0.72, "dignity": 0.75, "burden": 0.35},
}


def score(scenario: dict[str, float], access_weight: float) -> float:
    throughput_weight = 1.0 - access_weight
    return round(
        throughput_weight * scenario["throughput"]
        + access_weight * scenario["access"]
        + 0.5 * scenario["dignity"]
        - 0.5 * scenario["burden"],
        3,
    )


def main() -> None:
    for access_weight in [0.0, 0.25, 0.5, 0.75, 1.0]:
        ranked = sorted(
            ((name, score(values, access_weight)) for name, values in SCENARIOS.items()),
            key=lambda item: item[1],
            reverse=True,
        )
        print(f"access_weight={access_weight:.2f}: {ranked}")


if __name__ == "__main__":
    main()
