from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    with (RAW / name).open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    path = OUT / name
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path.relative_to(ROOT)}")


def f(row: dict[str, str], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, default))
    except ValueError:
        return default


def avg(values: list[float]) -> float:
    return mean(values) if values else 0.0
