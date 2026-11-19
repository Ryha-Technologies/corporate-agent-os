"""Run the product-overhaul orchestrator on a project, safely, in two approval-separated phases.

Usage:
    python scripts/run/run_overhaul.py --project <dir> --phase audit --request "<what you want>" [--timeout-min 90]
    python scripts/run/run_overhaul.py --project <dir> --phase build [--timeout-min 240]
    python scripts/run/run_overhaul.py --project <dir> --preflight        # checks only, runs nothing
    python scripts/run/run_overhaul.py --project <dir> --check            # post-run checks on existing results

Why this exists: every flag below was learned from a failed live run (2026-11-18). Skills need
`disclose_context`; each specialist is a separate tool named `subagent_<id>`, so `subagent*` is needed;
a build started before approval is the failure the whole system exists to prevent.

Phases
  audit  Phase 0 to 2: inventory, parallel audits by specialists, executive review, overhaul proposal.
         Stops at AWAITING_APPROVAL. Writes nothing outside the stage folders.
  build  Phase 3 to 6 for the items you approved in 10-decisions/approvals.md. Refuses to start without
         at least one approval line of the form:
             - M-2: approved by <name> on YYYY-MM-DD
         and an approved design direction (04-design/research-record.md with 'Approved by').

After every run the script executes the checks that make the result trustworthy, prints PASS/FAIL per check
and writes <project>/.corporate-agent-os/runs/<stamp>/run-summary.md. Exit 0 only if the phase's checks pass.
"""
from __future__ import annotations
import datetime, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
TRUST = "fs_read,fs_write,shell,disclose_context,subagent*"
VERIFIED_KIRO = ("3.3.", "3.5.")  # delegation, trust flags and write-rule behaviour probed live on these (2026-11-18)

# Department -> (what must exist after the audit phase, as glob patterns relative to the project)
AUDIT_COVERAGE: dict[str, list[str]] = {
    "security": ["07-quality/security*.md", "07-quality/*security*.md", "10-decisions/audit/security*.md"],
    "code review": ["06-build/*review*.md", "07-quality/*code*.md", "10-decisions/audit/code*.md"],
    "ux / page logic": ["04-design/*page-logic*.md", "04-design/user-flows.md", "04-design/*ux*.md", "01-research/*ux*.md"],
    "ui / template signature": ["04-design/evidence/**/signature*", "04-design/evidence/**/*.png"],
    "brand": ["03-brand/*.md"],
    "accessibility": ["07-quality/*accessib*.md", "04-design/accessibility*.md"],
    "legal / licences": ["08-legal-oss/*.md"],
    "competitors": ["01-research/competitor*.md"],
    "money (model + payments)": ["02-product/business-model.md", "02-product/payments-plan.md", "02-product/financial-model.*"],
    "devops / performance": ["09-operations/*.md", "06-build/infra*.md", "06-build/platform/*.md"],
}
AUDIT_CORE = ["00-intake/brief.md", "00-intake/inventory.md", "00-intake/page-map.md",
              "10-decisions/audit-report.md", "10-decisions/executive-review.md", "10-decisions/overhaul-proposal.md"]
BUILD_CORE = ["07-quality/release-readiness.md", "10-decisions/final-report.md"]
APPROVAL_RE = re.compile(r"^\s*[-*]\s*([A-Z]-\d+)\s*:\s*approved by\s+(.+?)\s+on\s+(\d{4}-\d{2}-\d{2})\b", re.M | re.I)


def approvals(project: Path) -> list[tuple[str, str, str]]:
    f = project / "10-decisions" / "approvals.md"
    return APPROVAL_RE.findall(f.read_text(encoding="utf-8", errors="replace")) if f.exists() else []


def direction_approved(project: Path) -> bool:
    f = project / "04-design" / "research-record.md"
    if not f.exists():
        return False
    t = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"(?ms)^## +Approved direction\b(.*?)(?=^## |\Z)", t)
    return bool(m and re.search(r"approved by", m.group(1), re.I) and "AWAITING_APPROVAL" not in m.group(1))


