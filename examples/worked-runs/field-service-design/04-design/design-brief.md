# Design brief

Role: design-lead (T-001). Reviewed: ux-auditor (ACCEPTED, see task). All user statements are hypotheses unless marked F.

## Category and audience
Category: **operations tool (dense SaaS) with a field-mobile companion** — not a marketing site, not a consumer app. Two roles (A-004):

| Role | Device and context (H) | Expertise | Accessibility considerations |
|---|---|---|---|
| Dispatcher / owner | Phone during the day, laptop in the office; interrupted constantly (A-001, A-008) | Runs the business; not a software specialist | Larger targets on phone; glanceable status; low reading load |
| Technician | Low/mid Android phone, outdoors, one hand, intermittent network (A-003) | Varies; may prefer Hindi or a regional language (A-007) | Sunlight contrast; thumb-reach; offline tolerance; icons always paired with text |

## Top tasks (HYPOTHESIS, to confirm in PRD — Q-001)
Dispatcher: 1. see today's jobs and who is free; 2. assign or reassign a job in under 20 s (A-006); 3. see what is overdue or unconfirmed.
Technician: 1. see my jobs for today in order; 2. mark a job started/completed with notes or a photo; 3. call or navigate to the customer.

## What success looks like
Targets from A-006 are placeholders until a PRD sets them. The design is judged on task completion in usability tests with real dispatchers and technicians (none run yet; K-001).

## Constraints
- Mobile web first (A-008); must work at 360 px width; dispatcher board has a desktop layout from 1024 px.
- Personal data on screen (F-002): minimise what is shown in lists; no customer phone number on the technician list until the job is opened.
- No brand (F-003): neutral tokens; the visual direction expresses function and the audience, not a brand personality yet (Q-002).
- Accessibility target: WCAG 2.2 AA (default).
- Text expansion: Hindi strings can be ~30–40% longer than English; layouts must not truncate labels (A-007).

## Visual-direction hypothesis
Plain, high-contrast, dense where the dispatcher needs density and spacious where the technician needs one-handed speed. Colour used almost only for job status. No illustration, no decorative imagery. See `visual-direction.md`.

## Known gaps carried into this run
Q-001 no PRD · Q-002 no brandbook · Q-003 no competitor pattern map (differentiation cannot be assessed) · K-001 no customer research.
