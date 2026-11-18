#!/usr/bin/env python3
"""Validate platform adapters: generated agents match a fresh render, frontmatter uses only verified fields,
Kiro hooks and steering files are well-formed, Codex AGENTS.md present."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "package"))
from common import ROOT, Report, load_json, main_single, parse_frontmatter, rel  # noqa: E402
from build_adapters import build  # noqa: E402

# Kiro agent config fields (configuration reference, accessed 2026-11-18), current + accepted legacy.
KIRO_AGENT_FIELDS = {"name", "description", "prompt", "mcpServers", "tools", "permissions", "resources", "hooks",
                     "includeMcpJson", "includePowers", "model", "welcomeMessage", "excludedTools"}
KIRO_LEGACY_FIELDS = {"toolAliases", "allowedTools", "toolsSettings", "keyboardShortcut"}
KIRO_CAPABILITIES = {"fs_read", "fs_write", "shell", "web_fetch", "web_search", "mcp", "subagent", "skill", "power",
                     "context", "diagnostics", "sandbox_network", "all", "builtin", "filesystem"}
# Claude Code sub-agent frontmatter (accessed 2026-11-18).
CLAUDE_AGENT_FIELDS = {"name", "description", "tools", "disallowedTools", "model", "permissionMode", "maxTurns",
                       "autoCompactWindow", "skills", "mcpServers", "hooks", "memory", "background", "omitClaudeMd",
                       "isolation", "effort", "initialPrompt", "color"}
CLAUDE_MODELS = {"sonnet", "opus", "haiku", "fable", "inherit"}
HOOK_TRIGGERS = {"PreToolUse", "PostToolUse", "PostFileSave", "Stop", "UserPromptSubmit", "SessionStart", "AgentSpawn",
                 "PreFileEdit", "PostFileEdit", "FileCreated", "FileDeleted", "SubagentStop", "Notification"}


def run() -> Report:
    report = Report("adapters")
    rendered = build(write=False)
    for path, content in rendered.items():
        p = Path(path)
        if not p.exists():
            report.error(f"{rel(p)}: missing; run scripts/package/build_adapters.py")
        elif p.read_text(encoding="utf-8").replace("\r\n", "\n") != content:
            report.error(f"{rel(p)}: differs from a fresh render; run scripts/package/build_adapters.py")
    # Stale generated files
    for d in (ROOT / "adapters/kiro/agents", ROOT / "adapters/claude-code/agents"):
        for f in d.glob("*.md"):
            if str(f) not in rendered:
                report.error(f"{rel(f)}: not produced by the generator (stale agent)")

    # Kiro agent frontmatter
    for f in sorted((ROOT / "adapters/kiro/agents").glob("*.md")):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"), f, report)
        if not fm:
            continue
        unknown = set(fm) - KIRO_AGENT_FIELDS
        legacy = set(fm) & KIRO_LEGACY_FIELDS
        if unknown - KIRO_LEGACY_FIELDS:
            report.error(f"{rel(f)}: unknown Kiro agent fields {sorted(unknown - KIRO_LEGACY_FIELDS)}")
        if legacy:
            report.error(f"{rel(f)}: legacy CLI 2.x fields {sorted(legacy)} are ignored by CLI v3")
        for rule in fm.get("permissions", {}).get("rules", []):
            if rule.get("capability") not in KIRO_CAPABILITIES:
                report.error(f"{rel(f)}: unknown permission capability '{rule.get('capability')}'")
            if rule.get("effect") not in ("allow", "ask", "deny"):
                report.error(f"{rel(f)}: invalid effect '{rule.get('effect')}'")
        for r in fm.get("resources", []):
            if not (r.startswith("skill://") or r.startswith("file://")):
                report.error(f"{rel(f)}: resource '{r}' must use skill:// or file://")
        if any(t.startswith("subagent") for t in fm.get("tools", [])) and not any(
                r.get("capability") == "subagent" for r in fm.get("permissions", {}).get("rules", [])):
            report.error(f"{rel(f)}: subagent tool without a subagent permission rule")
    # Claude agent frontmatter
    for f in sorted((ROOT / "adapters/claude-code/agents").glob("*.md")):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"), f, report)
        if not fm:
            continue
        unknown = set(fm) - CLAUDE_AGENT_FIELDS
        if unknown:
            report.error(f"{rel(f)}: unknown Claude Code sub-agent fields {sorted(unknown)}")
        if "name" not in fm or "description" not in fm:
            report.error(f"{rel(f)}: name and description are required")
        if ":" in str(fm.get("name", "")):
            report.error(f"{rel(f)}: name must not contain ':'")
        model = fm.get("model")
        if model and model not in CLAUDE_MODELS and not str(model).startswith("claude-"):
            report.error(f"{rel(f)}: unexpected model '{model}'")
    # Kiro hooks
    for f in sorted((ROOT / "adapters/kiro/hooks").glob("*.json")):
        data = load_json(f, report)
        if not isinstance(data, dict):
            continue
        if data.get("version") != "v1":
            report.error(f"{rel(f)}: hook version must be 'v1'")
        for h in data.get("hooks", []):
            for k in ("name", "trigger", "action"):
                if k not in h:
                    report.error(f"{rel(f)}: hook missing '{k}'")
            if h.get("trigger") not in HOOK_TRIGGERS:
                report.warn(f"{rel(f)}: trigger '{h.get('trigger')}' not in the known trigger list; verify against kiro.dev/docs/hooks")
            act = h.get("action", {})
            if act.get("type") not in ("command", "agent"):
                report.error(f"{rel(f)}: action.type must be command or agent")
            if act.get("type") == "command" and not act.get("command"):
                report.error(f"{rel(f)}: command action without command")
            if act.get("type") == "agent" and not act.get("prompt"):
                report.error(f"{rel(f)}: agent action without prompt")
    # Kiro steering
    for f in sorted((ROOT / "adapters/kiro/steering").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text, f, report)
        if fm and fm.get("inclusion") not in (None, "always", "fileMatch", "manual"):
            report.error(f"{rel(f)}: inclusion must be always, fileMatch or manual")
        if fm and fm.get("inclusion") == "fileMatch" and not fm.get("fileMatchPattern"):
            report.error(f"{rel(f)}: fileMatch requires fileMatchPattern")
    # Presence of hand-written files
    for required in ("adapters/kiro/README.md", "adapters/kiro/steering/corporate-agent-os.md",
                     "adapters/claude-code/README.md", "adapters/claude-code/CLAUDE.md",
                     "adapters/codex/README.md", "adapters/codex/AGENTS.md", "adapters/portable/README.md"):
        if not (ROOT / required).exists():
            report.error(f"missing {required}")
    report.note(f"{len(rendered)} generated adapter files checked")
    return report


if __name__ == "__main__":
    main_single(run)
