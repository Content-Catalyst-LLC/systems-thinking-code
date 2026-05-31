"""Compare immediate and delayed limit feedback."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"


def run_case(label: str, delay: int) -> list[dict[str, float | int | str]]:
    pressure = 0.40
    limit = 0.60
    history = [pressure]
    rows = []
    for month in range(31):
        perceived = history[max(0, len(history) - delay - 1)]
        correction = max(0.0, perceived - limit) * 0.45
        pressure = max(0.0, min(1.2, pressure + 0.06 * pressure - correction))
        rows.append({"case": label, "month": month, "pressure": round(pressure, 4), "overshoot": round(max(0.0, pressure - limit), 4)})
        history.append(pressure)
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = run_case("immediate_feedback", 0) + run_case("delayed_feedback", 8)
    out_path = OUT / "delayed_limit_dynamics.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["case", "month", "pressure", "overshoot"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
