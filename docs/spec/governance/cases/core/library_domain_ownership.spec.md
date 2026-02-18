# Governance Cases

## SRGOV-LIB-DOMAIN-001

```yaml contract-spec
id: SRGOV-LIB-DOMAIN-001
title: library paths obey domain ownership
purpose: Ensures conformance cases use conformance libraries and governance cases use policy/path
  libraries.
type: contract.check
harness:
  root: .
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
      check: library.domain_ownership
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - std.object.get:
          - {var: subject}
          - check_id
        - library.domain_ownership
  target: summary_json
```
