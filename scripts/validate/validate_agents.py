#!/usr/bin/env python3
"""Validate canonical agent definitions under agents/**/*.yaml (see agents/README.md)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ABSTRACT_TOOLS, AGENT_ID_RE, ROOT, TIERS, TIER_TOOL_CEILING, Report,
    load_all_agents, load_all_skills, load_departments, load_gates, main_single,
)

REQUIRED = ["id", "tier", "department", "title", "description", "mission", "skills", "tools",
            "write_scope", "autonomy", "approval_required", "never", "model_class", "prompt"]
AUTONOMY = {"execute", "propose", "advise"}
MODEL_CLASSES = {"reasoning", "balanced", "fast"}
TIER_FOLDER = {
    "orchestrator": "orchestrator", "executive": "executive", "department-lead": "department-leads",
    "specialist": "specialists", "reviewer": "reviewers",
}


def run() -> Report:
    report = Report("agents")
    agents = load_all_agents(report)
    skills = load_all_skills()
    departments = load_departments(Report("departments-for-agents"))
    gates = load_gates(report)
    reviewers_by_gate: dict[str, list[str]] = {g: [] for g in gates}

    for aid, a in agents.items():
        where = f"{a['_file']} [{aid}]"
        for key in REQUIRED:
            if key not in a:
                report.error(f"{where}: missing field '{key}'")
        if not AGENT_ID_RE.match(aid):
            report.error(f"{where}: invalid id")
        tier = a.get("tier")
        if tier not in TIERS:
            report.error(f"{where}: invalid tier '{tier}'")
        else:
            expected_folder = TIER_FOLDER[tier]
            if f"agents/{expected_folder}/" not in a["_file"]:
                report.error(f"{where}: tier '{tier}' must live under agents/{expected_folder}/")
        if a.get("department") not in departments:
            report.error(f"{where}: unknown department '{a.get('department')}'")
        desc = a.get("description", "")
        if not isinstance(desc, str) or len(desc) > 200:
            report.error(f"{where}: description must be a string of at most 200 characters (got {len(desc) if isinstance(desc, str) else 'non-string'})")
        for s in a.get("skills", []):
            if s not in skills:
                report.error(f"{where}: unknown skill '{s}'")
        if "anti-slop-quality-gate" not in a.get("skills", []):
            report.warn(f"{where}: does not load anti-slop-quality-gate")
        tools = set(a.get("tools", []))
        unknown = tools - ABSTRACT_TOOLS
        if unknown:
            report.error(f"{where}: unknown tools {sorted(unknown)}")
        if tier in TIER_TOOL_CEILING:
            over = tools - TIER_TOOL_CEILING[tier]
            if over:
                report.error(f"{where}: tools {sorted(over)} exceed the ceiling for tier '{tier}'")
        if tier == "reviewer":
            if "write" in tools:
                report.error(f"{where}: reviewers must not have the write tool")
            if a.get("write_scope"):
                report.error(f"{where}: reviewers must have an empty write_scope")
            if a.get("autonomy") != "advise":
                report.error(f"{where}: reviewers must have autonomy 'advise'")
            revs = a.get("reviews")
            if not revs:
                report.error(f"{where}: reviewers must list 'reviews' gate ids")
            else:
                for g in revs:
                    if g not in gates:
                        report.error(f"{where}: unknown gate '{g}' in reviews")
                    else:
                        reviewers_by_gate[g].append(aid)
        if tier == "executive":
            if tools & {"write", "shell", "subagent"}:
                report.error(f"{where}: executives advise only; no write/shell/subagent")
            if a.get("autonomy") != "advise":
                report.error(f"{where}: executives must have autonomy 'advise'")
        if tier == "specialist" and "subagent" in tools:
            report.error(f"{where}: specialists may not delegate")
        if a.get("autonomy") not in AUTONOMY:
            report.error(f"{where}: invalid autonomy '{a.get('autonomy')}'")
        if a.get("model_class") not in MODEL_CLASSES:
            report.error(f"{where}: invalid model_class '{a.get('model_class')}'")
        prompt = a.get("prompt", "")
        if not isinstance(prompt, str) or len(prompt.strip()) < 120:
            report.error(f"{where}: prompt is missing or too short to be useful")
        if "write" in tools and not a.get("write_scope"):
            report.error(f"{where}: write tool without write_scope")

    for g, revs in reviewers_by_gate.items():
        gate_reviewer = gates[g].get("reviewer")
        if gate_reviewer not in agents:
            report.error(f"gates.yaml: gate '{g}' names unknown reviewer '{gate_reviewer}'")
        elif g not in agents[gate_reviewer].get("reviews", []):
            report.error(f"gates.yaml: gate '{g}' reviewer '{gate_reviewer}' does not list this gate in its reviews")
        if not revs:
            report.error(f"gate '{g}' has no reviewer agent")

    counts = {t: sum(1 for a in agents.values() if a.get("tier") == t) for t in sorted(TIERS)}
    report.note(f"{len(agents)} agents: {counts}")
    return report


if __name__ == "__main__":
    main_single(run)
