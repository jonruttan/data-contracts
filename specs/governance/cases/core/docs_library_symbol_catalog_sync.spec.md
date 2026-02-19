# Governance Cases

## SRGOV-DOCS-LIBSYM-004

```yaml contract-spec
id: SRGOV-DOCS-LIBSYM-004
title: library symbol catalog artifacts are synchronized
purpose: Ensures generated library symbol catalog and markdown references are up-to-date.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.library_symbol_catalog_sync
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
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.library_symbol_catalog_sync
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    imports:
      subject:
        from: artifact
        key: summary_json
```
