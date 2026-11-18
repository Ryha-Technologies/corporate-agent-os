# Layout principles from human perception and decision research

Each principle below is paired with how to check a real screen against it. Use the check, not the principle name, in audit findings. Names are given so the reader can look up the research; the claims here are the well-replicated core of each, not strong effect-size promises.

| Principle | What it says | How to check a screen | Typical fix |
|---|---|---|---|
| Hick's law | Decision time grows with the number and complexity of choices. | Count the interactive elements visible above the fold and the number of equally weighted calls to action. More than one primary button, or a nav with more than seven top-level items, is a finding. | One primary action per screen; demote the rest to secondary or text links; group nav items. |
| Fitts's law | Time to hit a target depends on its size and distance. | Measure tap targets (minimum 44×44 CSS px for touch, WCAG 2.5.8 says 24×24 at AA) and the distance between a field and its submit control. | Enlarge targets; place actions next to what they act on; put the primary action in the thumb zone on mobile. |
| Gestalt: proximity, similarity, common region, continuity | Things near each other, alike, inside the same boundary, or on the same line are read as related. | Check whether spacing between unrelated groups is larger than spacing inside a group (a 1.5× to 2× ratio reads clearly). Check whether elements that look alike behave alike. | Fix spacing scale before adding borders or cards; remove boxes that are doing the work spacing should do. |
| Visual hierarchy and reading patterns | Eyes land top-left, scan in an F pattern on text-heavy pages and a Z on sparse pages; size, weight, contrast and whitespace signal importance. | Squint test or 10 px blur of a screenshot: can you still tell the order of importance? Does the visual order match the DOM and tab order? | Fewer type sizes with a clear ratio; raise the contrast of the one thing that matters; move the primary action onto the scan path. |
| Progressive disclosure | Show what is needed now; reveal detail on request. | Count the fields and options a first-time user sees before they can do the main task. Forms with more than seven visible fields without grouping are a finding. | Steps, accordions, defaults, "advanced" sections; sensible defaults that most users never change. |
| Recognition over recall | People recognise options faster than they remember them. | Any place the user must remember something from a previous screen (an id, a format, a menu label) is a finding. | Show the value in context; use inline examples and placeholders that disappear only when typing starts. |
| Visibility of system status | People need to know what is happening within about one second. | Click every action and time the feedback. Missing loading, success, and error states are findings. | Instant local state change, skeletons for loads over 300 ms, explicit success and error messages near the action. |
| Error prevention and recovery | Prevent errors first; when they happen, say what went wrong and how to fix it in plain words. | Submit each form empty, with bad data, and with a network failure. Record what the user sees. | Validate inline, keep the user's input, give the fix in the message, make undo possible. |
| Serial position and primacy | First and last items in a list are remembered best. | Where is the most important nav item or feature? Buried in the middle is a finding. | Order lists by importance, not alphabet; put the primary item first and the second most important last. |
| Peak-end and expectation | People judge an experience by its most intense moment and its end. | What is the last thing a user sees after completing the main task? A blank page or a generic toast is a finding. | Design the completion screen; confirm what happened and what to do next. |
| Aesthetic-usability | People judge visually coherent interfaces as easier to use, which buys patience but does not fix broken flows. | Is the coherence real (consistent tokens) or cosmetic (gradients on top of inconsistency)? | Consistency through tokens first; decoration only where it carries meaning. |
| Jakob's law | Users spend most of their time on other sites and expect yours to work the same. | Which conventions are broken (logo not linking home, nav not where expected, non-standard icons)? Each is a finding unless it is deliberate and tested. | Keep conventions for mechanics; be distinctive in content, type, imagery and composition instead. |
| Von Restorff (isolation) effect | The one item that differs from the rest is remembered. | Is anything isolated on purpose? If everything is highlighted, nothing is. Count accent-coloured elements per screen. | Reserve the accent colour and the largest motion for the single element you want remembered. |
| Cognitive load | Working memory holds a few items; every extra concept costs. | Count distinct concepts, labels and icons introduced on the first screen. More than about seven new terms before the first task is a finding. | Cut, defer, or rename to the user's words. |
| Doherty threshold | Response under about 400 ms keeps attention. | Measure interaction latency and LCP. | Optimise, then show progress for anything slower. |

## Distinctiveness without breaking conventions

A layout can be both familiar in mechanics and unmistakably this product's. Decide, per page, the one thing that is deliberately different and write it down:

- **Composition**: asymmetric column widths, a strong vertical rhythm, a single oversized typographic element, a persistent side rail, an editorial two-column layout instead of a centred stack.
- **Type**: a display face with a specific voice paired with a workhorse text face, with a stated scale ratio. Record licences.
- **Imagery**: real product output, real diagrams of the real system, data from the repository, rather than illustrations of abstract people and blobs.
- **Colour**: one accent with a job, a surface palette that carries hierarchy, no gradients unless they encode something.
- **Motion**: see `motion-standards.md`. Three or four considered moments, not an animation on every card.

The swap test (from `skills/ui-ux-design/references/anti-template-review.md`) is the pass criterion: put the page next to three competitors with logos removed. If a stranger cannot pick which is yours, the layout is not finished.

## Measurement checklist for an audit

Record these numbers for the page under audit; they anchor the findings and make the before/after comparison honest.

- Interactive elements above the fold; primary CTAs above the fold.
- Distinct font sizes; distinct spacing values; distinct colours; distinct button styles.
- Smallest tap target (px); largest text block line length (characters per line, 45 to 75 is the readable range).
- Contrast ratio of body, muted and accent text on each surface.
- Steps and seconds for each of the three main tasks, first attempt.
- Count of elements that move on load and on scroll; which honour reduced motion.
- Horizontal overflow at 360 px; reflow at 400 % zoom.
- LCP, CLS, INP or TBT, total transfer, request count.
