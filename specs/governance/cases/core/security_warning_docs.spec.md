# Governance Cases

## SRGOV-DOC-SEC-001

```yaml contract-spec
id: SRGOV-DOC-SEC-001
title: required trust-model docs declare non-sandboxed trusted-input contract
purpose: Ensures required docs state that spec execution is not sandboxed and untrusted specs
  are unsafe.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.security_warning_contract
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
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
    imports:
    - from: artifact
      names:
      - summary_json
      as:
        summary_json: subject
```
