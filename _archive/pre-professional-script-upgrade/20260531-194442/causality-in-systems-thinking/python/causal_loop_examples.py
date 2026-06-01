"""
Causal loop examples for systems thinking.

This script compares a reinforcing trust loop and a balancing correction loop.
It uses only the Python standard library.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CausalLoopRow:
    period: int
    reinforcing_trust: float
    balancing_pressure: float


def simulate_loops(periods: int = 18) -> list[CausalLoopRow]:
    trust = 40.0
    performance = 50.0
    pressure = 80.0
    target_pressure = 45.0
    rows: list[CausalLoopRow] = []

    for period in range(1, periods + 1):
        performance += trust * 0.025
        trust += performance * 0.015

        correction = 0.22 * (target_pressure - pressure)
        pressure += correction

        rows.append(
            CausalLoopRow(
                period=period,
                reinforcing_trust=round(trust, 2),
                balancing_pressure=round(pressure, 2),
            )
        )

    return rows


def main() -> None:
    print("period,reinforcing_trust,balancing_pressure")
    for row in simulate_loops():
        print(f"{row.period},{row.reinforcing_trust},{row.balancing_pressure}")


if __name__ == "__main__":
    main()
