#!/usr/bin/env python3
"""Export a plain-text urban workflow manifest for documentation and review."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
MANIFEST = ROOT / "outputs" / "urban_outputs_manifest.txt"


def count_rows(path: Path) -> int:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return max(0, sum(1 for _ in csv.reader(handle)) - 1)


def main() -> None:
    paths = sorted(TABLES.glob("*.csv"))
    with MANIFEST.open("w", encoding="utf-8") as handle:
        handle.write("Urban systems generated outputs\n")
        handle.write("================================\n\n")
        for path in paths:
            handle.write(f"{path.relative_to(ROOT)}: {count_rows(path)} data rows\n")
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()
