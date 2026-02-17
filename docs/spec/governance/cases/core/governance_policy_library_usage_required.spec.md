# Governance Cases

## SRGOV-POLICY-LIB-002

```yaml spec-test
id: SRGOV-POLICY-LIB-002
title: governance policy expressions require shared library wiring
purpose: Ensures governance decision policies use shared spec-lang libraries and call exported
  library symbols.
type: governance.check
check: governance.policy_library_usage_required
harness:
  root: .
  policy_library_requirements:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_library_usage_required
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
      - governance.policy_library_usage_required
  target: summary_json
```
