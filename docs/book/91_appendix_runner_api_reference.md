# Runner API Reference

```yaml doc-meta
doc_id: DOC-REF-091
title: Appendix Runner API Reference
status: active
audience: reviewer
owns_tokens:
- appendix_runner_api_reference
requires_tokens:
- trusted_inputs_required
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated runner API surface is in sync.
examples:
- id: EX-APP-RUNNER-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

Machine-generated runner command catalog.

## Purpose

Provide generated command-surface documentation for the canonical runner interface.

## Inputs

- runner adapter scripts and rust CLI command registrations

## Outputs

- deterministic command parity table across implementations

## Failure Modes

- stale generated block when command surfaces change
- missing generated markers
- catalog/parity drift

<!-- GENERATED:START runner_api_catalog -->

## Generated Runner API Catalog

- command_count: 40
- python_command_count: 40
- rust_command_count: 40
- parity_command_count: 40
- all_commands_parity: true

| command | python | rust | parity |
|---|---|---|---|
| `ci-cleanroom` | true | true | true |
| `ci-gate-summary` | true | true | true |
| `compilecheck` | true | true | true |
| `conformance-parity` | true | true | true |
| `conformance-purpose-json` | true | true | true |
| `conformance-purpose-md` | true | true | true |
| `contract-assertions-json` | true | true | true |
| `contract-assertions-md` | true | true | true |
| `docs-build` | true | true | true |
| `docs-build-check` | true | true | true |
| `docs-generate` | true | true | true |
| `docs-generate-check` | true | true | true |
| `docs-graph` | true | true | true |
| `docs-lint` | true | true | true |
| `docs-operability-json` | true | true | true |
| `docs-operability-md` | true | true | true |
| `governance` | true | true | true |
| `lint` | true | true | true |
| `normalize-check` | true | true | true |
| `normalize-fix` | true | true | true |
| `objective-scorecard-json` | true | true | true |
| `objective-scorecard-md` | true | true | true |
| `python-dependency-json` | true | true | true |
| `python-dependency-md` | true | true | true |
| `runner-independence-json` | true | true | true |
| `runner-independence-md` | true | true | true |
| `schema-docs-build` | true | true | true |
| `schema-docs-check` | true | true | true |
| `schema-registry-build` | true | true | true |
| `schema-registry-check` | true | true | true |
| `spec-lang-adoption-json` | true | true | true |
| `spec-lang-adoption-md` | true | true | true |
| `spec-lang-stdlib-json` | true | true | true |
| `spec-lang-stdlib-md` | true | true | true |
| `spec-portability-json` | true | true | true |
| `spec-portability-md` | true | true | true |
| `style-check` | true | true | true |
| `test-core` | true | true | true |
| `test-full` | true | true | true |
| `typecheck` | true | true | true |
<!-- GENERATED:END runner_api_catalog -->
