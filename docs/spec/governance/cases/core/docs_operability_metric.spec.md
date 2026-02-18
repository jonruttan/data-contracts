# Governance Cases

## SRGOV-DOCS-OPER-001

```yaml contract-spec
id: SRGOV-DOCS-OPER-001
title: docs operability metric report generation is valid
purpose: Ensures docs operability report generation and shape are valid.
type: governance.check
check: docs.operability_metric
harness:
  root: .
  docs_operability:
    reference_manifest: /docs/book/reference_manifest.yaml
    policy_evaluate:
    - std.logic.and:
      - std.object.has_key:
        - var: subject
        - summary
      - std.object.has_key:
        - var: subject
        - segments
      - std.object.has_key:
        - std.object.get:
          - var: subject
          - summary
        - overall_docs_operability_ratio
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
      - docs.operability_metric
  target: summary_json
```
