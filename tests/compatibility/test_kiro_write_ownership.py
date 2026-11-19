"""Generated Kiro agents deny every workspace stage folder outside their own write scope (deny wins over allow)."""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STAGES = ["00-intake", "01-research", "02-product", "03-brand", "04-design", "05-architecture",
          "06-build", "07-quality", "08-legal-oss", "09-operations", "10-decisions"]


def agents():
    for f in (ROOT / "agents").rglob("*.yaml"):
        for a in yaml.safe_load(f.read_text(encoding="utf-8"))["agents"]:
            yield a


def test_delegating_agents_carry_no_stage_denies():
    """Sub-agents inherit the parent's deny rules (Kiro CLI 3.3.0), so a delegating agent must not deny stage folders."""
    for a in agents():
        if "subagent" not in a["tools"]:
            continue
        j = json.loads((ROOT / "adapters/kiro/agents" / f"{a['id']}.json").read_text(encoding="utf-8"))
        deny = {m for r in j["permissions"]["rules"] if r["capability"] == "fs_write" and r["effect"] == "deny" for m in r["match"]}
        assert not any(d.split("/")[0] in STAGES for d in deny), a["id"]


def test_every_writer_is_denied_foreign_stage_folders_and_never_its_own():
    for a in agents():
        if "write" not in a["tools"] or "subagent" in a["tools"]:
            continue
        j = json.loads((ROOT / "adapters/kiro/agents" / f"{a['id']}.json").read_text(encoding="utf-8"))
        deny = {m for r in j["permissions"]["rules"] if r["capability"] == "fs_write" and r["effect"] == "deny" for m in r["match"]}
        own = {w.split("/")[0] for w in a.get("write_scope") or []}
        for d in STAGES:
            if d in own:
                assert f"{d}/**" not in deny, (a["id"], d)
            else:
                assert f"{d}/**" in deny, (a["id"], d)


def test_ownership_check(tmp_path):
    import subprocess, sys
    script = ROOT / "skills/corporate-orchestrator/scripts/ownership_check.py"
    (tmp_path / "01-research").mkdir()
    (tmp_path / "01-research/competitor-map.md").write_text("# Map\nMade by: competitive-analyst\n", encoding="utf-8")
    ok = subprocess.run([sys.executable, "-B", str(script), str(tmp_path), "--agents", str(ROOT / "adapters/kiro/agents")], capture_output=True, text=True)
    assert ok.returncode == 0, ok.stdout
    (tmp_path / "01-research/audit.md").write_text("# Audit\nMade by: corporate-orchestrator\n", encoding="utf-8")
    bad = subprocess.run([sys.executable, "-B", str(script), str(tmp_path), "--agents", str(ROOT / "adapters/kiro/agents")], capture_output=True, text=True)
    assert bad.returncode == 1 and "orchestrator" in bad.stdout, bad.stdout
