# Research record: <product or screen>

Checked by `skills/ui-ux-design/scripts/design_gate.py`. Keep the `##` headings exactly; the gate looks for them. Fill every row with real evidence; the gate counts rows, dates and sources, a reviewer judges the content.

## Job
<Who (the real person and their situation), doing what task, on what device and context, deciding what in the first five seconds and after the main task. At least two sentences. "General users" is rejected.>

## Category research
Captured <YYYY-MM-DD>. Screenshots in `04-design/evidence/references/`.

| Reference | Role | Layout | Type | Colour | Imagery | Motion | Voice (3 sentences) | Does well | Does badly | Source | Captured |
|---|---|---|---|---|---|---|---|---|---|---|---|
| <name> | direct | | | | | | | | | <url or screenshot.png> | <YYYY-MM-DD> |
| <name> | direct | | | | | | | | | | |
| <name> | direct | | | | | | | | | | |
| <name> | adjacent | | | | | | | | | | |
| <name> | adjacent | | | | | | | | | | |
| <name> | non-digital | | | | | | | | | | |

## Pattern map
- **Category template (do not reproduce):** <what every reference does the same>
- **Conventions to keep:** <platform or category mechanics users rely on>
- **Free to change (habit, not convention):** <...>
- **What nobody does and this product truthfully can:** <...>
- **Template-signature score of the existing UI** (if any): `<paste template_signature.py / template_signature_android.py output>`

## Psychology
| Principle | Why it matters for this job | Concrete implication for this design |
|---|---|---|
| <Hick's law> | | |
| <Fitts's law> | | |
| <Gestalt proximity> | | |
| <Peak-end> | | |

## Directions
At least three. Different composition, not recoloured copies.

Follow `skills/ui-ux-design/references/creative-ideation.md`. Directions derive from the job and a lens; never from a reference screenshot. Raw material first:
- Core verb: | Emotional job: | Material truth (things that can be shown): | Hardest constraint: | User's own words:

### Direction A: <name>
- Lens: <lens>, family: <Material | Time | Scale | Voice | Analog source | Inversion> (why it fits the job and the hardest constraint)
- First-screen sentence (no UI terms):
- Signature element (from the material truth; what the swap test hinges on):
- Concept (one sentence):
- Deliberate departure from the category template:
- What this direction gives up:
- Principles it leans on:
- Type pairing (with licence):
- Palette (with contrast ratios):
- Layout in words + wireframe: `04-design/wireframes/A.png`
- Motion table (trigger, element, job, duration, fallback):
- Risk:

### Direction B: <name>
(same fields; different lens family)

### Direction C: <name>
(same fields; third lens family)

### Distance table (0 same, 1 similar, 2 different; seven axes: first-screen structure, navigation, dominant element, type character, colour model, density, signature; max 14)
| Direction | vs <Ref 1> | vs <Ref 2> | vs <Ref 3> | vs <Ref 4> | vs <Ref 5> | vs platform default | Min |
|---|---|---|---|---|---|---|---|
| A | | | | | | | |
| B | | | | | | | |
| C | | | | | | | |
Any Min under 8: redo that direction with another lens.

### Sibling check (same axes, directions against each other)
| Pair | Score /14 |
|---|---|
| A vs B | |
| A vs C | |
| B vs C | |

### Provocations on the recommended direction
- Remove the most conventional element: <what carries its job now; keep/reject and why>
- Exaggerate the signature ×3: <keep/reject and why>
- Swap the medium (print, wall display, voice): <what it taught the screen>

| Criterion | A | B | C |
|---|---|---|---|
| Job fit | | | |
| Uniqueness (swap test) | | | |
| Psychology | | | |
| Accessibility | | | |
| Cost | | | |
| Mobile / small screen | | | |
| **Total** | | | |

Recommendation and what would change it:

## Approved direction
<"Approved by <user> on <YYYY-MM-DD>: Direction <X> with changes: ..." or "AWAITING_APPROVAL">
