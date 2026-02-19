# Guide 02: First Spec Authoring

```yaml doc-meta
doc_id: DOC-GUIDE-202
title: Guide 02 First Spec Authoring
status: active
audience: author
owns_tokens:
- guide_first_spec_authoring
requires_tokens:
- guide_onboarding_flow
commands:
- run: ./runners/public/runner_adapter.sh --impl rust critical-gate
  purpose: Validate your first spec authoring changes end-to-end.
examples:
- id: EX-GUIDE-02-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Author a valid executable `.spec.md` case using the canonical contract shape.

## Inputs

- writable path under `specs/`
- case model rules from chapter 20
- assertion model rules from chapter 30

## Outputs

- new executable `*.spec.md` case
- passing `critical-gate` for authored change

## Failure Modes

- invalid `contract` mapping shape
- implicit imports or missing artifact imports
- missing domain index updates if required by local policy

## Do This Now

```bash
cat > specs/conformance/cases/core/example_minimal_check.spec.md <<'SPEC'
# Example Minimal Check

```yaml contract-spec
id: EX-CONF-GUIDE-001
title: example minimal check
purpose: Ensure a minimal check shape is valid.
type: contract.check
harness:
  check:
    profile: governance.scan
    config:
      check: docs.reference_manifest_sync
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names: [violation_count]
  steps:
  - id: assert_no_violations
    assert:
      std.logic.eq:
      - {var: violation_count}
      - 0
```
SPEC
./runners/public/runner_adapter.sh --impl rust critical-gate
```

## How To Verify Success

- [ ] new case parses and executes
- [ ] no schema violations reported
- [ ] `critical-gate` exits 0

## Common Failure Signatures

| Signature | Likely Cause | Action |
| --- | --- | --- |
| `contract.imports required` | imports omitted | add explicit `imports` entries for referenced vars |
| `type contract.check expected` | wrong top-level type | set `type: contract.check` |
| invalid fenced block parse | malformed YAML indentation | fix indentation and list syntax |
