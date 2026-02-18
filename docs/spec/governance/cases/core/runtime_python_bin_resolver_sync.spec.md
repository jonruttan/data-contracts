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
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.python_bin_resolver_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
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
  target: summary_json
```
