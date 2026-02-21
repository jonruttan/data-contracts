These fixtures pin down entrypoint resolution behavior for `type: cli.run`.

Coverage focus:

- explicit `harness.entrypoint` behavior
- capability-gated skip behavior for runtimes without `cli.run`


```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
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
      category:
    overrides:
    - runner: php
      status: skip
      category:
  harness: check
  clauses:
    defaults: {}
    steps: []
    profile: cli.run
    config:
      argv:
      - "--help"
      exit_code: 0
      entrypoint: spec_runner.conformance_fixtures:main
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
      category:
    overrides:
    - runner: php
      status: skip
      category:
  harness: check
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
        - var: stdout
        - '"ok": true'
    profile: cli.run
    config:
      argv:
      - "--json"
      exit_code: 0
      entrypoint: spec_runner.conformance_fixtures:main
```