def find_chrome() -> str | None:
    sys.path.insert(0, str(ROOT / "skills" / "ui-ux-design" / "scripts"))
    try:
        import template_signature as ts
        return ts.find_chrome()
    except Exception:
        return None


def preflight(project: Path, phase: str | None) -> list[tuple[str, bool, str]]:
    r: list[tuple[str, bool, str]] = []
    r.append(("project folder exists", project.is_dir(), str(project)))
    r.append(("python >= 3.10", sys.version_info >= (3, 10), sys.version.split()[0]))
    kiro = shutil.which("kiro-cli")
    ver = ""
    if kiro:
        try:
            ver = subprocess.run([kiro, "--version"], capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception as e:  # pragma: no cover
            ver = str(e)
    r.append(("kiro-cli on PATH", bool(kiro), ver or "not found"))
    if kiro and not any(v in ver for v in VERIFIED_KIRO):
        r.append(("kiro-cli version is one the delegation behaviour was verified on", False, f"{ver}; verified on {', '.join(VERIFIED_KIRO)}x; run a one-delegation probe before a long run"))
    chrome = find_chrome()
    r.append(("Chrome/Chromium for screenshots (set CHROME if not found)", bool(chrome), chrome or "not found: visual checks would be NOT_RUN"))
    agents = project / ".kiro" / "agents" / "corporate-orchestrator.json"
    r.append(("Corporate Agent OS installed in the project", agents.exists(), "run install.py --target kiro --destination <project> --yes" if not agents.exists() else "ok"))
    if agents.exists():
        n_agents = len(list((project / ".kiro" / "agents").glob("*.json")))
        n_skills = len([d for d in (project / ".kiro" / "skills").iterdir() if d.is_dir()]) if (project / ".kiro" / "skills").exists() else 0
        r.append(("58 agents and every skill installed", n_agents >= 58 and n_skills >= 52, f"{n_agents} agents, {n_skills} skills"))
    git = (project / ".git").exists()
    r.append(("project is a git repository (rollback possible)", git, "ok" if git else "run git init and commit first"))
    if git:
        dirty = subprocess.run(["git", "-C", str(project), "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
        # installed files and stage folders are expected; flag only tracked source changes
        r.append(("no uncommitted source changes", not [l for l in dirty.splitlines() if not re.search(r"\.kiro/|\.corporate-agent-os/|^\?\? \d\d-", l)], "commit or stash your changes" if dirty else "clean"))
    if phase == "build":
        ap = approvals(project)
        r.append(("approvals recorded (10-decisions/approvals.md)", bool(ap), f"{len(ap)} approved items: {', '.join(a[0] for a in ap)}" if ap else "add lines like '- M-2: approved by <name> on YYYY-MM-DD'"))
        r.append(("design direction approved (04-design/research-record.md)", direction_approved(project), "ok" if direction_approved(project) else "present the three directions and record 'Approved by <name> on <date>'"))
        r.append(("audit phase results present", all((project / c).exists() for c in AUDIT_CORE), "ok" if all((project / c).exists() for c in AUDIT_CORE) else "run --phase audit first"))
    if phase == "audit":
        r.append(("owner answers recorded (00-intake/owner-answers.md)", (project / "00-intake" / "owner-answers.md").exists(),
                  "ok" if (project / "00-intake" / "owner-answers.md").exists() else "recommended: answer who owns the name, what you sell, who pays, budget; the proposal blocks on these otherwise"))
    return r


def prompt_for(phase: str, project: Path, request: str) -> str:
    if phase == "audit":
        return (f"{request}\n\nUse the product-overhaul-orchestrator skill. Do Mode detection and Phase 0, then Phase 1 with every audit delegated to its specialist sub-agent in parallel "
                "(security, code, page-logic and UX, UI template signature with screenshots, brand, accessibility, legal and licences, competitors and pricing, money and payments, devops and performance). "
                "Each delegated file starts with 'Made by: <agent-id>' and lives in that agent's own folder. Then Phase 2: executive review and the overhaul proposal in 10-decisions with item ids (M-, S-, C-) for approval. "
                "Read 00-intake/owner-answers.md if it exists and use it instead of asking. Do not build or change any project file. End with AWAITING_APPROVAL.")
    ap = approvals(project)
    ids = ", ".join(a[0] for a in ap)
    return (f"{request}\n\nUse the product-overhaul-orchestrator skill. Run Phase 3 to Phase 6 for ONLY these approved items: {ids}. Anything else in the proposal is out of scope. "
            "Work on a branch named overhaul/<date>. Brand work only if approved. The design direction in 04-design/research-record.md is approved: run design_gate.py (it must print OPEN), tokens first, then pages; "
            "run visual_quality_loop.py with --maker set to the building agent after every pass and a reviewer file written by design-qa-auditor; the only finish is exit code DONE; exit 3 goes to the owner. "
            "Run copy_slop_check.py on all text and ownership_check.py at every gate. Security fixes first. Stop before merge, deploy or any payment switch and write release-readiness.md for the owner's approval.")


def check_results(project: Path, phase: str) -> list[tuple[str, bool, str]]:
    out: list[tuple[str, bool, str]] = []
    core = AUDIT_CORE if phase == "audit" else AUDIT_CORE + BUILD_CORE
    missing = [c for c in core if not (project / c).exists()]
    out.append((f"core {phase} files exist", not missing, "ok" if not missing else "missing: " + ", ".join(missing)))
    if phase == "audit":
        gaps = [d for d, pats in AUDIT_COVERAGE.items() if not any(list(project.glob(p)) for p in pats)]
        out.append(("every department audit is on disk (not only in chat)", not gaps, "ok" if not gaps else "missing: " + ", ".join(gaps)))
        prop = project / "10-decisions" / "overhaul-proposal.md"
        txt = prop.read_text(encoding="utf-8", errors="replace") if prop.exists() else ""
        built = [p for p in (project / "06-build").rglob("*") if p.is_file()] if (project / "06-build").exists() else []
        out.append(("proposal is AWAITING_APPROVAL and nothing was built", "AWAITING_APPROVAL" in txt and not built,
                    "ok" if "AWAITING_APPROVAL" in txt and not built else ("proposal does not state AWAITING_APPROVAL" if "AWAITING_APPROVAL" not in txt else f"{len(built)} files already in 06-build/")))
        changed = subprocess.run(["git", "-C", str(project), "diff", "--name-only"], capture_output=True, text=True).stdout.split() if (project / ".git").exists() else []
        src_changed = [c for c in changed if not re.match(r"(\.kiro|\.corporate-agent-os|\d\d-)", c)]
        out.append(("audit phase changed no project source file", not src_changed, "ok" if not src_changed else "changed: " + ", ".join(src_changed[:5])))
    own = subprocess.run([sys.executable, "-B", str(ROOT / "skills/corporate-orchestrator/scripts/ownership_check.py"), str(project)], capture_output=True, text=True)
    out.append(("ownership: every deliverable has a maker who owns the folder", own.returncode == 0, "ok" if own.returncode == 0 else " | ".join(l for l in own.stdout.splitlines() if l.startswith("FAIL"))[:300]))
    stages = [str(project / d) for d in ("00-intake", "01-research", "02-product", "03-brand", "10-decisions") if (project / d).exists()]
    cp = subprocess.run([sys.executable, "-B", str(ROOT / "skills/anti-slop-quality-gate/scripts/copy_slop_check.py"), *stages], capture_output=True, text=True)
    out.append(("copy slop check on written text", cp.returncode == 0, cp.stdout.strip().splitlines()[-1] if cp.stdout.strip() else "no text"))
    if phase == "build":
        gate = subprocess.run([sys.executable, "-B", str(ROOT / "skills/ui-ux-design/scripts/design_gate.py"), str(project)], capture_output=True, text=True)
        out.append(("design gate OPEN", gate.returncode == 0, gate.stdout.strip().splitlines()[0] if gate.stdout.strip() else ""))
        hist = sorted(project.glob("04-design/evidence/**/score-history.json"))
        done = False
        if hist:
            h = json.loads(hist[-1].read_text(encoding="utf-8"))
            done = len(h) >= 2 and all(x["score"] >= 90 and x["reviewed"] for x in h[-2:])
        out.append(("visual quality loop DONE (two reviewed passes >= 90)", done, "ok" if done else "no history or not two reviewed passes at 90"))
    return out


def install_if_needed(project: Path) -> None:
    if not (project / ".kiro" / "agents" / "corporate-orchestrator.json").exists():
        subprocess.run([sys.executable, "-B", str(ROOT / "scripts/install/install.py"), "--target", "kiro", "--destination", str(project), "--yes"], check=True)


def main(argv: list[str]) -> int:
    def opt(n, d=None):
        return argv[argv.index(n) + 1] if n in argv else d
    project = Path(opt("--project", ".")).resolve()
    phase = opt("--phase")
    if "--preflight" in argv or "--check" in argv or phase:
        pass
    else:
        print(__doc__); return 2
    if phase and phase not in ("audit", "build"):
        print("--phase must be audit or build"); return 2
    if "--check" in argv:
        res = check_results(project, phase or "audit")
        for n, ok, why in res:
            print(("PASS  " if ok else "FAIL  ") + n + ("" if ok else f"  -> {why}"))
        return 0 if all(ok for _, ok, _ in res) else 1
    install_ok = "--no-install" not in argv
    if install_ok and phase and project.is_dir():
        install_if_needed(project)
    pre = preflight(project, phase)
    hard = [c for c in pre if not c[1] and not c[0].startswith(("Chrome", "owner answers", "project is a git", "no uncommitted", "kiro-cli version"))]
    for n, ok, why in pre:
        print(("ok    " if ok else "FAIL  ") + n + f"  ({why})")
    if "--preflight" in argv:
        return 1 if hard else 0
    if hard:
        print("\nPreflight failed; nothing was run."); return 1
    if not phase:
        return 0
    request = opt("--request", "Do your work on this project.")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = project / ".corporate-agent-os" / "runs" / stamp
    run_dir.mkdir(parents=True, exist_ok=True)
    cmd = ["kiro-cli", "chat", "--agent", "corporate-orchestrator", "--no-interactive", f"--trust-tools={TRUST}", prompt_for(phase, project, request)]
    if "--dry-run" in argv:
        print("\nWould run:\n  " + " ".join(f'"{c}"' if " " in c else c for c in cmd[:5]) + ' "<prompt>"'); return 0
    log = run_dir / "run.log"
    print(f"\nRunning phase '{phase}' (log: {log}). This takes a while; Ctrl+C stops it and the results so far stay on disk.")
    try:
        with log.open("w", encoding="utf-8", errors="replace") as fh:
            subprocess.run(cmd, cwd=project, stdout=fh, stderr=subprocess.STDOUT, timeout=int(opt("--timeout-min", "120")) * 60)
    except subprocess.TimeoutExpired:
        print("Timed out; checking what exists.")
    subs = len(re.findall(r"\[tool\] Sub-agent: (\S+)", log.read_text(encoding="utf-8", errors="replace")))
    res = check_results(project, phase)
    res.insert(0, ("work was delegated to specialist sub-agents", subs >= 3, f"{subs} delegation calls"))
    kv = subprocess.run(["kiro-cli", "--version"], capture_output=True, text=True).stdout.strip()
    lines = [f"# Run summary: {phase} ({stamp})", "", f"Host: {kv}", "", "| Check | Result | Detail |", "|---|---|---|"]
    for n, ok, why in res:
        print(("PASS  " if ok else "FAIL  ") + n + ("" if ok else f"  -> {why}"))
        lines.append(f"| {n} | {'PASS' if ok else 'FAIL'} | {why} |")
    (run_dir / "run-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nSummary: {run_dir / 'run-summary.md'}")
    if phase == "audit":
        print("Next: read 10-decisions/overhaul-proposal.md, record your decisions in 10-decisions/approvals.md "
              "('- M-2: approved by <name> on YYYY-MM-DD'), then run --phase build.")
    return 0 if all(ok for _, ok, _ in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
