# Governance Cases

## SRGOV-DOCS-QUAL-007

```yaml contract-spec
id: SRGOV-DOCS-QUAL-007
title: docs example ids are unique
purpose: Ensures example identifiers are unique across canonical docs metadata.
type: contract.check
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
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
      check: docs.example_id_uniqueness
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
- id: assert_2
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
                - passed
              - true
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - check_id
              - docs.example_id_uniqueness
  target: summary_json
```
