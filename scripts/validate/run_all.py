#!/usr/bin/env python3
"""Run every repository validator and exit non-zero if any fails.

Usage: python scripts/validate/run_all.py [--json report.json]
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, finish  # noqa: E402
import validate_structure, validate_skills, validate_agents, validate_departments, validate_workflows  # noqa: E402
import validate_core, validate_power, validate_adapters, validate_links, validate_evaluations  # noqa: E402

VALIDATORS = [
    validate_structure.run,
    validate_skills.run,
    validate_agents.run,
    validate_departments.run,
    validate_workflows.run,
    validate_core.run,
    validate_power.run,
    validate_adapters.run,
    validate_links.run,
    validate_evaluations.run,
]


def main(argv: list[str]) -> int:
    reports: list[Report] = []
    for fn in VALIDATORS:
        try:
            reports.append(fn())
        except Exception as exc:  # noqa: BLE001
            r = Report(fn.__module__)
            r.error(f"validator crashed: {exc!r}")
            reports.append(r)
    code = finish(reports)
    if "--json" in argv:
        out = Path(argv[argv.index("--json") + 1])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "root": str(ROOT),
            "passed": code == 0,
            "validators": [{"name": r.name, "ok": r.ok, "errors": r.errors, "warnings": r.warnings, "info": r.info} for r in reports],
        }, indent=2), encoding="utf-8")
        print(f"JSON report written to {out}")
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
