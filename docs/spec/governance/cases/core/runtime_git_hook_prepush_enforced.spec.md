# Governance Cases

## SRGOV-RUNTIME-PREPUSH-003

```yaml spec-test
id: SRGOV-RUNTIME-PREPUSH-003
title: managed pre-push hook enforces local parity gate
purpose: Ensures repository-managed pre-push hook exists and is installable via canonical
  script.
type: governance.check
check: runtime.git_hook_prepush_enforced
harness:
  root: .
  git_hook_prepush:
    hook_path: /.githooks/pre-push
    install_script: /scripts/install_git_hooks.sh
    makefile_path: /Makefile
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
    - var: subject
    - 0
  target: violation_count
```
