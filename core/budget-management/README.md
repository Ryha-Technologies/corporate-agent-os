# Budget management

**Component type:** specification (policy data). No metering code is shipped; hosts expose usage differently and some expose nothing. The policy defines ceilings and what must be logged.

- `budget-policy.yaml` sets per-risk task defaults (model calls, retries, timeouts), parallelism limits, review-loop limits and stop conditions.
- The orchestrator copies the defaults into each task contract's `budget` and `timeout_minutes`, lowering them when the project charter is tighter.
- Actual consumption is recorded in `10-decisions/budget-log.md`. When the host exposes no usage, the entry is `NOT_MEASURED`; the orchestrator never estimates and presents it as measured.
- Fewer agents is the default. Engage a specialist only when a task needs its skills and its output will be reviewed. Role-playing many agents in one context is not delegation and is disclosed as sequential passes.
