# Accessibility review (design stage, WCAG 2.2 AA)

Role: accessibility-specialist (T-006). Scope: wireframes, tokens, component spec, states matrix. Method: manual review of specifications against `standards/accessibility/wcag-2.2-aa-checklist.md`; contrast computed with `contrast_check.py`. No rendered UI exists, so every criterion that needs a running interface is **NOT_TESTED**, not PASS.

| SC | Name | Result | Evidence / note |
|---|---|---|---|
| 1.1.1 | Non-text content | PASS (design) | Status dots `aria-hidden`; icons paired with text; no informational images |
| 1.3.1 | Info and relationships | PASS (design) | Headings, lists, grid semantics for board, dialog labelling specified |
| 1.3.2 | Meaningful sequence | NOT_TESTED | Needs rendered DOM |
| 1.3.5 | Identify input purpose | PASS (design) | Phone field `tel`, name fields autocomplete specified |
| 1.4.1 | Use of colour | PASS (design) | Every status has a text label |
| 1.4.3 | Contrast (minimum) | PASS (design) | text-primary 18.58:1 light; status colours 5.9–7.5:1; see tokens |
| 1.4.4 | Resize text | NOT_TESTED | Specified in responsive spec |
| 1.4.10 | Reflow | NOT_TESTED | Specified: no horizontal scroll at 320 px |
| 1.4.11 | Non-text contrast | PASS (design) | border-strong 3.11:1; focus 6.45:1; `border` 1.58:1 marked decorative-only (not a boundary users rely on; input borders use border-strong) |
| 1.4.12 | Text spacing | NOT_TESTED | |
| 1.4.13 | Content on hover/focus | PASS (design) | Disabled-reason tooltips dismissible and hoverable; also shown as helper text |
| 2.1.1 | Keyboard | PASS (design) | Board grid keyboard model; drag has select alternative |
| 2.1.2 | No keyboard trap | NOT_TESTED | Dialog focus trap must release on Escape (specified) |
| 2.4.3 | Focus order | NOT_TESTED | |
| 2.4.7 | Focus visible | PASS (design) | 2 px ring, 6.45:1, offset 2 px |
| 2.4.11 | Focus not obscured | NOT_TESTED | Sticky Save button must not cover focused fields; spec says scroll-margin |
| 2.5.7 | Dragging movements | PASS (design) | Select-based assign alternative |
| 2.5.8 | Target size (minimum) | PASS (design) | ≥ 44 px technician actions; board cells ≥ 24 px |
| 3.1.1/3.1.2 | Language | PASS (design) | `lang` switches with profile language; mixed-script strings marked |
| 3.2.6 | Consistent help | PASS (design) | "Contact dispatcher" in the same place on technician screens |
| 3.3.1/3.3.3 | Error identification / suggestion | PASS (design) | Field-level messages name the field and fix |
| 3.3.4 | Error prevention | PASS (design) | Cancel job confirms; completion undoable 10 min |
| 3.3.7 | Redundant entry | PASS (design) | Known customer prefill |
| 3.3.8 | Accessible authentication | NOT_TESTED | Login via code; no cognitive test specified — confirm in PRD |
| 4.1.2 | Name, role, value | NOT_TESTED | Specified per component; verify in implementation |
| 4.1.3 | Status messages | PASS (design) | `role="status"` on toasts, badges, chips that announce |

Blockers: none at design stage. Open: font script coverage (Q-004) affects 3.1.2 and legibility; implementation review required for all NOT_TESTED rows.
