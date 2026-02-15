# Governance Cases

## SRGOV-ASSERT-PROFILE-004

```yaml spec-test
id: SRGOV-ASSERT-PROFILE-004
title: domain conformance checks are library-backed
purpose: Ensures domain conformance checks use harness.spec_lang domain libraries rather than ad hoc inline-only policy.
type: governance.check
check: assert.domain_library_usage_required
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
