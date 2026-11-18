# Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `run_all.py` reports `PyYAML is not installed` | Validators need PyYAML | `pip install pyyaml` |
| `validate_adapters` says a file "differs from a fresh render" | Generated adapter edited by hand or YAML changed without rebuild | `python scripts/package/build_adapters.py` |
| `validate_power` says skills differ from canonical | Power not rebuilt after skill edits | `python scripts/package/build_power.py` |
| `validate_structure` flags a placeholder marker | TODO/TBD/FIXME/lorem ipsum in shipped Markdown | Replace with real content; only `evaluations/originality/slop-patterns.md` may list them |
| Installer says "Refusing to install into the Corporate Agent OS repository itself" | `--destination` points at this repo | Point it at your project |
| Installer wrote `CORPORATE-AGENT-OS-AGENTS.md` instead of `AGENTS.md` | You already had an `AGENTS.md` | Merge the guidance manually; the installer never replaces it |
| Uninstall kept some files | You modified them after install (hash mismatch) | Remove manually if you want them gone |
| Kiro: agents not listed | Workspace not trusted, or files not in `.kiro/agents/` | Trust the workspace; check paths |
| Kiro: skills not loading in a custom agent | Custom agents load skills only via `resources: skill://` | Use the generated agents or add `skill://.kiro/skills/*/SKILL.md` |
| Kiro: every sub-agent tool call prompts | Parent session policy has no rule for the call | Add allow rules to the parent agent or user `permissions.yaml` |
| Kiro: hook command fails | Python or PyYAML not on the shell PATH Kiro uses | Fix PATH or keep the hook disabled |
| Claude Code: sub-agent missing | `.claude/agents/` created during the session | Restart the session |
| Claude Code: warning about agent descriptions over 15,000 tokens | Too many sub-agents from several sources | Remove unused agents; ours are ≤ 200 chars each |
| Codex: skill descriptions truncated or skills missing | Skill-list context budget | Install a subset with `--skills` or raise `skills.max_context_tokens` |
| An agent claims tests passed but no commands are shown | Report lacks CHECKS_ACTUALLY_RUN | Reject the report; the reviewer re-runs; file the transcript as a regression case |
| An agent calls something "production-ready" | Gate evidence missing | Check `07-quality/` verdicts; treat the claim as a defect |
| `build_release.py` fails on validation | Any validator failing | Fix the reported errors; the release is not built until all pass |
| Zip reopens with entry-count mismatch | Files changed during packaging | Re-run the build in a quiet tree |
