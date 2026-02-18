# Python Script CLI Cases: Normalization

## SRPY-SCRIPT-NORM-001

```yaml contract-spec
id: SRPY-SCRIPT-NORM-001
title: normalize_docs_layout help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:normalize_docs_layout_main
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
    - --profile
```

## SRPY-SCRIPT-NORM-002

```yaml contract-spec
id: SRPY-SCRIPT-NORM-002
title: normalize_docs_layout rejects conflicting modes
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:normalize_docs_layout_main
  check:
    profile: cli.run
    config:
      argv:
      - --check
      - --write
      exit_code: 2
contract:
- id: assert_1
  class: MUST
  target: stderr
  asserts:
  - std.string.contains:
    - {var: subject}
    - not allowed with argument
```

## SRPY-SCRIPT-NORM-003

```yaml contract-spec
id: SRPY-SCRIPT-NORM-003
title: normalize_repo help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:normalize_repo_main
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
    - --scope
```

## SRPY-SCRIPT-NORM-004

```yaml contract-spec
id: SRPY-SCRIPT-NORM-004
title: normalize_repo rejects invalid scope
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:normalize_repo_main
  check:
    profile: cli.run
    config:
      argv:
      - --check
      - --scope
      - bad
      exit_code: 2
contract:
- id: assert_1
  class: MUST
  target: stderr
  asserts:
  - std.string.contains:
    - {var: subject}
    - invalid choice
```
