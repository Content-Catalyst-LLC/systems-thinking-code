"""Compensating feedback model.

A compact numerical example showing why direct intervention effects can be
partly offset by feedback loops that restore the old pattern.
"""
from __future__ import annotations


def observed_effect(intended_effect: float, compensation_strength: float) -> float:
    """Return net effect after compensation."""
    if not 0 <= compensation_strength <= 1.5:
        raise ValueError("compensation_strength should be between 0 and 1.5 for this demo")
    return intended_effect * (1 - compensation_strength)


def main() -> None:
    intended = 100.0
    for compensation in [0.0, 0.25, 0.5, 0.75, 1.0, 1.2]:
        net = observed_effect(intended, compensation)
        print(f"compensation={compensation:.2f} net_effect={net:.1f}")


if __name__ == "__main__":
    main()
