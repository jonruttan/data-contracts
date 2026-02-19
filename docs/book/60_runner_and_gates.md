# Chapter 60: Runner And Gates

```yaml doc-meta
doc_id: DOC-REF-160
title: Chapter 60 Runner And Gates
status: active
audience: maintainer
owns_tokens:
- rust_required_lane
requires_tokens:
- getting_started_minimal_flow
commands:
- run: ./runners/public/runner_adapter.sh --impl rust critical-gate
  purpose: Run the required merge-blocking lane.
- run: ./scripts/ci_gate.sh
  purpose: Run full CI-equivalent gate sequence locally.
examples:
- id: EX-RUNNER-GATES-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Document required runner interfaces, gate entrypoints, and blocking/non-blocking lane behavior.

## Inputs

- public adapter: `./runners/public/runner_adapter.sh`
- CI and local gate scripts under `scripts/`

## Outputs

- consistent local/CI execution paths
- clear blocking policy expectations

## Failure Modes

- invoking non-canonical runner paths
- compatibility-lane failures interpreted as blocking
- stale docs examples diverging from runner interface

## Required Rust Lane

Primary blocking commands:

- `./runners/public/runner_adapter.sh --impl rust critical-gate`
- `./runners/public/runner_adapter.sh --impl rust governance`
- `./runners/public/runner_adapter.sh --impl rust runner-certify --runner rust`
- compatibility certification for python/php is executed in `dc-runner-python` and `dc-runner-php`
- `./runners/public/runner_adapter.sh --impl rust test-full`

## Gate Sequence

- `./scripts/local_ci_parity.sh`
- `./scripts/ci_gate.sh`

## Exit Code Semantics

- `0`: success
- `1`: functional/runtime/assertion failure
- `2`: invalid args/config usage

## Compatibility (Non-Blocking)

Python/PHP lanes are compatibility telemetry and non-blocking by default.
Future lanes (Node, C) follow the same non-blocking default unless promoted by explicit contract change.
Compatibility certification reports are emitted in `dc-runner-python` and
`dc-runner-php` CI/release pipelines and ingested as external artifacts.

Detailed status exchange lifecycle and freshness policy are documented in
`docs/book/65_runner_status_and_compatibility.md`.


## API.HTTP Gate Notes

When validating `api.http` conformance and governance examples, cover method and scenario behavior explicitly:

- methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`
- scenario expectations include `api.http` round-trip behavior and `CORS` handling
