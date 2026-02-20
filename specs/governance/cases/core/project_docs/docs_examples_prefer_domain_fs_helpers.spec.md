# docs.examples_prefer_domain_fs_helpers

```yaml contract-spec
id: DCGOV-DOCS-FS-EXAMPLES-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: docs yaml examples prefer domain fs/path helpers over raw ops fs
purpose: Keeps contributor-facing docs examples aligned with the domain-library-first authoring
  model for filesystem/json/glob/path flows.
type: contract.check
harness:
  root: .
  examples_prefer_domain_fs_helpers:
    files:
    - docs/book/60_runner_and_gates.md
    - docs/book/90_reference_guide.md
    - specs/contract/04_harness.md
  check:
    profile: governance.scan
    config:
      check: docs.examples_prefer_domain_fs_helpers
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
