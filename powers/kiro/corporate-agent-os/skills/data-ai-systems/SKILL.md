---
name: data-ai-systems
description: Select, integrate, evaluate and operate data pipelines and AI model features with task definition first, deterministic alternatives considered, representative evaluation sets, data rights and privacy governance, structured outputs, constrained tools, cost and latency controls and monitoring. Use when a feature involves data processing or model calls.
license: MIT
metadata:
  author: Velluraju C
  version: "0.2.0"
  department: data-ai
---
# Data and AI systems

## Purpose
Use models only where they beat deterministic software on the real task, prove it with evaluations, and operate them with guardrails, rights, privacy and cost controls.

## When to use
- Any feature that processes data at scale or calls a model; any vendor or model selection.

## Preconditions
- Task definition with input/output, user value, error cost and acceptable failure modes; data inventory with rights.

## Inputs
- Task definition, representative examples, privacy and residency requirements, latency and cost targets.

## Procedure
1. **Define the task first.** Input, output, value, error cost, required accuracy, latency, volume, privacy, explainability, acceptable failures. Compare deterministic code, search, rules, classic ML and LLMs. Do not use AI because it is available.
2. **Build the evaluation set** before choosing: representative examples plus edge and adversarial cases (prompt injection, out-of-scope, ambiguous), with expected outcomes.
3. **Evaluate candidates** on the actual task: accuracy, robustness, structured-output reliability, tool-calling precision, multilingual behaviour, context limits, privacy and retention terms, regional availability, pricing, throughput, latency, rate limits, versioning, fallback. Public benchmarks count only when their method matches the workload.
4. **Data governance.** Source, owner, rights and licence, consent or legal basis, quality, freshness, schema, retention, access; lineage, validation, deduplication, sensitive-data handling, deletion propagation. No training or retrieval over data without permission.
5. **Architecture.** Schema-validated outputs, constrained tool access, deterministic policy enforcement and authorisation outside the model, timeouts, retries, fallbacks, retrieval filters, tenant isolation, secrets outside prompts, versioned prompts/models/tools/datasets.
6. **Monitoring.** Task success, factuality, citation correctness, refusal correctness, leakage, tool-call precision, consistency, latency, cost; sampled failures for review; drift and provider changes.
7. **Cost control.** Measure billable units by feature, model and tenant (prompt and completion separately where priced so; cache, tools, embeddings, media, retries). Tiered routing, caching, batching and smaller models only when evaluations show acceptable quality. Budgets, quotas, graceful degradation.
8. **Human oversight.** Human review for consequential decisions, uncertain high-impact outputs, regulated domains and external side effects; state limitations to users.

## Outputs
- `05-architecture/ai-design.md`, `07-quality/ai-eval-report.md`, data catalogue entries, cost model inputs, model/prompt version log.

## Quality criteria
- Deterministic alternative considered and the comparison recorded.
- Evaluation set exists with adversarial cases; results reported with method.
- Rights and legal basis recorded for every data source.
- Output validation, tool constraints and authorisation outside the model implemented.
- Cost per unit measured or marked NOT_MEASURED.

## Failure handling
- No representative data → build a small labelled set with the product owner before selection; do not pick on vendor claims.
- Eval shows marginal gains → recommend the deterministic option.

## Safety boundaries
- Model output is untrusted; never grant tools authority the user lacks.
- No training or fine-tuning on data without documented rights.
- Accuracy claims only from the evaluation set, with sample size.

## References
- `templates/engineering/ai-eval-report.md`
- `standards/engineering/engineering-standard.md`, `standards/security/secure-development.md`
- `skills/security-privacy/SKILL.md`
