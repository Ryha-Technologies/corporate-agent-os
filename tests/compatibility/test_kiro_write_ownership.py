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


def test_orchestrator_cannot_write_specialist_folders():
    j = json.loads((ROOT / "adapters/kiro/agents/corporate-orchestrator.json").read_text(encoding="utf-8"))
    deny = [m for r in j["permissions"]["rules"] if r["capability"] == "fs_write" and r["effect"] == "deny" for m in r["match"]]
    for d in ("01-research", "02-product", "03-brand", "04-design", "05-architecture", "06-build", "08-legal-oss", "09-operations"):
        assert f"{d}/**" in deny, d
    assert "00-intake/**" not in deny and "10-decisions/**" not in deny


def test_every_writer_is_denied_foreign_stage_folders_and_never_its_own():
    for a in agents():
        if "write" not in a["tools"]:
            continue
        j = json.loads((ROOT / "adapters/kiro/agents" / f"{a['id']}.json").read_text(encoding="utf-8"))
        deny = {m for r in j["permissions"]["rules"] if r["capability"] == "fs_write" and r["effect"] == "deny" for m in r["match"]}
        own = {w.split("/")[0] for w in a.get("write_scope") or []}
        for d in STAGES:
            if d in own:
                assert f"{d}/**" not in deny, (a["id"], d)
            else:
                assert f"{d}/**" in deny, (a["id"], d)
