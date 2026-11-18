# Bundled schemas

Copies of the official Agent Plugins 1.0.0 JSON schemas, fetched 2026-11-18 from:

- https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- https://agent-plugins.org/schemas/1.0.0/mcp.schema.json

They are bundled so validation works offline and in CI. Refresh them with `scripts/maintenance/refresh_schemas.py` and record the date in `research/source-register.md` when the upstream version changes. The validator rejects a manifest whose `$schema` is not the 1.0.0 constant, so a schema bump is a deliberate change.

The `plugin.schema.json` pattern uses a negative lookahead `(?!...)`, which Python's `re` supports.
