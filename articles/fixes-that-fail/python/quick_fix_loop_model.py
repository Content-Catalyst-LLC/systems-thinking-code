#!/usr/bin/env python3
"""Model the short-term balancing loop created by a quick fix."""
from __future__ import annotations


def apply_quick_fix(problem: float, fix_strength: float) -> float:
    """Return the post-fix problem level before delayed consequences arrive."""
    return max(0.0, problem * (1.0 - fix_strength))


def main() -> None:
    for strength in [0.10, 0.25, 0.40, 0.55]:
        print(f"fix_strength={strength:.2f}, remaining_problem={apply_quick_fix(100, strength):.1f}")


if __name__ == "__main__":
    main()
