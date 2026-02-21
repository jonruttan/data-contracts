```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-RSTAT-001
    title: runner status report schema is declared
    purpose: Ensures the producer-facing status report schema exists.
    harness:
      check:
        profile: text.file
        config: {}
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
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
          - {var: policy.text.contains_pair}
          - {var: text}
          - runtime.runner_status_report
          - command_results
  - id: DCCONF-RSTAT-002
    title: runner status matrix schema is declared
    purpose: Ensures the aggregate status matrix schema exists.
    harness:
      check:
        profile: text.file
        config: {}
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
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
          - {var: policy.text.contains_pair}
          - {var: text}
          - runtime.runner_status_matrix
          - freshness_state
  - id: DCCONF-RSTAT-003
    title: ingest script enforces freshness threshold
    purpose: Ensures ingest includes max-age controls and enforcement flag.
    harness:
      check:
        profile: text.file
        config: {}
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
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
          - {var: policy.text.contains_pair}
          - {var: text}
          - --max-age-hours
          - --enforce-freshness
  - id: DCCONF-RSTAT-004
    title: ingest tracks missing compatibility status visibility
    purpose: Ensures missing compatibility status is represented and policy-scored.
    harness:
      check:
        profile: text.file
        config: {}
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
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
          - {var: policy.text.contains_pair}
          - {var: text}
          - freshness_state
          - non_blocking_fail
  - id: DCCONF-RSTAT-005
    title: required lane policy remains blocking
    purpose: Ensures required lane status maps to blocking policy effect.
    harness:
      check:
        profile: text.file
        config: {}
      use:
      - ref: /specs/libraries/policy/policy_text.spec.md
        as: lib_policy_text
        symbols:
        - policy.text.contains_pair
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
          - {var: policy.text.contains_pair}
          - {var: text}
          - lane_class
          - blocking_fail
```









