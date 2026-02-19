# Guide 05: Release and Change Control

```yaml doc-meta
doc_id: DOC-GUIDE-205
title: Guide 05 Release and Change Control
status: active
audience: maintainer
owns_tokens:
- guide_release_change_control
requires_tokens:
- guide_running_checks_and_gates
commands:
- run: ./scripts/control_plane.sh critical-gate
  purpose: Ensure release candidate is gate clean.
examples:
- id: EX-GUIDE-05-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Define merge/release expectations for spec changes in a contract-first repo.

## Inputs

- finalized change diff
- passing required lane checks
- synchronized docs and manifest outputs

## Outputs

- release-ready change set
- clear traceability from narrative to contract updates

## Failure Modes

- releasing with stale generated surfaces
- changing policy/contract without updating docs mapping
- merging without required-lane green status

## Do This Now

```bash
./scripts/control_plane.sh critical-gate
./scripts/control_plane.sh governance
./scripts/control_plane.sh docs-generate-check
git status --short
```

## How To Verify Success

- [ ] all required lane checks pass
- [ ] no unexpected dirty files
- [ ] manifest and reference index are synchronized

## Common Failure Signatures

| Signature | Likely Cause | Action |
| --- | --- | --- |
| release PR blocked by governance | missing contract/doc alignment | update affected contracts/docs and rerun governance |
| generated refs changed unexpectedly | prior drift discovered late | include regenerated refs in same change |
| unresolved traceability | policy rule references outdated | update traceability/policy ids consistently |
