# Governance Cases

## SRGOV-DOC-SEC-001

```yaml spec-test
id: SRGOV-DOC-SEC-001
title: required trust-model docs declare non-sandboxed trusted-input contract
purpose: Ensures required docs state that spec execution is not sandboxed and untrusted specs
  are unsafe.
type: governance.check
check: docs.security_warning_contract
harness:
  root: .
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
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.security_warning_contract
  target: summary_json
```
