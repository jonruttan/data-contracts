# runtime.domain_library_preferred_for_fs_ops

```yaml contract-spec
id: SRGOV-DOMAIN-LIB-OPS-FS-001
title: executable specs prefer domain library helpers over raw ops fs symbols
purpose: Enforces domain.path/domain.fs usage in executable specs and allows raw ops.fs usage
  only in stdlib primitive conformance coverage.
type: contract.check
harness:
  root: .
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
      check: runtime.domain_library_preferred_for_fs_ops
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
