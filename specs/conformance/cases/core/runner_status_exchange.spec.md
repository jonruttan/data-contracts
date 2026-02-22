```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  harness: check
harness:
  type: unit.test
  profile: check
services:
  entries:
  - id: svc.assert_check.text_file.1
    type: assert.check
    io: input
    profile: text.file
    config:
      use:
      - as: lib_policy_text
        symbols:
        - policy.text.contains_pair
        artifact_id: art.svc.assert_check.text_file.1.use_1.1
contracts:
- id: DCCONF-RSTAT-001
  title: runner status report schema is declared
  purpose: Ensures the producer-facing status report schema exists.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.text.contains_pair
        - var: text
        - runtime.runner_status_report
        - command_results
- id: DCCONF-RSTAT-002
  title: runner status matrix schema is declared
  purpose: Ensures the aggregate status matrix schema exists.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.text.contains_pair
        - var: text
        - runtime.runner_status_matrix
        - freshness_state
- id: DCCONF-RSTAT-003
  title: ingest script enforces freshness threshold
  purpose: Ensures ingest includes max-age controls and enforcement flag.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.text.contains_pair
        - var: text
        - "--max-age-hours"
        - "--enforce-freshness"
- id: DCCONF-RSTAT-004
  title: ingest tracks missing compatibility status visibility
  purpose: Ensures missing compatibility status is represented and policy-scored.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.text.contains_pair
        - var: text
        - freshness_state
        - non_blocking_fail
- id: DCCONF-RSTAT-005
  title: required lane policy remains blocking
  purpose: Ensures required lane status maps to blocking policy effect.
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.text.contains_pair
        - var: text
        - lane_class
        - blocking_fail
artifacts:
- id: art.svc.assert_check.text_file.1.use_1.1
  ref: "/specs/libraries/policy/policy_text.spec.md"
  io: input
```









