# Governance Cases

## SRGOV-POLICY-REQ-002

```yaml contract-spec
id: SRGOV-POLICY-REQ-002
title: governance checks require structured assertion targets
purpose: Ensures governance cases validate deterministic structured result targets instead
  of relying on PASS text markers as primary contract truth.
type: contract.check
harness:
  root: .
  structured_assertions:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.structured_assertions_required
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: governance.structured_assertions_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - governance.structured_assertions_required
  target: summary_json
```
