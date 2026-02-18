# Governance Cases

## SRGOV-DOCS-QUAL-003

```yaml contract-spec
id: SRGOV-DOCS-QUAL-003
title: doc token ownership is unique
purpose: Ensures canonical documentation tokens have a single owner page.
type: governance.check
check: docs.token_ownership_unique
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
      - docs.token_ownership_unique
  target: summary_json
```
