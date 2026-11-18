# Brandbook — working title "Kaamline" (name not screened)

Version 0.1 · Role: identity-designer with brand-strategist · Status: draft pending brand gate and counsel. A stranger should be able to produce on-brand work from this document.

## 1. Foundation
Essence: the day board for small service teams. Positioning, audience, promise and proof: `brand-strategy.md`. Promise: nothing falls through.

## 2. Story and messaging
Narrative lengths in `brand-strategy.md`. Message hierarchy: (1) nothing falls through; (2) every job has a technician, a time and a status; (3) built for the phones, networks and languages your technicians use. Prohibited claims: "AI", "all-in-one", "automate", revenue or growth promises, "track your workers".

## 3. Logo system
Files: `assets/logo/symbol.svg`, `symbol-mono.svg`, `symbol-16.svg`, `wordmark-horizontal.svg`. Rules in `identity-concepts.md` (clear space 0.25×, min 16 px symbol / 20 px wordmark height, no gradients, shadows, rotation or recolouring of the placed block). Backgrounds: ink symbol on white or paper; mono white-on-ink for dark. Incorrect: placing the symbol on orange or blue; outlining; adding a wrench or pin.

## 4. Colour
Metaphor: ink on paper with one marker.

| Role | Light | Dark | Use | Contrast (computed, see tokens) |
|---|---|---|---|---|
| ink (text-primary) | `#1F1A2E` | #F4F2F8 | all text | see `04-design/design-tokens.json` |
| paper (background) | #FBFAF7 | #16131F | page | — |
| surface | #F2EFEA | #1F1B2B | panels, rows | — |
| brand (aubergine) | `#5B2A86` | #C9A6E6 | primary action, links, focus | measured |
| marker (yellow) | `#FFD23F` | `#FFD23F` | attention highlight **background only**, always with ink text | ink on marker measured |
| status-unassigned / assigned / started / completed / attention | see tokens | | status chips with text | measured ≥ 4.5:1 |

Usage ratio: paper and surface ~85%, ink ~10%, brand ≤ 4%, marker ≤ 1% (it must stay rare to mean "look here"). Marker is never used for text, borders or decoration. Dark mode tokens exist; v1 ships light only.

## 5. Typography
Family: **Anek** (variable; weight 400–700; width 100 for UI, 87 "semi-condensed" allowed in the desktop board time columns). Scripts: Latin, Devanagari, Tamil and the other Anek scripts from the same family — no fallback switch between English and Hindi labels. Fallback stack: system-ui, sans-serif. Scale in tokens: caption 12, body-sm 14, body 16, label 14/600, title-sm 18/600, title 22/700, display 28/700, next-job 20/700. Line height 1.5 body. Tabular figures for times: confirm `tnum` support in Anek before build (Q-005); otherwise use a tabular system font for time columns only.

## 6. Grid, spacing, layout
8 px base; scale 4/8/12/16/24/32/48/64. Desktop 12 columns, 24 px gutters, max content 1280. Phone single column, 16 px margins. Row heights 32 (board) / 56 (phone lists). Breakpoints 360/768/1024/1280.

## 7. Imagery and art direction
No stock photography, no illustrations, no 3D, no dashboard-screenshot heroes. Where a picture is needed (website, docs): photographs of real customers' boards and vans, with consent, shot plainly in daylight; or the product itself at real size with sample data labelled as sample. Prohibited: smiling-technician stock, abstract blobs, gradients.

## 8. Iconography and data visualisation
Icons: outline, 2 px stroke, 24 px grid, always paired with a text label in product UI; set to be chosen from an OFL/MIT icon set and recorded in provenance (Q-006). Charts: only when a decision depends on them; bars over donuts; ink and one brand tint; no decorative sparklines.

## 9. Motion
Only state feedback: 140–220 ms, standard easing; fade-only under reduced motion. No ambient animation, no animated heroes.

## 10. Voice and tone
Plain, steady, specific. Say "job", "technician", "customer", "today". Sentence case. Buttons name the result ("Assign to Ravi", "Save job"). Hindi and regional words where they are the real words; never transliterated marketing slogans. Sample: "3 jobs need attention." not "Action required!".

## 11. UI tokens
`04-design/design-tokens.json` (schema-valid; contrast computed by `contrast_check.py`).

## 12. Applications
Product: see `04-design/prototype/` and screenshots. Website: paper background, ink headline leading with the owner's problem, one product screenshot at real size, one CTA "Start free" (self-serve; teams of 5–50 do not book demos). Documents and decks: paper, ink, Anek; marker used once per page at most. Social avatar: `symbol.svg` on ink. WhatsApp notification templates: plain text, job window and address first.

## 13. Accessibility and localisation
WCAG 2.2 AA; body contrast target ≥ 7:1 outdoors. Strings sized for +40% length; Anek covers scripts without fallback jumps; RTL not required.

## 14. Distinctiveness
Against the pattern map: aubergine + marker vs orange/blue on navy (5 of 7); Anek multi-script vs Inter-family (5 of 7); problem-led headline vs "AI/all-in-one" (6 of 7); whiteboard symbol vs pin/wrench/check icons. Repeatable devices: the placed yellow block (logo and UI attention), lowercase wordmark. Legal distinctiveness NOT ASSESSED.

## 15. Governance
Owner: founder. Approvals: brand gate (brand-originality-auditor) then human. Asset inventory: `assets/asset-provenance.md`. Version history: 0.1 (2026-11-18) first draft.
