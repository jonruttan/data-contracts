---
id: CK-REVIEW-20260219
title: Review-Derived Spec Candidates
priority: P1
---

# Review-Derived Spec Candidates

Source snapshot: `docs/reviews/snapshots/2026-02-19_personas-run.md`

## Canonical Candidates

### PERSONA-RUN-001

- title: Stabilize rust governance adapter transient-failure diagnostics
- type: `contract.check`
- class: `MUST`
- target_area: `runtime.adapter`
- risk: `moderate`
- classification: `behavior`
- acceptance_criteria:
  - transient adapter failures include deterministic diagnostic context and retry guidance.
  - repeated governance invocations do not fail with unexplained process kills in steady state.
- affected_paths:
  - `/runners/rust/runner_adapter.sh`
  - `/docs/book/80_troubleshooting.md`

### PERSONA-RUN-002

- title: Align adoption persona prompt section headings with canonical snapshot contract
- type: `contract.check`
- class: `MUST`
- target_area: `docs.reviews`
- risk: `low`
- classification: `docs`
- acceptance_criteria:
  - adoption prompt output section list matches review snapshot schema contract exactly.
  - review outputs from persona prompt validate without section-header adaptation.
- affected_paths:
  - `/docs/reviews/prompts/adoption_7_personas.md`
  - `/specs/contract/26_review_output_contract.md`
