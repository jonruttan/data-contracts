```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-PHP-TEXT-001
    title: text.file contain assertion passes in php bootstrap
    purpose: Baseline positive contain check for the php text.file subset.
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
          - 'version: 1'
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-002
    title: text.file regex assertion can fail in php bootstrap
    purpose: Baseline failing regex check for the php text.file subset.
    expect:
      portable:
        status: fail
        category: assertion
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          std.string.regex_match:
          - {var: text}
          - \A\Z
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-003
    title: nested must group with inherited target passes
    purpose: Verifies nested must groups inherit target from parent nodes.
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
          - 'version: 1'
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-004
    title: can passes when at least one branch passes
    purpose: Verifies can succeeds when at least one branch succeeds.
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
        required: false
        assert:
        - std.string.regex_match:
          - {var: text}
          - (?!)
        - std.string.contains:
          - {var: text}
          - 'version: 1'
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-005
    title: can fails when all branches fail
    purpose: Verifies can fails when every branch assertion fails.
    expect:
      portable:
        status: fail
        category: assertion
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
        - std.string.regex_match:
          - {var: text}
          - \A\Z
        - std.string.regex_match:
          - {var: text}
          - (?!)
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-006
    title: cannot passes when all branches fail
    purpose: Verifies cannot succeeds when every branch assertion fails.
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
          std.logic.not:
          - std.logic.or:
            - std.string.regex_match:
              - {var: text}
              - \A\Z
            - std.string.regex_match:
              - {var: text}
              - (?!)
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-007
    title: cannot fails when any branch passes
    purpose: Verifies cannot fails when at least one branch succeeds.
    expect:
      portable:
        status: fail
        category: assertion
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          std.logic.not:
          - std.logic.or:
            - std.string.contains:
              - {var: text}
              - 'version: 1'
            - std.string.regex_match:
              - {var: text}
              - (?!)
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-008
    title: nested mixed groups with inherited target passes
    purpose: Covers mixed nested must/may/must_not evaluation with inherited targets.
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
        required: false
        assert:
        - std.string.regex_match:
          - {var: text}
          - \A\Z
        - std.string.contains:
          - {var: text}
          - 'version: 1'
      - id: assert_2
        assert:
          std.logic.not:
          - std.string.regex_match:
            - {var: text}
            - \A\Z
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-009
    title: evaluate regex remains pass under assert_health error mode
    purpose: Confirms evaluate regex assertions bypass sugar diagnostics and can pass under error
      mode.
    expect:
      portable:
        status: pass
        category: null
    assert_health:
      mode: error
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          std.string.regex_match:
          - {var: text}
          - '(?<=version: )1'
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-010
    title: evaluate empty contains remains pass under assert_health error mode
    purpose: Confirms evaluate contains with empty string does not trigger sugar diagnostic failures
      in error mode.
    expect:
      portable:
        status: pass
        category: null
    assert_health:
      mode: error
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
          - ''
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-011
    title: evaluate always-true regex remains pass under assert_health error mode
    purpose: Confirms evaluate regex assertions are evaluated directly without sugar-level AH002
      failures.
    expect:
      portable:
        status: pass
        category: null
    assert_health:
      mode: error
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          std.string.regex_match:
          - {var: text}
          - .*
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-012
    title: evaluate duplicate contains remain pass under assert_health error mode
    purpose: Confirms evaluate duplicate contains expressions do not trigger sugar-level AH003
      diagnostics.
    expect:
      portable:
        status: fail
        category: assertion
        message_tokens:
        - AH004
        - contract[0].asserts[0].MUST
    assert_health:
      mode: error
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - std.string.contains:
          - {var: text}
          - 'version: 1'
        - std.string.contains:
          - {var: text}
          - 'version: 1'
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-013
    title: evaluate sibling branches remain pass under assert_health error mode
    purpose: Confirms evaluate-only non-redundant sibling branches in can groups remain valid
      in error mode.
    expect:
      portable:
        status: pass
        category: null
    assert_health:
      mode: error
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
          - 'version: 1'
        - std.string.contains:
          - {var: text}
          - 'version: 2'
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-PHP-TEXT-014
    title: warn mode emits diagnostics without failing the case
    purpose: Checks warn mode emits diagnostics without converting the case to failure.
    expect:
      portable:
        status: pass
        category: null
    assert_health:
      mode: warn
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
          - ''
    harness:
      check:
        profile: text.file
        config: {}
```


























