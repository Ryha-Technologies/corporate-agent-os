# Platform compatibility matrix

Status values: **Supported** (verified against official docs and exercised by tests or validators) · **Limited** (works with documented constraints) · **Adapter** (needs the platform adapter; not usable by copying) · **Not supported** · **Not yet tested** (format verified from documentation, no live run in this build).

Verification date for all platform facts: 2026-11-18 (`research/source-register.md`). "Live run" means an agent session on that host loaded the files; none was performed in this build, so every row that depends on host behaviour is at best *Not yet tested*.

| Capability | Kiro IDE 1.x | Kiro CLI v3 | Claude Code | Codex CLI / IDE | Other Agent Skills clients |
|---|---|---|---|---|---|
| Skills discovered from project folder | Supported format (`.kiro/skills/`) — not yet tested live | Supported format — live install performed with CLI 3.3.0 (see platform guide) | Supported format (`.claude/skills/`) — not yet tested live | Supported format (`.agents/skills/`) — not yet tested live | Limited: copy `skills/<name>/`; frontmatter uses only spec fields |
| Skills at user scope | `~/.kiro/skills/` | `~/.kiro/skills/` | `~/.claude/skills/` | `~/.agents/skills/` | Varies |
| Skill frontmatter fields used | 6 spec fields | 6 spec fields | 6 spec fields (Claude extensions not used) | 2 required + 4 optional spec fields | 6 spec fields |
| Explicit skill invocation | `/skill-name` | `/skill-name` (CLI also `$ARGUMENTS`) | `/skill-name` | `$skill-name` | Varies |
| Custom agents / sub-agents | Adapter: `.kiro/agents/<id>.json` (generated) — JSON validated by `kiro-cli agent validate` | Adapter: same files — **live: listed by `kiro-cli agent list` 3.3.0** (Markdown agents were NOT discovered by CLI 3.3.0, so JSON is shipped) | Adapter: `.claude/agents/<id>.md` (generated) — not yet tested live | Not supported (roles in `AGENTS.md`) | Not supported |
| Parallel delegation | Supported by host (`subagent` tool, DAG, review loops) — not yet tested live | Supported by host — not yet tested live | Supported by host (Agent tool, worktree isolation) — not yet tested live | Not supported; sequential passes | Not supported |
| Restrict which agents an orchestrator may spawn | Supported: `subagent/<id>` tool entries + `subagent` permission rules | Supported | Not supported as a field; description-driven | n/a | n/a |
| Path-scoped write permission | Supported: `permissions.rules` `fs_write` matchers | Supported | Not supported; instruction + review | Not supported; sandbox modes only | Not supported |
| Shell command allow/ask/deny | Supported via `permissions.rules` | Supported | Limited: `allowed-tools` per skill turn; user `settings.json` deny rules (not shipped) | Codex approval modes (user-configured) | n/a |
| Always-on instructions | `.kiro/steering/*.md` (`inclusion: always`) and `AGENTS.md` | Same | `CLAUDE.md` | `AGENTS.md` | Varies |
| Hooks | Supported format `.kiro/hooks/*.json` v1 (two disabled validators, one Stop reminder) — not yet tested live | Supported format (global hooks also) | Not shipped (Claude Code hooks live in `settings.json`; documented in platform guide) | Not supported | n/a |
| Packaging | Supported: Kiro Power (Agent Plugins 1.0.0, skills only) — validated by schema, not yet imported live | Supported | Not shipped: Claude Code plugin | Not shipped: Codex plugin | Agent Plugins clients can load the Power folder |
| Browser / screenshot tooling for design QA | Adapter: user-configured MCP (example provided) | Same | User-configured MCP | Not addressed | n/a |
| MCP configuration | Supported: `.kiro/settings/mcp.json`; Power `mcp.json` optional (none shipped) | Supported | Supported by host; not shipped | Supported by host; not shipped | Varies |
| Memory ledger and task validators (project side) | Supported: installed to `.corporate-agent-os/validators/` (Python 3.10+, PyYAML) | Supported | Supported | Supported | Supported |
| Installer | Tested on Windows (pytest); Linux/macOS not yet tested | Same | Same | Same | Manual copy |
| Cost reporting | Host-dependent; NOT_MEASURED when not exposed | Same | Same | Same | Same |

## Notes per platform

- **Kiro.** Custom agents load skills only through `resources: skill://…`; the generated agents include their skills and the steering file. Workspace agents require a trusted workspace. Kiro Web and Mobile can use project agents as sub-agents but not as the primary agent. The Power is skills-only because Kiro documents only `plugin.json`, `skills/` and `mcp.json` as Power components; the brief's suggested `dev.kiro/steering/` directory is not documented by Kiro and is not shipped.
- **Claude Code.** Sub-agent `skills:` preloads full skill content; combined descriptions are kept short. `permissionMode`, `hooks` and `mcpServers` are intentionally absent so the same files work from a plugin. Portable frontmatter means the skills also upload to claude.ai without edits.
- **Codex.** Skill list budget is about 2% of context by default; install a subset with `--skills` or raise `skills.max_context_tokens`. No per-agent tool restrictions exist; the orchestrator discloses sequential execution.

## What "not yet tested live" would take

Open each host in a clean project after `install.py`, confirm the skills list shows the 39 skills with their descriptions, invoke `/corporate-orchestrator` (or `$corporate-orchestrator`), confirm the agents appear (Kiro agent picker; Claude Code `@` mention), run regression case E15 and E18, and record the results in `evaluations/benchmark-reports/`.
