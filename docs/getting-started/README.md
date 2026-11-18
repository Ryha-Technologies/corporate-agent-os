# Getting started

Ten minutes from zip to first orchestrated request.

1. **Install** for your host following [`../installation/INSTALLATION.md`](../installation/INSTALLATION.md). Use `--dry-run` first.
2. **Read two pages:** [`../architecture/concepts.md`](../architecture/concepts.md) (what an agent, skill, workflow, power, steering file, hook, adapter, orchestrator and reviewer are) and [`../governance/orchestration-guide.md`](../governance/orchestration-guide.md) (how a project runs).
3. **Pick a workflow.** For a rough idea, `business-validation` is the cheapest honest start; it ends with a go / test-first / pivot / stop recommendation. For an existing product, `product-maintenance`. See [`../workflows/README.md`](../workflows/README.md).
4. **Make the request.** Example for Claude Code or Kiro:

   > Use the corporate orchestrator. Run the business-validation workflow for this idea: a scheduling tool for small field-service businesses in India that coordinate technicians over WhatsApp. My budget for validation is small. Ask me one blocking question if you need to, otherwise state assumptions and proceed.

5. **Expect a project workspace** in your repository: `00-intake/brief.md`, `10-decisions/memory-ledger.jsonl`, `10-decisions/tasks/*.json`, then research and assessment files as stages complete, and gate verdicts under `07-quality/`.
6. **Approve where asked.** The orchestrator pauses at human-approval stages and records your answer in `10-decisions/approvals.md`.
7. **Check the report.** The final report lists what was produced, how it was verified and what was not run. If it says "production-ready" without gate verdicts, that is a defect; report it with the transcript as a regression case.

## What good looks like on the first run

- Facts you stated appear as `F-` entries; everything inferred is `A-` or `H-` with a review date.
- The research brief has a disconfirming-evidence section.
- Market figures have formulas and ranges.
- A reviewer agent (not the author) produced each gate verdict.
- The recommendation could have been "stop".

## Next

- Tailor departments and roles for your company: edit `departments/*/roles.yaml` and rerun `python scripts/package/render_roles.py`.
- Trim agents or skills you do not need; rebuild adapters; reinstall.
- Run the evaluation harness on your host and record results: [`../governance/quality-and-evaluation-guide.md`](../governance/quality-and-evaluation-guide.md).
