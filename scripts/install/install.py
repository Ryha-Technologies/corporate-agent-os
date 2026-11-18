#!/usr/bin/env python3
"""Install Corporate Agent OS into a project (default) or user scope for Kiro, Claude Code or Codex.

Safety model
- Shows the plan (destination, every file to be created or replaced) before touching anything.
- --dry-run prints the plan and exits.
- Never overwrites a file it did not install: an existing file at a target path is backed up to
  <destination>/.corporate-agent-os/backup/<timestamp>/ before being replaced, and only files that belong to this
  product (same relative path in the source tree) are ever replaced. Unrelated files in the same folders are untouched.
- Writes a manifest (<destination>/.corporate-agent-os/manifest.json) listing installed files and their hashes.
- --uninstall removes only files listed in the manifest whose hash still matches (unchanged by the user), and
  restores backups taken at install time.
- Existing AGENTS.md / CLAUDE.md are never replaced; guidance is written next to them for manual merge.
- User scope (~/.kiro, ~/.claude, ~/.agents) requires --scope user explicitly.
- Standard library only.

Usage
  python scripts/install/install.py --target kiro|claude|codex|all [--destination DIR] [--scope project|user]
                                    [--dry-run] [--yes] [--skills a,b,c] [--uninstall] [--rollback TIMESTAMP]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCT = "corporate-agent-os"
STATE_DIR = f".{PRODUCT}"

TARGETS = {
    # target: list of (source relative to ROOT, destination relative to scope root, kind)
    "kiro": [
        ("skills", ".kiro/skills", "skills"),
        ("adapters/kiro/agents", ".kiro/agents", "tree"),
        ("adapters/kiro/steering", ".kiro/steering", "tree"),
        ("adapters/kiro/hooks", ".kiro/hooks", "tree"),
        ("scripts/validate", f"{STATE_DIR}/validators", "validators"),
    ],
    "claude": [
        ("skills", ".claude/skills", "skills"),
        ("adapters/claude-code/agents", ".claude/agents", "tree"),
        ("adapters/claude-code/CLAUDE.md", "CLAUDE.md", "merge-file"),
        ("scripts/validate", f"{STATE_DIR}/validators", "validators"),
    ],
    "codex": [
        ("skills", ".agents/skills", "skills"),
        ("adapters/codex/AGENTS.md", "AGENTS.md", "merge-file"),
        ("scripts/validate", f"{STATE_DIR}/validators", "validators"),
    ],
}
# Project-side validators: the two that operate on a project's own artefacts, plus their schemas.
VALIDATOR_FILES = [
    ("scripts/validate/common.py", "common.py"),
    ("scripts/validate/validate_tasks.py", "validate_tasks.py"),
    ("scripts/validate/validate_memory.py", "validate_memory.py"),
    ("core/task-management/task-contract.schema.json", "schemas/task-contract.schema.json"),
    ("core/memory/memory-entry.schema.json", "schemas/memory-entry.schema.json"),
]
USER_SCOPE_ROOTS = {"kiro": "~", "claude": "~", "codex": "~"}
# In user scope, Codex and Kiro expect skills directly under ~/.agents/skills and ~/.kiro/skills; AGENTS.md/CLAUDE.md
# merge files are skipped in user scope except Kiro steering which Kiro reads from ~/.kiro/steering.
USER_SCOPE_SKIP_KINDS = {"merge-file"}


@dataclass
class Action:
    src: Path | None
    dst: Path
    kind: str          # create | replace | merge-note | skip-same
    note: str = ""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def plan(target: str, dest_root: Path, scope: str, only_skills: set[str] | None) -> list[Action]:
    actions: list[Action] = []
    for src_rel, dst_rel, kind in TARGETS[target]:
        src = ROOT / src_rel
        dst = dest_root / dst_rel
        if kind == "merge-file":
            if scope == "user":
                continue
            if dst.exists():
                side = dst.with_name(f"CORPORATE-AGENT-OS-{dst.name}")
                actions.append(Action(src, side, "merge-note", f"existing {dst.name} kept; merge guidance from {side.name}"))
            else:
                actions.append(Action(src, dst, "create"))
            continue
        if kind == "validators":
            for src_file, dst_name in VALIDATOR_FILES:
                f, target_file = ROOT / src_file, dst / dst_name
                if not f.exists():
                    continue
                if target_file.exists():
                    actions.append(Action(f, target_file, "skip-same" if sha256(target_file) == sha256(f) else "replace",
                                          "" if sha256(target_file) == sha256(f) else "existing file will be backed up"))
                else:
                    actions.append(Action(f, target_file, "create"))
            continue
        if not src.exists():
            continue
        for f in sorted(src.rglob("*")):
            if not f.is_file() or "__pycache__" in f.parts:
                continue
            rel = f.relative_to(src)
            if kind == "skills" and only_skills is not None and rel.parts[0] not in only_skills:
                continue
            target_file = dst / rel
            if target_file.exists():
                if sha256(target_file) == sha256(f):
                    actions.append(Action(f, target_file, "skip-same"))
                else:
                    actions.append(Action(f, target_file, "replace", "existing file will be backed up"))
            else:
                actions.append(Action(f, target_file, "create"))
    return actions


def print_plan(actions: list[Action], dest_root: Path, target: str) -> None:
    counts = {k: sum(1 for a in actions if a.kind == k) for k in ("create", "replace", "merge-note", "skip-same")}
    print(f"\nTarget: {target}    Destination: {dest_root}")
    print(f"  create: {counts['create']}   replace (backed up): {counts['replace']}   merge notes: {counts['merge-note']}   unchanged: {counts['skip-same']}")
    for a in actions:
        if a.kind == "skip-same":
            continue
        try:
            shown = a.dst.relative_to(dest_root)
        except ValueError:
            shown = a.dst
        print(f"  {a.kind:10} {shown}" + (f"   ({a.note})" if a.note else ""))


def load_manifest(dest_root: Path) -> dict:
    mf = dest_root / STATE_DIR / "manifest.json"
    if mf.exists():
        return json.loads(mf.read_text(encoding="utf-8"))
    return {"product": PRODUCT, "installs": []}


def save_manifest(dest_root: Path, manifest: dict) -> None:
    (dest_root / STATE_DIR).mkdir(parents=True, exist_ok=True)
    (dest_root / STATE_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def apply(actions: list[Action], dest_root: Path, target: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_dir = dest_root / STATE_DIR / "backup" / stamp
    installed: list[dict] = []
    backups: list[dict] = []
    for a in actions:
        if a.kind == "skip-same":
            installed.append({"path": a.dst.relative_to(dest_root).as_posix(), "sha256": sha256(a.dst)})
            continue
        a.dst.parent.mkdir(parents=True, exist_ok=True)
        if a.kind == "replace":
            b = backup_dir / a.dst.relative_to(dest_root)
            b.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(a.dst, b)
            backups.append({"path": a.dst.relative_to(dest_root).as_posix(), "backup": b.relative_to(dest_root).as_posix()})
        shutil.copy2(a.src, a.dst)  # type: ignore[arg-type]
        installed.append({"path": a.dst.relative_to(dest_root).as_posix(), "sha256": sha256(a.dst)})
    manifest = load_manifest(dest_root)
    manifest["installs"].append({
        "target": target, "installed_at": stamp, "source": str(ROOT),
        "version": (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else "unknown",
        "files": installed, "backups": backups,
    })
    save_manifest(dest_root, manifest)
    print(f"\nInstalled {len([a for a in actions if a.kind != 'skip-same'])} files for {target}. Manifest: {dest_root / STATE_DIR / 'manifest.json'}")
    if backups:
        print(f"Backups of replaced files: {backup_dir}")


def uninstall(dest_root: Path, target: str | None, dry_run: bool) -> int:
    manifest = load_manifest(dest_root)
    installs = [i for i in manifest.get("installs", []) if target in (None, "all") or i["target"] == target]
    if not installs:
        print("Nothing recorded in the manifest for this destination/target.")
        return 0
    removed = kept = restored = 0
    for inst in installs:
        for f in inst["files"]:
            p = dest_root / f["path"]
            if not p.exists():
                continue
            if sha256(p) != f["sha256"]:
                print(f"  keep (modified by user): {f['path']}")
                kept += 1
                continue
            print(f"  remove: {f['path']}")
            if not dry_run:
                p.unlink()
            removed += 1
        for b in inst.get("backups", []):
            src = dest_root / b["backup"]
            if src.exists():
                print(f"  restore: {b['path']} <- {b['backup']}")
                if not dry_run:
                    (dest_root / b["path"]).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest_root / b["path"])
                restored += 1
    if not dry_run:
        manifest["installs"] = [i for i in manifest.get("installs", []) if i not in installs]
        save_manifest(dest_root, manifest)
        # remove empty directories we may have created, bottom-up, only under known product folders
        for sub in (".kiro/skills", ".kiro/agents", ".kiro/hooks", ".claude/skills", ".claude/agents", ".agents/skills"):
            d = dest_root / sub
            if d.exists():
                for sd in sorted(d.rglob("*"), key=lambda x: -len(x.parts)):
                    if sd.is_dir() and not any(sd.iterdir()):
                        sd.rmdir()
    print(f"\n{'Would remove' if dry_run else 'Removed'} {removed} files, kept {kept} user-modified files, restored {restored} backups.")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Install Corporate Agent OS into a project or user scope.")
    ap.add_argument("--target", choices=["kiro", "claude", "codex", "all"], required=True)
    ap.add_argument("--destination", default=".", help="Project directory (project scope). Ignored for --scope user.")
    ap.add_argument("--scope", choices=["project", "user"], default="project")
    ap.add_argument("--dry-run", action="store_true", help="Show the plan and exit without changing anything")
    ap.add_argument("--yes", action="store_true", help="Apply without interactive confirmation")
    ap.add_argument("--skills", default=None, help="Comma-separated subset of skills to install (default: all)")
    ap.add_argument("--uninstall", action="store_true", help="Remove files recorded in the manifest and restore backups")
    args = ap.parse_args(argv)

    targets = ["kiro", "claude", "codex"] if args.target == "all" else [args.target]
    only_skills = set(s.strip() for s in args.skills.split(",")) if args.skills else None
    if only_skills:
        missing = [s for s in only_skills if not (ROOT / "skills" / s / "SKILL.md").exists()]
        if missing:
            print(f"Unknown skills: {missing}", file=sys.stderr)
            return 2

    if args.scope == "user":
        dest_root = Path(os.path.expanduser("~")).resolve()
        print("USER SCOPE: files will be written under your home directory. Use --dry-run first.")
    else:
        dest_root = Path(args.destination).resolve()
        if not dest_root.is_dir():
            print(f"Destination is not a directory: {dest_root}", file=sys.stderr)
            return 2
        if dest_root == ROOT:
            print("Refusing to install into the Corporate Agent OS repository itself. Use --destination <your project>.", file=sys.stderr)
            return 2

    if args.uninstall:
        return uninstall(dest_root, None if args.target == "all" else args.target, args.dry_run)

    all_actions: dict[str, list[Action]] = {}
    for t in targets:
        acts = plan(t, dest_root, args.scope, only_skills)
        all_actions[t] = acts
        print_plan(acts, dest_root, t)
    if args.dry_run:
        print("\nDry run: no files were changed.")
        return 0
    if not args.yes:
        answer = input("\nProceed with installation? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted. No files were changed.")
            return 1
    for t, acts in all_actions.items():
        apply(acts, dest_root, t)
    if args.target == "all":
        print("Note: skills now exist in three locations; keep only the runtime you use to avoid duplicate context.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
