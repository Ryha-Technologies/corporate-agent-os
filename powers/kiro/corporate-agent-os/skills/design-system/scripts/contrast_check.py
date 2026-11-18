#!/usr/bin/env python3
"""Compute WCAG 2.x contrast ratios for a design-tokens.json file and optionally write them back.

For every colour role with `contrast_against`, computes the ratio of the role's light value against the target
role's light value (and dark against dark), fills `contrast_light` / `contrast_dark`, and reports roles that
fall below 4.5:1 (text) or 3:1 (non-text) unless marked `decorative_only`.

Usage:
  python contrast_check.py tokens.json            # report only
  python contrast_check.py tokens.json --write    # update contrast fields in place
Standard library only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def _lin(c: int) -> float:
    s = c / 255
    return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4


def luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return round((hi + 0.05) / (lo + 0.05), 2)


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    path = Path(argv[0])
    data = json.loads(path.read_text(encoding="utf-8"))
    colours = data.get("color", {})
    failures = 0
    for name, role in colours.items():
        target = role.get("contrast_against")
        if not target or target not in colours:
            continue
        cl = contrast(role["light"], colours[target]["light"])
        cd = contrast(role["dark"], colours[target]["dark"])
        role["contrast_light"], role["contrast_dark"] = cl, cd
        threshold = 3.0 if (name.startswith(("border", "focus")) or role.get("decorative_only")) else 4.5
        flag = ""
        if not role.get("decorative_only") and (cl < threshold or cd < threshold):
            flag = f"  BELOW {threshold}:1"
            failures += 1
        print(f"{name:16} vs {target:12} light {cl:5.2f}  dark {cd:5.2f}{flag}")
    if "--write" in argv:
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"updated {path}")
    print(f"{failures} role(s) below threshold")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
