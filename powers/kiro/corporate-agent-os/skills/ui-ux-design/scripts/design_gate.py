"""Design gate: refuses the build phase until the research record exists and is complete.

Usage:
    python design_gate.py <project-workdir> [--record 04-design/research-record.md]

Checks `research-record.md` for the sections and minimum evidence the research-first method requires.
Exit 0 = gate open (build may start). Exit 1 = gate closed, with the list of what is missing.
A reviewer runs the same command; a design handed over with a closed gate is rejected.

The gate checks structure and counts, not quality. It stops the most common failure (skipping research
entirely); the human swap test and the independent reviewer judge the quality.
"""
from __future__ import annotations
import re, sys
from pathlib import Path

REQUIRED = [
    ("## Job", r"^## +(1\. +)?Job\b", "Job statement section (who, doing what, where, deciding what)"),
    ("## Category research", r"^## +(2\. +)?Category research\b", "Category research section"),
    ("## Pattern map", r"^## +(2\.\d +|3\. +)?Pattern map\b", "Pattern map section (category template / keep / free to change / nobody does)"),
    ("## Psychology", r"^## +(3\. +|4\. +)?Psychology\b", "Psychology analysis section"),
    ("## Directions", r"^## +(4\. +|5\. +)?Directions\b", "Directions section (three or more, scored)"),
    ("## Approved direction", r"^## +(5\. +|6\. +)?Approved direction\b", "Approved direction section with the user's choice"),
]

def section(text: str, start_pat: str) -> str:
    m = re.search(start_pat, text, re.M | re.I)
    if not m:
        return ""
    rest = text[m.end():]
    n = re.search(r"^## ", rest, re.M)
    return rest[: n.start()] if n else rest

def table_rows(block: str) -> list[str]:
    rows = [l for l in block.splitlines() if l.strip().startswith("|")]
    rows = [r for r in rows if not re.match(r"^\|\s*-", r.strip()) and not re.match(r"^\|[\s|:-]+\|$", r.strip())]
    return rows[1:] if rows else []  # drop header

def check(record: Path) -> list[str]:
    problems: list[str] = []
    if not record.exists():
        return [f"{record} does not exist. Write the research record before any design output."]
    text = record.read_text(encoding="utf-8", errors="replace")
    for _, pat, why in REQUIRED:
        if not re.search(pat, text, re.M | re.I):
            problems.append(f"missing section: {why}")
    job = section(text, REQUIRED[0][1])
    if job and len(re.sub(r"\s+", " ", job).strip()) < 120:
        problems.append("Job statement is under 120 characters; say who, what task, in what situation, deciding what")
    if job and re.search(r"\b(general users|everyone|all users|anyone)\b", job, re.I):
        problems.append("Job statement names 'general users'; name the real person and situation")
    cat = section(text, REQUIRED[1][1])
    rows = table_rows(cat)
    direct = [r for r in rows if re.search(r"\|\s*direct", r, re.I)]
    adjacent = [r for r in rows if re.search(r"\|\s*adjacent", r, re.I)]
    nondigital = [r for r in rows if re.search(r"non-?digital|physical|print|analog", r, re.I)]
    if len(direct) < 3:
        problems.append(f"category table has {len(direct)} rows marked 'direct'; need at least 3 direct competitors")
    if len(adjacent) < 2:
        problems.append(f"category table has {len(adjacent)} rows marked 'adjacent'; need at least 2")
    if len(nondigital) < 1:
        problems.append("category table has no non-digital reference")
    dated = [r for r in rows if re.search(r"\b20\d\d-\d\d-\d\d\b", r)]
    if rows and len(dated) < len(rows):
        problems.append(f"{len(rows) - len(dated)} category rows have no capture date (YYYY-MM-DD)")
    sourced = [r for r in rows if re.search(r"https?://|\.png|\.jpg|screenshot", r, re.I)]
    if rows and len(sourced) < len(rows):
        problems.append(f"{len(rows) - len(sourced)} category rows have no URL or screenshot reference")
    pm = section(text, REQUIRED[2][1])
    for key in ("template", "keep", "free", "nobody"):
        if pm and key not in pm.lower():
            problems.append(f"pattern map does not cover '{key}' (category template / conventions to keep / free to change / what nobody does)")
    psy = section(text, REQUIRED[3][1])
    prow = table_rows(psy)
    if len(prow) < 4:
        problems.append(f"psychology table has {len(prow)} rows; need at least 4 principles with concrete implications")
    dirs = section(text, REQUIRED[4][1])
    heads = re.findall(r"^### +", dirs, re.M)
    if len(heads) < 3:
        problems.append(f"directions section has {len(heads)} '###' direction headings; need at least 3 distinct directions")
    for key, why in (("departure", "the deliberate departure from the category template"), ("motion", "a motion table or motion note"), ("risk", "a risk")):
        if dirs and dirs.lower().count(key) < max(1, len(heads)):
            problems.append(f"not every direction states {why}")
    if not re.search(r"\|\s*(total|score)", dirs, re.I):
        problems.append("directions section has no scoring table (job fit, uniqueness, psychology, accessibility, cost)")
    appr = section(text, REQUIRED[5][1])
    if appr and not re.search(r"approved by|user chose|chosen by|AWAITING_APPROVAL", appr, re.I):
        problems.append("approved-direction section must say who approved it ('approved by <user> on <date>') or 'AWAITING_APPROVAL'")
    if appr and re.search(r"AWAITING_APPROVAL", appr):
        problems.append("direction is AWAITING_APPROVAL: present the directions to the user and record the choice before building")
    return problems

def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__); return 2
    work = Path(argv[0])
    rel = argv[argv.index("--record") + 1] if "--record" in argv else "04-design/research-record.md"
    record = work / rel
    problems = check(record)
    if problems:
        print(f"DESIGN GATE CLOSED ({record})")
        for p in problems:
            print("  - " + p)
        print("No screen, component, layout, logo, deck or UI code may be produced until this gate is open.")
        return 1
    print(f"DESIGN GATE OPEN ({record}): research record complete; build may start on the approved direction.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
