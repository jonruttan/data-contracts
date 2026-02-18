# Governance Cases

## SRGOV-RUNTIME-CONFIG-005

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-005
title: ci python parity lane is non-blocking telemetry
purpose: Ensures CI keeps Python parity visible without blocking merge lanes.
type: governance.check
check: runtime.ci_python_lane_non_blocking_required
harness:
  root: .
  ci_python_lane_non_blocking:
    workflow: /.github/workflows/ci.yml
    required_tokens:
    - 'python-parity-lane:'
    - 'continue-on-error: true'
    - python scripts/run_governance_specs.py --liveness-level basic
    - python scripts/compare_conformance_parity.py --cases docs/spec/conformance/cases --out
      .artifacts/conformance-parity-python.json
    forbidden_tokens:
    - ./scripts/runner_adapter.sh --impl python
    - Enforce Python parity lane result
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
