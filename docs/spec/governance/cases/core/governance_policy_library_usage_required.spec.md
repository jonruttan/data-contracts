# Governance Cases

## SRGOV-POLICY-LIB-002

```yaml contract-spec
id: SRGOV-POLICY-LIB-002
title: governance policy expressions require shared library wiring
purpose: Ensures governance decision policies use shared spec-lang libraries and call exported
  library symbols.
type: contract.check
harness:
  root: .
  policy_library_requirements:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_library_usage_required
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
      check: governance.policy_library_usage_required
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
            - governance.policy_library_usage_required
  target: summary_json
```
