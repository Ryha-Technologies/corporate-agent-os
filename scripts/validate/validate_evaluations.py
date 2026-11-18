#!/usr/bin/env python3
"""Validate evaluation assets: regression dataset shape, golden task files, rubrics and originality scorecard."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Report, load_json, load_yaml, main_single, rel  # noqa: E402

CASE_REQUIRED = {"id", "prompt", "expected", "forbidden", "skills", "dimensions"}
GOLDEN_REQUIRED = {"id", "name", "input", "workflow", "expected_evidence", "evaluation_dimensions", "human_review_required"}


def run() -> Report:
    report = Report("evaluations")
    ds = load_json(ROOT / "evaluations/datasets/regression-cases.json", report)
    if isinstance(ds, dict):
        dims = set(ds.get("scoring_dimensions", []))
        ids: set[str] = set()
        skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        for c in ds.get("cases", []):
            missing = CASE_REQUIRED - set(c)
            if missing:
                report.error(f"regression case {c.get('id')}: missing {sorted(missing)}")
            if c.get("id") in ids:
                report.error(f"regression case {c.get('id')}: duplicate id")
            ids.add(c.get("id"))
            for s in c.get("skills", []):
                if s not in skills:
                    report.error(f"regression case {c.get('id')}: unknown skill '{s}'")
            for d in c.get("dimensions", []):
                if d not in dims:
                    report.error(f"regression case {c.get('id')}: unknown dimension '{d}'")
        report.note(f"{len(ids)} regression cases")
    golden = sorted((ROOT / "evaluations/golden-tasks").glob("*.yaml"))
    if len(golden) < 5:
        report.error(f"expected at least 5 golden tasks (benchmarks A-E), found {len(golden)}")
    workflows = {p.parent.name for p in (ROOT / "workflows").glob("*/workflow.yaml")}
    for g in golden:
        data = load_yaml(g, report)
        if not isinstance(data, dict):
            continue
        missing = GOLDEN_REQUIRED - set(data)
        if missing:
            report.error(f"{rel(g)}: missing {sorted(missing)}")
        if data.get("workflow") not in workflows:
            report.error(f"{rel(g)}: unknown workflow '{data.get('workflow')}'")
        if data.get("human_review_required") is not True:
            report.error(f"{rel(g)}: human_review_required must be true; model outputs are not self-certifying")
    for required in ("evaluations/README.md", "evaluations/rubrics/README.md", "evaluations/originality/originality-scorecard.md",
                     "evaluations/originality/slop-patterns.md", "evaluations/benchmark-reports/README.md", "evaluations/run_evals.py"):
        if not (ROOT / required).exists():
            report.error(f"missing {required}")
    rubrics = list((ROOT / "evaluations/rubrics").glob("*.md"))
    if len(rubrics) < 4:
        report.error(f"expected rubrics for research, business, brand, design, engineering, security; found {len(rubrics)} files")
    return report


if __name__ == "__main__":
    main_single(run)
