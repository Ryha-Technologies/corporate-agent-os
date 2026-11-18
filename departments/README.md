# Departments and roles

**Component type:** specification (canonical YAML) → rendered documentation in `docs/organization/`.

Each `departments/<id>/roles.yaml` defines one department and its roles with the fifteen fields required by the operating model:

mission · scope · activities · inputs · outputs · decides · needs_approval · collaborates_with · reports_to · kpis · quality · tools · failure_modes · ai_autonomy · human_approval

The `department.startup_stage` field says how the roles collapse in a small company (who holds them when there are two to five people) so the model never forces an enterprise org chart onto a startup. `department.agents` lists the agents under `agents/` that operate in this department.

| Department id | Function group (brief §4) |
|---|---|
| executive | Executive leadership |
| research, ux-research, data-ai | Research and intelligence |
| strategy, product, finance | Business and product strategy |
| branding, naming-ip | Branding and creative |
| design | Product experience and design |
| architecture, engineering, infrastructure | Technology and engineering |
| qa, cybersecurity | Quality and security |
| marketing, sales, customer-success | Growth and revenue |
| legal, people, procurement, operations | Corporate support functions |

Render: `python scripts/package/render_roles.py` → `docs/organization/<department>.md` and `docs/organization/README.md`.
Validate: `python scripts/validate/validate_departments.py`.
