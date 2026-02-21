```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-SCHEMA-CASE-001
    title: valid core shape compiles and runs
    purpose: Ensures standard top-level keys accepted by registry validation continue to execute
      successfully.
    expect:
      portable:
        status: pass
        category: null
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
          - Spec-Test Schema (v1)
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-SCHEMA-CASE-002
    title: unknown evaluate symbol is rejected as schema
    purpose: Ensures unknown spec-lang symbols fail as schema in both runtimes.
    expect:
      portable:
        status: fail
        category: schema
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          lit:
            unknown_symbol_for_schema_case:
            - var: text
    harness:
      check:
        profile: text.file
        config: {}
```


