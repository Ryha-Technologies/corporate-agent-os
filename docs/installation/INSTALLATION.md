# Installation

## Requirements

- Python 3.10 or newer on your PATH (`python --version`).
- PyYAML for the repository validators (`pip install pyyaml`). The installer itself uses only the standard library.
- One of: Kiro IDE 1.x / Kiro CLI v3, Claude Code, or Codex CLI / IDE extension.

## 1. Get the repository

Unzip `corporate-agent-os-final.zip` or clone the repository. Run the validators once to confirm the copy is intact:

```bash
cd corporate-agent-os
python scripts/validate/run_all.py
```

Expected: `10/10 validators passed`.

## 2. Preview what will be installed

The installer always shows its plan. Use `--dry-run` first.

```bash
python scripts/install/install.py --target kiro --destination /path/to/your/project --dry-run
```

The plan lists every file as `create`, `replace (backed up)`, `merge-note` or unchanged, with the destination path. Nothing is written in a dry run.

## 3. Install

```bash
# Kiro IDE / CLI
python scripts/install/install.py --target kiro --destination /path/to/your/project

# Claude Code
python scripts/install/install.py --target claude --destination /path/to/your/project

# Codex
python scripts/install/install.py --target codex --destination /path/to/your/project

# All three (only if you actually use all three)
python scripts/install/install.py --target all --destination /path/to/your/project
```

The installer asks for confirmation unless you pass `--yes`.

What gets written per target is listed in the adapter READMEs: [`adapters/kiro/README.md`](../../adapters/kiro/README.md), [`adapters/claude-code/README.md`](../../adapters/claude-code/README.md), [`adapters/codex/README.md`](../../adapters/codex/README.md).

### Safety behaviour

- Existing `AGENTS.md` or `CLAUDE.md` files are never replaced. Guidance is written to `CORPORATE-AGENT-OS-AGENTS.md` / `CORPORATE-AGENT-OS-CLAUDE.md` for you to merge.
- A file that already exists at a target path and differs is backed up to `<project>/.corporate-agent-os/backup/<timestamp>/` before replacement. Files that are identical are left alone.
- A manifest of installed files and hashes is written to `<project>/.corporate-agent-os/manifest.json`.
- The installer refuses to install into the Corporate Agent OS repository itself.
- Your home directory is never touched unless you pass `--scope user`.

### Options

| Option | Effect |
|---|---|
| `--skills a,b,c` | Install only the named skills (useful for Codex's skill-list budget) |
| `--scope user` | Install to `~/.kiro`, `~/.claude` or `~/.agents` instead of a project |
| `--yes` | Skip the confirmation prompt |
| `--uninstall` | Remove files recorded in the manifest that you have not modified, and restore backups |

## 4. Verify in your host

- **Kiro IDE:** open the project, trust the workspace, open the agent picker and select `corporate-orchestrator`; type `/` to see the skills. Alternatively import the Power: Powers → Add Custom Power → Import power from a folder → `powers/kiro/corporate-agent-os`.
- **Kiro CLI:** `kiro-cli agent list` should show the agents; `/skills` lists skills.
- **Claude Code:** type `/` and look for `corporate-orchestrator`; `@` should list the sub-agents.
- **Codex:** `/skills` or `$` lists skills; `AGENTS.md` is read automatically.

These checks were not performed live in this build; see `docs/platform-compatibility-matrix.md`.

## 5. Upgrade

Run the same install command with the new repository version. Unchanged files are skipped, changed files are backed up and replaced, and the manifest records the new version. Review `CHANGELOG.md` first.

## 6. Uninstall

```bash
python scripts/install/install.py --target kiro --destination /path/to/your/project --uninstall --dry-run
python scripts/install/install.py --target kiro --destination /path/to/your/project --uninstall
```

Files you modified after installation are kept (the hash no longer matches the manifest) and reported.

## Troubleshooting

See [`docs/troubleshooting/README.md`](../troubleshooting/README.md).
