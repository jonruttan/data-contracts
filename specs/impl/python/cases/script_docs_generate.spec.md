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
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - --surface
    imports:
      subject:
        from: artifact
        key: stdout
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
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - 1
      - 1
    imports:
      subject:
        from: artifact
        key: stdout
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
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - --cases
    imports:
      subject:
        from: artifact
        key: stdout
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
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - unknown surface_id
    imports:
      subject:
        from: artifact
        key: stdout
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
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - --write
    imports:
      subject:
        from: artifact
        key: stdout
```

## SRPY-SCRIPT-DOCS-006

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-006
title: evaluate_style check defaults to docs spec tree
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:evaluate_style_main
  check:
    profile: cli.run
    config:
      argv:
      - --check
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - formatting is canonical
    imports:
      subject:
        from: artifact
        key: stdout
```

## SRPY-SCRIPT-DOCS-007

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-007
title: docs_build_reference writes artifacts to explicit outputs
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:docs_build_reference_main
  check:
    profile: cli.run
    config:
      argv:
      - --manifest
      - docs/book/reference_manifest.yaml
      - --index-out
      - .artifacts/docs-build-reference-index.md
      - --coverage-out
      - .artifacts/docs-build-reference-coverage.md
      - --graph-out
      - .artifacts/docs-build-reference-graph.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
    - std.string.contains:
      - {var: subject}
      - wrote .artifacts/docs-build-reference-index.md
    - std.string.contains:
      - {var: subject}
      - wrote .artifacts/docs-build-reference-coverage.md
    - std.string.contains:
      - {var: subject}
      - wrote .artifacts/docs-build-reference-graph.json
    imports:
      subject:
        from: artifact
        key: stdout
```

## SRPY-SCRIPT-DOCS-008

```yaml contract-spec
id: SRPY-SCRIPT-DOCS-008
title: docs_build_reference rejects unknown args
type: contract.check
harness:
  entrypoint: spec_runner.script_entrypoints:docs_build_reference_main
  check:
    profile: cli.run
    config:
      argv:
      - --bad-flag
      exit_code: 2
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - unrecognized arguments
    imports:
      subject:
        from: artifact
        key: stderr
```
