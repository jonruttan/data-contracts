# Governance Cases

## SRGOV-RUNTIME-CONFIG-002

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-002
title: python-invoking adapter scripts use shared python-bin resolver helper
purpose: Keeps shared Python resolver helper contract stable for remaining tooling paths.
type: contract.check
harness:
  root: .
  python_bin_resolver:
    helper: scripts/lib/python_bin.sh
    files:
    - scripts/lib/python_bin.sh
    required_tokens:
    - resolve_python_bin() {
    - ${root_dir}/.venv/bin/python
    - ${root_dir}/../../.venv/bin/python
    - python3
    forbidden_tokens: []
  check:
    profile: governance.scan
    config:
      check: runtime.python_bin_resolver_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.python_bin_resolver_sync
```
