# Guide 08: CI Integration

```yaml doc-meta
doc_id: DOC-GUIDE-208
title: Guide 08 CI Integration
status: active
audience: maintainer
owns_tokens:
- guide_ci_integration
requires_tokens:
- guide_running_checks_and_gates
commands:
- run: ./runners/public/runner_adapter.sh --impl rust critical-gate
  purpose: Reproduce CI required lane behavior locally.
examples:
- id: EX-GUIDE-08-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Align local checks with CI job order and artifact expectations.

## Inputs

- `.github/workflows/ci.yml`
- runner adapter commands
- docs/status artifacts under `.artifacts/`

## Outputs

- local reproduction of CI pass/fail
- reliable mapping from failing CI job to local command

## Failure Modes

- relying on CI-only diagnosis
- missing artifact inspection after job failure
- treating compatibility lanes as merge blockers

## CI Flow

```mermaid
flowchart LR
  A[PR change] --> B[runner-status-ingest]
  B --> C[critical-gate]
  C --> D[governance]
  D --> E[docs/reference checks]
  E --> F[artifacts uploaded]
```

Interpretation:
- ingest artifacts should exist before docs/reference steps.
- required-lane checks are authoritative for merge blocking.
- compatibility telemetry informs governance freshness and visibility.

## Do This Now

```bash
./runners/public/runner_adapter.sh --impl rust critical-gate
./runners/public/runner_adapter.sh --impl rust governance
./runners/public/runner_adapter.sh --impl rust docs-generate-check
```

## How To Verify Success

- [ ] local commands reproduce CI outcomes
- [ ] expected artifacts are present in `.artifacts/`
- [ ] no required-lane failures

## Common Failure Signatures

| Signature | Likely Cause | Action |
| --- | --- | --- |
| CI governance fails, local skipped | local sequence incomplete | run full required sequence locally |
| missing ingest artifacts | ingest stage failed or skipped | inspect `runner-status-ingest-log.json` and rerun |
| docs step red only in CI | manifest/index drift | regenerate docs surfaces and commit |
