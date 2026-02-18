# Governance Cases

## SRGOV-RUNTIME-TRIAGE-020

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-020
title: local prepush has check_sets fast path skips for normalize and docs generate
type: governance.check
purpose: Ensures local prepush avoids normalize and docs generation checks for check_sets-only
  edits.
check: runtime.local_prepush_check_sets_fast_path_required
harness:
  root: .
  local_prepush_check_sets_fast_path:
    path: /scripts/local_ci_parity.sh
    required_tokens:
    - paths_all_in_list "docs/spec/governance/check_sets_v1.yaml"
    - skip normalize-check (check_sets-only change)
    - skip docs-generate-check (check_sets-only change)
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
