#!/usr/bin/env python3
"""Distributional goal analysis using synthetic group-level outcomes."""

from __future__ import annotations

GROUPS = {
    "high_buffer_households": {"delay_sensitivity": 0.15, "burden_sensitivity": 0.2},
    "low_buffer_households": {"delay_sensitivity": 0.75, "burden_sensitivity": 0.85},
    "disabled_applicants": {"delay_sensitivity": 0.65, "burden_sensitivity": 0.95},
    "frontline_workers": {"delay_sensitivity": 0.4, "burden_sensitivity": 0.7},
}


def harm_score(delay: float, burden: float, sensitivities: dict[str, float]) -> float:
    return round(delay * sensitivities["delay_sensitivity"] + burden * sensitivities["burden_sensitivity"], 3)


def main() -> None:
    delay = 0.6
    burden = 0.7
    for group, sensitivities in GROUPS.items():
        print(group, harm_score(delay, burden, sensitivities))


if __name__ == "__main__":
    main()
