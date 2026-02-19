# Chapter 70: Governance And Quality

```yaml doc-meta
doc_id: DOC-REF-170
title: Chapter 70 Governance And Quality
status: active
audience: maintainer
owns_tokens:
- governance_triage_workflow
requires_tokens:
- rust_required_lane
commands:
- run: ./runners/public/runner_adapter.sh --impl rust governance
  purpose: Execute governance checks and policy scans.
- run: ./runners/public/runner_adapter.sh --impl rust docs-generate-check
  purpose: Ensure generated docs surfaces are synchronized.
examples:
- id: EX-GOV-QUALITY-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Describe governance enforcement and quality gates for schema/docs/runtime consistency.

## Inputs

- governance cases in `specs/governance/cases/core`
- contract policy and check maps

## Outputs

- deterministic policy enforcement
- traceable check IDs and remediation paths

## Failure Modes

- drift between docs, schema, and runtime behavior
- missing generated artifacts
- stale or misordered reference manifest entries

## Governance Model

- Checks run as executable specs (`contract.check` / `governance.scan`).
- Policies are contract-backed and machine enforced.
- Triage artifacts provide targeted-first failure context.

## Quality Gates

- spec-lang lint/format checks
- docs generation/check synchronization
- governance prefix and broad scans
- CI summary contract output

## Triage Workflow

1. Run targeted governance checks.
2. Regenerate affected docs/artifacts.
3. Re-run lint/format/check gates.
4. Confirm parity in local CI gate path.
