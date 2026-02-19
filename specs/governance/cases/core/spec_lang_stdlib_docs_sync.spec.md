# Governance Cases

## SRGOV-STDLIB-003

```yaml contract-spec
id: SRGOV-STDLIB-003
title: stdlib profile references are synchronized in schema contract and book docs
purpose: Ensures core docs reference the canonical stdlib profile artifacts.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec_lang.stdlib_docs_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
