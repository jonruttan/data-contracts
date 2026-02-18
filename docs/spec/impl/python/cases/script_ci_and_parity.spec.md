# Python Script CLI Cases: CI and Parity

## SRPY-SCRIPT-CI-001

```yaml contract-spec
id: SRPY-SCRIPT-CI-001
title: ci_gate_summary command help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:ci_gate_summary_main
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - {var: subject}
    - --runner-bin
```

## SRPY-SCRIPT-CI-002

```yaml contract-spec
id: SRPY-SCRIPT-CI-002
title: ci_gate_summary requires runner-bin
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:ci_gate_summary_main
  check:
    profile: cli.run
    config:
      argv: []
      exit_code: 2
contract:
- id: assert_1
  class: MUST
  target: stderr
  asserts:
  - std.string.contains:
    - {var: subject}
    - --runner-bin
```

## SRPY-SCRIPT-CI-003

```yaml contract-spec
id: SRPY-SCRIPT-CI-003
title: compare_conformance_parity command help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:compare_conformance_parity_main
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - {var: subject}
    - --cases
```

## SRPY-SCRIPT-CI-004

```yaml contract-spec
id: SRPY-SCRIPT-CI-004
title: compare_conformance_parity rejects invalid timeout arg
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:compare_conformance_parity_main
  check:
    profile: cli.run
    config:
      argv:
      - --python-timeout-seconds
      - x
      exit_code: 2
contract:
- id: assert_1
  class: MUST
  target: stderr
  asserts:
  - std.string.contains:
    - {var: subject}
    - invalid int value
```

## SRPY-SCRIPT-CI-005

```yaml contract-spec
id: SRPY-SCRIPT-CI-005
title: python conformance runner help renders required flags
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:python_conformance_runner_main
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - {var: subject}
    - --case-file-pattern
```

## SRPY-SCRIPT-CI-006

```yaml contract-spec
id: SRPY-SCRIPT-CI-006
title: python conformance runner rejects empty case pattern
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:python_conformance_runner_main
  check:
    profile: cli.run
    config:
      argv:
      - --cases
      - docs/spec/conformance/cases
      - --out
      - .artifacts/python-conformance-script-case.json
      - --case-file-pattern
      - ''
      exit_code: 2
contract:
- id: assert_1
  class: MUST
  target: stderr
  asserts:
  - std.string.contains:
    - {var: subject}
    - case-file-pattern
```
