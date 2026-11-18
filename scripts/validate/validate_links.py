#!/usr/bin/env python3
"""Check that relative Markdown links across the repository resolve to existing files or directories."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, main_single, rel  # noqa: E402

IGNORED = {".git", "__pycache__", ".pytest_cache", "dist", "node_modules", ".venv"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def run() -> Report:
    report = Report("links")
    checked = 0
    for md in ROOT.rglob("*.md"):
        if any(p in IGNORED for p in md.relative_to(ROOT).parts):
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for m in list(LINK_RE.finditer(text)) + list(IMG_RE.finditer(text)):
            target = unquote(m.group(1))
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#")[0]
            if not target:
                continue
            candidate = (md.parent / target).resolve() if not target.startswith("/") else (ROOT / target.lstrip("/")).resolve()
            checked += 1
            if not candidate.exists():
                report.error(f"{rel(md)}: broken link -> {target}")
    report.note(f"{checked} relative links checked")
    return report


if __name__ == "__main__":
    main_single(run)
