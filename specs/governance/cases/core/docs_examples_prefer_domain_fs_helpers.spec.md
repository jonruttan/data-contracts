# docs.examples_prefer_domain_fs_helpers

```yaml contract-spec
id: SRGOV-DOCS-FS-EXAMPLES-001
title: docs yaml examples prefer domain fs/path helpers over raw ops fs
purpose: Keeps contributor-facing docs examples aligned with the domain-library-first authoring
  model for filesystem/json/glob/path flows.
type: contract.check
harness:
  root: .
  examples_prefer_domain_fs_helpers:
    files:
    - docs/book/05_howto.md
    - docs/book/07_spec_lang_reference.md
    - specs/contract/04_harness.md
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.examples_prefer_domain_fs_helpers
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```
