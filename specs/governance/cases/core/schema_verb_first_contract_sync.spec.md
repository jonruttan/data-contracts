# Governance Cases

## SRGOV-SCHEMA-VERB-001

```yaml contract-spec
id: SRGOV-SCHEMA-VERB-001
title: verb-first contract wording remains synchronized
purpose: Ensures schema/contract/current docs use defines wording and reject non-canonical
  definitions wording.
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
      check: schema.verb_first_contract_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - schema.verb_first_contract_sync
  target: summary_json
```
