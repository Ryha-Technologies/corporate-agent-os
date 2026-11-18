# Visual direction

Role: ui-designer (T-004). Status: in REVIEW; gate finding F-1 blocks approval (no comparison set).

## Product category and audience
Dense operations tool (desktop board) plus field-mobile companion (A-008). Audience: dispatchers under interruption and technicians outdoors on low-end Android (A-003). Accessibility target WCAG 2.2 AA.

## Direction statement
**Plain, legible, status-led.** The interface should feel like a well-kept whiteboard: neutral surfaces, strong black text, colour reserved for job status and the one thing to do next. Adjectives map to: *plain* → no illustration or decorative imagery because nothing in the task needs them (job test); *legible* → sunlight and low-end screens (A-003) demand ≥ 7:1 body contrast and 16 px minimum; *status-led* → the dispatcher's job is spotting exceptions (D3), so status colour is the only accent. Brand personality is deliberately absent until a brandbook exists (Q-002, HYPOTHESIS that a neutral system will later take brand tokens without structural change).

## Conventions kept
| Convention | Why users expect it |
|---|---|
| Board with technician rows × time | Dispatch boards and paper diaries use this shape (A-005; HYPOTHESIS, to confirm against pattern map Q-003) |
| Bottom tab bar on phone | Android convention; thumb reach |
| Status chips with colour + text | Colour alone fails WCAG 1.4.1 |

## Where this direction departs from the category default
| Element | Category default (unverified; Q-003) | This direction | Reason |
|---|---|---|---|
| Technician home | Calendar or map first | One ordered list with the next job enlarged | One-handed speed and connectivity (A-003, H-001) |
| Colour | Brand accent across chrome | Neutrals carry everything; accent only for status and primary action | Exceptions must pop (D3) |
| Imagery | Hero or empty-state illustrations | None; empty states are one sentence plus the action | Job test: no element without a job |
| Data on lists | Full customer details | First name and area only | Personal data minimisation (F-002) |

## System decisions
| Area | Decision | Token or spec |
|---|---|---|
| Density | Board: compact (32 px rows); phone lists: comfortable (56 px rows); technician next-job card: large | spacing 2–5 |
| Typography character | Humanist sans with wide language coverage incl. Devanagari fallback (A-007); 16 px body, 600 for labels | `typography.*` |
| Colour logic | Neutral greys; one blue for primary/focus; four status colours each with text label | `color.*` |
| Layout and grid | 8 px base; 12-column desktop; single column phone | `spacing`, `breakpoints` |
| Imagery | None in v1 | — |
| Motion | Only state feedback (toast, chip change) ≤ 220 ms; reduced-motion respected | `motion.*` |
| Dark mode | Not in v1; tokens carry dark values for later | `color.*.dark` |

## Comparison set used
**NOT_ASSESSABLE.** No competitor pattern map exists (Q-003) and none was produced in this run; the category-default column above is the designer's expectation, not evidence. The anti-template review cannot be completed; the design gate records this as a high finding. Required: run `competitive-analysis` to produce `01-research/competitor-pattern-map.md`, then redo this section.

## Swap test result
Not performed (no competitor screens to swap against). Elements expected to be recognisable: next-job card, needs-attention strip — HYPOTHESIS.

## Risks and open questions
Q-002 brand traits; Q-003 pattern map; K-001 no research; A-007 font coverage for Hindi and regional scripts must be confirmed with the chosen font's character set and licence (asset provenance row pending).
