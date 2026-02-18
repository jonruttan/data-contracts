# Governance Cases

## SRGOV-DOCS-QUAL-005

```yaml contract-spec
id: SRGOV-DOCS-QUAL-005
title: instruction pages contain required operational sections
purpose: Ensures docs metadata required sections are present in canonical chapter content.
type: governance.check
check: docs.instructions_complete
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
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
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.instructions_complete
  target: summary_json
```
