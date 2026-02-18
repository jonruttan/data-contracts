# Governance Cases

## SRGOV-LIB-VERB-001

```yaml contract-spec
id: SRGOV-LIB-VERB-001
title: library schema uses verb-first key names
purpose: Ensures spec_lang.export authoring uses defines.public/defines.private and
  rejects legacy definitions keys.
type: governance.check
check: library.verb_first_schema_keys_required
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
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - library.verb_first_schema_keys_required
  target: summary_json
```
