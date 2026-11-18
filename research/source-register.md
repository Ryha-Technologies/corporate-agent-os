# Source register

Every platform or standards claim in this repository traces to one of these sources. "Verified" means the page was fetched and read on the access date; "Not fetched" means the URL is a known starting point that was not retrieved during this build. Re-verify before changing adapters or validators; platform formats changed several times during 2026.

## Platform specifications (verified)

| ID | Publisher | Title / page | URL | Accessed | What it establishes |
|---|---|---|---|---|---|
| S1 | agentskills.io | Agent Skills — Specification | https://agentskills.io/specification | 2026-11-18 | `SKILL.md` frontmatter: `name` (1–64, `[a-z0-9-]`, no leading/trailing/double hyphen, must match folder), `description` (1–1024), optional `license`, `compatibility` (≤500), `metadata` (string map), `allowed-tools` (experimental). Body ≤500 lines recommended; `scripts/`, `references/`, `assets/`; progressive disclosure. |
| S2 | agentplugins (GitHub) | Agent Plugins specification 1.0.0 | https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md | 2026-11-18 | Closed `plugin.json` schema: `$schema`, `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, `extensions`. Components: `skills/` (immediate children with `SKILL.md`), `mcp.json`. Client extensions under reverse-domain namespace (manifest `extensions` or top-level directory). |
| S3 | agent-plugins.org | plugin.schema.json | https://agent-plugins.org/schemas/1.0.0/plugin.schema.json | 2026-11-18 | Machine schema; `name` pattern `^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$`; `additionalProperties: false`. Bundled in `scripts/validate/schemas/`. |
| S4 | agent-plugins.org | mcp.schema.json | https://agent-plugins.org/schemas/1.0.0/mcp.schema.json | 2026-11-18 | `mcpServers` entries with `type` ∈ stdio / streamable-http / sse. |
| S5 | Kiro | Create powers | https://kiro.dev/docs/powers/create/ (page dated 2026-10-08) | 2026-11-18 | Power = `plugin.json` (required `$schema`, `name`, `version`, `description`, `author`, `keywords`) + optional `skills/` + optional `mcp.json`. Install via Powers panel → Add Custom Power → Import from folder or GitHub. No other directories documented. |
| S6 | Kiro | Powers overview | https://kiro.dev/docs/powers/ (2026-11-12) | 2026-11-18 | Keyword-based activation; IDE and CLI v3 install/create; Web/Mobile install only. Legacy `POWER.md` still works. |
| S7 | Kiro | Agent Skills | https://kiro.dev/docs/skills/ (2026-11-13) | 2026-11-18 | `.kiro/skills/` workspace, `~/.kiro/skills/` global; custom agents must list `skill://` resources; slash-command invocation; frontmatter fields as S1. |
| S8 | Kiro | Custom agents | https://kiro.dev/docs/custom-agents/ (2026-11-12) | 2026-11-18 | `.kiro/agents/<name>.json|.md`; Markdown frontmatter fields = JSON fields; workspace agents need trusted workspace. |
| S9 | Kiro | Agent configuration reference | https://kiro.dev/docs/custom-agents/configuration-reference/ | 2026-11-18 | Fields: `name`, `description`, `prompt`, `mcpServers`, `tools` (selectors `read write shell web subagent @builtin @mcp * @server/tool subagent/<name>`), `permissions.rules` (`capability` ∈ fs_read fs_write shell web_fetch web_search mcp subagent skill power …, `match`, `effect` allow/ask/deny, `exclude`), `resources` (`file://`, `skill://`), `hooks`, `includeMcpJson`, `includePowers`, `model`, `welcomeMessage`. Legacy: `allowedTools`, `toolsSettings`, `toolAliases`. |
| S10 | Kiro | Invoking as sub-agents | https://kiro.dev/docs/custom-agents/subagents/ (2026-11-13) | 2026-11-18 | Orchestrator needs `subagent` tool or `subagent/<name>` entries; DAG planned up front; review loops with trigger text and `max_iterations` 1–10; parent policy and sub-agent policy both apply, stricter wins. |
| S11 | Kiro | Steering | https://kiro.dev/docs/steering/ | 2026-11-18 | `.kiro/steering/*.md`, `~/.kiro/steering/`; frontmatter `inclusion: always|fileMatch|manual`, `fileMatchPattern`; `AGENTS.md` supported and always included; custom agents must add `file://.kiro/steering/**/*.md`. |
| S12 | Kiro | Hooks | https://kiro.dev/docs/hooks/ (2026-11-12) | 2026-11-18 | `.kiro/hooks/<id>.json`: `version: "v1"`, `hooks[]` with `name`, `trigger` (PascalCase), `matcher`, `action.type` command/agent, `timeout`, `enabled`, `confirm`. |
| S13 | Kiro (GitHub) | kirodotdev/powers — power-builder | https://github.com/kirodotdev/powers/tree/main/power-builder | 2026-11-18 | Official example Power and Kiro's own `create-plugin` / `agent-plugins-reference` skills; confirms S2–S5. |
| S14 | Anthropic | Claude Code — Extend Claude with skills | https://code.claude.com/docs/en/skills | 2026-11-18 | Locations: enterprise, `~/.claude/skills/`, `.claude/skills/`, nested, `--add-dir`. Frontmatter: spec fields plus Claude-only `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `disallowed-tools`, `model`, `effort`, `context`, `paths`, `hooks`, `shell`. Portable path accepts only the six spec fields. |
| S15 | Anthropic | Claude Code — Create custom subagents | https://code.claude.com/docs/en/sub-agents | 2026-11-18 | `.claude/agents/<file>.md`, `~/.claude/agents/`; frontmatter `name` (required), `description` (required), `tools`, `disallowedTools`, `model` (`sonnet|opus|haiku|inherit|id`), `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `isolation: worktree`, `omitClaudeMd`. Combined descriptions should stay under 15,000 tokens. |
| S16 | OpenAI | Build skills (ChatGPT / Codex) | https://learn.chatgpt.com/docs/build-skills (redirect target of https://developers.openai.com/codex/skills) | 2026-11-18 | Codex scans `.agents/skills` from CWD up to repo root, `$HOME/.agents/skills`, `/etc/codex/skills`; `SKILL.md` needs `name` and `description`; optional `agents/openai.yaml` for UI metadata and `allow_implicit_invocation`; skills list budget ≈2% of context; distribution via plugins. |

