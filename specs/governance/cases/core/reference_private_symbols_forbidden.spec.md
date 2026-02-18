# Governance Cases

## SRGOV-REF-SYMBOLS-004

```yaml contract-spec
id: SRGOV-REF-SYMBOLS-004
title: private library symbols are not referenced externally
purpose: Ensures conformance/governance/impl cases do not reference defines.private symbols
  from library docs.
type: contract.check
harness:
  root: .
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
      check: reference.private_symbols_forbidden
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - reference.private_symbols_forbidden
  target: summary_json
```
