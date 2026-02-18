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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: contract.coverage_threshold
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
