"""Unit tests for the memory ledger and task contract validators."""
import json
from pathlib import Path

import validate_memory
import validate_tasks
from common import Report


def _entry(**kw):
    base = {"id": "F-001", "type": "fact", "statement": "The user stated the target market is India.",
            "provenance": {"kind": "user_statement", "source": "00-intake/brief.md"}, "confidence": "high",
            "recorded_by": "corporate-orchestrator", "recorded_at": "2026-11-18T09:00:00Z", "status": "active"}
    base.update(kw)
    return base


def _ledger(tmp_path: Path, entries) -> Path:
    p = tmp_path / "ledger.jsonl"
    p.write_text("\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8")
    return p


def test_valid_ledger(tmp_path):
    r = Report("m")
    validate_memory.validate_ledger(_ledger(tmp_path, [_entry()]), r)
    assert r.ok


def test_fact_needs_strong_provenance(tmp_path):
    r = Report("m")
    validate_memory.validate_ledger(_ledger(tmp_path, [_entry(provenance={"kind": "agent_inference"})]), r)
    assert any("a fact needs provenance" in e for e in r.errors)


def test_prefix_must_match_type(tmp_path):
    r = Report("m")
    validate_memory.validate_ledger(_ledger(tmp_path, [_entry(id="H-001")]), r)
    assert any("prefix does not match type" in e for e in r.errors)


def test_duplicate_and_supersedes(tmp_path):
    r = Report("m")
    validate_memory.validate_ledger(_ledger(tmp_path, [_entry(), _entry(), _entry(id="F-002", supersedes="F-999")]), r)
    assert any("duplicate id" in e for e in r.errors)
    assert any("supersedes unknown entry" in e for e in r.errors)


def test_hypothesis_without_review_by_warns(tmp_path):
    r = Report("m")
    validate_memory.validate_ledger(_ledger(tmp_path, [_entry(id="H-001", type="hypothesis", provenance={"kind": "agent_inference"}, confidence="low")]), r)
    assert r.ok and any("without review_by" in w for w in r.warnings)


def _task(**kw):
    base = json.loads((Path(__file__).resolve().parents[2] / "core/task-management/examples/T-003-competitor-map.json").read_text(encoding="utf-8"))
    base.update(kw)
    return base


def _tasks(tmp_path: Path, tasks) -> Path:
    d = tmp_path / "tasks"
    d.mkdir()
    for t in tasks:
        (d / f"{t['task_id']}.json").write_text(json.dumps(t), encoding="utf-8")
    return d


def test_example_task_valid(tmp_path):
    r = Report("t")
    validate_tasks.validate_task_folder(_tasks(tmp_path, [_task()]), r)
    assert r.ok


def test_reviewer_equals_agent_rejected(tmp_path):
    r = Report("t")
    validate_tasks.validate_task_folder(_tasks(tmp_path, [_task(reviewer="competitive-analyst")]), r)
    assert any("reviewer must differ" in e for e in r.errors)


def test_output_outside_ownership_rejected(tmp_path):
    r = Report("t")
    validate_tasks.validate_task_folder(_tasks(tmp_path, [_task(outputs=["02-product/prd.md"])]), r)
    assert any("not covered by file_ownership" in e for e in r.errors)


def test_high_risk_needs_reviewer_and_approval(tmp_path):
    r = Report("t")
    t = _task(risk="high", approval=["none"])
    del t["reviewer"]
    validate_tasks.validate_task_folder(_tasks(tmp_path, [t]), r)
    assert any("need a reviewer" in e for e in r.errors)
    assert any("cannot have approval ['none']" in e for e in r.errors)


def test_active_tasks_with_overlapping_ownership_rejected(tmp_path):
    r = Report("t")
    a = _task(task_id="T-010", status="RUNNING")
    b = _task(task_id="T-011", status="READY")
    validate_tasks.validate_task_folder(_tasks(tmp_path, [a, b]), r)
    assert any("share ownership" in e for e in r.errors)


def test_unknown_field_rejected(tmp_path):
    r = Report("t")
    validate_tasks.validate_task_folder(_tasks(tmp_path, [_task(surprise=1)]), r)
    assert any("unexpected field 'surprise'" in e for e in r.errors)
