```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-LIB-CONTRACT-001
    title: policy library uses producer harness exports
    purpose: Ensures policy library authoring uses producer-owned harness.exports with assert.function
      source mappings.
    expect:
      portable:
        status: pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - call:
          - {var: policy.text.contains_all}
          - {var: text}
          - lit:
            - 'type: spec.export'
            - 'harness:'
            - 'exports:'
            - 'from: assert.function'
        - call:
          - {var: policy.text.contains_none}
          - {var: text}
          - lit:
            - 'defines:'
    harness:
      check:
        profile: text.file
        config:
          path: /specs/libraries/policy/policy_core.spec.md
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
        - policy.text.contains_none
  - id: DCCONF-LIB-CONTRACT-002
    title: path library uses producer harness exports
    purpose: Ensures path library authoring uses producer-owned harness.exports with assert.function
      source mappings.
    expect:
      portable:
        status: pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - call:
          - {var: policy.text.contains_all}
          - {var: text}
          - lit:
            - 'type: spec.export'
            - 'harness:'
            - 'exports:'
            - 'from: assert.function'
        - call:
          - {var: policy.text.contains_none}
          - {var: text}
          - lit:
            - 'defines:'
    harness:
      check:
        profile: text.file
        config:
          path: /specs/libraries/path/path_core.spec.md
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
        - policy.text.contains_none
  - id: DCCONF-LIB-CONTRACT-003
    title: policy library index tracks canonical files
    purpose: Ensures generated policy library index includes canonical file references.
    expect:
      portable:
        status: pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - call:
          - {var: policy.text.contains_all}
          - {var: text}
          - lit:
            - /specs/libraries/policy/policy_core.spec.md
            - /specs/libraries/policy/policy_metrics.spec.md
    harness:
      check:
        profile: text.file
        config:
          path: /specs/libraries/policy/index.md
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_all
```




