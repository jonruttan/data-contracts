# Governance Cases

## SRGOV-DOCS-LAYOUT-002

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-002
title: docs use index.md as canonical directory index filename
purpose: Enforces index.md-only docs directory index policy.
type: governance.check
check: docs.index_filename_policy
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
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.index_filename_policy
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
