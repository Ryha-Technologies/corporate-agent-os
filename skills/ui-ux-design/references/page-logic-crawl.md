# Page-logic crawl: think through a product page by page, element by element

Used in audits (`codebase-audit-upgrade`, `product-overhaul-orchestrator`) and before any redesign. The crawl is systematic so nothing is judged by impression: every page, every element on it, every transition out of it, every state it can be in. The output is a map and a decision per element: keep, change, merge, remove, add.

## 1. Build the map (the spider)
Starting from the entry points (home, deep links, app launch, notifications, emails that link in), follow every link, button, tab, gesture and redirect until no new page or state appears. Record in `page-map.md`:

| Page / screen | Route or file | Reached from | Leads to | Job (one sentence) | Primary action | States seen | Owner module |
|---|---|---|---|---|---|---|---|

Also record: orphan pages (no inbound path), dead ends (no onward path except back), loops, duplicate pages that do the same job, pages reachable only by URL, and every page that needs a login or permission. For apps, include system entry points (share sheet, widget, notification tap, deep link) and the back-stack behaviour from each.

## 2. Per page: the logic questions
Answer in writing for each page before touching its design.
1. **Job.** What must the person know, feel or do here? If the answer has two jobs, the page probably wants to be two pages or one job is a distraction.
2. **Arrival.** Where do they come from and what do they already know? Does the page repeat what the previous one said (waste) or assume something it never said (gap)?
3. **Primary action.** Exactly one. Is it the largest, highest-contrast, most reachable control? What happens in the 300 ms after it is pressed?
4. **Reading order.** Write the order the eye should move. Compare to the DOM/tab order and to what the layout actually emphasises (squint test on a screenshot).
5. **Exit.** Where do they go next on success, on failure, on cancel? Is each exit visible without searching?
6. **Data truth.** For every number, label and status shown: where does it come from, how fresh is it, what does the user do with it? A figure the user cannot act on is a candidate for removal.
7. **States.** First visit, loading, empty, partial, full, error, offline, no permission, expired, success, destructive-confirm. Which exist, which are missing, which are the same screen with a different message.
8. **Logic defects.** Buttons that do nothing or do the same thing as another; conditions that cannot occur; validation that fires after the user could have been warned; order of fields that does not match how the person thinks; steps that could be defaulted or inferred; data asked for twice.

## 3. Per element: the keep/change/remove table
For every visible element on the page (every button, link, label, icon, image, divider, badge, card, number, input, animation):

| Element | Job for the user | Evidence it is used or needed | Psychology (which principle it serves or breaks) | Decision | Why |
|---|---|---|---|---|---|

Decision rules:
- **Remove** if no user job can be written for it, if it duplicates another element, if it is decoration without information (gradient, glow, shadow, icon tile, eyebrow label, numbered marker on a non-sequence), or if its only job is to make the page look fuller.
- **Merge** if two elements serve one job.
- **Change** if the job is real but the element is the wrong control, wrong size, wrong place, wrong words, wrong state coverage, or breaks a principle (three equal CTAs: Hick's law; 20 px target: Fitts; related items far apart: proximity).
- **Keep** only with the job and evidence written.
- **Add** where a job in step 2 has no element serving it (the missing empty state, the missing exit, the missing confirmation).

Then the detail pass on what is kept or changed, each with a stated reason:
- **Colour**: role (text, surface, accent, status), contrast ratio, is the accent reserved for the one thing to remember on this page?
- **Type**: size on the scale, weight, line length, does the hierarchy match the reading order?
- **Spacing**: which step of the scale, does proximity group the right things, is the gap between groups larger than within?
- **Shape and border**: does the radius or border say anything (grouping, interactivity) or is it a default?
- **Words**: the user's vocabulary, verb-first labels on actions, no formula headlines, no slop words (`slop-mechanics.md` §2).
- **Motion**: job (feedback, continuity, attention, explanation), duration, reduced-motion fallback, or none.
- **Accessibility**: name, role, state, focus order, target size.

## 4. Cross-page pass
- Consistency: same job, same control, same words everywhere (one term per concept).
- Navigation model: does the structure match the top tasks (from research) or the org chart of the codebase?
- Redundancy: pages or sections that repeat each other; merge or remove.
- Missing: the task flows from research that have no path, or a path with a gap.
- Rebranding sweep (when applicable): every place the old name, mark, colour, voice or domain appears, including favicons, OG images, 404s, emails, store listings, legal text, repository metadata.

## 5. Output
`page-map.md`, `page-logic.md` (per-page answers), `element-decisions.md` (tables), and a summary of counts: pages kept / merged / removed / added; elements removed; defects found. These feed the proposal. Nothing is removed or rebuilt before the owner approves the proposal; the crawl is analysis.
