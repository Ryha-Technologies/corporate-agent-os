"""Generate one entry-point skill per department group (skills/dept-*/SKILL.md).

A department skill is what a user invokes when they want a whole department to handle a request
("design department: redesign my dashboard"). It routes to the member skills, carries the
department's non-negotiables (research-first for design, evidence for research, approval gates),
and ends with an independent review. Member lists and descriptions are read from the real skills
so the generated text cannot drift.

Run: python scripts/package/build_department_skills.py   (also run by build_power.py's callers in CI)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

GROUPS: dict[str, dict] = {
    "dept-design": {
        "title": "Design department",
        "department": "design",
        "members": ["ux-research", "information-architecture", "ui-ux-design", "design-system",
                    "accessibility-audit", "codebase-audit-upgrade"],
        "reviewers": ["design-qa-auditor", "ux-auditor"],
        "lead": "design-lead",
        "scope": "any user-experience or interface request: new screens or flows, redesign of an existing UI, 'make it unique', design systems and tokens, accessibility, audits of existing apps and sites, motion",
        "nonneg": [
            "Research before design: category table, pattern map, psychology analysis and three scored directions exist and are shown to the user before anything is built (`skills/ui-ux-design/references/design-research-method.md`).",
            "An existing UI is scored with `skills/ui-ux-design/scripts/template_signature.py` (web) or `template_signature_android.py` (Android) first; `COMMON` means redesign, not a report. The platform default (Material 3, HIG) counts as part of the category template (`skills/ui-ux-design/references/mobile-android-patterns.md`).",
            "Directions come from `skills/ui-ux-design/references/creative-ideation.md`: a lens per direction from three families, derived from the job and never from a reference, with a distance table (minimum 8/14 against every reference) and a sibling check; 'like <competitor>' is discarded.",
            "No screen, component, theme, logo or UI code is produced until `python skills/ui-ux-design/scripts/design_gate.py <workdir>` prints `DESIGN GATE OPEN`; a request to skip research is answered with the shortest compliant path, never by skipping.",
            "The result is re-scored, swap-tested and screenshotted at 360/768/1280 before it is called done.",
        ],
        "routes": [
            ("Redesign or 'it looks generic / AI-made'", "ui-ux-design (Phase 0 score → research → directions → approval → build → re-score), design-system, accessibility-audit"),
            ("New product screens or flows", "ux-research → information-architecture → ui-ux-design → design-system → accessibility-audit"),
            ("Audit an existing app or site", "codebase-audit-upgrade (security, UX, UI, branding, slop → approved proposal → build)"),
            ("Design tokens or component library", "design-system, then ui-ux-design for the reference screens"),
            ("Accessibility review", "accessibility-audit"),
        ],
    },
    "dept-branding": {
        "title": "Branding and creative department",
        "department": "branding",
        "members": ["brand-strategy-story", "naming-ip-screen", "logo-design", "brandbook-identity",
                    "creative-production", "originality-audit"],
        "reviewers": ["brand-originality-auditor"],
        "lead": "brand-creative-director",
        "scope": "any brand or creative request: positioning and story, names and preliminary IP screening, logos and identity systems, brandbooks, decks, documents, image and video briefs, campaigns",
        "nonneg": [
            "Category audit with dated references before any creative work; clichés listed and avoided.",
            "Names are screened (`naming-ip-screen`) before they are used anywhere; statuses are preliminary, never legal advice.",
            "Every creative deliverable passes `originality-audit` by an agent that did not make it.",
        ],
        "routes": [
            ("Brand from scratch", "brand-strategy-story → naming-ip-screen → logo-design → brandbook-identity → originality-audit"),
            ("Logo or identity only", "logo-design → brandbook-identity (logo system section) → originality-audit"),
            ("Deck, document, poster, campaign asset", "creative-production (research-first) → originality-audit"),
            ("Rename or check a name", "naming-ip-screen"),
        ],
    },
    "dept-engineering": {
        "title": "Engineering department",
        "department": "engineering",
        "members": ["architecture-system-design", "api-database-design", "software-engineering", "code-review",
                    "devops-sre", "data-ai-systems", "technical-documentation"],
        "reviewers": ["architecture-reviewer", "code-reviewer", "test-auditor"],
        "lead": "engineering-lead",
        "scope": "any software request: architecture and ADRs, API and data design, implementation in the existing stack, refactors, CI/CD and operations, data and AI systems, documentation",
        "nonneg": [
            "Inspect before editing; never replace the stack or reformat unrelated code.",
            "Every change ships with tests that were actually run; output is pasted, failures disclosed.",
            "Code review by an agent that did not write the code before merge is proposed.",
        ],
        "routes": [
            ("Build or change a feature", "software-engineering (vertical slices) → code-review → technical-documentation"),
            ("Design a system or service", "architecture-system-design → api-database-design → software-engineering"),
            ("Deploy, CI, reliability", "devops-sre"),
            ("Data pipelines, models, evaluations", "data-ai-systems"),
            ("Docs, README, guides", "technical-documentation"),
        ],
    },
    "dept-security": {
        "title": "Security and privacy department",
        "department": "cybersecurity",
        "members": ["threat-modeling", "security-privacy", "incident-response"],
        "reviewers": ["security-auditor"],
        "lead": "security-lead",
        "scope": "any security or privacy request: threat models, application and infrastructure reviews, dependency and secret scanning, privacy analysis, incident handling",
        "nonneg": [
            "Findings carry severity, exact location and a retest method; scanner output is pasted, never summarised from memory.",
            "Secrets found are reported by location only.",
            "No offensive testing against systems the user has not confirmed they own.",
        ],
        "routes": [
            ("Review an application or repo", "security-privacy (with codebase-audit-upgrade Phase A step 2 for the checklist)"),
            ("Design-time security", "threat-modeling → security-privacy"),
            ("Something is happening now", "incident-response"),
        ],
    },
    "dept-quality": {
        "title": "Quality and evaluation department",
        "department": "qa",
        "members": ["test-strategy", "qa-evaluation", "anti-slop-quality-gate", "originality-audit"],
        "reviewers": ["test-auditor", "documentation-auditor"],
        "lead": "qa-lead",
        "scope": "any verification request: test strategy and plans, independent evaluation of a deliverable, release readiness, anti-slop and originality checks",
        "nonneg": [
            "A verdict is GO, GO_WITH_ACCEPTED_RISKS or NO_GO with evidence; polish is not evidence.",
            "`NOT_RUN` is stated for every check that was not executed.",
            "The evaluator did not make the artefact.",
        ],
        "routes": [
            ("Is this ready to ship?", "qa-evaluation (release readiness)"),
            ("Plan testing for a product", "test-strategy"),
            ("Does this look generic or fabricated?", "anti-slop-quality-gate (self) or originality-audit (independent)"),
        ],
    },
    "dept-research": {
        "title": "Research and intelligence department",
        "department": "research",
        "members": ["research-intelligence", "competitive-analysis", "ux-research"],
        "reviewers": ["research-auditor"],
        "lead": "research-lead",
        "scope": "any evidence request: market, customer, competitor and technology research, source evaluation, user research planning and synthesis",
        "nonneg": [
            "Every claim has a dated source or is labelled as an assumption; confidence stated; disconfirming evidence sought.",
            "No fabricated interviews, statistics or quotes.",
        ],
        "routes": [
            ("Market or technology question", "research-intelligence"),
            ("Who are the competitors and what do they do", "competitive-analysis"),
            ("What do users need", "ux-research"),
        ],
    },
    "dept-strategy-product": {
        "title": "Strategy and product department",
        "department": "product",
        "members": ["executive-business-review", "strategy-market-sizing", "business-idea-validation", "business-model-unit-economics", "product-discovery-prd"],
        "reviewers": ["business-model-auditor"],
        "lead": "product-lead",
        "scope": "any strategy or product-definition request: idea validation with kill criteria, market sizing, business models and unit economics, PRDs with testable acceptance criteria",
        "nonneg": [
            "Numbers are ranges with stated assumptions; search volume is never presented as demand.",
            "A PRD has acceptance criteria a tester can run.",
        ],
        "routes": [
            ("Review the whole business, decide, and plan to production", "executive-business-review (commissions dept-research and business-model-unit-economics as needed) → workflows/idea-to-production"),
            ("Is this idea worth building", "business-idea-validation → strategy-market-sizing → business-model-unit-economics"),
            ("Define the product", "product-discovery-prd"),
        ],
    },
    "dept-growth": {
        "title": "Growth, sales and customer department",
        "department": "marketing",
        "members": ["growth-gtm", "product-launch", "sales-partnerships", "customer-success-support"],
        "reviewers": ["documentation-auditor"],
        "lead": "growth-lead",
        "scope": "any go-to-market request: positioning into channels, launch plans, sales motions and partnerships, onboarding and support playbooks",
        "nonneg": [
            "No invented testimonials, logos, user counts or urgency.",
            "Launch plans name the rollback and the monitoring, not just the announcement.",
        ],
        "routes": [
            ("Go to market", "growth-gtm → product-launch"),
            ("Sell or partner", "sales-partnerships"),
            ("Keep customers successful", "customer-success-support"),
        ],
    },
    "dept-operations": {
        "title": "Finance, people and operations department",
        "department": "operations",
        "members": ["finance-operations", "people-operations"],
        "reviewers": ["business-model-auditor"],
        "lead": "operations-lead",
        "scope": "any operating request: budgets and runway, pricing operations, hiring plans, role charters, onboarding, operating cadences",
        "nonneg": [
            "Budgets reconcile; assumptions are listed; nothing is presented as advice on tax, employment law or securities.",
        ],
        "routes": [
            ("Money", "finance-operations"),
            ("People", "people-operations"),
        ],
    },
    "dept-legal": {
        "title": "Legal research department",
        "department": "legal",
        "members": ["legal-risk-governance", "oss-reuse-license"],
        "reviewers": ["legal-licensing-reviewer"],
        "lead": "legal-lead",
        "scope": "any legal-research request: risk registers, governance, privacy obligations, open-source licence compatibility and reuse",
        "nonneg": [
            "Output is research and questions for counsel, never legal advice; this is stated in every deliverable.",
        ],
        "routes": [
            ("Can we use this library or asset", "oss-reuse-license"),
            ("What are our obligations and risks", "legal-risk-governance"),
        ],
    },
}


def first_sentence(text: str) -> str:
    t = re.sub(r"\s+", " ", text.strip().strip('"'))
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    return (m.group(1) if m else t).strip()


def read_desc(skill: str) -> str:
    md = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")
    fm = md.split("---")[1]
    m = re.search(r"^description:\s*(.+?)(?=^\w+:|\Z)", fm, re.S | re.M)
    if not m:
        raise SystemExit(f"{skill}: no description")
    return first_sentence(m.group(1))


def render(name: str, g: dict) -> str:
    members = "\n".join(f"| `{m}` | {read_desc(m)} |" for m in g["members"])
    routes = "\n".join(f"| {req} | {path} |" for req, path in g["routes"])
    nonneg = "\n".join(f"- {n}" for n in g["nonneg"])
    reviewers = ", ".join(f"`{r}`" for r in g["reviewers"])
    desc = (f"Single entry point for the {g['title'].lower()}: handles {g['scope']}. "
            f"Routes the request to the department's skills in the right order, enforces the department's non-negotiables, "
            f"and ends with independent review. Use when the user names the department or asks for anything in its scope without naming a skill.")
    return f"""---
