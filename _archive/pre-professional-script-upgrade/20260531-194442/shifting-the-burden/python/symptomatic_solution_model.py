#!/usr/bin/env python3
"""Model short-term relief produced by a symptomatic solution."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SymptomaticSolution:
    problem_pressure: float
    intensity: float
    relief_rate: float

    def after_relief(self) -> float:
        return max(0.0, self.problem_pressure - self.relief_rate * self.intensity)


def main() -> None:
    cases = [
        SymptomaticSolution(problem_pressure=80, intensity=10, relief_rate=0.5),
        SymptomaticSolution(problem_pressure=80, intensity=30, relief_rate=0.5),
        SymptomaticSolution(problem_pressure=80, intensity=50, relief_rate=0.5),
    ]

    print("Symptomatic solution model")
    for case in cases:
        print(
            f"pressure={case.problem_pressure:.1f}, "
            f"intensity={case.intensity:.1f}, "
            f"after_relief={case.after_relief():.1f}"
        )


if __name__ == "__main__":
    main()
