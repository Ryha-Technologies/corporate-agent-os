#!/usr/bin/env python3
"""Validate departments/*/roles.yaml: fifteen fields per role, startup-stage guidance, agent references."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Report, load_all_agents, load_departments, main_single  # noqa: E402

DEPT_REQUIRED = ["id", "name", "mission", "startup_stage", "agents"]
ROLE_REQUIRED = ["id", "title", "mission", "scope", "activities", "inputs", "outputs", "decides",
                 "needs_approval", "collaborates_with", "reports_to", "kpis", "quality", "tools",
                 "failure_modes", "ai_autonomy", "human_approval"]
AUTONOMY = {"execute", "propose", "advise"}


def run() -> Report:
    report = Report("departments")
    deps = load_departments(report)
    agents = load_all_agents(Report("agents-for-departments"))
    if not deps:
        report.error("no departments found")
        return report
    role_count = 0
    for did, data in deps.items():
        where = data["_file"]
        dept = data["department"]
        for k in DEPT_REQUIRED:
            if k not in dept:
                report.error(f"{where}: department missing '{k}'")
        folder = Path(where).parent.name
        if dept.get("id") != folder:
            report.error(f"{where}: department id '{dept.get('id')}' does not match folder '{folder}'")
        if isinstance(dept.get("startup_stage"), str) and len(dept["startup_stage"]) < 60:
            report.error(f"{where}: startup_stage guidance too short")
        for aid in dept.get("agents", []):
            if aid not in agents:
                report.error(f"{where}: unknown agent '{aid}'")
        roles = data.get("roles", [])
        if not roles:
            report.error(f"{where}: no roles defined")
        seen: set[str] = set()
        for role in roles:
            role_count += 1
            rid = role.get("id", "?")
            if rid in seen:
                report.error(f"{where}: duplicate role id '{rid}'")
            seen.add(rid)
            for k in ROLE_REQUIRED:
                if k not in role:
                    report.error(f"{where} [{rid}]: missing field '{k}'")
                elif isinstance(role[k], list) and not role[k]:
                    report.error(f"{where} [{rid}]: field '{k}' is empty")
            if role.get("ai_autonomy") not in AUTONOMY:
                report.error(f"{where} [{rid}]: invalid ai_autonomy '{role.get('ai_autonomy')}'")
    # Every agent's department must exist
    for aid, a in agents.items():
        if a.get("department") not in deps:
            report.error(f"agent '{aid}' references unknown department '{a.get('department')}'")
    report.note(f"{len(deps)} departments, {role_count} roles")
    return report


if __name__ == "__main__":
    main_single(run)
