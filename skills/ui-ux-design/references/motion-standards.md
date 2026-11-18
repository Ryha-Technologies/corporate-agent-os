# Motion standards

Motion is information. Each animated moment must answer "what does the user learn from this movement that they would not learn from a cut?" If there is no answer, there is no animation.

## The four legitimate jobs of motion
1. **Continuity**: show where something came from or went (a panel sliding from the control that opened it; a list item leaving where it was).
2. **Feedback**: confirm an input was received (button press state, toggle, successful copy).
3. **Attention**: direct the eye to the one thing that changed (a newly added row, a validation message). At most one attention animation per interaction.
4. **Explanation**: reveal structure or sequence (a diagram drawing its edges in the order data flows; steps appearing in order on a how-it-works section once).

Decoration (parallax backgrounds, floating blobs, perpetual gradients, cards that lift on hover for no reason, text that types itself) is not a job.

## Rules
- **Duration**: 100 to 200 ms for feedback, 200 to 350 ms for continuity and attention, up to 600 ms for a one-time explanation. Nothing loops except a loading indicator.
- **Easing**: ease-out for things entering, ease-in for leaving, ease-in-out for moving between places. Define them once as tokens (`--ease-out: cubic-bezier(0.2, 0, 0, 1)` and so on).
- **Properties**: animate `transform` and `opacity`. Avoid animating layout properties (width, height, top, margin) except via `grid-template-rows` or FLIP techniques; avoid `filter: blur` on large areas.
- **Trigger**: user action, or the element entering the viewport once (`IntersectionObserver`, threshold around 0.2, `once`). No scroll-linked (scrubbed) animation for content; no scroll hijacking; no autoplay media with sound.
- **Interruptible**: a user action during an animation wins; never block input while something animates.
- **Reduced motion**: `@media (prefers-reduced-motion: reduce)` disables transforms and reduces to opacity or instant changes. Test it.
- **Budget**: count animated moments per page. A content page should have fewer than six distinct ones. Write the list in the design notes.
- **Performance**: 60 fps on a mid-range phone; measure with the browser's performance panel, not by eye. No layout thrash; use `will-change` only on elements about to animate and remove it after.
- **Accessibility**: no flashing more than three times per second; nothing essential conveyed by motion alone; focus management after a transition (focus the new panel's heading, return focus on close).

## Choosing moments (do this before writing any CSS)
For the page, list: trigger, element, job (one of the four), property, duration, easing, reduced-motion fallback. Example:

| Trigger | Element | Job | Property | Duration | Fallback |
|---|---|---|---|---|---|
| Page load | Architecture diagram edges | Explanation | stroke-dashoffset | 600 ms, staggered 80 ms | drawn static |
| Copy button press | Button label | Feedback | opacity swap to "Copied" | 150 ms | instant swap |
| Filter input | Non-matching cards | Continuity | opacity + translateY 4px | 200 ms | instant hide |
| Scroll into view, once | Section heading underline | Attention | transform: scaleX | 300 ms | static |

## Review questions
- Remove every animation; what information is lost? That is the list of ones to keep.
- Does any animation make the page feel slower than the static version? Shorten or remove.
- Does the motion vocabulary match the brand voice (precise and quiet for tooling; warmer for consumer)? One vocabulary per product.
