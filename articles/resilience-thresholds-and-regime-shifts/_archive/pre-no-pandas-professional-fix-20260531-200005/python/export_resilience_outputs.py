#!/usr/bin/env python3
"""Create a compact manifest of generated resilience outputs."""

from __future__ import annotations

from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"


def main() -> None:
    manifest = []
    for path in sorted(TABLE_DIR.glob("*.csv")):
        try:
            rows = len(pd.read_csv(path))
        except Exception:
            rows = None
        manifest.append({"file": str(path.relative_to(ROOT)), "rows": rows})
    (ROOT / "outputs" / "resilience_output_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Output manifest written")
    for item in manifest:
        print(f"- {item['file']} ({item['rows']} rows)")


if __name__ == "__main__":
    main()
