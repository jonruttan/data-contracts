# Governance Cases

## SRGOV-DOCS-GEN-025

```yaml contract-spec
id: SRGOV-DOCS-GEN-025
title: spec lang namespace chapters are present and manifest-synced
purpose: Ensures generated namespace chapter files exist and are listed in the book manifest.
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
      check: docs.reference_namespace_chapters_sync
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
              - docs.reference_namespace_chapters_sync
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - passed
              - true
  target: summary_json
```
