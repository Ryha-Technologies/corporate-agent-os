#!/usr/bin/env python3
"""Validate a project memory ledger (JSON Lines) against core/memory/memory-entry.schema.json and ledger rules.

Usage: python scripts/validate/validate_memory.py <ledger.jsonl>   (default: core/memory/examples/memory-ledger.jsonl)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, find_schema, finish, load_json, rel, validate_schema  # noqa: E402

SCHEMA = find_schema("memory-entry.schema.json", "core/memory/memory-entry.schema.json")
PREFIX = {"fact": "F", "hypothesis": "H", "assumption": "A", "recommendation": "R", "decision": "D",
          "risk": "K", "lesson": "L", "open_question": "Q", "rejected_alternative": "X"}
FACT_PROVENANCE = {"user_statement", "primary_source", "observation", "experiment", "human_decision"}


def validate_ledger(path: Path, report: Report) -> None:
    schema = load_json(SCHEMA, report)
    if schema is None or not path.exists():
        report.error(f"{rel(path)}: missing")
        return
    ids: dict[str, dict] = {}
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as exc:
            report.error(f"{rel(path)}:{n}: invalid JSON: {exc}")
            continue
        for err in validate_schema(entry, schema):
            report.error(f"{rel(path)}:{n}: {err}")
        eid, etype = entry.get("id", ""), entry.get("type")
        if etype in PREFIX and not eid.startswith(PREFIX[etype] + "-"):
            report.error(f"{rel(path)}:{n}: id '{eid}' prefix does not match type '{etype}'")
        if etype == "fact" and entry.get("provenance", {}).get("kind") not in FACT_PROVENANCE:
            report.error(f"{rel(path)}:{n}: a fact needs provenance from {sorted(FACT_PROVENANCE)}, got '{entry.get('provenance', {}).get('kind')}'")
        if etype in ("hypothesis", "assumption") and not entry.get("review_by"):
            report.warn(f"{rel(path)}:{n}: {etype} without review_by date")
        if eid in ids:
            report.error(f"{rel(path)}:{n}: duplicate id '{eid}'")
        ids[eid] = entry
    for eid, e in ids.items():
        sup = e.get("supersedes")
        if sup and sup not in ids:
            report.error(f"{rel(path)}: {eid} supersedes unknown entry '{sup}'")
        for r in e.get("related", []):
            if r not in ids:
                report.warn(f"{rel(path)}: {eid} relates to unknown entry '{r}'")
    report.note(f"{rel(path)}: {len(ids)} ledger entries")


def run(path: Path | None = None) -> Report:
    report = Report("memory")
    validate_ledger(path or ROOT / "core/memory/examples/memory-ledger.jsonl", report)
    return report


if __name__ == "__main__":
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
    sys.exit(finish([run(target)]))
