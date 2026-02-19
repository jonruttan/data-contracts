# Chapter 10: Getting Started

```yaml doc-meta
doc_id: DOC-REF-110
title: Chapter 10 Getting Started
status: active
audience: author
owns_tokens:
- getting_started_minimal_flow
requires_tokens:
- rust_required_lane
commands:
- run: ./runners/public/runner_adapter.sh --impl rust governance
  purpose: Validate core governance checks in the required lane.
- run: ./runners/public/runner_adapter.sh --impl rust test-full
  purpose: Execute full executable-spec coverage in the required lane.
examples:
- id: EX-GETTING-STARTED-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Give a minimal, deterministic author workflow for writing and executing a valid `.spec.md` case.

## Inputs

- repo checkout
- Rust runner adapter: `./runners/public/runner_adapter.sh`
- spec files under `specs/**/*.spec.md`

## Outputs

- a valid executable case
- reproducible local validation results
- clear fail-path diagnostics

## Failure Modes

- invalid case shape (`contract` not in canonical mapping form)
- missing explicit imports for assertion variables
- stale generated docs/reference surfaces

## Minimal Case Skeleton

Use canonical v1 assertion shape:

```yaml
id: EX-CASE-001
type: contract.check
title: minimal canonical check
harness:
  check:
    profile: text.file
    config:
      path: /README.md
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names: [text]
  steps:
  - id: contains_title
    assert:
      std.string.contains:
      - {var: text}
      - spec_runner
```

## First Run Sequence

1. `./runners/public/runner_adapter.sh --impl rust governance`
2. `./runners/public/runner_adapter.sh --impl rust test-full`
3. `./scripts/local_ci_parity.sh`

## Compatibility (Non-Blocking)

Python and PHP are compatibility lanes. They are informative and non-blocking:

- `PYTHONPATH=runners/python .venv/bin/python -m pytest`
- `php runners/php/conformance_runner.php --cases specs/conformance/cases --case-formats md`
