# Design rationale

Role: ui-designer with design-lead (T-004).

## Decisions
| Decision | Rationale (id) | Alternative considered | Pattern-map comparison |
|---|---|---|---|
| Technician home is an ordered list with the next job enlarged | H-001, A-003 | Calendar (X-001), map-first | NOT_ASSESSABLE (Q-003) |
| Needs-attention strip at the top of Today | D3 flow; exceptions are the dispatcher's job (A-002) | Filter only | NOT_ASSESSABLE |
| Technician picker shows load and skill match, not a map | Decision data a dispatcher states in calls (A-001, HYPOTHESIS) | Map with pins | NOT_ASSESSABLE |
| Neutral palette with status-only colour | Legibility outdoors (A-003); exceptions must stand out | Brand-coloured chrome | NOT_ASSESSABLE |
| No illustrations or decorative imagery | Job test: none has a job | Empty-state illustrations | — |
| Drag-and-drop only as accelerator | WCAG 2.5.7; phone use | Drag as primary | — |
| Minimal personal data in lists | F-002 | Full details | — |

## Elements that needed a stated job
| Element | Job | Kept? |
|---|---|---|
| Status colour chips | Convey state at a glance with text | kept |
| Next-job card enlargement | Reduce taps and reading for the most frequent action (T1) | kept |
| Needs-attention strip | Surface exceptions (D3) | kept |
| Empty-state illustration | none | removed |
| Hero header on login | none | removed |
| Progress ring on job cards | duplicate of status chip | removed |

## Accessibility decisions
Body contrast ≥ 7:1 target (exceeds AA) for outdoor use; focus ring 2 px blue, offset 2 px; targets ≥ 44 px for technician primary actions; reduced motion disables toast slide.

## Directions compared
Three directions were sketched as structural alternatives, not recolours: (1) list-first technician + board dispatcher (chosen); (2) calendar-first for both roles (rejected, X-001); (3) chat-style timeline mirroring WhatsApp (rejected: hides status and ordering; recorded X-003 in rejected-concepts). The comparison lacks pattern-map evidence; see gate verdict.

## What is deliberately different from the category default
Stated in `visual-direction.md`; unverified until Q-003 is resolved.
