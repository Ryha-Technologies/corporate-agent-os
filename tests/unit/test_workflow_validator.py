"""Unit tests for the workflow DAG validator using synthetic workflows."""
from pathlib import Path

import yaml

import validate_workflows
from common import Report, load_all_agents, load_all_skills, load_gates, load_json

SCHEMA = load_json(validate_workflows.SCHEMA_PATH, Report("s"))
AGENTS = load_all_agents(Report("a"))
SKILLS = load_all_skills()
GATES = load_gates(Report("g"))


def _run(tmp_path: Path, wf: dict) -> Report:
    d = tmp_path / wf["id"]
    d.mkdir(exist_ok=True)
    p = d / "workflow.yaml"
    p.write_text(yaml.safe_dump(wf, sort_keys=False), encoding="utf-8")
    r = Report("wf")
    validate_workflows.validate_workflow(p, r, AGENTS, SKILLS, GATES, SCHEMA)
    return r


def _base(**overrides) -> dict:
    wf = {
        "id": "synthetic-flow",
        "name": "Synthetic flow",
        "summary": "A synthetic workflow used only by the test suite to exercise validator rules.",
        "trigger": "Test suite invocation.",
        "stages": [
            {"id": "a", "agent": "corporate-orchestrator", "objective": "Write the intake brief", "depends_on": [], "outputs": ["00-intake/brief.md"]},
            {"id": "b", "agent": "research-analyst", "objective": "Gather evidence for the brief", "depends_on": ["a"], "outputs": ["01-research/evidence-ledger.md"],
             "gate": "discovery", "review": "research-auditor"},
        ],
    }
    wf.update(overrides)
    return wf


def test_valid_workflow_passes(tmp_path):
    assert _run(tmp_path, _base()).ok


def test_cycle_detected(tmp_path):
    wf = _base()
    wf["stages"][0]["depends_on"] = ["b"]
    r = _run(tmp_path, wf)
    assert any("cycle" in e for e in r.errors)


def test_unknown_dependency(tmp_path):
    wf = _base()
    wf["stages"][1]["depends_on"] = ["zzz"]
    r = _run(tmp_path, wf)
    assert any("unknown stage 'zzz'" in e for e in r.errors)


def test_reviewer_equals_author_rejected(tmp_path):
    wf = _base()
    wf["stages"][1]["review"] = "research-analyst"
    r = _run(tmp_path, wf)
    assert any("reviewer equals the producing agent" in e for e in r.errors)


def test_gate_requires_review(tmp_path):
    wf = _base()
    del wf["stages"][1]["review"]
    r = _run(tmp_path, wf)
    assert any("requires an independent 'review' agent" in e for e in r.errors)


def test_parallel_group_output_overlap_rejected(tmp_path):
    wf = _base()
    wf["stages"].append({"id": "c", "agent": "competitive-analyst", "objective": "Map the competitor landscape", "depends_on": ["a"],
                         "outputs": ["01-research/evidence-ledger.md"], "parallel_group": "g"})
    wf["stages"][1]["parallel_group"] = "g"
    r = _run(tmp_path, wf)
    assert any("both write" in e for e in r.errors)


def test_reviewer_tier_cannot_write_outside_quality(tmp_path):
    wf = _base()
    wf["stages"].append({"id": "c", "agent": "code-reviewer", "objective": "Review the implemented code", "depends_on": ["a"],
                         "outputs": ["06-build/code.md"]})
    r = _run(tmp_path, wf)
    assert any("outside 07-quality/" in e for e in r.errors)


def test_gate_with_human_approval_requirement(tmp_path):
    wf = _base()
    wf["stages"][1]["gate"] = "opportunity"
    wf["stages"][1]["review"] = "business-model-auditor"
    r = _run(tmp_path, wf)
    assert any("requires human_approval: true" in e for e in r.errors)
    wf["stages"][1]["human_approval"] = True
    assert _run(tmp_path, wf).ok


def test_unknown_agent_skill_gate(tmp_path):
    wf = _base()
    wf["stages"][1]["agent"] = "nobody"
    wf["stages"][1]["skills"] = ["no-such-skill"]
    wf["stages"][1]["gate"] = "no-gate"
    r = _run(tmp_path, wf)
    assert any("unknown agent 'nobody'" in e for e in r.errors)
    assert any("unknown skill 'no-such-skill'" in e for e in r.errors)
    assert any("unknown gate 'no-gate'" in e for e in r.errors)


def test_repository_workflows_pass(root):
    assert validate_workflows.run().ok
