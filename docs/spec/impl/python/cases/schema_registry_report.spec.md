# Python Schema Registry Report Command Cases

## SRPY-SCHEMA-REG-001

```yaml spec-test
id: SRPY-SCHEMA-REG-001
title: schema_registry_report_main writes report file
type: cli.run
argv:
- --format
- json
- --out
- .artifacts/schema-registry-impl-case.json
exit_code: 0
harness:
  entrypoint: spec_runner.cli:schema_registry_report_main
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - std.string.contains:
    - var: subject
    - 'wrote .artifacts/schema-registry-impl-case.json'
```

## SRPY-SCHEMA-REG-002

```yaml spec-test
id: SRPY-SCHEMA-REG-002
title: schema_registry_report_main check mode fails on stale artifact
type: cli.run
argv:
- --format
- json
- --check
- --out
- docs/spec/impl/python/fixtures/schema_registry_report_stale.json
exit_code: 1
harness:
  entrypoint: spec_runner.cli:schema_registry_report_main
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - std.string.contains:
    - var: subject
    - 'stale report artifact'
```
