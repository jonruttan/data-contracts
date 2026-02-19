# Governance Cases

## SRGOV-REF-PATHS-001

```yaml contract-spec
id: SRGOV-REF-PATHS-001
title: contract paths referenced by specs exist
purpose: Ensures referenced contract-root paths fail fast when missing.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: reference.contract_paths_exist
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - reference.contract_paths_exist
```
