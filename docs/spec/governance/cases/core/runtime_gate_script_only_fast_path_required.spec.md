# Governance Cases

## SRGOV-RUNTIME-TRIAGE-022

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-022
title: gate script only edits use local fast path skips
type: governance.check
purpose: Ensures local gate scripts include gate-script-only fast path skip/delegation logic.
check: runtime.gate_script_only_fast_path_required
harness:
  root: .
  gate_script_only_fast_path:
    file_token_sets:
    - path: /scripts/local_ci_parity.sh
      required_tokens:
      - is_fast_path_script_only_change
      - paths_all_in_list "scripts/local_ci_parity.sh" "scripts/ci_gate.sh"
      - skip normalize-check (gate-script-only change)
      - skip docs-generate-check (gate-script-only change)
    - path: /scripts/ci_gate.sh
      required_tokens:
      - only_gate_script_changes
      - SPEC_CI_GATE_LOCAL_FAST_PATH
      - CI:-}
      - local fast path
      - local_ci_parity.sh
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