name: {name}
description: "{desc}"
license: MIT
metadata:
  author: Velluraju C
  version: "{VERSION}"
  department: {g['department']}
---
# {g['title']} (entry point)

## Purpose
Let a user hand the whole department a request and get the complete result: the department selects its skills, runs them in order, applies its standards, and has the output reviewed by an agent that did not make it. Generated by `scripts/package/build_department_skills.py` from the member skills, so the table below cannot drift from them.

## When to use
- The user names the department ("design department, redesign this", "ask security to review this repo") or asks for something in this scope without naming a skill.
- The orchestrator delegates a department-sized stage of a workflow.

## Preconditions
- The request, the user's constraints (stack, must-not-change list, deadline, budget) and access to the relevant files or product.
- Where the request is a design of any kind, the research-first method is in force before anything is produced (`skills/ui-ux-design/references/design-research-method.md`).

## Inputs
- The user's request in their words; existing artefacts (repo, site, documents, brand assets, research); prior decisions.

## Procedure
1. **Intake.** Restate the request as a job: who, what outcome, by when, with what constraints. Ask one question if the outcome is ambiguous; do not assume.
2. **Route.** Pick the member skills and their order from the table below. For requests that span departments, hand the other part to the owning department skill (`dept-*`) or the orchestrator; do not improvise outside this scope.
3. **Non-negotiables.** Apply the department's rules throughout:
{nonneg}
4. **Run the skills** in order, each with its own procedure, outputs and `CHECKS_ACTUALLY_RUN`. Where a skill requires user approval (directions, proposals, names, destructive changes), stop and get it; approval of one step is not approval of the next.
5. **Self-check** with `anti-slop-quality-gate` before review.
6. **Independent review** by {reviewers} (agents that did not make the work). Fix findings or record them as accepted risks with the user's agreement.
7. **Report** in one place: what was asked, what was done, evidence per check, `NOT_RUN` list, open questions, and how to roll back.

