# Governance Cases

## SRGOV-ASSERT-PROFILE-004

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-004
title: domain conformance checks are library-backed
purpose: Ensures domain conformance checks use harness.spec_lang domain libraries rather than
  ad hoc inline-only policy.
type: governance.check
check: assert.domain_library_usage_required
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
