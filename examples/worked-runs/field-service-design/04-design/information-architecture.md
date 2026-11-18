# Information architecture

Role: ux-designer (T-002). Reviewed: ux-auditor (ACCEPTED).

## User goals and top tasks
| Role | Task | Frequency (H) | Importance |
|---|---|---|---|
| Dispatcher | Assign / reassign a job | many per day | critical |
| Dispatcher | See who is free, late or overdue | continuous | critical |
| Dispatcher | Create a job from a customer call or WhatsApp message | several per day | high |
| Dispatcher | Review completed jobs and notes for billing | daily | medium |
| Technician | See today's jobs in order | several per day | critical |
| Technician | Mark started / completed, add note or photo | per job | critical |
| Technician | Call or navigate to customer | per job | high |
| Owner | Change technicians, service types, working hours | rare | low |

## Content model
| Entity | Key attributes | Relationships | Lifecycle states |
|---|---|---|---|
| Job | customer, address, service type, scheduled window, assigned technician, status, notes, photos, created-from (call / WhatsApp / manual) | belongs to Customer; assigned to Technician | unassigned → assigned → confirmed → en route → started → completed / cancelled / no-answer |
| Customer | name, phone, addresses, past jobs | has Jobs | active / archived |
| Technician | name, phone, skills (service types), working hours, status (available / on job / off) | has Jobs | active / inactive |
| Service type | name, default duration | used by Jobs | active / inactive |

The "things" users talk about: **jobs**, **technicians**, **customers**. Navigation is built on those three words; "tickets", "work orders" and "resources" are not used (jargon flag).

## Navigation
Dispatcher (desktop and phone): **Today** (board / list) · **Jobs** (all, filters) · **Customers** · **Technicians** · **Settings**. Global action: **New job** (always visible).
Technician (phone): **My jobs** (today, default) · **Done** (recent completed) · **Profile** (language, availability). No settings beyond that.

Depth: ≤ 2 levels. Labels tested with real dispatchers: NOT_RUN (planned tree test, see K-001).

## Page types
| Page type | Purpose | Primary action | Template |
|---|---|---|---|
| Today board (desktop) | See all technicians and today's jobs by time | Assign (drag or select) | board |
| Today list (phone, dispatcher) | Same, scannable on phone | Assign from job row | list |
| Job detail | Everything about one job; status actions | Context-dependent status action | detail |
| New job form | Capture a job fast | Save job | form |
| Jobs list | Find and filter jobs | Open job | list |
| Customer detail | Addresses, history | New job for customer | detail |
| Technician detail | Skills, hours, today's load | Edit | detail |
| My jobs (technician) | Today's ordered list | Open job | list |
| Technician job detail | Call, navigate, start, complete, note, photo | Start / Complete | detail |

## Task flows
See `user-flows.md`.

## Interaction models
- Assign: select job → choose technician from a list showing current load and distance-free availability → confirm. Drag-and-drop on desktop is an accelerator with the same select-based alternative (WCAG 2.5.7).
- Status changes: single tap on a large button; destructive or irreversible changes (cancel job) confirm; completion can be undone for 10 minutes.
- Search and filter: jobs by status, date, technician, customer phone.
- Bulk actions: none in v1 (X-002, keeps the board simple).

## States per page type
See `states-matrix.md`.

## Responsive behaviour
| Breakpoint | Dispatcher navigation | Hierarchy | Deprioritised |
|---|---|---|---|
| ≥ 1024 px | Left rail with labels | Board: technician rows × time columns | — |
| 768–1023 px | Top tabs | Board collapses to per-technician lists side by side (2 columns) | Time axis |
| < 768 px | Bottom tabs (Today, Jobs, New job, More) | Single list grouped by technician, status chips first | Customers and Technicians move under More |
Technician UI is single-column at all widths.

## Validation
Tree test and label test: NOT_RUN. Flows walked by ux-auditor as each role (T-002 review).
