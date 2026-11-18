# Screens (high-fidelity specification)

Role: ui-designer (T-004/T-005 follow-on). No image renderings were produced in this run; each screen is specified by wireframe reference, tokens and states so an engineer or designer can render it. Realistic content rules: customer first names and areas only; times in 24 h; no invented metrics.

| Screen | Wireframe | Key tokens | States (see matrix) | Notes |
|---|---|---|---|---|
| Today board (desktop) | W1 | `spacing.row-compact`, `color.surface`, status colours | all | Unassigned lane first; attention strip above |
| Today list (phone) | W2 | `spacing.row-comfortable`, `typography.body` | all | Groups collapsible; New job in centre tab |
| Technician picker | W3 | `elevation.2` | loading, empty, populated, selected, error, offline | Conflict warning inline |
| New job | W4 | form tokens | initial, validation error, system error, offline draft, success | Phone field first |
| My jobs (technician) | W5 | `typography.next-job`, `spacing.target-min` | all | Next job enlarged |
| Technician job detail | W6 | large buttons 48 px | all | Primary changes Start → Complete |
| Jobs list, Customer detail, Technician detail, Done, Profile, Login | — | standard list/detail/form tokens | all | Per states matrix |

Sample content used in specs: "14:00–16:00 · Priya K. · Andheri East · AC repair · Assigned" — fictional, labelled sample data; never shown as real in demos (regression case E28).
