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
  check:
    profile: governance.scan
    config:
      check: docs.example_id_uniqueness
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
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
      - docs.example_id_uniqueness
    imports:
      subject:
        from: artifact
        key: summary_json
```
