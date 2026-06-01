"""Detect overshoot in growth trajectories."""

from __future__ import annotations

from pathlib import Path
import csv


def diagnose(path: Path) -> list[dict[str, str]]:
    with path.open() as f:
        rows = list(csv.DictReader(f))
    diagnostics = []
    for row in rows:
        scenario = row.get("scenario", "unknown")
        final_scale = float(row.get("final_scale", 0))
        remaining_resource = float(row.get("remaining_resource", 0))
        overshoot = row.get("overshoot_flag", "false").lower() == "true"
        diagnostics.append(
            {
                "scenario": scenario,
                "overshoot": str(overshoot).lower(),
                "risk_level": "high" if overshoot and remaining_resource < 300 else "moderate" if overshoot else "low",
                "diagnosis": "growth exceeded support conditions" if overshoot else "growth remained within modeled support conditions",
                "final_scale": str(final_scale),
            }
        )
    return diagnostics


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    rows = diagnose(base / "data" / "synthetic_outputs.csv")
    out = base / "outputs" / "tables" / "overshoot_diagnostics.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
