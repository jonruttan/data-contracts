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
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
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
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stderr
    as:
      stderr: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
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
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
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
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stderr
    as:
      stderr: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
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
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
    - std.string.contains:
      - {var: subject}
      - --cases
    - std.string.contains:
      - {var: subject}
      - --out
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
      - specs/conformance/cases
      - --out
      - .artifacts/python-conformance-script-case.json
      - --case-file-pattern
      - ''
      exit_code: 2
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stderr
    as:
      stderr: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - case-file-pattern
```

## SRPY-SCRIPT-CI-007

```yaml contract-spec
id: SRPY-SCRIPT-CI-007
title: php conformance runner usage includes required flags
type: contract.check
harness:
  check:
    profile: text.file
    config:
      path: /runners/php/conformance_runner.php
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
    as:
      text: subject
  steps:
  - id: assert_1
    assert:
    - std.string.contains:
      - {var: subject}
      - --cases <dir-or-file>
    - std.string.contains:
      - {var: subject}
      - --out <file>
    - std.string.contains:
      - {var: subject}
      - --case-file-pattern <glob>
```

## SRPY-SCRIPT-CI-008

```yaml contract-spec
id: SRPY-SCRIPT-CI-008
title: compare_conformance_parity rejects empty case formats
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:compare_conformance_parity_main
  check:
    profile: cli.run
    config:
      argv:
      - --case-formats
      - ''
      exit_code: 2
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stderr
    as:
      stderr: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - --case-formats requires at least one format
```

## SRPY-SCRIPT-CI-009

```yaml contract-spec
id: SRPY-SCRIPT-CI-009
title: compare_conformance_parity reports missing php executable
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:compare_conformance_parity_main
  env:
    PATH: /nonexistent
  check:
    profile: cli.run
    config:
      argv:
      - --cases
      - specs/conformance/cases
      exit_code: 2
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stderr
    as:
      stderr: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - php executable not found in PATH
```
