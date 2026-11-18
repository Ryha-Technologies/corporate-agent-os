# Design run — field-service dispatch tool (working title, name not screened)

**Status of this run:** a worked execution of the `product-design` workflow performed by one model acting as each role in turn (orchestrator, ux-designer, ui-designer, design-systems-engineer, accessibility-specialist, design-qa-auditor). It is not a benchmark result: there were no independent human raters, no real user research, and the reviewer roles ran in the same model as the creator roles (different passes, same context). Treat every persona and finding labelled HYPOTHESIS as untested.

**What was skipped and why:** the `product-design` workflow assumes a PRD, brandbook and competitor pattern map exist. None did for this product. The design brief therefore states hypotheses in their place; the competitor pattern map is `NOT_ASSESSABLE`, which the design gate records as a high finding (see `07-quality/gate-design-spec.md`). The run demonstrates the artefact shapes and the gate behaving honestly on missing inputs; it does not produce an approved design.

## Workspace

| Path | Stage | Status |
|---|---|---|
| `00-intake/brief.md` | intake | written |
| `10-decisions/memory-ledger.jsonl` | intake | written, validated |
| `10-decisions/tasks/*.json` | plan | written, validated |
| `04-design/design-brief.md` | design-brief | written |
| `04-design/information-architecture.md`, `user-flows.md`, `states-matrix.md` | ia-and-flows | written |
| `04-design/wireframes/README.md` | wireframes | written (text wireframes) |
| `04-design/visual-direction.md`, `design-rationale.md` | visual-direction | written; comparison set NOT_ASSESSABLE |
| `04-design/design-tokens.json`, `component-spec.md` | tokens-and-components | written, schema-validated, contrast computed |
| `04-design/screens/README.md`, `responsive-spec.md`, `motion-spec.md` | screens | written (specifications, not renderings) |
| `04-design/accessibility-review.md` | accessibility-review | written (design stage; implementation criteria NOT_TESTED) |
| `07-quality/gate-design-spec.md` | design-qa (pass 1) | FAIL (missing pattern map, missing PRD) |
| `01-research/competitor-pattern-map.md`, `competitor-capture.json` | rework T-008 | written from 7 live homepage captures (marketing sites) |
| `03-brand/*` (category audit, strategy, naming report, identity concepts, brandbook, provenance, logo SVGs) | brand-development stages | written; name unscreened, direction pending approval |
| `04-design/prototype/*` + `07-quality/screenshots/*` | screens (rendered) | 4 HTML prototypes from tokens; 6 headless-Chrome screenshots; 3 defects found and fixed in review |
| `07-quality/design-qa-report.md`, `gate-design-rendered.md` | design-qa (pass 2) | FAIL on PRD/research and unscreened name; originality scorecard now passes |
| `10-decisions/approvals.md` | — | pending human |

## Validation commands run

```
python ../corporate-agent-os/scripts/validate/validate_memory.py 10-decisions/memory-ledger.jsonl
python ../corporate-agent-os/scripts/validate/validate_tasks.py 10-decisions/tasks
python ../corporate-agent-os/skills/design-system/scripts/contrast_check.py 04-design/design-tokens.json
```
