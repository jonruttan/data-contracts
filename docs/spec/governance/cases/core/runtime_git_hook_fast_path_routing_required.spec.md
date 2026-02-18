# Governance Cases

## SRGOV-RUNTIME-PREPUSH-006

```yaml spec-test
id: SRGOV-RUNTIME-PREPUSH-006
title: managed pre-push hook contains local fast path routing
purpose: Ensures repository-managed pre-push hook routes check_sets-only and gate-script-only
  edits through the fast local parity path.
type: governance.check
check: runtime.git_hook_fast_path_routing_required
harness:
  root: .
  git_hook_fast_path:
    hook_path: /.githooks/pre-push
    required_tokens:
    - is_check_sets_only_change
    - is_gate_script_only_change
    - docs/spec/governance/check_sets_v1.yaml
    - scripts/local_ci_parity.sh
    - scripts/ci_gate.sh
    - 'fast path: check_sets-only change'
    - 'fast path: gate-script-only change'
    - make prepush
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
