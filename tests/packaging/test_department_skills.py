"""Department entry skills are generated, current, and cover every non-orchestrator skill."""
import subprocess
import sys
from pathlib import Path

import build_department_skills as bds


def test_department_skills_are_current():
    assert bds.check() == []


def test_every_skill_belongs_to_a_department():
    grouped = {m for g in bds.GROUPS.values() for m in g["members"]}
    for d in bds.SKILLS.iterdir():
        if d.is_dir() and not d.name.startswith("dept-") and d.name != "corporate-orchestrator":
            assert d.name in grouped, d.name


def test_department_skill_mentions_each_member():
    for name, g in bds.GROUPS.items():
        text = (bds.SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        for m in g["members"]:
            assert f"`{m}`" in text, (name, m)


def test_template_signature_runs_static(tmp_path: Path):
    """The scorer must work without a browser (static fallback) and flag a textbook template."""
    html = tmp_path / "t.html"
    html.write_text(
        "<html><body><section class='hero' style='text-align:center'><h1>Build AI agents</h1><p>Supercharge your workflow</p>"
        "<a class='btn'>Start</a><a class='btn'>Docs</a></section>"
        + "".join(f"<section><h2>F{i}</h2><div class='grid'>" + "".join(f"<div class='card'><h3>x</h3><p>y</p></div>" for _ in range(4)) + "</div></section>" for i in range(5))
        + "<section><p>Trusted by thousands</p></section></body></html>", encoding="utf-8")
    script = bds.SKILLS / "ui-ux-design" / "scripts" / "template_signature.py"
    import os
    env = dict(os.environ, CHROME=str(tmp_path / "no-chrome"), TEMPLATE_SIGNATURE_STATIC="1")
    r = subprocess.run([sys.executable, str(script), str(html)], capture_output=True, text=True, env=env)
    assert "COMMON" in r.stdout, r.stdout + r.stderr
    assert r.returncode == 1