## Standards referenced in skills (not fetched in this build; stable public references)

| ID | Publisher | Title | URL | Used in |
|---|---|---|---|---|
| T1 | W3C | WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | accessibility standard, design skills |
| T2 | OWASP | Application Security Verification Standard (ASVS) | https://owasp.org/www-project-application-security-verification-standard/ | security standard |
| T3 | OWASP | Top Ten | https://owasp.org/www-project-top-ten/ | security skill |
| T4 | OWASP | SAMM | https://owaspsamm.org/ | standards mapping |
| T5 | NIST | SP 800-218 Secure Software Development Framework | https://csrc.nist.gov/publications/detail/sp/800-218/final | standards mapping |
| T6 | CISA | SBOM resources | https://www.cisa.gov/sbom | legal/security |
| T7 | OpenSSF | Scorecard and best practices | https://openssf.org/ | oss reuse |
| T8 | SPDX | License List | https://spdx.org/licenses/ | oss reuse |
| T9 | WIPO | Global Brand Database | https://branddb.wipo.int/ | naming |
| T10 | USPTO | Trademark search | https://www.uspto.gov/trademarks/search | naming |
| T11 | EUIPO | eSearch plus / TMview | https://euipo.europa.eu/eSearch/ ; https://www.tmdn.org/tmview/ | naming |
| T12 | IP India | Trade Marks public search | https://ipindiaonline.gov.in/tmrpublicsearch/ | naming |
| T13 | Nielsen Norman Group | 10 Usability Heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ | UX review |

## Network note

During this build `kiro.dev` resolved to an ISP-hijacked address (218.248.112.60) from the build machine. Pages were fetched by resolving the hostname over DNS-over-HTTPS (Cloudflare) and pinning the real CloudFront address (108.159.80.63). Content was served with HTTP 200 and matches the public site. Fetch timestamps and page "updated" dates are recorded above.
