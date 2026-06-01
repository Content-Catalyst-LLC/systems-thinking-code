#!/usr/bin/env python3
"""Generate a structural sensitivity checklist for model review."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

CHECKS = [
    "Does the model include the feedback loop most likely to create policy resistance?",
    "Does the model include administrative burden, trust, capacity, and delay where relevant?",
    "Does the conclusion change if harm continues while repair increases?",
    "Does the conclusion change when distributional groups are modeled separately?",
    "Does the conclusion change if implementation delay doubles?",
    "Does the conclusion change if a threshold is closer than expected?",
]

def main() -> None:
    text = "# Structural Sensitivity Checklist\n\n" + "\n".join(f"- {item}" for item in CHECKS) + "\n"
    path = OUT / "structural_sensitivity_checklist.md"
    path.write_text(text, encoding="utf-8")
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
