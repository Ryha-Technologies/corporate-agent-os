#!/usr/bin/env python3
"""Validate core/ specifications: quality gates, permission policy, budget policy, task examples, memory examples."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, load_json, load_yaml, main_single, rel, validate_schema  # noqa: E402
from validate_tasks import validate_task_folder  # noqa: E402
from validate_memory import validate_ledger  # noqa: E402

GATE_REQUIRED = ["id", "name", "reviewer", "evidence", "pass", "fail", "remediation", "human_approval"]
SEVERITIES = {"critical", "high", "medium", "low"}


def run() -> Report:
    report = Report("core")
    # Gates
    gates = load_yaml(ROOT / "core/quality-gates/gates.yaml", report)
    if isinstance(gates, dict):
        ids = set()
        for g in gates.get("gates", []):
            gid = g.get("id", "?")
            if gid in ids:
                report.error(f"gates.yaml: duplicate gate '{gid}'")
            ids.add(gid)
            for k in GATE_REQUIRED:
                if k not in g:
                    report.error(f"gates.yaml [{gid}]: missing '{k}'")
            for f in g.get("fail", []):
                if f.get("severity") not in SEVERITIES:
                    report.error(f"gates.yaml [{gid}]: fail condition with invalid severity '{f.get('severity')}'")
                if not f.get("condition"):
                    report.error(f"gates.yaml [{gid}]: fail condition without text")
            if not isinstance(g.get("human_approval"), bool):
                report.error(f"gates.yaml [{gid}]: human_approval must be boolean")
        report.note(f"{len(ids)} quality gates")
    # Permissions policy
    pol = load_yaml(ROOT / "core/permissions/policy.yaml", report)
    if isinstance(pol, dict):
        for k in ("tools", "autonomy_levels", "tier_defaults", "human_approval_required", "denied", "shell", "untrusted_inputs"):
            if k not in pol:
                report.error(f"policy.yaml: missing '{k}'")
        for tier, d in pol.get("tier_defaults", {}).items():
            unknown = set(d.get("tools", [])) - set(pol.get("tools", {}).keys())
            if unknown:
                report.error(f"policy.yaml: tier '{tier}' uses undefined tools {sorted(unknown)}")
        if not pol.get("shell", {}).get("deny"):
            report.error("policy.yaml: shell.deny list is empty")
    # Budget policy
    bud = load_yaml(ROOT / "core/budget-management/budget-policy.yaml", report)
    if isinstance(bud, dict):
        for k in ("project_defaults", "task_defaults", "cost_tracking", "stop_conditions", "audit_trail"):
            if k not in bud:
                report.error(f"budget-policy.yaml: missing '{k}'")
        by_risk = bud.get("task_defaults", {}).get("by_risk", {})
        for r in ("low", "medium", "high", "critical"):
            if r not in by_risk:
                report.error(f"budget-policy.yaml: task_defaults.by_risk missing '{r}'")
            elif by_risk[r].get("max_retries", 0) > 3:
                report.error(f"budget-policy.yaml: max_retries for '{r}' exceeds schema maximum 3")
    # Schemas parse and are draft 2020-12
    for schema_path in (ROOT / "core/task-management/task-contract.schema.json",
                        ROOT / "core/workflow-engine/workflow.schema.json",
                        ROOT / "core/memory/memory-entry.schema.json"):
        s = load_json(schema_path, report)
        if isinstance(s, dict) and s.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            report.error(f"{rel(schema_path)}: expected JSON Schema draft 2020-12")
    # Examples
    validate_task_folder(ROOT / "core/task-management/examples", report)
    validate_ledger(ROOT / "core/memory/examples/memory-ledger.jsonl", report)
    # Orchestrator docs exist
    for doc in ("core/orchestrator/operating-procedure.md", "core/orchestrator/report-format.md",
                "core/model-routing/routing-policy.md"):
        if not (ROOT / doc).exists():
            report.error(f"missing {doc}")
    return report


if __name__ == "__main__":
    main_single(run)
