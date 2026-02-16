# Governance Cases

## SRGOV-SCHEMA-VERB-001

```yaml spec-test
id: SRGOV-SCHEMA-VERB-001
title: verb-first contract wording remains synchronized
purpose: Ensures schema/contract/current docs use defines wording and reject legacy definitions
  wording.
type: governance.check
check: schema.verb_first_contract_sync
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - schema.verb_first_contract_sync
```
