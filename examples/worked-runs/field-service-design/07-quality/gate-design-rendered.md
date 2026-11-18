# Gate verdict

```
GATE: design
STAGE: design-qa (brand + rendered prototypes, second pass)
REVIEWER: design-qa-auditor (same model, separate pass — provisional)
DATE: 2026-11-18
VERDICT: FAIL
```

Progress since `gate-design-spec.md`: F-1 (no pattern map) partially remediated — a pattern map now exists from seven competitor **marketing sites** with dated captures; product-UI screenshots are still missing. F-3 (font) remediated — Anek, OFL 1.1, scripts verified, provenance recorded; version pin pending. F-4 (no renderings) partially remediated — four prototypes rendered and reviewed at three widths; three real defects found and fixed in review (overflow, link styling, class collision). F-2 (no PRD or research) unchanged.

## Evidence checked
| Required evidence | Present | Path |
|---|---|---|
| Flows, IA, states matrix | yes | `04-design/` |
| Tokens with contrast, component spec | yes; brand palette applied; 0 roles below threshold after one fix (border-strong 2.98 → 4.04) | `04-design/design-tokens.json` |
| Accessibility review | design-stage only; implementation criteria NOT_TESTED | `04-design/accessibility-review.md` |
| Design rationale and pattern-map comparison | yes, against marketing-site proxies | `04-design/design-rationale.md`, `01-research/competitor-pattern-map.md`, `design-qa-report.md` |
| Brand strategy, category audit, naming report, identity concepts, brandbook, asset provenance | yes | `03-brand/` |
| Rendered screenshots | yes, 6 | `07-quality/screenshots/` |

## Findings
| # | Severity | Finding | Required fix |
|---|---|---|---|
| G-1 | high | No PRD and no customer research; all task priorities and copy are hypotheses (F-2 carried) | PRD or ≥ 10 interviews; convert A-/H- entries |
| G-2 | high | Working title "Kaamline" unscreened in any register; "Kaam" prefix crowded; name appears in the wordmark and prototypes | Counsel-led IN search (classes 9/42/35) before any public use; keep "working title" label on every artefact |
| G-3 | medium | Pattern map built from marketing sites; product UIs not compared (swap test partial) | Capture product UI from trials of ≥ 3 competitors (T-012) |
| G-4 | medium | Unassigned lane missing on board (Q-5); dispatcher phone view not built (Q-6); interaction states not rendered (Q-8) | Extend prototypes |
| G-5 | medium | Implementation WCAG criteria NOT_TESTED; font axis behaviour and `tnum` unconfirmed (Q-005, Q-9) | Build and test |
| G-6 | low | Design-mark similarity search NOT_RUN for the symbol | IP India / WIPO image search with counsel |

## Scorecard (originality)
| Dimension | Score | Change |
|---|---|---|
| Research depth | 2 (was 0) | pattern map and category audit exist; product-UI gap |
| Relevance | 2 | — |
| Specificity | 3 (was 2) | rendered, token-driven, sample data labelled |
| Differentiation | 2 (was NOT_ASSESSABLE) | documented against 7 marketing sites; product UI outstanding |
| Strategic coherence | 2 (was 1) | brand strategy exists; still rests on hypotheses |
| Practical usefulness | 3 | buildable tokens, CSS, SVGs |
| Craftsmanship | 2 | three defects found and fixed; open majors remain |
| Evidence quality | 2 (was 1) | sourced captures and font licence; no customer evidence |
| Consistency | 3 | — |
| Audience suitability | 2 | — |

No dimension at 0; two at 2 or above everywhere; evidence quality 2. The originality check passes; the **gate** still fails on G-1 and G-2, which are not design-fixable.

## Not assessed
Legal distinctiveness of name and mark; product-UI comparison; implementation accessibility.

## Human approval
PENDING. Recommended decision for the owner: approve the direction for continued work (not for publication), fund counsel screening and ten interviews.
