#!/usr/bin/env python3
"""Warn when access dates in research/source-register.md are older than a threshold (default 90 days).

Usage: python scripts/maintenance/check_source_dates.py [--days N]
Exit code 0 always; this is advisory."""
from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "research/source-register.md"


def main(argv: list[str]) -> int:
    days = int(argv[argv.index("--days") + 1]) if "--days" in argv else 90
    cutoff = date.today() - timedelta(days=days)
    stale = 0
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| S") and not line.startswith("| T"):
            continue
        m = re.search(r"\| (\d{4}-\d{2}-\d{2}) \|", line)
        if m and date.fromisoformat(m.group(1)) < cutoff:
            stale += 1
            print(f"STALE ({m.group(1)}): {line.split('|')[1].strip()} {line.split('|')[3].strip()[:60]}")
    print(f"{stale} source(s) accessed more than {days} days ago; re-verify before relying on them.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
