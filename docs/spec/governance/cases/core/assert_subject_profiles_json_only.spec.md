# Governance Cases

## SRGOV-ASSERT-PROFILE-002

```yaml spec-test
id: SRGOV-ASSERT-PROFILE-002
title: evaluator and schema enforce json-core subjects
purpose: Ensures subject profile schema and evaluator enforce JSON-core subject values.
type: governance.check
check: assert.subject_profiles_json_only
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
```
