# Portable layer and adding a new platform adapter

The canonical layer is platform-independent:

| Canonical source | Format | Portable to |
|---|---|---|
| `skills/<name>/SKILL.md` (+ `references/`) | Agent Skills specification, six frontmatter fields only | Any Agent Skills client (Kiro, Claude Code, Codex, others) by copying the folder |
| `agents/**/*.yaml` | Repository schema (see `agents/README.md`) | Rendered per platform |
| `core/permissions/policy.yaml` | Repository schema | Mapped per platform |
| `workflows/*/workflow.yaml` | Repository schema | Executed by any orchestrator that can read YAML |
| `departments/`, `standards/`, `templates/`, `evaluations/` | Markdown / YAML / JSON | Platform-neutral documents |

## Adding an adapter in five steps

1. **Verify the platform's formats** from official documentation. Record every URL with an access date in `research/source-register.md`. Do not infer fields from examples or blog posts.
2. **Decide what maps.** Fill a row per concept in `docs/platform-compatibility-matrix.md`: skills location, agent/sub-agent config (if any), always-on instructions file, hooks, permissions, packaging, delegation. Mark each as supported, limited, adapter required, not supported or not yet tested.
3. **Add a renderer** in `scripts/package/build_adapters.py`: a `render_<platform>(agent, ...)` function that writes only verified fields, plus a `<platform>/model-map.yaml` if the platform selects models. Keep output deterministic so the drift check works.
4. **Add validation** in `scripts/validate/validate_adapters.py`: an allow-list of frontmatter fields and any structural rules the platform documents.
5. **Add install targets** in `scripts/install/install.py → TARGETS` and a `adapters/<platform>/README.md` with install steps, feature mapping and limits. Run `python scripts/validate/run_all.py` and `pytest`.

No skill text should change when adding a platform. If a platform needs different wording, add a `compatibility` field or a platform note in the adapter README rather than forking the skill.

## MCP-enabled applications

Applications that support Agent Plugins can load `powers/kiro/corporate-agent-os/` directly (it contains only spec-defined components). Applications that only support MCP can expose the skills as resources through a thin MCP server; that server is not part of this repository.
