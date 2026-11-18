"""Shared helpers for Corporate Agent OS validators.

Dependencies: Python 3.10+, PyYAML. No other third-party packages.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - reported at runtime
    yaml = None

ROOT = Path(__file__).resolve().parents[2]

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PLUGIN_NAME_RE = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
AGENT_ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Agent Skills specification frontmatter fields (agentskills.io/specification, accessed 2026-11-18).
SKILL_ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

# Required H2 sections for every SKILL.md body in this repository (R3).
SKILL_REQUIRED_SECTIONS = [
    "Purpose", "When to use", "Preconditions", "Inputs", "Procedure",
    "Outputs", "Quality criteria", "Failure handling", "Safety boundaries", "References",
]

TIERS = {"orchestrator", "executive", "department-lead", "specialist", "reviewer"}
ABSTRACT_TOOLS = {"read", "write", "shell", "web", "subagent", "browser", "mcp"}
TIER_TOOL_CEILING = {
    "orchestrator": {"read", "write", "shell", "web", "subagent", "browser", "mcp"},
    "executive": {"read", "web"},
    "department-lead": {"read", "write", "shell", "web", "subagent", "browser"},
    "specialist": {"read", "write", "shell", "web", "browser", "mcp"},
    "reviewer": {"read", "shell", "web", "browser"},
}


@dataclass
class Report:
    name: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def note(self, msg: str) -> None:
        self.info.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors

    def print(self) -> None:
        status = "PASS" if self.ok else "FAIL"
        print(f"[{status}] {self.name}")
        for line in self.info:
            print(f"    {line}")
        for w in self.warnings:
            print(f"    WARN  {w}")
        for e in self.errors:
            print(f"    ERROR {e}")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def require_yaml(report: Report) -> bool:
    if yaml is None:
        report.error("PyYAML is not installed. Install with: pip install pyyaml")
        return False
    return True


def load_yaml(path: Path, report: Report) -> Any:
    if not require_yaml(report):
        return None
    try:
        with path.open("r", encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    except Exception as exc:  # noqa: BLE001
        report.error(f"{rel(path)}: invalid YAML: {exc}")
        return None


def load_json(path: Path, report: Report) -> Any:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:  # noqa: BLE001
        report.error(f"{rel(path)}: invalid JSON: {exc}")
        return None


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter_text, body). Frontmatter must start on the first line."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.S)
    if not m:
        return None, text
    return m.group(1), m.group(2)


def parse_frontmatter(text: str, path: Path, report: Report) -> tuple[dict | None, str]:
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        report.error(f"{rel(path)}: missing YAML frontmatter on the first line")
        return None, body
    data = None
    if require_yaml(report):
        try:
            data = yaml.safe_load(fm_text)
        except Exception as exc:  # noqa: BLE001
            report.error(f"{rel(path)}: frontmatter is not valid YAML: {exc}")
            return None, body
    if not isinstance(data, dict):
        report.error(f"{rel(path)}: frontmatter must be a mapping")
        return None, body
    return data, body


def h2_sections(body: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+?)\s*$", body, re.M)]


def markdown_links(body: str) -> list[str]:
    """Return link targets from [text](target) and bare `path` code spans that look like repo paths."""
    targets = [m.group(1) for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", body)]
    return targets


# --- Minimal JSON Schema subset validator -------------------------------------------------------
# Supports: type, required, properties, additionalProperties(false), enum, const, items, minItems,
# minLength, maxLength, minimum, maximum, pattern. Enough for the repository's own schemas and for the
# Agent Plugins manifest schema. Not a general-purpose implementation.

def validate_schema(instance: Any, schema: dict, path: str = "$") -> list[str]:
    errors: list[str] = []
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} not in {schema['enum']}")
    t = schema.get("type")
    if t:
        types = t if isinstance(t, list) else [t]
        if not any(_is_type(instance, tt) for tt in types):
            errors.append(f"{path}: expected type {t}, got {type(instance).__name__}")
            return errors
    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errors.append(f"{path}: missing required field '{req}'")
        props = schema.get("properties", {})
        for key, val in instance.items():
            if key in props:
                errors.extend(validate_schema(val, props[key], f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected field '{key}'")
            elif isinstance(schema.get("additionalProperties"), dict):
                errors.extend(validate_schema(val, schema["additionalProperties"], f"{path}.{key}"))
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: expected at least {schema['minItems']} items")
        if "items" in schema:
            for i, item in enumerate(instance):
                errors.extend(validate_schema(item, schema["items"], f"{path}[{i}]"))
    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: shorter than minLength {schema['minLength']}")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: longer than maxLength {schema['maxLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: value {instance!r} does not match pattern {schema['pattern']!r}")
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: above maximum {schema['maximum']}")
    return errors


def _is_type(value: Any, t: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }.get(t, False)


# --- Repository loaders -------------------------------------------------------------------------

def load_all_agents(report: Report) -> dict[str, dict]:
    agents: dict[str, dict] = {}
    for path in sorted((ROOT / "agents").rglob("*.yaml")):
        data = load_yaml(path, report)
        if not isinstance(data, dict) or "agents" not in data:
            report.error(f"{rel(path)}: expected a mapping with an 'agents' list")
            continue
        for a in data["agents"]:
            if not isinstance(a, dict) or "id" not in a:
                report.error(f"{rel(path)}: agent entry without id")
                continue
            if a["id"] in agents:
                report.error(f"{rel(path)}: duplicate agent id '{a['id']}'")
            a["_file"] = rel(path)
            agents[a["id"]] = a
    return agents


def load_all_skills() -> dict[str, Path]:
    return {p.parent.name: p for p in sorted((ROOT / "skills").glob("*/SKILL.md"))}


def load_departments(report: Report) -> dict[str, dict]:
    deps: dict[str, dict] = {}
    for path in sorted((ROOT / "departments").glob("*/roles.yaml")):
        data = load_yaml(path, report)
        if not isinstance(data, dict) or "department" not in data:
            report.error(f"{rel(path)}: expected 'department' and 'roles' keys")
            continue
        data["_file"] = rel(path)
        deps[data["department"].get("id", path.parent.name)] = data
    return deps


def load_gates(report: Report) -> dict[str, dict]:
    data = load_yaml(ROOT / "core" / "quality-gates" / "gates.yaml", report)
    if not isinstance(data, dict) or "gates" not in data:
        report.error("core/quality-gates/gates.yaml: expected 'gates' list")
        return {}
    return {g["id"]: g for g in data["gates"] if isinstance(g, dict) and "id" in g}


def find_schema(filename: str, repo_relative: str) -> Path:
    """Locate a schema either next to this file (installed copy in a project) or in the repository."""
    local = Path(__file__).resolve().parent / "schemas" / filename
    if local.exists():
        return local
    return ROOT / repo_relative


def finish(reports: list[Report]) -> int:
    for r in reports:
        r.print()
    failed = [r for r in reports if not r.ok]
    print()
    print(f"{len(reports) - len(failed)}/{len(reports)} validators passed")
    return 1 if failed else 0


def main_single(fn) -> None:  # pragma: no cover - CLI glue
    report = fn()
    sys.exit(finish([report]))
