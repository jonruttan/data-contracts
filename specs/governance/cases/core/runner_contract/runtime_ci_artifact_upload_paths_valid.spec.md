```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-TRIAGE-013
  title: ci workflow uploads artifacts from canonical .artifacts path
  purpose: Ensures CI uploads gate and triage artifacts using a recursive .artifacts path.
  harness:
    root: "."
    ci_artifact_upload:
      path: "/.github/workflows/ci.yml"
      required_tokens:
      - actions/upload-artifact@v4
      - ".artifacts/**"
      - 'if: always()'
    check:
      profile: governance.scan
      config:
        check: runtime.ci_artifact_upload_paths_valid
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
```
