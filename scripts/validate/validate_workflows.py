#!/usr/bin/env python3
"""Validate workflows/*/workflow.yaml against core/workflow-engine/workflow.schema.json and DAG rules.

Usage:
  python scripts/validate/validate_workflows.py                 # all workflows
  python scripts/validate/validate_workflows.py path/to/workflow.yaml
"""
from __future__ import annotations

import fnmatch
import sys
from collections import defaultdict, deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ROOT, Report, finish, load_all_agents, load_all_skills, load_gates, load_json, load_yaml, rel, validate_schema,
)

SCHEMA_PATH = ROOT / "core" / "workflow-engine" / "workflow.schema.json"


def _overlap(a: str, b: str) -> bool:
    return a == b or fnmatch.fnmatch(a, b) or fnmatch.fnmatch(b, a)


def validate_workflow(path: Path, report: Report, agents: dict, skills: dict, gates: dict, schema: dict) -> None:
    wf = load_yaml(path, report)
    if not isinstance(wf, dict):
        return
    for err in validate_schema(wf, schema):
        report.error(f"{rel(path)}: {err}")
    stages = wf.get("stages", [])
    if not isinstance(stages, list):
        return
    ids = [s.get("id") for s in stages if isinstance(s, dict)]
    if len(ids) != len(set(ids)):
        report.error(f"{rel(path)}: duplicate stage ids")
    idset = set(ids)
    if wf.get("id") != path.parent.name:
        report.error(f"{rel(path)}: workflow id '{wf.get('id')}' does not match folder '{path.parent.name}'")

    # Graph checks
    indeg = {i: 0 for i in idset}
    adj = defaultdict(list)
    for s in stages:
        sid = s.get("id")
        for dep in s.get("depends_on", []):
            if dep not in idset:
                report.error(f"{rel(path)} [{sid}]: depends_on unknown stage '{dep}'")
                continue
            if dep == sid:
                report.error(f"{rel(path)} [{sid}]: stage depends on itself")
            adj[dep].append(sid)
            indeg[sid] += 1
    # Kahn
    q = deque([i for i in idset if indeg[i] == 0])
    visited = 0
    while q:
        n = q.popleft()
        visited += 1
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    if visited != len(idset):
        report.error(f"{rel(path)}: dependency graph contains a cycle")
    roots = [s.get("id") for s in stages if not s.get("depends_on")]
    if not roots:
        report.error(f"{rel(path)}: no root stage (every stage has dependencies)")

    # Per-stage semantic checks
    groups: dict[str, list[dict]] = defaultdict(list)
    for s in stages:
        sid = s.get("id")
        agent = s.get("agent")
        if agent not in agents:
            report.error(f"{rel(path)} [{sid}]: unknown agent '{agent}'")
        for sk in s.get("skills", []):
            if sk not in skills:
                report.error(f"{rel(path)} [{sid}]: unknown skill '{sk}'")
            elif agent in agents and sk not in agents[agent].get("skills", []):
                report.warn(f"{rel(path)} [{sid}]: skill '{sk}' is not in agent '{agent}' skill list")
        rev = s.get("review")
        if rev is not None:
            if rev == agent:
                report.error(f"{rel(path)} [{sid}]: reviewer equals the producing agent")
            if rev not in agents:
                report.error(f"{rel(path)} [{sid}]: unknown reviewer '{rev}'")
            elif agents[rev].get("tier") != "reviewer":
                report.error(f"{rel(path)} [{sid}]: '{rev}' is not a reviewer-tier agent")
        gate = s.get("gate")
        if gate is not None:
            if gate not in gates:
                report.error(f"{rel(path)} [{sid}]: unknown gate '{gate}'")
            else:
                if rev is None:
                    report.error(f"{rel(path)} [{sid}]: gate '{gate}' requires an independent 'review' agent")
                if gates[gate].get("human_approval") and not s.get("human_approval"):
                    report.error(f"{rel(path)} [{sid}]: gate '{gate}' requires human_approval: true")
        if agent in agents and agents[agent].get("tier") == "reviewer" and s.get("outputs"):
            # reviewers may only write verdict files under 07-quality or 10-decisions
            for out in s["outputs"]:
                if not (out.startswith("07-quality/") or out.startswith("10-decisions/")):
                    report.error(f"{rel(path)} [{sid}]: reviewer-tier agent writes '{out}' outside 07-quality/ or 10-decisions/")
        if agent in agents and agents[agent].get("tier") == "executive":
            for out in s.get("outputs", []):
                if not out.startswith("10-decisions/"):
                    report.error(f"{rel(path)} [{sid}]: executive agent may only write decision records under 10-decisions/")
        if s.get("risk") in ("high", "critical") and not (s.get("review") or s.get("human_approval")):
            report.warn(f"{rel(path)} [{sid}]: high/critical risk stage without review or human approval")
        if s.get("parallel_group"):
            groups[s["parallel_group"]].append(s)

    # Disjoint outputs within a parallel group
    for g, members in groups.items():
        for i, a in enumerate(members):
            for b in members[i + 1:]:
                for oa in a.get("outputs", []):
                    for ob in b.get("outputs", []):
                        if _overlap(oa, ob):
                            report.error(f"{rel(path)}: parallel group '{g}' stages '{a['id']}' and '{b['id']}' both write '{oa}'")
    # Outputs unique across the whole workflow unless the later stage depends (transitively) on the earlier one
    owners: dict[str, str] = {}
    for s in stages:
        for out in s.get("outputs", []):
            if out in owners and owners[out] != s["id"]:
                report.warn(f"{rel(path)}: output '{out}' written by '{owners[out]}' and '{s['id']}'")
            owners.setdefault(out, s["id"])
    report.note(f"{rel(path)}: {len(stages)} stages, {len(groups)} parallel groups")


def run(paths: list[Path] | None = None) -> Report:
    report = Report("workflows")
    schema = load_json(SCHEMA_PATH, report)
    if schema is None:
        return report
    agents = load_all_agents(Report("agents-for-workflows"))
    skills = load_all_skills()
    gates = load_gates(report)
    targets = paths or sorted((ROOT / "workflows").glob("*/workflow.yaml"))
    if not targets:
        report.error("no workflows found")
    for p in targets:
        validate_workflow(p, report, agents, skills, gates, schema)
    return report


if __name__ == "__main__":
    args = [Path(a).resolve() for a in sys.argv[1:]]
    sys.exit(finish([run(args or None)]))
