# Governance Cases

## SRGOV-REF-PATHS-001

```yaml contract-spec
id: SRGOV-REF-PATHS-001
title: contract paths referenced by specs exist
purpose: Ensures referenced contract-root paths fail fast when missing.
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
      check: reference.contract_paths_exist
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
          - reference.contract_paths_exist
  target: summary_json
```
