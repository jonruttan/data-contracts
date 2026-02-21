```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-OPS-OS-CAP-001
  title: ops.os usage requires explicit capability gate
  purpose: Ensures spec-lang enforces capability.ops_os.required and harness capability parsing.
  harness:
    root: "."
    ops_os_capability:
      path: "/dc-runner-python"
      required_tokens:
      - capability.ops_os.required
      - def capabilities_from_harness
      - ops.os.exec
    check:
      profile: governance.scan
      config:
        check: runtime.ops_os_capability_required
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
```
