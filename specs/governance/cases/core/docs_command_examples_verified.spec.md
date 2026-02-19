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
  check:
    profile: governance.scan
    config:
      check: docs.command_examples_verified
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
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
    imports:
      subject:
        from: artifact
        key: summary_json
```
