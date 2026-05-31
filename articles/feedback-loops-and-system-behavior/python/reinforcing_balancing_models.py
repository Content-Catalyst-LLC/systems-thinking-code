"""Reusable reinforcing and balancing feedback functions."""

from __future__ import annotations


def reinforcing_next(current: float, rate: float) -> float:
    """Return the next value for a proportional reinforcing process."""
    return current * (1.0 + rate)


def balancing_next(current: float, goal: float, adjustment_rate: float) -> float:
    """Return the next value for a goal-seeking balancing process."""
    return current + adjustment_rate * (goal - current)


def classify_loop(number_of_negative_links: int) -> str:
    """Classify a loop as reinforcing or balancing from causal polarity."""
    if number_of_negative_links < 0:
        raise ValueError("number_of_negative_links must be non-negative")
    return "reinforcing" if number_of_negative_links % 2 == 0 else "balancing"


def main() -> None:
    print("negative_links,loop_type")
    for negative_links in range(0, 6):
        print(f"{negative_links},{classify_loop(negative_links)}")


if __name__ == "__main__":
    main()
