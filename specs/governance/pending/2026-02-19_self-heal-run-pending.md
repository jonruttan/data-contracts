---
id: CK-REVIEW-20260219
title: Review-Derived Spec Candidates
priority: P1
---

# Review-Derived Spec Candidates

Source snapshot: `docs/reviews/snapshots/2026-02-19_self-heal-run.md`

## Canonical Candidates

### SELFHEAL-RUN-001

- title: Improve rust governance command failure diagnostics and retry behavior
- type: `contract.check`
- class: `MUST`
- target_area: `runtime.adapter`
- risk: `moderate`
- classification: `behavior`
- acceptance_criteria:
  - governance adapter failures emit deterministic diagnostics with retry context.
  - repeated governance invocations in the same environment complete without transient unexplained exit 137 events.
- affected_paths:
  - `/dc-runner-rust/runner_adapter.sh`
  - `/docs/book/80_troubleshooting.md`
