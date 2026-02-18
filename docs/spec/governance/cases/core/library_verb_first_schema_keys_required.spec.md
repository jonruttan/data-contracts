# Governance Cases

## SRGOV-LIB-VERB-001

```yaml contract-spec
id: SRGOV-LIB-VERB-001
title: library schema uses verb-first key names
purpose: Ensures spec_lang.export authoring uses defines.public/defines.private and rejects
  non-canonical definitions keys.
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
      check: library.verb_first_schema_keys_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - std.object.get:
            - {var: subject}
            - check_id
          - library.verb_first_schema_keys_required
  target: summary_json
```
