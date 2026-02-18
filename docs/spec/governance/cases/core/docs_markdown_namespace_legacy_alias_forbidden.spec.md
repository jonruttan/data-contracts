# docs.markdown_namespace_legacy_alias_forbidden

```yaml spec-test
id: SRGOV-DOCS-MD-002
title: docs forbid legacy markdown alias namespace
purpose: Ensures documentation surfaces use domain.markdown.* and reject legacy md.* references.
type: governance.check
check: docs.markdown_namespace_legacy_alias_forbidden
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - passed
    - true
  target: summary_json
```

