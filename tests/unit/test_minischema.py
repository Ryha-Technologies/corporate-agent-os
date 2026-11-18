"""Unit tests for the minimal JSON Schema validator used across the repository."""
from common import validate_schema

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["name", "count"],
    "properties": {
        "name": {"type": "string", "minLength": 2, "maxLength": 5, "pattern": "^[a-z]+$"},
        "count": {"type": "integer", "minimum": 1, "maximum": 3},
        "tags": {"type": "array", "minItems": 1, "items": {"type": "string", "enum": ["a", "b"]}},
        "kind": {"const": "x"},
    },
}


def test_valid_instance_passes():
    assert validate_schema({"name": "abc", "count": 2, "tags": ["a"], "kind": "x"}, SCHEMA) == []


def test_missing_required_and_unknown_field():
    errs = validate_schema({"name": "abc", "extra": 1}, SCHEMA)
    assert any("missing required field 'count'" in e for e in errs)
    assert any("unexpected field 'extra'" in e for e in errs)


def test_type_pattern_length_and_range():
    errs = validate_schema({"name": "ABCDEFG", "count": 7}, SCHEMA)
    assert any("maxLength" in e for e in errs)
    assert any("pattern" in e for e in errs)
    assert any("above maximum" in e for e in errs)


def test_enum_items_and_const():
    errs = validate_schema({"name": "abc", "count": 1, "tags": ["z"], "kind": "y"}, SCHEMA)
    assert any("not in ['a', 'b']" in e for e in errs)
    assert any("expected constant 'x'" in e for e in errs)


def test_boolean_is_not_integer():
    errs = validate_schema({"name": "abc", "count": True}, SCHEMA)
    assert any("expected type integer" in e for e in errs)


def test_negative_lookahead_pattern_from_plugin_schema():
    pattern = r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$"
    s = {"type": "string", "pattern": pattern}
    assert validate_schema("corporate-agent-os", s) == []
    assert validate_schema("bad--name", s)
    assert validate_schema("-bad", s)
    assert validate_schema("Bad", s)
