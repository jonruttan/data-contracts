# Governance Cases

## SRGOV-DOCS-REF-007

```yaml contract-spec
id: SRGOV-DOCS-REF-007
title: docs use canonical make command entrypoints
purpose: Keeps contributor docs aligned on the canonical make-based command entrypoints
  for verification and gate execution.
type: governance.check
check: docs.make_commands_sync
harness:
  root: .
  make_commands:
    files:
    - README.md
    - docs/development.md
    - .github/pull_request_template.md
    required_tokens:
    - make verify-docs
    - make core-check
    - make check
    - make prepush
    - make prepush-fast
    - make ci-cleanroom
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
      - docs.make_commands_sync
  target: summary_json
```
