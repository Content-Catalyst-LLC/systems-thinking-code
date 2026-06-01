"""Shared utilities for professional synthetic public-policy workflows."""
from __future__ import annotations

from pathlib import Path
import csv
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_TABLES = ROOT / "outputs" / "tables"
OUT_FIGURES = ROOT / "outputs" / "figures"


def ensure_outputs() -> None:
    OUT_TABLES.mkdir(parents=True, exist_ok=True)
    OUT_FIGURES.mkdir(parents=True, exist_ok=True)


def read_csv_dict(path: Path, required: Iterable[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Required input not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required_set = set(required)
        missing = required_set - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path} is missing required columns: {sorted(missing)}")
        return list(reader)


def write_csv_dict(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def to_float(row: dict[str, str], key: str) -> float:
    try:
        return float(row[key])
    except KeyError as exc:
        raise KeyError(f"Missing column {key!r} in row {row}") from exc
    except ValueError as exc:
        raise ValueError(f"Column {key!r} must be numeric in row {row}") from exc


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))
