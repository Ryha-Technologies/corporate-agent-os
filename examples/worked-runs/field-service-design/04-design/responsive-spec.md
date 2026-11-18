# Responsive specification

Breakpoints (`design-tokens.json`): sm 360, md 768, lg 1024, xl 1280 (CSS px). Content-driven: the board needs ≥ 1024 for a time axis; lists work from 320.

| Width | Dispatcher | Technician |
|---|---|---|
| < 768 | Bottom tabs; Today as grouped list; New job as centre tab; board unavailable (explained) | Single column; next-job card; bottom tabs |
| 768–1023 | Top tabs; two-column per-technician lists | Single column, wider rows |
| ≥ 1024 | Left rail; board rows × hours; detail opens in side panel | Same as phone layout centred, max 480 px |

Rules: no horizontal scroll at 320 px (WCAG 1.4.10); labels wrap, never truncate (A-007); primary actions in bottom third on phone; text zoom 200% reflows without clipping; board cells keep ≥ 24 px targets.
