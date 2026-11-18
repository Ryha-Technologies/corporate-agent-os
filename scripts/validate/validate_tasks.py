#!/usr/bin/env python3
"""Validate task contracts (*.json) in a folder against core/task-management/task-contract.schema.json.

Usage: python scripts/validate/validate_tasks.py <folder>   (default: core/task-management/examples)
"""
from __future__ import annotations

import fnmatch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, find_schema, finish, load_json, rel, validate_schema  # noqa: E402

SCHEMA = find_schema("task-contract.schema.json", "core/task-management/task-contract.schema.json")


def validate_task_folder(folder: Path, report: Report) -> None:
    schema = load_json(SCHEMA, report)
    if schema is None:
        return
    files = sorted(folder.glob("*.json"))
    if not files:
        report.error(f"{rel(folder)}: no task files")
        return
    tasks: dict[str, dict] = {}
    for f in files:
        t = load_json(f, report)
        if not isinstance(t, dict):
            continue
        for err in validate_schema(t, schema):
            report.error(f"{rel(f)}: {err}")
        tid = t.get("task_id")
        if tid in tasks:
            report.error(f"{rel(f)}: duplicate task_id {tid}")
        tasks[tid] = t
        if t.get("reviewer") and t.get("reviewer") == t.get("assigned_agent"):
            report.error(f"{rel(f)}: reviewer must differ from assigned_agent")
        if t.get("risk") in ("high", "critical") and not t.get("reviewer"):
            report.error(f"{rel(f)}: high/critical risk tasks need a reviewer")
        if t.get("risk") in ("high", "critical") and t.get("approval") == ["none"]:
            report.error(f"{rel(f)}: high/critical risk tasks cannot have approval ['none']")
        for out in t.get("outputs", []):
            if not any(fnmatch.fnmatch(out, pat) for pat in t.get("file_ownership", [])):
                report.error(f"{rel(f)}: output '{out}' is not covered by file_ownership")
    for tid, t in tasks.items():
        for dep in t.get("dependencies", []):
            if dep not in tasks:
                report.warn(f"task {tid}: dependency {dep} not present in this folder")
    active = [t for t in tasks.values() if t.get("status") in ("READY", "RUNNING")]
    for i, a in enumerate(active):
        for b in active[i + 1:]:
            for pa in a.get("file_ownership", []):
                for pb in b.get("file_ownership", []):
                    if pa == pb or fnmatch.fnmatch(pa, pb) or fnmatch.fnmatch(pb, pa):
                        report.error(f"tasks {a['task_id']} and {b['task_id']} are both active and share ownership '{pa}'")
    report.note(f"{rel(folder)}: {len(tasks)} task contracts")


def run(folder: Path | None = None) -> Report:
    report = Report("tasks")
    validate_task_folder(folder or ROOT / "core/task-management/examples", report)
    return report


if __name__ == "__main__":
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
    sys.exit(finish([run(target)]))
