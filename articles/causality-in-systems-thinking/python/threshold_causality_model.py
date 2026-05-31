"""
Threshold causality model.

Below a threshold, stress has modest effects. Above it, decline accelerates.
"""

from __future__ import annotations


def response(stress: float, threshold: float = 70.0) -> float:
    if stress < threshold:
        return 0.25 * stress
    return 0.25 * threshold + 1.15 * (stress - threshold)


def main() -> None:
    print("stress,response")
    for stress in range(40, 101, 5):
        print(f"{stress},{round(response(float(stress)), 2)}")


if __name__ == "__main__":
    main()
