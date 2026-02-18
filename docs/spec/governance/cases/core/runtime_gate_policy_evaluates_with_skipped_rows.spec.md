# Governance Cases

## SRGOV-RUNTIME-FAILFAST-004

```yaml spec-test
id: SRGOV-RUNTIME-FAILFAST-004
title: gate policy evaluation treats skipped rows as non-pass
purpose: Ensures fail-fast skipped rows stay in policy subject and preserve failing verdict
  semantics.
type: governance.check
check: runtime.gate_policy_evaluates_with_skipped_rows
harness:
  root: .
  gate_policy_skipped_rows:
    files:
    - /scripts/ci_gate_summary.py
    required_tokens:
    - _evaluate_gate_policy
    - all(str(row.get("status", "")) == "pass"
    - status
    - pass
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
