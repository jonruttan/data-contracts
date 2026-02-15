# Governance Cases

## SRGOV-POLICY-LIB-002

```yaml spec-test
id: SRGOV-POLICY-LIB-002
title: governance policy expressions require shared library wiring
purpose: Ensures governance decision policies use shared spec-lang libraries unless an explicit inline-policy reason is documented.
type: governance.check
check: governance.policy_library_usage_required
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_library_requirements:
    cases_path: docs/spec/governance/cases
    case_file_pattern: '*.spec.md'
    ignore_checks:
    - governance.policy_library_usage_required
    require_inline_reason: true
    inline_reason_key: policy_inline_reason
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - governance.policy_library_usage_required
```
