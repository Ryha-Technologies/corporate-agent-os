# Golden tasks (benchmarks A–E)

Five end-to-end benchmarks matching brief §16. Each YAML file defines the input a rater gives the system, the workflow to run, the evidence expected in the project workspace, the dimensions to score and the rubric to use. The inputs are deliberately realistic and under-specified so the system must do discovery rather than pattern-match.

| Id | Benchmark | Workflow | Rubrics |
|---|---|---|---|
| A | Business opportunity from a rough idea | business-validation | research, business, behaviour |
| B | New brand for a described product and audience | brand-development | brand, behaviour |
| C | SaaS product from idea to implementation slice | idea-to-business → software-development | business, design, engineering, security |
| D | Existing application improvement | product-maintenance | design, engineering, security |
| E | Product launch | product-launch | brand, business, behaviour |

Scores are produced by independent human raters (or a model that did not perform the task) and recorded in `benchmark-reports/`. `human_review_required: true` on every task is a reminder that model output is not self-certifying.
