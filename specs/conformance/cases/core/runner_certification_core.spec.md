```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-RCERT-001
    title: runner certification core checks MUST assertions deterministically
    purpose: Confirms required certification core clauses remain strict and deterministic.
    harness:
      check:
        profile: text.file
        config: {}
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          std.string.contains:
          - {var: text}
          - contract-spec
  - id: DCCONF-RCERT-002
    title: runner certification core MAY assertions remain available
    purpose: Ensures MAY clauses remain supported for compatibility-oriented certification checks.
    harness:
      check:
        profile: text.file
        config: {}
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        required: false
        assert:
        - std.string.contains:
          - {var: text}
          - version
        - std.string.contains:
          - {var: text}
          - contract-spec
```


