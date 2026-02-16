# Governance Cases

## SRGOV-CONF-POLICY-LIB-001

```yaml spec-test
id: SRGOV-CONF-POLICY-LIB-001
title: conformance governance checks require library-backed policy calls
purpose: Ensures conformance-prefixed governance checks use shared spec-lang library wiring
  and policy_evaluate library calls.
type: governance.check
check: conformance.library_policy_usage_required
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  conformance_policy_library_requirements:
    cases_path: /docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - conformance.library_policy_usage_required
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
      - conformance.library_policy_usage_required
```
