# Identity concepts

Role: identity-designer (T-015). Three territories explored; one developed. Vector files in `assets/logo/`. Name shown is the unscreened working title.

## Visual audit summary
From the pattern map: accents orange/blue on navy; geometric sans wordmarks; dashboard-screenshot heroes. Clichés to avoid: pin/map markers, wrench/gear icons, checkmark-in-circle, lightning bolts, "AI sparkle".

## Territories
| # | Idea | Why / why not |
|---|---|---|
| A **Board row** (developed) | A rounded board with three rows; one job block sits in marker yellow — "the placed job". Reads as a schedule at 16 px; the yellow block is the brand device reused in UI for attention highlights. | Expresses the product's one promise; no icon cliché from the audit |
| B Knock | Two concentric arcs (a knock at the door), tying to the visit | Lost with the Dastak name conflict; also resembles sound/wifi icons (X-007) |
| C Marker stroke | A hand-drawn yellow highlight under a wordmark | Decorative; fails small-size test (stroke becomes a smudge) (X-008) |

## Concept A specification
- Geometry: 64-unit grid; container radius 10/64; rows 7 units tall, 11.5 apart; the placed block starts at 31 (golden-ish split 14/36 → 17/19), yellow `#FFD23F`.
- Monochrome: works with white rows on black (`symbol-mono.svg`); the placed block is full-opacity white, others 45%.
- 16 px: `symbol-16.svg` drops radii to 3 and row height to 2 px; still reads as three rows with one highlighted block.
- Wordmark: lowercase "kaamline" in Anek, weight 700, slightly tightened; lowercase keeps it plain-spoken. Horizontal lockup only in v1; stacked variant deferred.
- Clear space: 0.25 × symbol height on all sides. Minimum symbol size 16 px; wordmark minimum height 20 px.
- Misuse: no gradients, no drop shadow, never recolour the placed block to orange or blue (category colours), never rotate.

## Tests performed
- Rendered as SVG at 64, 16 and in the wordmark; monochrome variant produced. Screenshot inspection at these sizes: see `07-quality/screenshots/` (brand sheet).
- Design-mark similarity search: NOT_RUN (needs IP India / WIPO image search with counsel).

## Rights
All vectors drawn in this run; no third-party elements. Font licence recorded in `assets/asset-provenance.md`.
