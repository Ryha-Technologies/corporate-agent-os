# Skill development guide

## Format

A skill is `skills/<name>/SKILL.md` plus optional `references/`, `scripts/`, `assets/`. Frontmatter uses only the six Agent Skills specification fields:

```yaml
---
name: <folder-name>              # 1-64 chars, a-z 0-9 and single hyphens
description: <what and when>     # <= 1024 chars; say when to use it; include trigger words
license: MIT
metadata:
  author: Corporate Agent OS contributors
  version: "0.2.0"
  department: <department id>
---
```

The body has exactly these H2 sections in this order: Purpose · When to use · Preconditions · Inputs · Procedure · Outputs · Quality criteria · Failure handling · Safety boundaries · References. Keep the body under 500 lines; put depth in `references/<topic>.md` and link it one level deep.

## Writing rules

- One skill owns one coherent workflow. If a procedure needs a different reviewer or different inputs, it is a different skill.
- Procedure steps are imperative and specific: what to read, what to produce, what to check. Name the template and the standard.
- Outputs are paths in the project workspace (`00-intake` … `10-decisions`).
- Quality criteria are checkable by a reviewer without talking to the author.
- Failure handling says what to do when inputs are missing, tools are unavailable, evidence conflicts or the user asks for a shortcut.
- Safety boundaries name the refusals and approvals that apply.
- No fabricated examples that look like research results. Illustrative content is labelled illustrative.

## Adding a skill

1. Create the folder and `SKILL.md`.
2. Add it to the agents that should load it (`agents/**/*.yaml → skills`).
3. Reference it from workflow stages where it applies.
4. Add at least one regression case to `evaluations/datasets/regression-cases.json` for the failure mode it prevents.
5. Run `python scripts/validate/run_all.py`, rebuild adapters and the Power, run `pytest`.
6. Add a changelog entry.

## Portability

Because only the six spec fields are used, the same folder works on Kiro, Claude Code, Codex and other Agent Skills clients, and uploads to claude.ai or packages with Anthropic's tooling without edits. Platform-specific behaviour belongs in adapters, not in skills.
