"""Schema tests: repository schemas parse, examples validate, bundled external schemas are the expected versions."""
import json

from common import ROOT, Report, load_json, validate_schema


def test_core_schemas_are_draft_2020_12():
    for rel in ("core/task-management/task-contract.schema.json", "core/workflow-engine/workflow.schema.json",
                "core/memory/memory-entry.schema.json", "templates/design/design-tokens.schema.json"):
        s = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        assert s["$schema"] == "https://json-schema.org/draft/2020-12/schema", rel


def test_bundled_agent_plugins_schemas():
    p = json.loads((ROOT / "scripts/validate/schemas/plugin.schema.json").read_text(encoding="utf-8"))
    m = json.loads((ROOT / "scripts/validate/schemas/mcp.schema.json").read_text(encoding="utf-8"))
    assert p["$id"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert m["$id"] == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
    assert p["additionalProperties"] is False
    assert set(p["required"]) == {"$schema", "name"}


def test_power_manifest_validates_against_bundled_schema():
    schema = load_json(ROOT / "scripts/validate/schemas/plugin.schema.json", Report("s"))
    manifest = load_json(ROOT / "powers/kiro/corporate-agent-os/plugin.json", Report("m"))
    assert validate_schema(manifest, schema) == []
    assert manifest["version"] == (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def test_manifest_with_unknown_field_fails():
    schema = load_json(ROOT / "scripts/validate/schemas/plugin.schema.json", Report("s"))
    manifest = load_json(ROOT / "powers/kiro/corporate-agent-os/plugin.json", Report("m"))
    manifest["steering"] = ["x"]
    assert any("unexpected field 'steering'" in e for e in validate_schema(manifest, schema))


def test_example_task_and_ledger_validate():
    import validate_tasks, validate_memory
    assert validate_tasks.run().ok
    assert validate_memory.run().ok


def test_design_tokens_schema_accepts_minimal_tokens():
    schema = json.loads((ROOT / "templates/design/design-tokens.schema.json").read_text(encoding="utf-8"))
    tokens = {
        "meta": {"product": "demo", "version": "0.1", "contrast_target": "WCAG 2.2 AA"},
        "color": {"text-primary": {"light": "#111111", "dark": "#F5F5F5", "contrast_against": "surface", "contrast_light": 15.2}},
        "typography": {"families": {"body": {"stack": "Inter, sans-serif", "license": "SIL OFL 1.1"}},
                       "scale": {"body": {"size": "1rem", "line_height": "1.5"}}},
        "spacing": {"1": "4px"}, "radius": {"sm": "4px"},
        "motion": {"durations": {"fast": "120ms"}, "easings": {"standard": "ease-out"}, "reduced_motion": "disable non-essential motion"},
        "focus": {"ring": "2px solid #005FCC"},
    }
    assert validate_schema(tokens, schema) == []
    tokens["color"]["bad"] = {"light": "red", "dark": "#000000"}
    assert validate_schema(tokens, schema)


def test_example_tokens_validate_and_meet_contrast():
    import subprocess, sys
    schema = json.loads((ROOT / "templates/design/design-tokens.schema.json").read_text(encoding="utf-8"))
    tokens_path = ROOT / "skills/design-system/assets/design-tokens.example.json"
    tokens = json.loads(tokens_path.read_text(encoding="utf-8"))
    assert validate_schema(tokens, schema) == []
    res = subprocess.run([sys.executable, str(ROOT / "skills/design-system/scripts/contrast_check.py"), str(tokens_path)],
                         capture_output=True, text=True)
    assert res.returncode == 0, res.stdout
    assert "0 role(s) below threshold" in res.stdout
