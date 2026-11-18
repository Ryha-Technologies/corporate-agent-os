# Research-first design method (applies to any design artefact)

Use this for a website, app screen, dashboard, logo, deck, document layout, email, poster, README, component library or motion piece. Nothing is designed before steps 1 to 4 are written down. The written record is the proof; a design without it is treated as a template guess and rejected at review.

The record is written to `04-design/research-record.md` (template: `templates/design/research-record.md`) and checked by `scripts/design_gate.py`; the build phase of every design skill is blocked while the gate is closed. Mobile apps: also read `mobile-android-patterns.md`; the platform default (Material 3 / HIG) is part of the category template.

## 1. Understand before anything else
- **The job.** One sentence: who uses this, to do what, in what situation, with what going on around them. If the answer is "general users", stop and ask.
- **The decision the design must support.** What should a person know, feel or do within the first five seconds, and after the main task?
- **Constraints.** Stack, brand assets, legal, accessibility level, performance budget, deadline, what must not change.
- **Existing evidence.** Analytics, support tickets, reviews, previous audits, interviews. Record access dates. Where none exists, write "no user evidence; findings below are expert review, confidence medium".

## 2. Research the category (minimum effort: three direct competitors, two adjacent categories, one non-digital reference)
For each reference capture screenshots at the same widths and record, in a table:
- Layout structure (columns, hero type, nav pattern, density).
- Type (families, number of sizes, weight contrast).
- Colour (count, accent use, surface model, light/dark).
- Imagery (illustration style, photography, product shots, diagrams, none).
- Motion (what moves, on what trigger, how long).
- Copy voice (three representative sentences).
- One thing each does well and one thing each does badly for the job in step 1.
Then write the **pattern map**: what everyone does the same (the category template), what is required by convention (keep), and what is simply habit (free to change). The category template is what the design must not reproduce. Sources: `skills/competitive-analysis/SKILL.md`, `product-category-patterns.md`.

## 3. Research the people
Pick the principles in `layout-psychology.md` that matter for this job and say why. For each, write the concrete implication for this design (for example: "Users arrive from a CLI error message; the primary action is 'copy the install command'; by Hick's law the hero carries one action and the nav shrinks to three items"). Add domain reading where the design is specialised: reading research for long-form text, data-visualisation research for dashboards, wayfinding for navigation-heavy products, trust and credibility research for anything that asks for money or data. Cite the source, not a vague "studies show".

## 4. Generate and compare ideas (never build the first idea)
Use `creative-ideation.md`: extract the raw material from the job, pick three lenses from three different families, develop each from its lens (never from a reference screenshot), prove distance from every reference and from each other with the scored tables, then push the recommended one with the three provocations.
- Produce at least three distinct directions. Distinct means different composition, not the same layout with a different accent colour.
- For each: the concept in one sentence; the one deliberate departure from the category template; the psychology it leans on; a low-fidelity sketch or wireframe render; a risk.
- Score each against the job in step 1, the pattern map (uniqueness: run the swap test from `anti-template-review.md`), the psychology implications, accessibility, and build cost. Use a table; show the scores.
- Recommend one, keep the runner-up, and say what would make you change your mind. Present the comparison to the user for approval. Do not merge directions into a compromise.

## 5. Build the approved direction from a system, not from pieces
- Tokens first: type scale with its ratio, spacing scale, colour roles with contrast ratios, radii, borders, elevation (if any), motion durations and easings (`motion-standards.md`).
- Per screen or artefact: job, primary action, reading order, the deliberate departure, the elements that may animate and why. Written before layout.
- Copy written for the real product with real numbers; no filler sentences, no claims the evidence does not support.
- Real content at real lengths in every state (empty, loading, error, long text, RTL if applicable).

## 6. Prove uniqueness and quality
- **Swap test** with three competitors, logos removed; record who could tell and how.
- **Slop checklist** (`evaluations/originality/slop-patterns.md`): every hit either removed or justified in writing.
- **Psychology check**: for each principle chosen in step 3, show the screen element that implements it.
- **Measurements** from `layout-psychology.md` (counts, contrast, targets, overflow, performance) before and after.
- **Accessibility**: scanner output plus manual WCAG 2.2 AA items.
- **Independent review** by `design-qa-auditor` or `ux-auditor`; the maker does not sign off alone.

## What counts as templated (reject)
A default framework look with colours changed; a hero with centred headline, subhead and two buttons over a gradient; three feature cards with icons; a "trusted by" logo strip with no logos; cards for everything; identical section rhythm down the page; stock illustrations of people at laptops; motion on every element; copy that would fit a different product with the name swapped. Any of these may still be used if step 4 shows it is the best choice for the job and the written justification survives review. Habit is not a justification.
