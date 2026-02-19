# Governance Cases

## SRGOV-CONTRACT-002

```yaml contract-spec
id: SRGOV-CONTRACT-002
title: contract must-rule coverage stays complete
purpose: Ensures all MUST policy rules remain covered by traceability evidence and keeps overall
  contract coverage above a minimum baseline.
type: contract.check
harness:
  root: .
  contract_coverage:
    require_all_must_covered: true
    min_coverage_ratio: 0.5
  check:
    profile: governance.scan
    config:
      check: contract.coverage_threshold
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
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
      - contract.coverage_threshold
    imports:
      subject:
        from: artifact
        key: summary_json
```
