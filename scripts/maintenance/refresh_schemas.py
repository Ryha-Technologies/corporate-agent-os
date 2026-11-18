#!/usr/bin/env python3
"""Re-download the Agent Plugins 1.0.0 schemas into scripts/validate/schemas/. Network access required.
Run deliberately; record the date in research/source-register.md if the content changed."""
from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "scripts/validate/schemas"
URLS = {
    "plugin.schema.json": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
    "mcp.schema.json": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
}


def main() -> int:
    changed = 0
    for name, url in URLS.items():
        with urllib.request.urlopen(url, timeout=30) as resp:  # noqa: S310 - fixed https URLs
            data = resp.read()
        target = DEST / name
        old = target.read_bytes() if target.exists() else b""
        if hashlib.sha256(old).hexdigest() != hashlib.sha256(data).hexdigest():
            target.write_bytes(data)
            changed += 1
            print(f"updated {name}")
        else:
            print(f"unchanged {name}")
    print(f"{changed} file(s) changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
