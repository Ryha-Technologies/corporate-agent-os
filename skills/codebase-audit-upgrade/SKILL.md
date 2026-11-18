---
name: codebase-audit-upgrade
description: Audit an existing code repository or website for security, UX, UI, branding, accessibility, performance and AI-slop problems, write a prioritised upgrade proposal, stop for the user's approval, then implement the approved items to a professional standard with purposeful motion, distinctive layout and evidence of every check. Use when a user says "audit this repo", "review my site", "improve the UI", "why does this look generic", or asks to upgrade something that already exists.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: design
---
# Codebase audit and approved upgrade
## Purpose
Turn "please look at my existing project" into two separate, gated pieces of work: an evidence-backed audit with a proposal the user can accept or reject line by line, and then an implementation of only the approved items that has to pass the same audit it started from. The two halves are split on purpose. Auditing and rebuilding in one pass is how an agent replaces a user's working product with a generic one.
## When to use
- The repository, site or app already exists and the user asks for an audit, review, redesign, polish, "make it better", or a security or UX check.
- The user complains that something "looks like AI made it", is "generic", "template", or "slop".
- A product is about to go public and nobody has independently looked at it.
Do not use for greenfield builds (use `product-discovery-prd` then `ui-ux-design` and `software-engineering`), or for a single bug fix.
## Preconditions
- Read access to the repository and a way to run it (build, dev server, or static file open). If it cannot be run, say so; a code-only audit is labelled as such.
- A browser or headless renderer for real screenshots at 360, 768 and 1280 px plus keyboard focus states.
- Any brand material the user has (brandbook, logo, tokens). If none exists, note that "branding missing" is itself a finding, not an excuse to invent a brand silently.
- Knowledge of what the product is for and who uses it. Ask one question if unclear; do not assume a persona.
## Inputs
- Repository path or URL; the running product or build command.
- User's stated goals and constraints (stack, budget, must-not-change list, deadline).
- Existing brand assets, design tokens, analytics or support tickets if available.
## Procedure
Research precedes design throughout: no layout, component, logo, deck or motion is produced until the category has been studied, the people understood, and several ideas compared (`references/design-research-method.md`).
### Phase A: audit (read and measure, change nothing)
1. **Inventory.** Record stack, entry points, build and test commands, dependency manifest, hosting, third-party calls, repository size, last commit date. Run the build and tests and record actual output. Everything not run is `NOT_RUN`.
2. **Security audit.** Work through, in order: secrets in the tree or history (`git log -p` grep, `.env` committed); dependency vulnerabilities (`npm audit`, `pip-audit`, or equivalent, with output pasted); auth and session handling; input validation and injection surfaces (SQL, command, template, path); XSS and CSP; CSRF; security headers (CSP, HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy); CORS; file upload handling; rate limiting; logging of personal data; outdated runtime. Map each finding to an OWASP Top 10 or ASVS item and a severity (Critical, High, Medium, Low) with the exact file and line. See `skills/security-privacy/SKILL.md` and `skills/threat-modeling/SKILL.md` for depth.
3. **UX audit.** Walk the top three user tasks end to end as a first-time user and record where you hesitated. Check against the psychology principles in `references/layout-psychology.md`: one primary action per screen (Hick's law), target sizes and reach (Fitts's law), grouping and proximity (Gestalt), progressive disclosure, visible system status, recovery from errors, recognition over recall, reading order matching visual order (F and Z patterns), cognitive load of each form. Record task completion time, steps, dead ends.
4. **UI audit.** Measure, do not opine: type scale (how many sizes, ratio), spacing scale (how many distinct values; more than eight is drift), colour count and contrast (run `skills/design-system/scripts/contrast_check.py` on the real palette), alignment grid, component consistency (how many button styles exist), empty and loading states, responsive behaviour at 360/768/1280 with screenshots, focus visibility, motion (does anything move; does it respect `prefers-reduced-motion`). Run the `visual-design-checklist.md` in `skills/ui-ux-design/references/`.
5. **Branding audit.** Is there a name, mark, voice and palette, and are they used consistently across favicon, title, OG image, 404, emails, README, error states? Does the product look like its category's template (compare against three competitors using the swap test in `anti-template-review.md`)? Record "branding missing" explicitly if there is no identity to be consistent with.
6. **Accessibility and performance.** Run an automated scanner (axe, Lighthouse, pa11y) and paste results; check WCAG 2.2 AA items the scanner cannot (focus order, labels in context, reflow at 400 % zoom). Measure LCP, CLS, INP or TBT, transfer size, request count, and render-blocking resources. Numbers, not adjectives.
7. **AI-slop audit.** Apply `evaluations/originality/slop-patterns.md` and the `originality-audit` skill: identical card grids, three-column feature rows with icons, gradient hero text, stock "trusted by" strips, generic copy that would fit any product, emoji bullets, placeholder stats, fabricated testimonials, default framework styling, unexplained shadows and radii, animations that decorate rather than explain. For each hit, cite the file and line and say what a specific, product-grounded alternative would be.
8. **Content and code quality.** Dead links, placeholder text, console errors, unused dependencies, missing README or licence, test coverage of the paths that matter, duplicated components.
### Phase B: proposal (stop here)
9. **Write `audit-report.md`** with the structure in the Outputs section (`templates/testing/qa-report.md` and `templates/design/design-qa-report.md` cover the UX and security sub-reports). Every finding carries: id, category, severity, evidence (path:line or screenshot name or command output), user impact in one sentence, proposed fix, estimated effort (S/M/L), and whether the fix changes behaviour the user may depend on.
10. **Research before proposing any design.** Follow `references/design-research-method.md` steps 1 to 4 in full and attach the written record: the job statement, the category research table (at least three direct competitors, two adjacent, one non-digital reference, with screenshots and a pattern map of what the category template looks like), the psychology analysis (which principles from `references/layout-psychology.md` apply to this job and the concrete implication of each), and at least three distinct design directions scored in a table against job fit, uniqueness (swap test), psychology, accessibility and cost. This applies to every kind of design: page, screen, component, logo, deck, document, email, motion. A proposal with one direction and no research record is incomplete.
11. **Write `upgrade-proposal.md`.** Group fixes into: Must (security Critical/High, broken flows, legal), Should (UX, accessibility, branding gaps), Could (distinctiveness, motion, polish). For the design track include the research record from step 10 and, for the recommended direction, a **visual direction** (`templates/design/visual-direction.md`): the concept in one sentence, the deliberate departure from the category template, type pairing with licence, palette with contrast ratios, layout described in words plus a low-fidelity wireframe render, and the motion table from `references/motion-standards.md` (trigger, element, job, duration, fallback). Keep the runner-up direction visible so the choice is the user's.
12. **Ask for approval.** Present the proposal and the question set: which groups or items to do, which direction, anything that must not change, and the acceptance check the user will use. Do not begin Phase C until the user answers. Approval of a direction is approval to build that direction, not licence to change scope. If the host runs non-interactively, write the proposal and end the run with status `AWAITING_APPROVAL`.
### Phase C: build (approved items only)
13. **Branch and baseline.** Work on a branch. Capture before screenshots and metrics so the after comparison is honest.
14. **Security first.** Fix approved security items before touching visuals; re-run the scanner and paste output.
15. **Design system before pages.** Create or correct tokens (type scale, spacing scale, colour roles, radii, motion durations and easings) in one file; every page consumes them. Run the contrast script on the final tokens.
16. **Layout from hierarchy, not from a template.** For each page write the one-line job, the single primary action, the order a user should read, and the one element that is deliberately different from the category norm. Build from that. See `references/layout-psychology.md` for the principles and `references/motion-standards.md` for animation rules (purposeful, short, interruptible, reduced-motion honoured, no scroll hijacking, no parallax for decoration).
17. **Copy.** Rewrite generic text with specifics: real numbers, real names, concrete verbs, the user's words. No claims the repository cannot support.
18. **Verify like Phase A.** Repeat steps 2, 4, 6 and 7 on the result. Screenshots at 360/768/1280, keyboard walk, scanner output, performance numbers, contrast table, slop checklist. Put before and after side by side.
19. **Hand over.** `upgrade-report.md` with: what was approved, what was done, what was deferred and why, every check run with output, every `NOT_RUN`, and how to roll back (branch name, commit range). Run `anti-slop-quality-gate` on your own report before submitting.
## Outputs
- `audit-report.md`: inventory; findings table (id, category, severity, evidence, impact, fix, effort, behaviour change); `CHECKS_ACTUALLY_RUN` with pasted outputs; `NOT_RUN` list.
- `upgrade-proposal.md`: Must/Should/Could groups, visual direction(s), approval questions.
- After approval: a branch with commits per group, `upgrade-report.md`, `before/` and `after/` screenshot folders, scanner and metric outputs.
## Quality criteria
- A written research record (job, category table with pattern map, psychology analysis, three scored directions) exists before any design is built; it is attached to the proposal.
- Every finding has a file:line, a screenshot name or a pasted command output. A finding without evidence is removed, not softened.
- The proposal can be accepted or rejected item by item; nothing is bundled so that a user must take a redesign to get a security fix.
- Phase C touches only approved items; unrequested refactors are listed as suggestions, not done.
- After the build, the slop checklist has zero unexplained hits, contrast passes AA, and no horizontal overflow exists at 360 px.
- Motion: every animation names the information it conveys; total animated moments on a page are countable and justified; `prefers-reduced-motion` is honoured.
- Before and after metrics are both real and both shown.
## Failure handling
- Cannot run the project: audit the code, mark every runtime check `NOT_RUN`, say which findings are therefore unconfirmed.
- No brand exists: report it, propose two directions, do not pick one silently.
- User approves "everything": still implement in Must, Should, Could order and stop after each group for a look, because an approval given before seeing results is not an approval of the results.
- Scanner unavailable: use the manual WCAG and OWASP checklists and label the gap.
- The approved direction turns out to conflict with a constraint discovered during the build: stop and ask; do not quietly pick a middle path.
## Safety boundaries
- Never commit to the user's main branch or deploy. Branch, report, let the user merge.
- Never remove or weaken a security control to make a visual change easier.
- Never fabricate scanner results, metrics or screenshots; never crop a screenshot to hide a defect.
- Never rebrand a product without written approval of a specific direction.
- Secrets found during the audit are reported by location only, never copied into the report.
## References
- `references/design-research-method.md` (mandatory research, idea comparison and uniqueness proof for any design)
- `references/layout-psychology.md` (principles and how to measure against them)
- `references/motion-standards.md` (when and how to animate)
- `skills/ui-ux-design/references/visual-design-checklist.md`, `anti-template-review.md`
- `skills/security-privacy/SKILL.md`, `skills/threat-modeling/SKILL.md`, `skills/accessibility-audit/SKILL.md`, `skills/originality-audit/SKILL.md`, `skills/design-system/SKILL.md`
- `evaluations/originality/slop-patterns.md`
- OWASP Top 10 (2021) and ASVS 4.0; WCAG 2.2; Nielsen's ten usability heuristics
