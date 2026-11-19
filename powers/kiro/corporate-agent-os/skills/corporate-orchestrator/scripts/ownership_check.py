"""Ownership check: every deliverable in the workspace stage folders names its maker, and the maker owns that folder.

Usage:
    python ownership_check.py <project-workdir> [--agents .kiro/agents] [--json]

Each Markdown deliverable under 01-research/ ... 09-operations/ must contain a line
`Made by: <agent-id>` (the maker) and, after review, may contain `Reviewed by: <agent-id>`.
The maker must have a write-scope allow rule in its agent file whose top-level stage folder
matches the file's folder. The orchestrator may own only 00-intake/ and 10-decisions/.
Reviewer must differ from maker.

Why a script and not a permission rule: in Kiro CLI 3.3.0 a sub-agent inherits its parent's deny
rules (observed 2026-11-18), so the orchestrator cannot be denied specialist folders without also
blocking the specialists it delegates to. The check runs at every gate instead.

Exit 0 when every deliverable passes; 1 otherwise. Evidence files (png, json, txt, csv) are skipped.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

STAGES = ["01-research", "02-product", "03-brand", "04-design", "05-architecture",
          "06-build", "07-quality", "08-legal-oss", "09-operations"]
ORCH = "corporate-orchestrator"

def owned_stages(agents_dir: Path) -> dict[str, set[str]]:
    owners: dict[str, set[str]] = {}
    for f in agents_dir.glob("*.json"):
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        dirs = set()
        for r in (j.get("permissions") or {}).get("rules", []):
            if r.get("capability") == "fs_write" and r.get("effect") == "allow":
                dirs |= {m.split("/")[0] for m in r.get("match", [])}
        owners[j.get("name", f.stem)] = dirs
    return owners

ALL_STAGES = set(STAGES) | {"00-intake", "10-decisions"}


def check(work: Path, agents_dir: Path) -> list[dict]:
    owners = owned_stages(agents_dir)
    results = []
    # Stray stage folders (e.g. an agent inventing 06-security/) escape both the write rules and the ownership map.
    for d in sorted(work.iterdir()) if work.exists() else []:
        if d.is_dir() and re.match(r"^\d\d-", d.name) and d.name not in ALL_STAGES:
            files = [f for f in d.rglob("*") if f.is_file()]
            results.append({"file": d.name + "/", "maker": None, "reviewer": None, "ok": False,
                            "problem": f"stray stage folder with {len(files)} files; stage folders are fixed ({', '.join(sorted(ALL_STAGES))}); move the files into the owning stage folder"})
    for stage in STAGES:
        for f in sorted((work / stage).rglob("*.md")) if (work / stage).exists() else []:
            if "evidence" in f.parts:
                continue
            text = f.read_text(encoding="utf-8", errors="replace")
            maker = (re.search(r"(?mi)^\W*made by:\s*`?([a-z0-9-]+)`?", text) or [None, None])[1]
            reviewer = (re.search(r"(?mi)^\W*reviewed by:\s*`?([a-z0-9-]+)`?", text) or [None, None])[1]
            rel = f.relative_to(work).as_posix()
            problem = None
            if not maker:
                problem = "no 'Made by: <agent-id>' line"
            elif maker == ORCH:
                problem = "made by the orchestrator, which may write only 00-intake/ and 10-decisions/; delegate to the owning agent"
            elif maker not in owners:
                problem = f"maker '{maker}' is not an installed agent"
            elif stage not in owners[maker]:
                problem = f"maker '{maker}' does not own {stage}/ (owns: {', '.join(sorted(owners[maker])) or 'nothing'})"
            elif reviewer and reviewer == maker:
                problem = "reviewer is the maker"
            results.append({"file": rel, "maker": maker, "reviewer": reviewer, "ok": problem is None, "problem": problem})
    return results

def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    work = Path(args[0])
    agents_dir = Path(argv[argv.index("--agents") + 1]) if "--agents" in argv else work / ".kiro" / "agents"
    res = check(work, agents_dir)
    if "--json" in argv:
        print(json.dumps(res, indent=2))
    else:
        for r in res:
            print(("PASS  " if r["ok"] else "FAIL  ") + r["file"] + ("" if r["ok"] else f"  -> {r['problem']}"))
        bad = sum(not r["ok"] for r in res)
        print(f"\n{len(res)} deliverables, {bad} failing  ->  {'FAIL' if bad else 'PASS'}")
    return 1 if any(not r["ok"] for r in res) else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
