# Python Script CLI Cases: Governance Runner

## SRPY-SCRIPT-GOV-001

```yaml contract-spec
id: SRPY-SCRIPT-GOV-001
title: governance runner help renders usage
type: contract.check
harness:
  entrypoint: spec_runner.governance_runner:run_governance_specs_main
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
      - --check-prefix
```

## SRPY-SCRIPT-GOV-002

```yaml contract-spec
id: SRPY-SCRIPT-GOV-002
title: governance runner rejects empty case pattern
type: contract.check
harness:
  entrypoint: spec_runner.governance_runner:run_governance_specs_main
  check:
    profile: cli.run
    config:
      argv:
      - --cases
      - specs/governance/cases
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

## SRPY-SCRIPT-GOV-003

```yaml contract-spec
id: SRPY-SCRIPT-GOV-003
title: governance runner rejects check prefix that selects no cases
type: contract.check
harness:
  entrypoint: spec_runner.governance_runner:run_governance_specs_main
  check:
    profile: cli.run
    config:
      argv:
      - --cases
      - specs/governance/cases
      - --check-prefix
      - zz.nonexistent.prefix
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
      - selected zero cases
```

## SRPY-SCRIPT-GOV-004

```yaml contract-spec
id: SRPY-SCRIPT-GOV-004
title: governance runtime registers required docgen quality checks
type: contract.check
harness:
  check:
    profile: text.file
    config:
      path: /runners/python/spec_runner/governance_runtime.py
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
      - docs.stdlib_symbol_docs_complete
    - std.string.contains:
      - {var: subject}
      - docs.stdlib_examples_complete
    - std.string.contains:
      - {var: subject}
      - docs.harness_reference_semantics_complete
    - std.string.contains:
      - {var: subject}
      - docs.runner_reference_semantics_complete
    - std.string.contains:
      - {var: subject}
      - docs.reference_namespace_chapters_sync
    - std.string.contains:
      - {var: subject}
      - docs.docgen_quality_score_threshold
```
