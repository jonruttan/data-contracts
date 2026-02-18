# Governance Cases

## SRGOV-CONF-POLICY-LIB-001

```yaml contract-spec
id: SRGOV-CONF-POLICY-LIB-001
title: conformance governance checks require library-backed policy calls
purpose: Ensures conformance-prefixed governance checks use shared spec-lang library wiring
  and evaluate library calls.
type: contract.check
harness:
  root: .
  conformance_policy_library_requirements:
    cases_path: /specs/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - conformance.library_policy_usage_required
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
      check: conformance.library_policy_usage_required
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
    - conformance.library_policy_usage_required
  target: summary_json
```
