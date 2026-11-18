# Permissions

**Component type:** specification (policy data) + adapter mapping.

`policy.yaml` is the single statement of what agents may do. It is deliberately platform-neutral: each adapter translates it into the host's native permission system, and the host remains the final authority.

## How the policy reaches each platform

| Policy element | Kiro | Claude Code | Codex |
|---|---|---|---|
| `tools` per agent | `tools` selectors in `.kiro/agents/<id>.json` (`read`, `write`, `shell`, `web`, `subagent/<name>`) | `tools:` list in `.claude/agents/<id>.md` (`Read, Grep, Glob, Write, Edit, Bash, WebFetch, WebSearch`) | No per-agent config; stated in `AGENTS.md` |
| `write_scope` | `permissions.rules: {capability: fs_write, match: [...], effect: allow}` plus a deny for everything else is not expressible, so the host prompts for writes outside the match | Not enforceable per path; the prompt instructs and the reviewer checks the diff | Instruction only |
| `shell.allow_without_prompt` | `permissions.rules: {capability: shell, match: [...], effect: allow}` | `allowed-tools` in skills for the invoking turn, or project `settings.json` permissions (not shipped) | Codex sandbox and approval modes (user-configured) |
| `shell.deny` | `effect: deny` rules | `disallowedTools` cannot match command text; rely on user settings `permissions.deny` | Instruction only |
| `human_approval_required` | Orchestrator prompt + `ask` effects; approvals recorded in `10-decisions/approvals.md` | Same | Same |
| Sub-agent allow-list | Orchestrator `tools: [subagent/<id>, ...]` and `permissions.rules capability: subagent` | Descriptions drive delegation; no allow-list field | n/a |

## Design decisions

- **Default deny for destructive shell patterns** in every generated Kiro agent, including the orchestrator.
- **Reviewers never get `write`.** They produce findings; remediation is a new task for the original owner.
- **Executives never get `write` or `shell`.** They decide and advise; artefacts are written by leads and specialists from their guidance.
- **Global installation is opt-in.** The installer writes to the project by default; `--scope user` is required for `~/.kiro`, `~/.claude`, `~/.agents`.

## Limits you should know

- Path-scoped write permission is enforceable only on Kiro (CLI v3 / IDE 1.x `fs_write` matchers). On Claude Code and Codex the write scope is an instruction verified by review, not a technical control.
- Hosts may prompt more often than this policy suggests; the policy never suppresses a host prompt.
- Secrets never belong in agent files. MCP configs use `${ENV_VAR}` expansion where the host supports it.
