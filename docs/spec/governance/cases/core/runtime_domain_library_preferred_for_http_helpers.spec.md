# runtime.domain_library_preferred_for_http_helpers

```yaml spec-test
id: SRGOV-DOMAIN-LIB-HTTP-001
title: api.http context assertions prefer domain http helpers
purpose: Enforces `domain.http.*` helper usage for oauth meta assertions in api.http cases
  instead of raw std.object.get projection chains.
type: governance.check
check: runtime.domain_library_preferred_for_http_helpers
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
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - passed
    - true
  target: summary_json
```
