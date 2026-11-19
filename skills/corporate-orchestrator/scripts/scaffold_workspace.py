"""Create the fixed project workspace: eleven stage folders, each with a README naming its owners and outputs.

Usage:
    python scaffold_workspace.py <project-workdir> [--agents .kiro/agents]

Why: in a live run an agent invented `06-security/` because no folder was obviously right. With the
scaffold present, every stage folder exists from intake, its README lists which agents may write there
(read from the installed agent files) and what belongs in it, and `ownership_check.py` flags anything else.
Idempotent: existing files are never overwritten.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

STAGES = {
    "00-intake": "Brief, inventory, page map, owner answers. Written by the orchestrator.",
    "01-research": "Research plans, evidence ledger, competitor map and pricing, customer findings, research brief.",
    "02-product": "Strategy memo, business model, payments plan, financial model, PRD, acceptance criteria, roadmap.",
    "03-brand": "Category audit, brand strategy, messaging, naming report, identity concepts, brandbook, creative assets.",
    "04-design": "Research record (design gate), user flows, IA, states matrix, visual direction, tokens, screens, motion spec, accessibility review, evidence/ (screenshots, scores, pass folders).",
    "05-architecture": "Architecture, ADRs, data model, API contract, threat model, cost model.",
    "06-build": "Build plan, implementation notes per slice, integration report, docs. Code lives on the branch, not here.",
    "07-quality": "Gate verdicts, test strategy and reports, security findings, accessibility reports, traceability, release readiness.",
    "08-legal-oss": "Issue register, counsel questions, component register (libraries and licences), asset provenance.",
    "09-operations": "Positioning, channel and launch plans, runbooks, release record, post-launch review.",
    "10-decisions": "Memory ledger, task contracts, approvals, executive review, audit report, overhaul proposal, final report. Written by the orchestrator.",
}

def owners_by_stage(agents_dir: Path) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {s: [] for s in STAGES}
    for f in sorted(agents_dir.glob("*.json")) if agents_dir.exists() else []:
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for r in (j.get("permissions") or {}).get("rules", []):
            if r.get("capability") == "fs_write" and r.get("effect") == "allow":
                for m in r.get("match", []):
                    top = m.split("/")[0]
                    if top in out and j.get("name") not in out[top]:
                        out[top].append(j.get("name", f.stem))
    return out

def scaffold(work: Path, agents_dir: Path) -> list[str]:
    created: list[str] = []
    owners = owners_by_stage(agents_dir)
    for stage, what in STAGES.items():
        d = work / stage
        d.mkdir(parents=True, exist_ok=True)
        readme = d / "README.md"
        if not readme.exists():
            who = ", ".join(f"`{o}`" for o in owners.get(stage, [])) or "(no installed agent owns this folder)"
            readme.write_text(
                f"# {stage}\n\n{what}\n\n**May write here:** {who}\n\n"
                "Every Markdown deliverable starts with `Made by: <agent-id>`. Reviewed files add `Reviewed by: <agent-id>`.\n"
                "No other stage folders exist; do not create new numbered folders. `ownership_check.py` fails the gate otherwise.\n",
                encoding="utf-8")
            created.append(f"{stage}/README.md")
    ev = work / "04-design" / "evidence"
    ev.mkdir(exist_ok=True)
    return created

def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    work = Path(args[0])
    agents_dir = Path(argv[argv.index("--agents") + 1]) if "--agents" in argv else work / ".kiro" / "agents"
    created = scaffold(work, agents_dir)
    print(f"workspace ready at {work}: {len(created)} README(s) created, {len(STAGES) - len(created)} already present")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
