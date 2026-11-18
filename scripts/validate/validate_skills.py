#!/usr/bin/env python3
"""Validate every skill under skills/ against the Agent Skills specification and repository rules.

Checks (spec, agentskills.io/specification accessed 2026-11-18):
- frontmatter present on line 1, valid YAML mapping
- only the six spec fields; name/description required
- name: 1-64 chars, [a-z0-9-], no leading/trailing/double hyphen, equals folder name
- description: 1-1024 chars, non-empty
- compatibility <= 500 chars when present; metadata is a string->string map
Repository rules (R2, R3):
- body has the ten required H2 sections in order
- body <= 500 lines
- relative links in the body resolve inside the repository
- unique names
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ROOT, Report, SKILL_ALLOWED_FIELDS, SKILL_NAME_RE, SKILL_REQUIRED_SECTIONS,
    h2_sections, load_all_skills, main_single, markdown_links, parse_frontmatter, rel,
)


def validate_skill_dir(skill_dir: Path, report: Report, seen: set[str]) -> None:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text, skill_md, report)
    if fm is None:
        return
    extra = set(fm) - SKILL_ALLOWED_FIELDS
    if extra:
        report.error(f"{rel(skill_md)}: unsupported frontmatter fields {sorted(extra)}")
    name = fm.get("name")
    desc = fm.get("description")
    if not isinstance(name, str) or not name:
        report.error(f"{rel(skill_md)}: 'name' is required")
    else:
        if not (1 <= len(name) <= 64) or not SKILL_NAME_RE.match(name):
            report.error(f"{rel(skill_md)}: invalid name '{name}' (1-64 chars, lowercase a-z 0-9 and single hyphens)")
        if name != skill_dir.name:
            report.error(f"{rel(skill_md)}: name '{name}' does not match folder '{skill_dir.name}'")
        if name in seen:
            report.error(f"{rel(skill_md)}: duplicate skill name '{name}'")
        seen.add(name)
    if not isinstance(desc, str) or not desc.strip():
        report.error(f"{rel(skill_md)}: 'description' is required")
    else:
        if len(desc) > 1024:
            report.error(f"{rel(skill_md)}: description exceeds 1024 characters ({len(desc)})")
        if len(desc) < 60:
            report.warn(f"{rel(skill_md)}: description is short ({len(desc)} chars); include what and when")
        if "use " not in desc.lower() and "when " not in desc.lower():
            report.warn(f"{rel(skill_md)}: description should say when to use the skill")
    comp = fm.get("compatibility")
    if comp is not None and (not isinstance(comp, str) or not (1 <= len(comp) <= 500)):
        report.error(f"{rel(skill_md)}: compatibility must be a string of 1-500 chars")
    meta = fm.get("metadata")
    if meta is not None:
        if not isinstance(meta, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in meta.items()):
            report.error(f"{rel(skill_md)}: metadata must be a map of string keys to string values")
    lic = fm.get("license")
    if lic is not None and not isinstance(lic, str):
        report.error(f"{rel(skill_md)}: license must be a string")
    tools = fm.get("allowed-tools")
    if tools is not None and not isinstance(tools, str):
        report.error(f"{rel(skill_md)}: allowed-tools must be a space-separated string")

    # Body rules
    lines = body.count("\n") + 1
    if lines > 500:
        report.error(f"{rel(skill_md)}: body has {lines} lines; keep SKILL.md under 500 and move depth to references/")
    sections = h2_sections(body)
    missing = [s for s in SKILL_REQUIRED_SECTIONS if s not in sections]
    if missing:
        report.error(f"{rel(skill_md)}: missing required sections {missing}")
    else:
        order = [sections.index(s) for s in SKILL_REQUIRED_SECTIONS]
        if order != sorted(order):
            report.warn(f"{rel(skill_md)}: required sections are not in the standard order")
    import re as _re
    if _re.search(r"(?m)^\s*(?:[-*]\s*)?(?:TODO|TBD|FIXME)\b[:\s]|lorem ipsum dolor|\{placeholder\}", body):
        report.error(f"{rel(skill_md)}: contains a leftover placeholder marker")

    # Links and references
    for target in markdown_links(body):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        candidate = (skill_dir / target).resolve() if not target.startswith("/") else (ROOT / target.lstrip("/")).resolve()
        if not candidate.exists():
            candidate2 = (ROOT / target).resolve()
            if not candidate2.exists():
                report.error(f"{rel(skill_md)}: link target not found: {target}")
    # Backtick references to repo paths (templates/, standards/, core/, skills/, evaluations/, research/, workflows/)
    import re
    for m in re.finditer(r"`((?:templates|standards|core|skills|evaluations|research|workflows|docs|references)/[^`\s]+)`", body):
        target = m.group(1).split("#")[0]
        if target.endswith("/"):
            continue
        # allow glob-like or pattern references
        if any(ch in target for ch in "*<>|"):
            continue
        # strip trailing punctuation
        target = target.rstrip(".,;:)")
        # alternation like api-contract.(yaml|md)
        if "(" in target:
            continue
        paths = [ROOT / target, skill_dir / target]
        if not any(p.exists() for p in paths):
            report.error(f"{rel(skill_md)}: referenced path does not exist: {target}")

    # Supporting directories must not be empty
    for sub in ("references", "scripts", "assets"):
        d = skill_dir / sub
        if d.exists() and not any(d.iterdir()):
            report.error(f"{rel(d)}: empty directory")


def run() -> Report:
    report = Report("skills")
    skills = load_all_skills()
    if not skills:
        report.error("no skills found under skills/")
        return report
    seen: set[str] = set()
    for name, path in skills.items():
        validate_skill_dir(path.parent, report, seen)
    # Folders without SKILL.md
    for d in (ROOT / "skills").iterdir():
        if d.is_dir() and not (d / "SKILL.md").exists():
            report.error(f"{rel(d)}: skill folder without SKILL.md")
    report.note(f"{len(skills)} skills checked")
    return report


if __name__ == "__main__":
    main_single(run)
