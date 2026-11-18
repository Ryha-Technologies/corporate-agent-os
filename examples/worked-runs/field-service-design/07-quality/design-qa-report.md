# Design QA report — rendered prototypes

Role: design-qa-auditor. Date: 2026-11-18. Scope: `04-design/prototype/` (board.html, my-jobs.html, job-detail.html, brand-sheet.html) rendered with headless Chrome at 1280×800, 768×900, 360×760/800; screenshots in `screenshots/`. Tokens: `04-design/design-tokens.json` (schema-valid; contrast computed, 0 roles below threshold). Fonts loaded from Google Fonts at render time (Anek Latin, Anek Devanagari); offline rendering would fall back to system-ui.

Independence note: same model as the creator, separate pass. Provisional until an independent reviewer repeats it.

## Findings (chronological; fixed items retained as evidence that review changed the artefact)
| # | Screen | Viewport | Finding | Category | Severity | Evidence | Fix | Retest |
|---|---|---|---|---|---|---|---|---|
| Q-1 | my-jobs | 360 | Content overflowed the viewport and was clipped on the right; rows wider than 360 because the status chip column forced the grid wider | responsive / overflow | blocker | `screenshots/my-jobs-360.png` (first render, overwritten) | `.row` columns `56px minmax(0,1fr) auto`, `.row *{min-width:0}`, frame fixed at 360 | PASS (current screenshot) |
| Q-2 | my-jobs, job-detail | 360 | Row links and buttons showed browser default blue underlines | fidelity / colour role | major | first renders | `a.row{color:inherit;text-decoration:none}`, `.btn{text-decoration:none}` | PASS |
| Q-3 | brand-sheet | 1000 | "Not answering" chip rendered with yellow marker background: CSS class `.attention` collided between the strip and the chip | consistency / colour role (marker is background-only for the strip) | major | `screenshots/brand-sheet-1000.png` (first render) | Renamed strip class to `.attention-strip` | PASS |
| Q-4 | board | 1280 | Technician load read "1 jobs" | content | minor | first render | plural handling | PASS |
| Q-5 | board | 1280 | Unassigned job (Imran · Khan) sits in a technician row; IA specifies an **Unassigned lane** at the top of the board | fidelity to spec | major | `screenshots/board-1280.png` | Not fixed in this pass; add lane | OPEN |
| Q-6 | board | 360 | Dispatcher phone layout (grouped list, bottom tabs) not prototyped; desktop board overflows at 360 as expected for a desktop-only view | not built | major (coverage) | `screenshots/board-360.png` | Build W2 prototype | OPEN |
| Q-7 | all | all | Icons absent (tab bar is text-only; back arrow is a glyph) pending icon set choice (Q-006) | not built | minor | all screenshots | choose OFL/MIT set | OPEN |
| Q-8 | all | all | Keyboard focus ring, hover, loading, empty, error and offline states not rendered (static prototypes) | states coverage | major (coverage) | — | state pages or storybook | OPEN |
| Q-9 | board | 1280 | Time header cells use `font-stretch:87%`; whether Anek's width axis applied could not be confirmed visually at this size | typography | low | `board-1280.png` | verify with dev tools / larger sample | OPEN |

## Visual checklist (rendered, current screenshots)
| Check | Result | Evidence |
|---|---|---|
| One primary action per screen | PASS | board: New job; my-jobs: Open job; detail: Complete job |
| Body ≥ 16 px, line height 1.5 | PASS (by tokens) | tokens.css |
| Text contrast ≥ 4.5:1 | PASS (computed) | contrast_check output; marker strip ink-on-yellow 11.68:1 |
| Non-text contrast ≥ 3:1 (borders used as boundaries, focus) | PASS (computed) | border-strong 4.04:1; focus 9.49:1 |
| Colour not sole signal | PASS | chips carry text; job blocks carry text; marker strip carries text |
| Touch targets ≥ 44 px on technician primary actions | PASS (by CSS: 48 px buttons, 56 px rows/tabs) | my-jobs-360, job-detail-360 |
| No horizontal scroll at 360 | PASS for phone screens; N/A for desktop-only board (Q-6) | my-jobs-360, job-detail-360 |
| Decorative elements have a job | PASS | no illustration, no gradient; only marker strip (attention) and status colours |
| Fake data labelled | PASS | "Sample data — fictional" on every screen |
| Terminology | PASS | jobs / technicians / customers throughout |
| Brand accent share ≤ ~10% | PASS (visual estimate) | board-1280: brand on primary button and assigned blocks only |
| Marker ≤ 1% and background-only | PASS after Q-3 | brand-sheet-1000 |
| Longest realistic strings | NOT_TESTED | no Hindi UI strings rendered beyond the brand sheet sample |
| Console errors | NOT_TESTED | headless screenshot mode only |

## Anti-template review (structural comparison, marketing-site proxies)
| Our element | Closest competitor pattern | Closest template pattern | Relation | Reason | Verdict |
|---|---|---|---|---|---|
| Left rail + board grid | Common dispatch-board shape (assumed; product UIs not captured) | Admin template sidebar + table | same (convention) | Dispatchers expect rows × time (A-005, HYPOTHESIS) | PASS as convention; verify against product screenshots (T-012) |
| Marker-yellow attention strip at top | none in captured set | KPI card row | different | Exceptions first (D3); whiteboard metaphor | PASS |
| Aubergine primary, paper background | orange/blue on navy (5 of 7) | purple-gradient SaaS | different (flat, no gradient) | pattern-map gap | PASS |
| Anek multi-script type | Inter-family (5 of 7) | Inter | different | script coverage (A-007) | PASS |
| Technician next-job card + list | not captured | card list | variant of a list | one-handed speed (H-001) | PASS with reason |
| Logo: board rows with placed block | pins/wrenches/checks (audit) | generic rounded square app icon | different motif; container is conventional | motif carries the promise | PASS; design-mark screening NOT_RUN |

Swap test: with a competitor's logo swapped in, the board would still read as "a dispatch board" (convention), but the marker strip, paper/aubergine palette and type would not match any captured competitor. Partial pass; product-UI comparison outstanding.

## Verdict input
Blockers: none open (Q-1 fixed). Open majors: Q-5, Q-6, Q-8. See `gate-design-rendered.md`.
