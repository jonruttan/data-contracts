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
    cases_path: /specs/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_library_usage_required
  check:
    profile: governance.scan
    config:
      check: governance.policy_library_usage_required
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
      key: violation_count
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
      - governance.policy_library_usage_required
    imports:
      subject:
        from: artifact
        key: summary_json
```
