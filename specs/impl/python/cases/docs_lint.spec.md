# Python Docs Lint Command Cases

## SRPY-DOCSLINT-001

```yaml contract-spec
id: SRPY-DOCSLINT-001
title: docs_lint_main passes for canonical reference manifest
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:docs_lint_main
  check:
    profile: cli.run
    config:
      argv: []
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - {var: subject}
    - 'OK: docs lint passed'
```

## SRPY-DOCSLINT-002

```yaml contract-spec
id: SRPY-DOCSLINT-002
title: docs_lint_main fails when manifest path is missing
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:docs_lint_main
  check:
    profile: cli.run
    config:
      argv:
      - --manifest
      - specs/impl/python/fixtures/missing_reference_manifest.yaml
      exit_code: 1
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - {var: subject}
    - missing reference manifest
```
