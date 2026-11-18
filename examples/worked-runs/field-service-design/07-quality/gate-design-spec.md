# Gate verdict

```
GATE: design
STAGE: design-qa (specification set, T-007)
REVIEWER: design-qa-auditor
DATE: 2026-11-18
VERDICT: FAIL
```

Independence note: this reviewer role was executed by the same model that produced the artefacts, in a separate pass. That is weaker than the policy requires (separate context, ideally a different model). The verdict is therefore provisional and must be repeated by an independent reviewer before it counts.

## Evidence checked
| Required evidence (gates.yaml → design) | Present? | Path |
|---|---|---|
| user-flows.md and information-architecture.md | yes | `04-design/` |
| design-tokens.json and component-spec.md | yes; tokens schema-validated, contrast computed (0 roles below threshold) | `04-design/` |
| states-matrix.md with all states | yes; no "missing" cell for 14 screens | `04-design/states-matrix.md` |
| accessibility-review.md against WCAG 2.2 AA | yes; design-stage only, implementation criteria NOT_TESTED | `04-design/accessibility-review.md` |
| design-rationale.md tracing decisions to brand and research | partial: decisions trace to A-/H- ledger entries (hypotheses), not to research or brand | `04-design/design-rationale.md` |

## Findings
| # | Severity | Finding | Evidence | Impact | Required fix | Retest |
|---|---|---|---|---|---|---|
| F-1 | high | Differentiation `NOT_ASSESSABLE`: no competitor pattern map exists; the anti-template comparison table, swap test and "category default" column rest on the designer's expectations (Q-003). Gate fail condition "template-like layout with no rationale" cannot be ruled out. | `visual-direction.md` → Comparison set; `anti-template-review.md` §1 | Design may replicate a competitor or category default unknowingly | Run `competitive-analysis` to produce `01-research/competitor-pattern-map.md` with dated screenshots of ≥ 3 dispatch tools' board, mobile job list and job detail; redo the comparison table, swap test and rationale column | Re-review the comparison table against the map |
| F-2 | high | No PRD or customer research: every flow priority and the success targets (A-006) are hypotheses; the states matrix and IA may be optimised for the wrong tasks (K-001). | `design-brief.md`, ledger A-001..A-008, H-001, H-002 | Design decisions untestable against requirements | Produce PRD (`product-discovery-prd`) or at minimum five dispatcher and five technician interviews with the interview guide; convert A-/H- entries to F- or withdraw | Check that flows map to PRD stories and criteria |
| F-3 | medium | Font family is a placeholder; Devanagari and regional script coverage, version and licence unconfirmed (Q-004); no `asset-provenance.md` row. | `design-tokens.json` → typography.families.ui.license | Legibility and licensing risk for A-007 languages | Select font, record source/version/licence in `03-brand/assets/asset-provenance.md`, confirm glyph coverage for target scripts | Provenance row present; coverage note |
| F-4 | medium | No rendered screens; implementation-only WCAG criteria and the visual checklist's rendered-UI section are NOT_TESTED. | `screens/README.md`, `accessibility-review.md` | Fidelity, reflow, focus order unverified | Build or prototype the six wireframed screens; run the rendered-UI checks at 360/768/1280 | Design QA report with screenshots |
| F-5 | low | "Category default" statements in `visual-direction.md` read as facts in places ("Dispatch boards and paper diaries use this shape") though marked HYPOTHESIS in the table; tighten wording so every such claim carries its label inline. | `visual-direction.md` → Conventions kept | Reader may take expectation for evidence | Edit wording | Read-through |

## What passed
- States matrix complete (14 screens × 11 states, every cell specified or n/a with reason).
- Tokens machine-readable, schema-valid, every text/control colour pairing measured ≥ 4.5:1 (text) or ≥ 3:1 (non-text); `border` 1.58:1 correctly marked decorative-only with input borders using `border-strong` 3.11:1.
- Job test applied: three elements removed (empty-state illustration, hero header, duplicate progress ring); every remaining element has a stated job.
- Three structural directions compared (list-first, calendar-first, chat-timeline), not recolours; rejections recorded (X-001..X-003).
- Personal-data minimisation reflected in list content (F-002).
- Drag-and-drop has a select-based alternative (2.5.7); targets ≥ 44 px for technician actions (2.5.8).

## Scorecard (originality, dimensions assessable)
| Dimension | Score | Note |
|---|---|---|
| Research depth | 0 | no category audit or pattern map |
| Relevance | 2 | addresses the stated roles and tasks; tasks are hypotheses |
| Specificity | 2 | concrete flows, states, tokens; sample content labelled |
| Differentiation | NOT_ASSESSABLE | F-1 |
| Strategic coherence | 1 | traces to hypotheses, not strategy or brand |
| Practical usefulness | 3 | implementable specs |
| Craftsmanship | 2 | tokens validated; no renderings |
| Evidence quality | 1 | no fabricated claims, but almost no evidence either |
| Consistency | 3 | one vocabulary (jobs, technicians, customers) across all artefacts |
| Audience suitability | 2 | accessibility and device constraints addressed as hypotheses |

Research depth 0 → fails the originality check regardless of other scores.

## Accepted risks
None. Critical/high findings cannot be accepted at this gate without the human owner; none requested.

## Not assessed
Rendered UI, implementation accessibility criteria, differentiation. Human approval: PENDING (`10-decisions/approvals.md`).

## Rework contracts proposed
- T-008 competitive-analyst → `01-research/competitor-pattern-map.md` (F-1)
- T-009 customer-researcher → interview plan and sessions; product-manager → PRD (F-2)
- T-010 design-systems-engineer → font selection and provenance (F-3)
- T-011 frontend-engineer or prototyper → render six screens; design-qa-auditor → implementation review (F-4)
