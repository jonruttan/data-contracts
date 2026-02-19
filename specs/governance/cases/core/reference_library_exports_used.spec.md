# Governance Cases

## SRGOV-REF-SYMBOLS-003

```yaml contract-spec
id: SRGOV-REF-SYMBOLS-003
title: library exports are referenced
purpose: Ensures exported library symbols are referenced by case policies/expressions or harness
  exports.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: reference.library_exports_used
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - reference.library_exports_used
```
