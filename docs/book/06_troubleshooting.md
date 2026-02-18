# Chapter 6: Troubleshooting

```yaml doc-meta
doc_id: DOC-REF-010
title: Chapter 6 Troubleshooting
status: active
audience: maintainer
owns_tokens:
- troubleshooting_triage_matrix
- first_command_on_failure
requires_tokens:
- governance_workflow_quickpath
commands:
- run: ./scripts/runner_adapter.sh ci-cleanroom
  purpose: Reproduce CI-equivalent failures in a clean local pass.
examples:
- id: EX-TROUBLE-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a deterministic triage flow for docs/spec/governance failures.

## Inputs

- failing check id or command output
- local repo state

## Outputs

- root-cause classification and first corrective action

## Failure Modes

- chasing symptoms without reproducing with canonical commands
- fixing generated files manually instead of generators
- patching runtime code for documentation drift issues

## Triage Flow

1. Run `make prepush` (parity-default path includes triage-first governance).
2. If governance fails/stalls, read `/.artifacts/governance-triage-summary.md`.
3. Run the suggested targeted command from that summary.
4. Re-run `make prepush`; only then run full gate if needed.

## Local Pre-Push Enforcement

- Parity-default gate: `make prepush`
- Fast opt-out gate: `make prepush-fast` (or `SPEC_PREPUSH_MODE=fast make prepush`)
- Install managed hook: `make hooks-install`
- Emergency bypass: `SPEC_PREPUSH_BYPASS=1 git push` (run `make prepush` immediately after)
- Rust target strict mode: `SPEC_RUNNER_RUST_TARGET_STRICT=1 ./scripts/runner_adapter.sh --impl rust governance`

## Check-ID To Cause Mapping

| Check ID / Surface | Likely Cause | First Command |
|---|---|---|
| `docs.*_sync` | generated docs drift | `./scripts/runner_adapter.sh docs-generate` |
| `docs.markdown_structured_assertions_required` | markdown checks use brittle plain contains assertions | migrate assertions to `md.*` / `domain.markdown.*` helpers |
| `schema.registry_*` | registry/docs mismatch | `./scripts/runner_adapter.sh schema-registry-build` |
| `normalization.*` | canonical formatting/path drift | `./scripts/runner_adapter.sh normalize-check` |
| `runtime.*` | adapter/runner contract drift | `./scripts/runner_adapter.sh governance` |
| `runtime.api_http_*` | `api.http` verbs/CORS/scenario drift | `./scripts/runner_adapter.sh governance` |
| `SRGOV-*` mixed failure set | broad run failed/stalled; targeted retry needed | `./scripts/governance_triage.sh --mode auto --impl rust` |

## API HTTP Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| schema error for `request.method` | verb not in supported suite | use `GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS` |
| schema error for `request.cors.preflight` | method is not `OPTIONS` | set `method: OPTIONS` for preflight |
| schema error for `requests` scenario shape | invalid step id/order/fields | validate each `requests[*]` step has `id`, `method`, and `url` |
| chain schema failure for step class | missing or invalid `harness.chain.steps[*].class` | use one of `must`, `can`, `cannot` |
| chain reference/schema failure | invalid `harness.chain.steps[*].ref` or unresolved case | validate scalar ref format `[path][#case_id]` and run governance chain checks |
| chain template resolution failure | `{{chain.<step>.<export>}}` points to missing export | add explicit `exports` on prerequisite step and use exact export names |
| chain import alias collision | duplicate imported local names or reserved name shadowing | fix `harness.chain.imports` names/aliases and avoid reserved names |
| runtime error in deterministic mode | network URL used without live mode | set `harness.api_http.mode: live` |
| missing round-trip values | bad `{{steps.*}}` path | verify step `id` and `steps_json` structure |
| CORS assertion fails | raw headers differ from expectation | assert via normalized `cors_json` fields |
| liveness watchdog failure (`stall.*` / `timeout.hard_cap.emergency`) | no progress detected or emergency cap exceeded | rerun with `--profile-level debug` and tune `--liveness-*` knobs |

First command for API flow issues:

- `./scripts/runner_adapter.sh governance`
- `./scripts/runner_adapter.sh normalize-check`

First command for governance hang/long-cycle issues:

- `./scripts/governance_triage.sh --mode auto --impl rust`
- Review `/.artifacts/governance-triage-summary.md`

## Liveness Controls

Governance now uses progress-based hang detection:

- `--liveness-level off|basic|strict`
- `--liveness-stall-ms` (default `30000`)
- `--liveness-min-events` (default `1`)
- `--liveness-hard-cap-ms` (default `1800000`)
- `--liveness-kill-grace-ms` (default `5000`)

Legacy variables `SPEC_RUNNER_TIMEOUT_GOVERNANCE_SECONDS` and
`SPEC_RUNNER_GOVERNANCE_SUBPROCESS_TIMEOUT_SECONDS` are deprecated and map to
emergency hard-cap behavior.

## Timeout Profiling

Use profiling for deterministic timeout diagnosis:

```bash
./scripts/runner_adapter.sh --profile-level detailed \
  --profile-out .artifacts/run-trace.json \
  --profile-summary-out .artifacts/run-trace-summary.md \
  governance
```

Artifacts:

- `/.artifacts/run-trace.json` (full span/event trace)
- `/.artifacts/run-trace-summary.md` (hotspots + timeout/stall hints)

For deeper diagnostics:

```bash
./scripts/runner_adapter.sh --profile-level debug \
  --profile-heartbeat-ms 250 \
  --profile-stall-threshold-ms 2000 \
  governance
```

## Fast Recovery Playbook

1. Generate docs and schema surfaces.
2. Run normalize fixer if needed.
3. Re-run governance.
4. Re-run cleanroom gate.

## When To Escalate

Escalate to implementation docs when the issue is runner-internal behavior:

- `/docs/impl/index.md`
- `/docs/impl/python.md`
- `/docs/impl/php.md`
- `/docs/spec/contract/12_runner_interface.md`
