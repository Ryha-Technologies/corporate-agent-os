"""Compatibility tests: generated files use only verified platform fields and skills use only spec fields."""
from common import ROOT, Report, parse_frontmatter
import validate_adapters
import validate_skills
import validate_power
from build_adapters import build


def test_adapters_match_fresh_render():
    rendered = build(write=False)
    for path, content in rendered.items():
        from pathlib import Path
        assert Path(path).read_text(encoding="utf-8").replace("\r\n", "\n") == content, path


def test_adapter_validator_passes():
    assert validate_adapters.run().ok


def test_skill_frontmatter_only_spec_fields():
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    for f in (ROOT / "skills").glob("*/SKILL.md"):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"), f, Report("s"))
        assert set(fm) <= allowed, f
        assert fm["name"] == f.parent.name
        assert len(fm["description"]) <= 1024
        assert all(isinstance(v, str) for v in fm.get("metadata", {}).values()), f


def test_skills_validator_passes():
    assert validate_skills.run().ok


def test_power_validator_passes():
    assert validate_power.run().ok


def test_kiro_agent_resources_point_to_installed_paths():
    for f in (ROOT / "adapters/kiro/agents").glob("*.md"):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"), f, Report("k"))
        for r in fm["resources"]:
            if r.startswith("skill://"):
                skill = r.split("/")[-2]
                assert (ROOT / "skills" / skill / "SKILL.md").exists(), r
            else:
                assert r == "file://.kiro/steering/corporate-agent-os.md"


def test_claude_agent_descriptions_are_short():
    total = 0
    for f in (ROOT / "adapters/claude-code/agents").glob("*.md"):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"), f, Report("c"))
        assert len(fm["description"]) <= 200
        total += len(fm["description"])
    # 15,000 tokens is the Claude Code warning threshold; ~4 chars per token keeps us far below.
    assert total < 15000 * 4 * 0.25


def test_codex_agents_md_lists_all_agents():
    from common import load_all_agents
    text = (ROOT / "adapters/codex/AGENTS.md").read_text(encoding="utf-8")
    for aid in load_all_agents(Report("a")):
        assert f"`{aid}`" in text
