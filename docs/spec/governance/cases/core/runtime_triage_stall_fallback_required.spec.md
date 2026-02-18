# Governance Cases

## SRGOV-RUNTIME-TRIAGE-007

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-007
title: triage enforces stall fallback to targeted retries
purpose: Ensures broad governance stall/failure path falls back to targeted retries with explicit
  stalled semantics.
type: governance.check
check: runtime.triage_stall_fallback_required
harness:
  root: .
  triage_stall_fallback:
    path: /scripts/governance_triage.sh
    required_tokens:
    - timeout
    - targeted-governance
    - retry=
    - triage_result
    - stalled
    - broad-governance
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
