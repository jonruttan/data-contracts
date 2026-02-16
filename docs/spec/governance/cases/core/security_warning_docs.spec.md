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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.security_warning_contract
```
