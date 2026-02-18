# Governance Cases

## SRGOV-RUNTIME-TRIAGE-011

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-011
title: governance triage selects prefixes from changed paths
type: governance.check
purpose: Ensures triage auto mode derives targeted check prefixes from changed paths before
  fallback prefixes.
check: runtime.governance_prefix_selection_from_changed_paths
harness:
  root: .
  triage_prefix_selection:
    path: /scripts/governance_triage.sh
    required_tokens:
    - collect_changed_paths
    - select_prefixes_from_changed_paths
    - selection_source="changed_paths"
    - CHECK_PREFIXES
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
