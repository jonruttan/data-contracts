# Governance Cases

## DCGOV-RUNTIME-PREPUSH-005

```yaml contract-spec
id: DCGOV-RUNTIME-PREPUSH-005
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: local ci parity entrypoint is documented for contributors
purpose: Ensures contributor docs cover parity-default prepush, fast opt-out, and hook installation.
type: contract.check
harness:
  root: .
  local_ci_parity_docs:
    files:
    - /README.md
    - /docs/development.md
    - /docs/book/60_runner_and_gates.md
    - /docs/book/80_troubleshooting.md
    required_tokens:
    - make prepush
    - make prepush-fast
    - make hooks-install
    - SPEC_PREPUSH_BYPASS=1
  check:
    profile: governance.scan
    config:
      check: runtime.local_ci_parity_entrypoint_documented
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```
