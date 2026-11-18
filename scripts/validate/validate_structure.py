#!/usr/bin/env python3
"""Validate repository structure: required files, no empty directories, VERSION consistency, all JSON/YAML parse,
no secrets-looking strings, no placeholder markers in shipped Markdown."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, load_json, load_yaml, main_single, rel  # noqa: E402

REQUIRED_FILES = [
    "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md", "VERSION",
    "AGENTS.md", ".gitignore",
    "docs/platform-compatibility-matrix.md", "docs/installation/INSTALLATION.md", "docs/known-limitations.md",
    "research/source-register.md",
    "core/orchestrator/operating-procedure.md", "core/task-management/task-contract.schema.json",
    "core/workflow-engine/workflow.schema.json", "core/memory/memory-entry.schema.json",
    "core/permissions/policy.yaml", "core/model-routing/routing-policy.md",
    "core/budget-management/budget-policy.yaml", "core/quality-gates/gates.yaml",
    "powers/kiro/corporate-agent-os/plugin.json",
    "evaluations/datasets/regression-cases.json", "evaluations/originality/originality-scorecard.md",
    "scripts/install/install.py", "scripts/package/build_power.py", "scripts/package/build_release.py",
]
REQUIRED_DIRS = ["docs", "research", "core", "departments", "agents", "skills", "workflows", "powers", "adapters",
                 "standards", "templates", "evaluations", "tests", "examples", "scripts"]
IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", "dist", "node_modules", ".venv"}
SECRET_RE = re.compile(r"(?i)(aws_secret_access_key\s*[=:]\s*\S{16,}|-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----|sk-[A-Za-z0-9]{32,}|ghp_[A-Za-z0-9]{36,}|AKIA[0-9A-Z]{16})")
# Leftover placeholders: a marker used as a value (start of line, after a colon, alone in a table cell or in
# angle/square brackets) or the classic filler sentence. Prose that merely mentions the words is allowed.
PLACEHOLDER_RE = re.compile(r"(?m)(^\s*(?:[-*]\s*)?(?:TODO|TBD|FIXME)\b[:\s]|:\s*(?:TODO|TBD|FIXME)\s*$|\|\s*(?:TODO|TBD|FIXME)\s*\||[<\[](?:TODO|TBD|FIXME)[>\]]|lorem ipsum dolor)")


def run() -> Report:
    report = Report("structure")
    for f in REQUIRED_FILES:
        if not (ROOT / f).exists():
            report.error(f"missing required file {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT / d).is_dir():
            report.error(f"missing required directory {d}/")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else None
    if version and not re.match(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?$", version):
        report.error(f"VERSION '{version}' is not semantic")
    if version:
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""
        if f"## [{version}]" not in changelog:
            report.error(f"CHANGELOG.md has no section for version {version}")
        readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
        if version not in readme:
            report.warn(f"README.md does not mention version {version}")
    empty = 0
    for d in ROOT.rglob("*"):
        if d.is_dir() and not any(part in IGNORED_DIRS for part in d.relative_to(ROOT).parts):
            if not any(d.iterdir()):
                report.error(f"{rel(d)}: empty directory")
                empty += 1
    parsed = 0
    for f in ROOT.rglob("*"):
        if not f.is_file() or any(part in IGNORED_DIRS for part in f.relative_to(ROOT).parts):
            continue
        if f.suffix == ".json":
            load_json(f, report)
            parsed += 1
        elif f.suffix in (".yaml", ".yml"):
            load_yaml(f, report)
            parsed += 1
        elif f.suffix == ".jsonl":
            for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                if line.strip():
                    try:
                        import json
                        json.loads(line)
                    except ValueError as exc:
                        report.error(f"{rel(f)}:{n}: invalid JSON line: {exc}")
            parsed += 1
        if f.suffix in (".md", ".yaml", ".yml", ".json", ".py", ".jsonl", ".txt", ".toml"):
            text = f.read_text(encoding="utf-8", errors="ignore")
            if SECRET_RE.search(text):
                report.error(f"{rel(f)}: contains a secret-looking string")
            if f.suffix == ".md" and PLACEHOLDER_RE.search(text):
                report.error(f"{rel(f)}: leftover placeholder marker (TODO/TBD/FIXME/lorem ipsum dolor)")
    report.note(f"{parsed} JSON/YAML files parsed; version {version}")
    return report


if __name__ == "__main__":
    main_single(run)
