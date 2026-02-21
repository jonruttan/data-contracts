These fixtures pin down entrypoint resolution behavior for `type: cli.run`.

Coverage focus:

- explicit `harness.entrypoint` behavior
- capability-gated skip behavior for runtimes without `cli.run`


```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-CLI-001
    title: conformance fixture sets explicit cli.run harness.entrypoint
    purpose: Defines portable behavior for explicit cli.run entrypoint when capability is present.
    requires:
      capabilities:
      - cli.run
      - cli.run.entrypoint_conformance
      when_missing: skip
    expect:
      portable:
        status: skip
        category: null
      impl:
        php:
          status: skip
          category: null
    harness:
      entrypoint: spec_runner.conformance_fixtures:main
      check:
        profile: cli.run
        config:
          argv:
          - --help
          exit_code: 0
    clauses:
      defaults: {}
      steps: []
  - id: DCCONF-CLI-002
    title: explicit entrypoint drives cli.run behavior deterministically
    purpose: Pins deterministic behavior for explicit harness entrypoint execution.
    requires:
      capabilities:
      - cli.run
      - cli.run.entrypoint_conformance
      when_missing: skip
    expect:
      portable:
        status: skip
        category: null
      impl:
        php:
          status: skip
          category: null
    harness:
      entrypoint: spec_runner.conformance_fixtures:main
      check:
        profile: cli.run
        config:
          argv:
          - --json
          exit_code: 0
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - stdout
      predicates:
      - id: assert_1
        assert:
          std.string.contains:
          - {var: stdout}
          - '"ok": true'
```