### Routing table
| Request | Skills in order |
|---|---|
{routes}

### Member skills
| Skill | Does |
|---|---|
{members}

## Outputs
- The member skills' outputs, one department report (`<stage>/department-report.md`) with evidence and `NOT_RUN`, and the reviewer's verdict.

## Quality criteria
- Every member skill used lists its checks actually run; nothing is claimed that was not executed.
- The department's non-negotiables above are each demonstrably met or the exception is written down with the user's agreement.
- Review came from an agent that did not produce the work.
- Nothing outside this department's scope was improvised; cross-department needs were routed.

## Failure handling
- Request does not fit this department: say which `dept-*` skill or the orchestrator owns it, and stop.
- A member skill cannot complete (tooling missing, access denied): record `NOT_RUN` with the reason and continue with the rest; never infer the missing result.
- User asks to skip the review or an approval step: do the work up to that step, explain what the step protects, and wait.

## Safety boundaries
- No deployments, merges to main, payments, sends or deletions without explicit human approval.
- No fabricated evidence, metrics, screenshots, sources or test results.
- Legal, tax and medical content is research, never advice.

## References
- Member skills listed above (`skills/<name>/SKILL.md`)
- Department lead agent `{g['lead']}` and reviewers {reviewers} (`agents/`)
- `skills/corporate-orchestrator/SKILL.md` for multi-department work
- `skills/anti-slop-quality-gate/SKILL.md`
"""


def build() -> list[str]:
    written = []
    for name, g in GROUPS.items():
        for m in g["members"]:
            if not (SKILLS / m / "SKILL.md").exists():
                raise SystemExit(f"{name}: member skill {m} does not exist")
        out = SKILLS / name / "SKILL.md"
        out.parent.mkdir(exist_ok=True)
        out.write_text(render(name, g), encoding="utf-8", newline="\n")
        written.append(name)
    return written


def check() -> list[str]:
    """Return problems: department skill text out of date, or a non-department skill in no group."""
    problems = []
    grouped = {m for g in GROUPS.values() for m in g["members"]}
    for d in SKILLS.iterdir():
        if not d.is_dir():
            continue
        if d.name.startswith("dept-"):
            if d.name not in GROUPS:
                problems.append(f"{d.name}: not defined in build_department_skills.GROUPS")
            elif (d / "SKILL.md").read_text(encoding="utf-8") != render(d.name, GROUPS[d.name]):
                problems.append(f"{d.name}: SKILL.md is out of date; run build_department_skills.py")
        elif d.name not in grouped and d.name != "corporate-orchestrator":
            problems.append(f"{d.name}: belongs to no department group")
    return problems


if __name__ == "__main__":
    if "--check" in sys.argv:
        p = check()
        print("\n".join(p) if p else "department skills up to date")
        sys.exit(1 if p else 0)
    names = build()
    print(f"Wrote {len(names)} department skills: {', '.join(names)}")
