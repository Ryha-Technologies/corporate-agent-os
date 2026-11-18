#!/usr/bin/env python3
"""Produce a file inventory (path, bytes, SHA-256) for a directory, as Markdown or JSON.

Usage: python scripts/audit/inventory.py <dir> [--json] [--summary]
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

IGNORED = {".git", "__pycache__", ".pytest_cache", "node_modules", ".venv"}


def inventory(base: Path) -> list[dict]:
    rows = []
    for p in sorted(base.rglob("*")):
        if p.is_file() and not any(part in IGNORED for part in p.relative_to(base).parts):
            rows.append({"path": p.relative_to(base).as_posix(), "bytes": p.stat().st_size,
                         "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    return rows


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    base = Path(argv[0]).resolve()
    rows = inventory(base)
    if "--json" in argv:
        print(json.dumps(rows, indent=2))
        return 0
    if "--summary" in argv:
        by_top = Counter(r["path"].split("/")[0] if "/" in r["path"] else "(root)" for r in rows)
        by_ext = Counter(Path(r["path"]).suffix or "(none)" for r in rows)
        print(f"{len(rows)} files, {sum(r['bytes'] for r in rows):,} bytes under {base}")
        print("\nBy top-level folder:")
        for k, v in sorted(by_top.items()):
            print(f"  {k:28} {v}")
        print("\nBy extension:")
        for k, v in sorted(by_ext.items(), key=lambda kv: -kv[1]):
            print(f"  {k:10} {v}")
        return 0
    print("| Path | Bytes | SHA-256 |")
    print("|---|---|---|")
    for r in rows:
        print(f"| {r['path']} | {r['bytes']} | {r['sha256'][:16]}… |")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
