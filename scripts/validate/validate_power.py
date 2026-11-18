#!/usr/bin/env python3
"""Validate the Kiro Power at powers/kiro/corporate-agent-os against Agent Plugins 1.0.0 and Kiro's documented
requirements (kiro.dev/docs/powers/create, accessed 2026-11-18), and check it is an exact build of canonical skills.

Usage: python scripts/validate/validate_power.py [power_dir]
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PLUGIN_NAME_RE, ROOT, Report, finish, load_json, rel, validate_schema  # noqa: E402

PLUGIN_SCHEMA = ROOT / "scripts/validate/schemas/plugin.schema.json"
MCP_SCHEMA = ROOT / "scripts/validate/schemas/mcp.schema.json"
# Kiro documents these as required for a power even though the spec requires only $schema and name.
KIRO_REQUIRED = ["$schema", "name", "version", "description", "author", "keywords"]
ALLOWED_TOP_LEVEL = {"plugin.json", "mcp.json", "skills", "README.md", "LICENSE", "CHANGELOG.md"}
BROAD_KEYWORDS = {"company", "ui", "qa", "security", "engineering", "test", "api", "data", "code", "app", "design"}


def _hash(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def validate_power(power_dir: Path, report: Report, canonical_skills: Path | None = ROOT / "skills") -> None:
    manifest = power_dir / "plugin.json"
    if not manifest.exists():
        report.error(f"{rel(power_dir)}: plugin.json missing")
        return
    data = load_json(manifest, report)
    schema = load_json(PLUGIN_SCHEMA, report)
    if data is None or schema is None:
        return
    for err in validate_schema(data, schema):
        report.error(f"{rel(manifest)}: {err}")
    for k in KIRO_REQUIRED:
        if k not in data:
            report.error(f"{rel(manifest)}: Kiro requires '{k}'")
    name = data.get("name", "")
    if not PLUGIN_NAME_RE.match(name or ""):
        report.error(f"{rel(manifest)}: invalid plugin name '{name}'")
    if name != power_dir.name:
        report.error(f"{rel(manifest)}: name '{name}' should match the power directory '{power_dir.name}'")
    if isinstance(data.get("author"), dict) and not data["author"].get("name"):
        report.error(f"{rel(manifest)}: author.name is required by Kiro")
    kws = data.get("keywords", [])
    if isinstance(kws, list):
        broad = [k for k in kws if k.lower() in BROAD_KEYWORDS]
        if broad:
            report.warn(f"{rel(manifest)}: broad keywords may cause false activation: {broad}")
        if len(kws) > 12:
            report.warn(f"{rel(manifest)}: {len(kws)} keywords; Kiro's power-builder recommends 5-7 specific ones")
    version_file = ROOT / "VERSION"
    if version_file.exists() and data.get("version") != version_file.read_text(encoding="utf-8").strip():
        report.error(f"{rel(manifest)}: version '{data.get('version')}' differs from VERSION file")

    # Top-level layout: only documented components
    for child in power_dir.iterdir():
        if child.name not in ALLOWED_TOP_LEVEL:
            report.error(f"{rel(child)}: undocumented top-level entry in a power (spec allows plugin.json, skills/, mcp.json; client extension dirs must be reverse-domain names)")
    mcp = power_dir / "mcp.json"
    if mcp.exists():
        mdata = load_json(mcp, report)
        mschema = load_json(MCP_SCHEMA, report)
        if mdata is not None and mschema is not None:
            for err in validate_schema(mdata, mschema):
                report.error(f"{rel(mcp)}: {err}")
            for sname, server in (mdata.get("mcpServers") or {}).items():
                env = server.get("env", {}) if isinstance(server, dict) else {}
                for k, v in env.items():
                    if k in ("PLUGIN_ROOT", "PLUGIN_DATA"):
                        report.error(f"{rel(mcp)}: env key '{k}' is reserved")
                    if isinstance(v, str) and any(tok in v.lower() for tok in ("sk-", "secret", "password", "token")) and "${" not in v:
                        report.error(f"{rel(mcp)}: server '{sname}' env '{k}' looks like an embedded secret")

    # Skills: immediate children with SKILL.md, matching canonical bytes
    skills_dir = power_dir / "skills"
    if not skills_dir.exists():
        report.warn(f"{rel(power_dir)}: no skills/ directory")
        return
    packaged = {d.name: d for d in skills_dir.iterdir() if d.is_dir()}
    for sname, sdir in packaged.items():
        if not (sdir / "SKILL.md").exists():
            report.error(f"{rel(sdir)}: skill folder without SKILL.md")
    if canonical_skills and canonical_skills.exists():
        canonical = {d.name: d for d in canonical_skills.iterdir() if d.is_dir()}
        missing = sorted(set(canonical) - set(packaged))
        extra = sorted(set(packaged) - set(canonical))
        if missing:
            report.error(f"power is missing canonical skills: {missing} (run scripts/package/build_power.py)")
        if extra:
            report.error(f"power contains non-canonical skills: {extra}")
        for sname in set(canonical) & set(packaged):
            for cfile in canonical[sname].rglob("*"):
                if cfile.is_file():
                    pfile = packaged[sname] / cfile.relative_to(canonical[sname])
                    if not pfile.exists():
                        report.error(f"power skill '{sname}' is missing {cfile.relative_to(canonical[sname]).as_posix()}")
                    elif _hash(pfile) != _hash(cfile):
                        report.error(f"power skill '{sname}' file {pfile.name} differs from canonical (rebuild the power)")
    report.note(f"{rel(power_dir)}: {len(packaged)} skills packaged")


def run(power_dir: Path | None = None) -> Report:
    report = Report("power")
    validate_power(power_dir or ROOT / "powers/kiro/corporate-agent-os", report)
    return report


if __name__ == "__main__":
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
    sys.exit(finish([run(target)]))
