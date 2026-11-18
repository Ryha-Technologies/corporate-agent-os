# Product category patterns

What changes between categories, so the same visual style is not forced on every project. Use this to pick a direction and to know which conventions users expect (and therefore should not be broken without reason).

| Category | Primary tasks | Density and hierarchy | Conventions users expect | Common failure |
|---|---|---|---|---|
| SaaS application (B2B workflow) | Repeated daily tasks, data entry, review | Medium-high density; task-first hierarchy; persistent navigation | Tables with sort/filter, saved views, keyboard shortcuts, clear empty states, permissions | Marketing-style hero inside the app; cards hiding data |
| Enterprise software | Complex multi-role workflows, audit, configuration | High density; strong IA; role-based views | Audit trails, bulk actions, export, admin consoles, consistent terminology | Consumer-style minimalism that hides needed controls |
| Admin dashboard / internal tool | Monitoring, triage, configuration | High density; status first; scannable | Real metrics with time ranges and definitions, alert states, drill-down | Decorative charts with fake data; vanity KPIs |
| Marketplace | Search, compare, trust, transact (two sides) | Browse density on listing, focus on detail | Faceted search, trust signals (reviews, verification), clear fees, two-sided dashboards | Treating sellers and buyers identically |
| E-commerce | Find, evaluate, buy, return | Product imagery first; low friction checkout | Cart persistence, shipping/returns clarity, payment trust, accessible product info | Dark patterns, hidden costs |
| Social platform | Create, consume, respond | Feed density; content first; low chrome | Clear privacy controls, reporting, notification control, accessibility of media | Engagement-bait patterns |
| Fintech | Move money, check status, trust | Clarity over density; confirmation and reversibility | Explicit amounts and fees, confirmation steps, statements, security cues, error specificity | Playful styling that undermines trust; ambiguous states |
| Education | Learn, practise, track progress | Focus mode; progress visibility | Clear progress, feedback on practice, accessible content and captions, pacing control | Gamification without learning value |
| Healthcare | Record, review, act under constraint | Legibility, error prevention, interruption tolerance | Patient identification, units, timestamps, consent, privacy, safe defaults | Decorative design over safety; low contrast |
| Mobile application | Short sessions, one-handed, interruptions | Low density per screen; thumb-reachable actions | Platform conventions (iOS/Android), offline behaviour, permission prompts with reasons | Desktop layouts shrunk; permission over-asking |
| Developer tool | Configure, run, debug, read docs | Dense, text-heavy, monospace where relevant | Copyable commands, logs, keyboard focus, dark/light themes, precise errors, fast search | Marketing gloss in docs; hiding errors |
| Marketing website | Understand, trust, convert | Narrative hierarchy; one primary action per section | Specific value statements, proof, pricing clarity, accessible navigation, performance | Generic hero + three cards + testimonials template |
| Landing page (experiment) | Decide in seconds | Single message; single action | Specific headline, honest claim, one CTA, fast load | Stock imagery, vague superlatives, fake urgency |

## Choosing a direction

1. Identify the category and the top three tasks.
2. List the conventions users will expect (keep them unless research says otherwise).
3. From brand personality and audience, pick where the product should feel different: tone, type, colour temperature, density, motion. Write why.
4. Check against the competitor pattern map: the direction should be recognisably not the category default and not any single competitor.
5. Record the decision in `design-rationale.md`.
