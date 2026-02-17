# runtime.domain_library_preferred_for_fs_ops

```yaml spec-test
id: SRGOV-DOMAIN-LIB-OPS-FS-001
title: executable specs prefer domain library helpers over raw ops fs symbols
purpose: Enforces domain.path/domain.fs usage in executable specs and allows raw ops.fs usage
  only in stdlib primitive conformance coverage.
type: governance.check
check: runtime.domain_library_preferred_for_fs_ops
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
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
