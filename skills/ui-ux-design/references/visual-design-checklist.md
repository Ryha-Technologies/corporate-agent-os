# Visual design checklist (measurable)

Use during design and at design QA. Each item is a check with a measurement or an observable, not an opinion. Record PASS / FAIL / N/A per screen in the design QA report.

## Hierarchy
| Check | Measure |
|---|---|
| One primary action per screen or section | Count of primary-styled buttons visible at once = 1 |
| Heading levels reflect content importance | Visual size order matches semantic h1 > h2 > h3; no skipped levels |
| The most important data is reachable without scrolling on the smallest supported viewport | Confirm at 360×640 CSS px (mobile) and the smallest desktop breakpoint |
| Decorative elements do not outrank content | No decorative element has higher contrast, size or motion than the primary content on the screen |

## Typography
| Check | Measure |
|---|---|
| Scale is a defined ratio applied consistently | Every text size maps to a token in `design-tokens.json`; no ad-hoc sizes |
| Body text size | ≥ 16 CSS px (mobile), line height 1.4–1.6 |
| Line length | 45–80 characters for body paragraphs; data tables exempt |
| Weights | ≤ 3 weights per family in product UI |
| Families | ≤ 2 families; each with a licence row in asset provenance |
| Real text lengths tested | Longest realistic string (names, addresses, error messages) rendered without clipping |

## Spacing and layout
| Check | Measure |
|---|---|
| Spacing comes from the scale | Every margin/padding maps to a spacing token (e.g. 4/8/12/16/24/32/48) |
| Grid | Columns and gutters defined per breakpoint; elements align to it |
| Density fits the category | Compare against `product-category-patterns.md`; a dispatch board is not a landing page |
| Whitespace has a purpose | Empty areas separate groups or carry a documented reason; no "padding to look modern" |
| Touch targets | ≥ 24×24 CSS px (WCAG 2.5.8); 44×44 recommended for primary mobile actions |

## Colour
| Check | Measure |
|---|---|
| Semantic roles only | Every colour use maps to a role token (background, surface, text, border, brand, status) |
| Text contrast | ≥ 4.5:1 normal, ≥ 3:1 large (WCAG 1.4.3) — measured, recorded in tokens |
| Non-text contrast | ≥ 3:1 for controls, focus rings, chart elements (WCAG 1.4.11) |
| Colour is not the only signal | Status conveyed by icon or text as well (WCAG 1.4.1) |
| Brand colour usage | Brand accent on ≤ ~10% of a typical screen's area; neutrals carry the structure |
| Dark mode (if offered) | Every role has a dark value with contrast re-measured |

## States and interaction
| Check | Measure |
|---|---|
| States matrix complete | No "missing" cell for screens in scope |
| Focus visible | Focus ring token applied; ≥ 3:1 against adjacent colours; not obscured (WCAG 2.4.11) |
| Loading | Skeleton or indicator after 300 ms; no layout jump on completion |
| Errors | Message identifies field and fix (WCAG 3.3.1, 3.3.3); not colour-only |
| Destructive actions | Confirmation or undo; destructive button never the default-focused action |

## Motion
| Check | Measure |
|---|---|
| Purpose | Each animation names the information it conveys (state change, spatial relationship, feedback) |
| Duration | 100–300 ms for UI feedback; ≤ 500 ms for transitions |
| Reduced motion | `prefers-reduced-motion` behaviour specified per animation |

## Content
| Check | Measure |
|---|---|
| No placeholder content | Zero instances of lorem ipsum, fake metrics, invented testimonials, stock-photo people |
| Terminology | Matches PRD glossary; one term per concept |
| Microcopy | Buttons are verbs naming the result ("Save schedule"), not "Submit"/"OK" |

## Implementation review (rendered UI)
| Check | Measure |
|---|---|
| Viewports | Screenshots at 360, 768, 1280 CSS px widths minimum |
| Overflow and wrapping | No horizontal scroll at 320 px (WCAG 1.4.10); long strings wrap or truncate with full text accessible |
| Console | Zero errors on the critical path |
| Fidelity | Rendered values match tokens (spot-check 5 colours, 5 spacings, 3 type sizes with dev tools) |
