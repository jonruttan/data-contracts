# Python Script CLI Cases: Docs Generate and Style

## SRPY-SCRIPT-DOCS-001

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-001
title: docs_generate_all help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:docs_generate_all_main
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
        - --surface
```

## SRPY-SCRIPT-DOCS-002

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-002
title: docs_generate_all fails on unknown surface
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:docs_generate_all_main
  check:
    profile: cli.run
    config:
      argv:
      - --check
      - --surface
      - nope
      exit_code: 1
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.logic.eq:
        - 1
        - 1
```

## SRPY-SCRIPT-DOCS-003

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-003
title: docs_generate_specs help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:docs_generate_specs_main
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

## SRPY-SCRIPT-DOCS-004

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-004
title: docs_generate_specs fails on unknown surface
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:docs_generate_specs_main
  check:
    profile: cli.run
    config:
      argv:
      - --check
      - --surface
      - nope
      exit_code: 1
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
        - {var: subject}
        - unknown surface_id
```

## SRPY-SCRIPT-DOCS-005

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-005
title: evaluate_style help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:evaluate_style_main
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
        - --write
```

## SRPY-SCRIPT-DOCS-006

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-006
title: evaluate_style rejects missing file path
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:evaluate_style_main
  check:
    profile: cli.run
    config:
      argv:
      - --check
      exit_code: 1
contract:
- id: assert_1
  class: MUST
  target: stderr
  asserts:
  - std.logic.eq:
        - 1
        - 1
```
