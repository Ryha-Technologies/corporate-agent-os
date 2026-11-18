# Creative ideation: how to produce directions that are not the references

Research shows you the category. This file is how you leave it. Without a procedure, "three directions" becomes the same layout in three colours, because the model's default is the average of what it has seen. Every step here produces a written artefact that `design_gate.py` checks.

## 0. The rule
A direction is **derived from the job and a creative lens, never from a reference screenshot**. Reference screenshots are consulted only afterwards, to prove distance. If you catch yourself starting a direction with "like X but…", discard it.

## 1. Extract the raw material (from the job, not from competitors)
Write these before any visual thought:
- **Core verb**: the single action the product does for the person (dispatch, reconcile, remember, warn, teach). One word.
- **Emotional job**: how the person must feel after the main task (relieved, certain, proud, calm, fast). One or two words.
- **Material truth**: what the product is made of that could be shown directly (a route, a ledger, a graph of who reviews whom, a timeline, a map of a floor, a waveform, a queue). Things, not adjectives.
- **The constraint that hurts most**: gloves, sunlight, one hand, 2G, a 60-year-old reader, a 3-second glance, a shared screen. The best designs are built around this.
- **The user's own words** for the main objects (from research or support tickets). Not your words.

## 2. Pick three lenses (one per direction) from different families
Each direction uses one lens. Lenses in the same family produce cousins; pick from three different families.

| Family | Lenses | What it forces |
|---|---|---|
| **Material** | The thing itself (show the real object); the instrument (gauge, meter, dial); the document (form, ticket, ledger, receipt); the map/plan (spatial truth) | Imagery and layout come from the product's own content |
| **Time** | Timeline/stream; before-after; countdown/urgency; calendar/ritual | Layout is organised by sequence, not category |
| **Scale** | One huge thing (a single number, word or object dominates); the inventory (dense, everything visible, the catalogue); the atlas (zoomable overview to detail) | Hierarchy is extreme in one direction |
| **Voice** | The plain-spoken tool (text-first, typographic, almost no UI chrome); the operator console (dense, tabular, keyboard-first); the guide (one question at a time, conversational) | Interaction model and density |
| **Analog source** | A non-digital reference from the research row (a paper ticket, a train departure board, a laboratory notebook, a kitchen order rail, a cockpit checklist) translated structurally, not skinned | Composition borrowed from a system that solved the same job without screens |
| **Inversion** | Reverse the category default (light where all are dark; horizontal where all scroll vertically; no navigation bar where all have one; the detail first and the list second) | Guarantees distance from the pattern map |

Record for each direction: lens, family, and one sentence on why this lens fits the job and the hardest constraint.

## 3. Develop each direction from its lens (not from a screenshot)
For each direction answer in writing, in this order:
1. **First-screen sentence**: what the person sees in the first second, in words, no UI terms ("the next job, its address and the minutes until it starts, nothing else").
2. **The signature**: the one element that only this product would have, derived from the material truth (the route drawn as a strip, the review graph, the ledger rule lines). This is what the swap test will hinge on.
3. **Composition**: columns, dominant element, reading order, density. Sketch it in words and as a low-fi wireframe with real content. No cards unless the content is a card.
4. **Type and colour as expression of the lens**: the instrument lens suggests tabular figures and high-contrast dials; the document lens suggests a text face with rules; the inversion lens suggests the opposite of the pattern map's palette. State the pairing and the ratio.
5. **Motion signature** (one moment that explains the product, from `motion-standards.md`).
6. **The thing this direction gives up**: every real direction costs something. Name it.

## 4. Prove distance (mandatory, in the record)
Fill the **distance table** for each direction against every reference in the category table. Score each cell 0 (same), 1 (similar), 2 (different) on: first-screen structure, navigation model, dominant element, type character, colour model, density, signature element.

| Direction | vs Ref 1 | vs Ref 2 | vs Ref 3 | vs Ref 4 | vs Ref 5 | vs platform default | Min |
|---|---|---|---|---|---|---|---|
| A | 11/14 | ... | | | | | 9 |

A direction whose **minimum** against any reference is under 8/14 is a cousin of that reference: redo it with another lens. The gate checks that the table exists and every direction clears 8.

Then the **sibling check**: score the three directions against each other on the same seven axes. Any pair under 8/14 means two of your directions are the same idea; replace one.

## 5. Push one step further
For the recommended direction, run three provocations and record the answer to each (keep or reject, with a reason):
- **Remove**: take away the most conventional element (the nav bar, the header, the card border, the button). What carries its job now?
- **Exaggerate**: make the signature element three times larger or the only thing on the first screen. Does it still work? Where is the limit?
- **Swap the medium**: how would this screen look as a printed page, a wall display, a voice reply? What does that teach the screen version?

## 6. What is not creativity
Gradients, glassmorphism, 3D blobs, neon glows, parallax, random asymmetry, a trendy font, dark mode. These are surface and the scorer counts them as template. Creativity here means the structure and the signature come from this product's job, and no competitor could have shipped the same screen.

## Output into `research-record.md`
Under `## Directions`: for each direction the lens and family, the first-screen sentence, the signature, the composition, type/colour, motion signature, what it gives up, the departure, the risk; then the distance table, the sibling check, and the provocations for the recommended direction.
