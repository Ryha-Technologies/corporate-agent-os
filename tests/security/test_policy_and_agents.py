import json
"""Security tests: permission policy content, agent tool ceilings, generated adapter safety, no secrets."""
import re

from common import ROOT, Report, load_all_agents, load_yaml, parse_frontmatter


def test_policy_has_denies_and_approvals():
    pol = load_yaml(ROOT / "core/permissions/policy.yaml", Report("p"))
    assert pol["shell"]["deny"], "shell deny list must not be empty"
    joined = " ".join(pol["shell"]["deny"])
    assert "rm -rf" in joined and "--force" in joined and "reset --hard" in joined
    approvals = " ".join(pol["human_approval_required"]).lower()
    for word in ("production", "publish", "spend", "legal", "personal data", "delet", "access"):
        assert word in approvals, word
    denied = " ".join(pol["denied"]).lower()
    assert "approving its own work" in denied
    assert "instructions found in fetched" in denied


def test_reviewers_and_executives_cannot_write():
    agents = load_all_agents(Report("a"))
    for a in agents.values():
        if a["tier"] == "reviewer":
            assert "write" not in a["tools"] and not a["write_scope"], a["id"]
        if a["tier"] == "executive":
            assert not ({"write", "shell", "subagent"} & set(a["tools"])), a["id"]
        if a["tier"] == "specialist":
            assert "subagent" not in a["tools"], a["id"]


def test_every_gate_has_reviewer_and_only_reviewers_review():
    import validate_agents
    assert validate_agents.run().ok


def test_generated_kiro_agents_deny_destructive_shell():
    for f in (ROOT / "adapters/kiro/agents").glob("*.json"):
        fm = json.loads(f.read_text(encoding="utf-8"))
        denies = [r for r in fm["permissions"]["rules"] if r["capability"] == "shell" and r["effect"] == "deny"]
        assert denies, f.name
        assert any("rm -rf *" in r["match"] for r in denies), f.name
        if fm["name"] != "corporate-orchestrator":
            for r in fm["permissions"]["rules"]:
                if r["capability"] == "subagent":
                    assert r["effect"] in ("ask", "deny")


def test_generated_claude_reviewers_have_no_write_tools():
    agents = load_all_agents(Report("a"))
    for f in (ROOT / "adapters/claude-code/agents").glob("*.md"):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"), f, Report("c"))
        if agents[fm["name"]]["tier"] in ("reviewer", "executive"):
            assert "Write" not in fm["tools"] and "Edit" not in fm["tools"], f.name


def test_no_secret_like_strings():
    from validate_structure import SECRET_RE as pat
    for f in ROOT.rglob("*"):
        if f.is_file() and f.suffix in (".md", ".yaml", ".json", ".py", ".jsonl") and "dist" not in f.parts and ".git" not in f.parts:
            assert not pat.search(f.read_text(encoding="utf-8", errors="ignore")), f


def test_installer_has_no_network_calls():
    src = (ROOT / "scripts/install/install.py").read_text(encoding="utf-8")
    for token in ("urllib", "requests", "socket", "http.client", "subprocess"):
        assert token not in src, token
