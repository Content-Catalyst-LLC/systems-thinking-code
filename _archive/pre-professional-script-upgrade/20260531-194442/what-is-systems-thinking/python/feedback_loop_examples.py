"""
Feedback loop examples for "What Is Systems Thinking?"

This script demonstrates simple reinforcing and balancing feedback behavior.
It uses only the Python standard library.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FeedbackResult:
    period: int
    reinforcing_value: float
    balancing_value: float


def simulate_feedback(periods: int = 20) -> list[FeedbackResult]:
    reinforcing_value = 10.0
    balancing_value = 80.0
    target = 50.0
    results: list[FeedbackResult] = []

    for period in range(1, periods + 1):
        reinforcing_value = reinforcing_value + (0.12 * reinforcing_value)
        adjustment = 0.20 * (target - balancing_value)
        balancing_value = balancing_value + adjustment
        results.append(
            FeedbackResult(
                period=period,
                reinforcing_value=round(reinforcing_value, 2),
                balancing_value=round(balancing_value, 2),
            )
        )

    return results


def main() -> None:
    print("period,reinforcing_value,balancing_value")
    for row in simulate_feedback():
        print(f"{row.period},{row.reinforcing_value},{row.balancing_value}")


if __name__ == "__main__":
    main()
