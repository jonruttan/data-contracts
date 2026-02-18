# Governance Cases

## SRGOV-DOCS-LAYOUT-002

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-002
title: docs use index.md as canonical directory index filename
purpose: Enforces index.md-only docs directory index policy.
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
      check: docs.index_filename_policy
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
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
  target: summary_json
```
