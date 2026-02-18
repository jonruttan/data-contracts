# Governance Cases

## SRGOV-DOCS-QUAL-006

```yaml contract-spec
id: SRGOV-DOCS-QUAL-006
title: docs command and example blocks are validated
purpose: Ensures runnable example blocks parse/validate unless explicitly opted out.
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
      check: docs.command_examples_verified
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - docs.command_examples_verified
  target: summary_json
```
