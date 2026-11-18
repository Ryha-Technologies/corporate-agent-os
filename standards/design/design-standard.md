# Design standard

Applies to UX research synthesis, IA, flows, visual design, design systems and implemented UI.

| # | Requirement | Verified by |
|---|---|---|
| D1 | IA and flows derive from user goals and the PRD; labels use user language with a research source. | IA document |
| D2 | Every screen has every state in the states matrix specified or marked n/a with reason. | States matrix |
| D3 | A visual direction appropriate to the product category and audience is chosen and justified in the design rationale; the same style is not forced across projects. | Design rationale |
| D4 | Visual hierarchy follows importance; spacing, typography and colour roles are consistent and token-based. | Design QA |
| D5 | Every decorative or structural element has a stated job; fake data, lorem ipsum and invented testimonials are absent from production flows. | Design QA |
| D6 | Responsive behaviour is specified per content breakpoint, including navigation and density changes. | Responsive spec |
| D7 | Motion has purpose, timing and a reduced-motion fallback. | Motion spec |
| D8 | WCAG 2.2 AA is met or a justified alternative is documented and approved. | Accessibility review and test report |
| D9 | Tokens are machine-readable; components list variants, states, content rules and accessibility requirements; the system is as small as the product needs. | Tokens JSON, component spec |
| D10 | The design is compared against the competitor pattern map and template conventions; what is different is written down. | Design rationale, design QA |
| D11 | Implementation review uses rendered UI at representative viewports (overflow, wrapping, focus, contrast, console errors, task completion); mockups are not evidence. | Design QA report |
| D12 | Usability findings come from real sessions with stated sample and bias; simulated users are labelled. | Usability report |

## Category guidance
See `skills/ui-ux-design/references/product-category-patterns.md`.
