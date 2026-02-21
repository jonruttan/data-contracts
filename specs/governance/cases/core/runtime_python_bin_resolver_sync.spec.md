```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-CONFIG-002
  title: python-invoking adapter scripts use shared python-bin resolver helper
  purpose: Keeps shared Python resolver helper contract stable for remaining tooling paths.
  harness:
    root: "."
    python_bin_resolver:
      helper: scripts/lib/python_bin.sh
      files:
      - scripts/lib/python_bin.sh
      required_tokens:
      - resolve_python_bin() {
      - "${root_dir}/.venv/bin/python"
      - "${root_dir}/../../.venv/bin/python"
      - python3
      forbidden_tokens: []
    check:
      profile: governance.scan
      config:
        check: runtime.compatibility_python_lane_bin_resolver_sync
    use:
    - ref: "/specs/libraries/policy/policy_assertions.spec.md"
      as: lib_policy_core_spec
      symbols:
      - policy.assert.no_violations
      - policy.assert.summary_passed
      - policy.assert.summary_check_id
      - policy.assert.scan_pass
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
    - id: assert_2
      assert:
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - runtime.compatibility_python_lane_bin_resolver_sync
      imports:
      - from: artifact
        names:
        - summary_json
```
