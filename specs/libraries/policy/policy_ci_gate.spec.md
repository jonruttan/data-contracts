```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
contracts:
  - id: LIB-POLICY-CI-001
    type: contract.export
    title: ci gate predicates
    clauses:
      defaults: {}
      predicates:
        - id: __export__policy.ci.required_profiles_pass
          assert:
            std.logic.eq:
              - std.object.get:
                  - std.object.get:
                      - {var: subject}
                      - gate_summary
                  - status
              - pass
        - id: __export__policy.ci.optional_profile_report_only
          assert:
            std.logic.eq:
              - std.object.get:
                  - std.object.get:
                      - {var: subject}
                      - optional_report
                  - status
              - report-only
        - id: __export__policy.ci.artifacts_present
          assert:
            std.logic.and:
              - std.object.has:
                  - {var: subject}
                  - gate_summary
              - std.object.has:
                  - {var: subject}
                  - optional_report
    harness:
      exports:
        - as: policy.ci.required_profiles_pass
          from: assert.function
          path: /__export__policy.ci.required_profiles_pass
          params: [subject]
          required: true
        - as: policy.ci.optional_profile_report_only
          from: assert.function
          path: /__export__policy.ci.optional_profile_report_only
          params: [subject]
          required: true
        - as: policy.ci.artifacts_present
          from: assert.function
          path: /__export__policy.ci.artifacts_present
          params: [subject]
          required: true
    library:
      id: policy.ci.gate
      module: policy
      stability: alpha
      owner: data-contracts
      tags: [policy, ci]
  - id: LIB-POLICY-CI-900
    type: contract.check
    title: ci gate policy library smoke
    harness:
      check:
        profile: text.file
        config: {}
      use:
        - ref: '#LIB-POLICY-CI-001'
          as: lib_policy_ci
          symbols:
            - policy.ci.required_profiles_pass
            - policy.ci.optional_profile_report_only
            - policy.ci.artifacts_present
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [text]
      predicates:
        - id: assert_1
          assert:
            - call:
                - {var: policy.ci.required_profiles_pass}
                - lit:
                    gate_summary:
                      status: pass
            - call:
                - {var: policy.ci.optional_profile_report_only}
                - lit:
                    optional_report:
                      status: report-only
            - call:
                - {var: policy.ci.artifacts_present}
                - lit:
                    gate_summary: {}
                    optional_report: {}
```


