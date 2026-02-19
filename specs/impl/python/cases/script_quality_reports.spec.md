# Python Script CLI Cases: Quality and Registry Reports

## SRPY-SCRIPT-QUALITY-001

```yaml contract-spec
id: SRPY-SCRIPT-QUALITY-001
title: objective_scorecard_report writes json artifact
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:objective_scorecard_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --out
      - .artifacts/objective-scorecard-script-case.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': stdout
    assert:
      std.string.contains:
      - {var: subject}
      - wrote .artifacts/objective-scorecard-script-case.json
```

## SRPY-SCRIPT-QUALITY-002

```yaml contract-spec
id: SRPY-SCRIPT-QUALITY-002
title: objective_scorecard_report rejects invalid format
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:objective_scorecard_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --format
      - bad
      exit_code: 2
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': stderr
    assert:
      std.string.contains:
      - {var: subject}
      - invalid choice
```

## SRPY-SCRIPT-QUALITY-003

```yaml contract-spec
id: SRPY-SCRIPT-QUALITY-003
title: quality metric report fanout writes json artifact
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:quality_metric_reports_main
  check:
    profile: cli.run
    config:
      argv:
      - spec-lang-adoption
      - --out
      - .artifacts/spec-lang-adoption-script-case.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': stdout
    assert:
      std.string.contains:
      - {var: subject}
      - wrote .artifacts/spec-lang-adoption-script-case.json
```

## SRPY-SCRIPT-QUALITY-004

```yaml contract-spec
id: SRPY-SCRIPT-QUALITY-004
title: quality metric report fanout rejects unknown report key
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:quality_metric_reports_main
  check:
    profile: cli.run
    config:
      argv:
      - nope
      - --out
      - .artifacts/quality-script-case.json
      exit_code: 1
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': stderr
    assert:
      std.string.contains:
      - {var: subject}
      - unsupported quality report
```

## SRPY-SCRIPT-QUALITY-005

```yaml contract-spec
id: SRPY-SCRIPT-QUALITY-005
title: schema registry report writes json artifact
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:schema_registry_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --format
      - json
      - --out
      - .artifacts/schema-registry-script-case.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': stdout
    assert:
      std.string.contains:
      - {var: subject}
      - wrote .artifacts/schema-registry-script-case.json
```

## SRPY-SCRIPT-QUALITY-006

```yaml contract-spec
id: SRPY-SCRIPT-QUALITY-006
title: schema registry report rejects invalid format
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:schema_registry_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --format
      - nope
      exit_code: 2
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': stderr
    assert:
      std.string.contains:
      - {var: subject}
      - invalid choice
```
