# Governance Cases

## SRGOV-DOCS-LAYOUT-002

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-002
title: docs use index.md as canonical directory index filename
purpose: Enforces index.md-only docs directory index policy.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.index_filename_policy
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
    as:
      summary_json: subject
  steps:
  - id: assert_1
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.index_filename_policy
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
