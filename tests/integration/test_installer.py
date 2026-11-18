"""Integration tests for scripts/install/install.py against a temporary project directory."""
import json
from pathlib import Path

import install


def _run(args):
    return install.main(args)


def test_dry_run_writes_nothing(project_dir: Path, capsys):
    code = _run(["--target", "kiro", "--destination", str(project_dir), "--dry-run"])
    assert code == 0
    assert not (project_dir / ".kiro").exists()
    out = capsys.readouterr().out
    assert "Dry run" in out and "Destination:" in out and "create" in out


def test_install_kiro_creates_expected_files(project_dir: Path):
    code = _run(["--target", "kiro", "--destination", str(project_dir), "--yes"])
    assert code == 0
    assert (project_dir / ".kiro/skills/corporate-orchestrator/SKILL.md").exists()
    assert (project_dir / ".kiro/agents/corporate-orchestrator.md").exists()
    assert (project_dir / ".kiro/steering/corporate-agent-os.md").exists()
    assert (project_dir / ".kiro/hooks/corporate-agent-os-guards.json").exists()
    assert (project_dir / ".corporate-agent-os/validators/validate_tasks.py").exists()
    assert (project_dir / ".corporate-agent-os/validators/schemas/task-contract.schema.json").exists()
    manifest = json.loads((project_dir / ".corporate-agent-os/manifest.json").read_text(encoding="utf-8"))
    assert manifest["installs"][0]["target"] == "kiro"
    assert manifest["installs"][0]["version"] == "0.2.0"
    assert len(manifest["installs"][0]["files"]) > 50


def test_existing_agents_md_is_preserved(project_dir: Path):
    (project_dir / "AGENTS.md").write_text("my own rules\n", encoding="utf-8")
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes"]) == 0
    assert (project_dir / "AGENTS.md").read_text(encoding="utf-8") == "my own rules\n"
    assert (project_dir / "CORPORATE-AGENT-OS-AGENTS.md").exists()


def test_existing_file_is_backed_up_before_replace(project_dir: Path):
    target = project_dir / ".claude/skills/corporate-orchestrator/SKILL.md"
    target.parent.mkdir(parents=True)
    target.write_text("user version\n", encoding="utf-8")
    assert _run(["--target", "claude", "--destination", str(project_dir), "--yes"]) == 0
    assert target.read_text(encoding="utf-8") != "user version\n"
    backups = list((project_dir / ".corporate-agent-os/backup").rglob("SKILL.md"))
    assert backups and backups[0].read_text(encoding="utf-8") == "user version\n"


def test_unrelated_files_untouched(project_dir: Path):
    other = project_dir / ".kiro/skills/my-own-skill/SKILL.md"
    other.parent.mkdir(parents=True)
    other.write_text("---\nname: my-own-skill\ndescription: mine\n---\nkeep me\n", encoding="utf-8")
    assert _run(["--target", "kiro", "--destination", str(project_dir), "--yes"]) == 0
    assert other.read_text(encoding="utf-8").endswith("keep me\n")


def test_reinstall_is_idempotent(project_dir: Path, capsys):
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes"]) == 0
    capsys.readouterr()
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes"]) == 0
    out = capsys.readouterr().out
    assert "create: 0" in out and "replace (backed up): 0" in out


def test_skill_subset(project_dir: Path):
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes", "--skills", "corporate-orchestrator,research-intelligence"]) == 0
    installed = {p.name for p in (project_dir / ".agents/skills").iterdir()}
    assert installed == {"corporate-orchestrator", "research-intelligence"}


def test_unknown_skill_rejected(project_dir: Path):
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes", "--skills", "does-not-exist"]) == 2


def test_refuses_to_install_into_repo(root: Path):
    assert _run(["--target", "kiro", "--destination", str(root), "--dry-run"]) == 2


def test_uninstall_removes_unmodified_and_keeps_modified(project_dir: Path):
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes"]) == 0
    modified = project_dir / ".agents/skills/research-intelligence/SKILL.md"
    modified.write_text(modified.read_text(encoding="utf-8") + "\nlocal edit\n", encoding="utf-8")
    assert _run(["--target", "codex", "--destination", str(project_dir), "--uninstall"]) == 0
    assert not (project_dir / ".agents/skills/corporate-orchestrator").exists()
    assert modified.exists()
    assert not (project_dir / "AGENTS.md").exists()


def test_uninstall_restores_backup(project_dir: Path):
    target = project_dir / ".agents/skills/corporate-orchestrator/SKILL.md"
    target.parent.mkdir(parents=True)
    target.write_text("original\n", encoding="utf-8")
    assert _run(["--target", "codex", "--destination", str(project_dir), "--yes"]) == 0
    assert _run(["--target", "codex", "--destination", str(project_dir), "--uninstall"]) == 0
    assert target.read_text(encoding="utf-8") == "original\n"


def test_installed_validators_run_standalone(project_dir: Path, tmp_path: Path):
    """The project-side validators must work without the repository (schema found next to them)."""
    import subprocess, sys
    assert _run(["--target", "kiro", "--destination", str(project_dir), "--yes"]) == 0
    tasks = project_dir / "10-decisions/tasks"
    tasks.mkdir(parents=True)
    src = Path(__file__).resolve().parents[2] / "core/task-management/examples/T-003-competitor-map.json"
    (tasks / "T-003.json").write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    res = subprocess.run([sys.executable, str(project_dir / ".corporate-agent-os/validators/validate_tasks.py"), str(tasks)],
                         capture_output=True, text=True, cwd=project_dir)
    assert res.returncode == 0, res.stdout + res.stderr
    assert "1 task contracts" in res.stdout
