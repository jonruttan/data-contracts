```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-CERT-005
  title: compatibility lanes remain non-blocking in certification
  purpose: Ensures compatibility lanes are classified and emitted as non-blocking in certification artifacts.
  harness:
    root: "."
    check:
      profile: governance.scan
      config:
        check: runtime.runner_certification_compat_lanes_non_blocking
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
```
