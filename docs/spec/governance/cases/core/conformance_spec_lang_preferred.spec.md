# Governance Cases

## SRGOV-CONF-SPECLANG-001

```yaml contract-spec
id: SRGOV-CONF-SPECLANG-001
title: conformance and governance fixtures require evaluate-only assertions
purpose: Enforces evaluate-only assertion authoring in conformance and governance
  case surfaces.
type: governance.check
check: conformance.spec_lang_preferred
harness:
  root: .
  spec_lang_preferred:
    roots:
    - /docs/spec/conformance/cases
    - /docs/spec/governance/cases
    policy_evaluate:
    - std.logic.eq:
      - std.collection.count:
        - std.collection.filter:
          - fn:
            - - row
            - std.logic.gt:
              - std.collection.count:
                - std.object.get:
                  - var: row
                  - non_evaluate_ops
              - 0
          - var: subject
      - 0
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
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - conformance.spec_lang_preferred
  target: summary_json
```
