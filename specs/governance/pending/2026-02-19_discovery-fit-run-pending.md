---
id: CK-REVIEW-20260219
title: Review-Derived Spec Candidates
priority: P1
---

# Review-Derived Spec Candidates

Source snapshot: `docs/reviews/snapshots/2026-02-19_discovery-fit-run.md`

## Canonical Candidates

### DISCOVERY-RUN-001

- title: Standardize explicit rust impl flags in development command examples
- type: `contract.check`
- class: `MUST`
- target_area: `docs.development`
- risk: `low`
- classification: `docs`
- acceptance_criteria:
  - docs/development required-lane commands consistently use `./runners/public/runner_adapter.sh --impl rust ...`.
- affected_paths:
  - `/docs/development.md`
  - `/specs/governance/cases/core/docs_make_commands_sync.spec.md`

### DISCOVERY-RUN-002

- title: Add discovery snapshot quality checklist before pending conversion
- type: `contract.check`
- class: `MUST`
- target_area: `docs.reviews`
- risk: `low`
- classification: `docs`
- acceptance_criteria:
  - docs/reviews README documents required synthesis completeness before review_to_pending.
- affected_paths:
  - `/docs/reviews/README.md`
  - `/specs/governance/cases/core/docs_reviews_discovery_workflow_sync.spec.md`

### DISCOVERY-RUN-003

- title: Enrich discovery fixture with realistic non-blocking concern
- type: `contract.check`
- class: `MAY`
- target_area: `docs.reviews`
- risk: `low`
- classification: `docs`
- acceptance_criteria:
  - discovery example snapshot includes at least one non-blocking risk and corresponding candidate.
- affected_paths:
  - `/docs/reviews/snapshots/2026-02-19_discovery_fit_example.md`
