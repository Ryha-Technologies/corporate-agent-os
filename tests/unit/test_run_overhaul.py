"""Launcher: approval parsing, build refusal without approvals, stray-folder detection, preflight shape."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "run"))
import run_overhaul as ro  # noqa: E402


def test_approval_parsing(tmp_path):
    (tmp_path / "10-decisions").mkdir()
    (tmp_path / "10-decisions/approvals.md").write_text(
        "# Approvals\n- M-2: approved by Velluraju C on 2026-11-18\n- S-1: rejected\n* M-3: Approved by Velluraju C on 2026-11-19\n", encoding="utf-8")
    ids = [a[0] for a in ro.approvals(tmp_path)]
    assert ids == ["M-2", "M-3"]


def test_direction_approval(tmp_path):
    (tmp_path / "04-design").mkdir()
    f = tmp_path / "04-design/research-record.md"
    f.write_text("## Approved direction\nAWAITING_APPROVAL\n", encoding="utf-8")
    assert not ro.direction_approved(tmp_path)
    f.write_text("## Approved direction\nApproved by Velluraju C on 2026-11-18: Direction A\n", encoding="utf-8")
    assert ro.direction_approved(tmp_path)


def test_build_phase_refuses_without_approval(tmp_path):
    pre = {n: ok for n, ok, _ in ro.preflight(tmp_path, "build")}
    assert pre["approvals recorded (10-decisions/approvals.md)"] is False
    assert pre["design direction approved (04-design/research-record.md)"] is False
    r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/run/run_overhaul.py"), "--project", str(tmp_path), "--phase", "build", "--no-install", "--dry-run"], capture_output=True, text=True)
    assert r.returncode == 1 and "nothing was run" in r.stdout, r.stdout


def test_prompt_lists_only_approved_items(tmp_path):
    (tmp_path / "10-decisions").mkdir()
    (tmp_path / "10-decisions/approvals.md").write_text("- M-2: approved by A on 2026-11-18\n", encoding="utf-8")
    p = ro.prompt_for("build", tmp_path, "go")
    assert "M-2" in p and "S-1" not in p and "ONLY these approved items" in p


def test_stray_stage_folder_detected(tmp_path):
    (tmp_path / "06-security").mkdir()
    (tmp_path / "06-security/notes.md").write_text("x", encoding="utf-8")
    r = subprocess.run([sys.executable, "-B", str(ROOT / "skills/corporate-orchestrator/scripts/ownership_check.py"), str(tmp_path), "--agents", str(ROOT / "adapters/kiro/agents")], capture_output=True, text=True)
    assert r.returncode == 1 and "stray stage folder" in r.stdout, r.stdout


def test_scaffold_is_idempotent_and_readmes_are_not_deliverables(tmp_path):
    scaf = ROOT / "skills/corporate-orchestrator/scripts/scaffold_workspace.py"
    own = ROOT / "skills/corporate-orchestrator/scripts/ownership_check.py"
    agents = ROOT / "adapters/kiro/agents"
    r1 = subprocess.run([sys.executable, "-B", str(scaf), str(tmp_path), "--agents", str(agents)], capture_output=True, text=True)
    assert "11 README(s) created" in r1.stdout
    (tmp_path / "03-brand/README.md").write_text("custom", encoding="utf-8")
    r2 = subprocess.run([sys.executable, "-B", str(scaf), str(tmp_path), "--agents", str(agents)], capture_output=True, text=True)
    assert "0 README(s) created" in r2.stdout and (tmp_path / "03-brand/README.md").read_text(encoding="utf-8") == "custom"
    assert "brand-strategist" in (tmp_path / "01-research/README.md").read_text(encoding="utf-8") or "competitive-analyst" in (tmp_path / "01-research/README.md").read_text(encoding="utf-8")
    r3 = subprocess.run([sys.executable, "-B", str(own), str(tmp_path), "--agents", str(agents)], capture_output=True, text=True)
    assert r3.returncode == 0, r3.stdout
