```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-JOB-DISPATCH-001
  title: contract.job dispatch must be declared in contract
  purpose: Ensures contract.job cases dispatch jobs via ops.job.dispatch in contract assertions.
  harness:
    root: "."
    check:
      profile: governance.scan
      config:
        check: runtime.contract_job_dispatch_in_contract_required
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
