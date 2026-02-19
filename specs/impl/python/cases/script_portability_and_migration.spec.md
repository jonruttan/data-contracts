# Python Script CLI Cases: Portability and Migration

## SRPY-SCRIPT-PORT-001

```yaml contract-spec
id: SRPY-SCRIPT-PORT-001
title: spec_portability_report writes json artifact
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:spec_portability_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --out
      - .artifacts/spec-portability-script-case.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stdout
    assert:
      std.string.contains:
      - {var: subject}
      - wrote .artifacts/spec-portability-script-case.json
```

## SRPY-SCRIPT-PORT-002

```yaml contract-spec
id: SRPY-SCRIPT-PORT-002
title: spec_portability_report rejects invalid format
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:spec_portability_report_main
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
    target: stderr
    assert:
      std.string.contains:
      - {var: subject}
      - invalid choice
```

## SRPY-SCRIPT-PORT-003

```yaml contract-spec
id: SRPY-SCRIPT-PORT-003
title: impl evaluate migration report help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:impl_evaluate_migration_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stdout
    assert:
      std.string.contains:
      - {var: subject}
      - --cases
```

## SRPY-SCRIPT-PORT-004

```yaml contract-spec
id: SRPY-SCRIPT-PORT-004
title: impl evaluate migration report rejects invalid option
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:impl_evaluate_migration_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --unknown-option
      exit_code: 2
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stderr
    assert:
      std.string.contains:
      - {var: subject}
      - unrecognized arguments
```

## SRPY-SCRIPT-PORT-005

```yaml contract-spec
id: SRPY-SCRIPT-PORT-005
title: split library cases command help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:split_library_cases_per_symbol_main
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stdout
    assert:
      std.string.contains:
      - {var: subject}
      - --write
```

## SRPY-SCRIPT-PORT-006

```yaml contract-spec
id: SRPY-SCRIPT-PORT-006
title: split library cases command requires input paths
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:split_library_cases_per_symbol_main
  check:
    profile: cli.run
    config:
      argv: []
      exit_code: 2
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stderr
    assert:
      std.string.contains:
      - {var: subject}
      - paths
```

## SRPY-SCRIPT-PORT-007

```yaml contract-spec
id: SRPY-SCRIPT-PORT-007
title: conformance purpose report writes json artifact
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:conformance_purpose_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --out
      - .artifacts/conformance-purpose-script-case.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stdout
    assert:
      std.string.contains:
      - {var: subject}
      - wrote .artifacts/conformance-purpose-script-case.json
```

## SRPY-SCRIPT-PORT-008

```yaml contract-spec
id: SRPY-SCRIPT-PORT-008
title: conformance purpose report rejects invalid format
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:conformance_purpose_report_main
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
    target: stderr
    assert:
      std.string.contains:
      - {var: subject}
      - invalid choice
```
