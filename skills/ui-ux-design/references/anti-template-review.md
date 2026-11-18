# Anti-template review procedure

A list of banned looks does not stop template output; the same layout returns in a different colour. This procedure compares the design against concrete references and requires a reason for every structural choice.

## 1. Assemble the comparison set (before judging)

| Set | Source | Minimum |
|---|---|---|
| Competitor screens | Competitor pattern map (`01-research/competitor-pattern-map.md`) with dated screenshots | 3 competitors, the screen type under review |
| Category default | The most common layout for this screen type in the category (write it down in one sentence, e.g. "sidebar nav, KPI cards row, table") | 1 description |
| Template galleries | Three widely used UI kits or template galleries for this product type; record names and access dates | 3 |

If the competitor pattern map does not exist, record `NOT_ASSESSABLE` for differentiation and stop. Do not judge from memory.

## 2. Structural comparison table

For each screen under review:

| Our element | Closest competitor pattern (ref) | Closest template pattern (ref) | Same / variant / different | Reason for our choice (brand trait, research id or usability principle) | Verdict |
|---|---|---|---|---|---|
| Navigation model | | | | | |
| Page structure (regions, order) | | | | | |
| Primary action placement | | | | | |
| Data presentation (table / cards / list / board) | | | | | |
| Hero or header treatment | | | | | |
| Imagery / illustration | | | | | |
| Colour temperature and accent use | | | | | |
| Typography character | | | | | |
| Motion and micro-interactions | | | | | |
| Empty and error state design | | | | | |

Verdict rules per row:
- **Same** as a competitor's distinctive asset (logo motif, signature illustration style, named layout) → FAIL (imitation).
- **Same** as the category default with no reason → finding (medium): either justify as a convention users expect, or change.
- **Same** as the category default with a stated reason (users expect it, research id) → PASS.
- **Variant** (recolour, reorder, swap icon) presented as differentiation → finding (medium): not a different direction.
- **Different** with a reason traceable to brand or research → PASS; record what is different in `design-rationale.md`.

## 3. The "swap test"

Replace the product name and logo with a competitor's. If the screen would pass as theirs, the design is a template. Record the result and which elements make the screen recognisably this product.

## 4. The "job test"

For each element flagged in the visual checklist (gradient, card, icon tile, illustration, chart, badge, animation): write the job it does for the user in one sentence. No sentence → remove it or FAIL.

## 5. Direction diversity check

When directions were compared, confirm they differ in at least two of: information architecture, density, typographic character, colour system logic, interaction model, imagery approach. Three palettes on one layout count as one direction.

## 6. Record

- `design-rationale.md`: what is deliberately different from the category default and from each competitor; conventions kept and why.
- `07-quality/design-qa-report.md`: the comparison table, swap-test result, job-test removals, verdict.
- `rejected-concepts.md`: directions dropped and why.

## Fail conditions (design gate)

- Imitation of a distinctive competitor asset (high).
- Differentiation `NOT_ASSESSABLE` because no pattern map exists (high; gate cannot pass).
- Two or more structural rows "same as default, no reason" (medium).
- Any element failing the job test still present (medium).
