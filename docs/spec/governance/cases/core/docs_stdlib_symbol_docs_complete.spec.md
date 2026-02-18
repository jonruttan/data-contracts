# Governance Cases

## SRGOV-DOCS-GEN-021

```yaml contract-spec
id: SRGOV-DOCS-GEN-021
title: stdlib symbols include semantic docs payload
purpose: Ensures every stdlib symbol has summary, params, returns, errors, and examples in
  generated catalogs.
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
      check: docs.stdlib_symbol_docs_complete
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            MUST:
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - check_id
              - docs.stdlib_symbol_docs_complete
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - passed
              - true
  target: summary_json
```
