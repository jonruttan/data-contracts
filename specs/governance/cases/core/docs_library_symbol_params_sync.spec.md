# Governance Cases

## SRGOV-DOCS-LIBSYM-002

```yaml contract-spec
id: SRGOV-DOCS-LIBSYM-002
title: library symbol doc params stay in sync
purpose: Ensures harness.exports params match doc.params names and order.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.library_symbol_params_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.library_symbol_params_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
