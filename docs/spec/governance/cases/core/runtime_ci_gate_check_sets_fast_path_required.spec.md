# Governance Cases

## SRGOV-RUNTIME-TRIAGE-021

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-021
title: ci gate local fast path skips full gate for check_sets-only edits
type: governance.check
purpose: Ensures ci_gate.sh contains local-only check_sets fast-path delegation to local_ci_parity.
check: runtime.ci_gate_check_sets_fast_path_required
harness:
  root: .
  ci_gate_check_sets_fast_path:
    path: /scripts/ci_gate.sh
    required_tokens:
    - SPEC_CI_GATE_LOCAL_FAST_PATH
    - only_check_sets_changes
    - docs/spec/governance/check_sets_v1.yaml
    - CI:-}
    - scripts/local_ci_parity.sh
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
