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

1. Run `./scripts/runner_adapter.sh ci-cleanroom`.
2. Identify first failing surface/check id.
3. Apply the first-command from the table below.
4. Re-run check mode, then full gate.

## Check-ID To Cause Mapping

| Check ID / Surface | Likely Cause | First Command |
|---|---|---|
| `docs.*_sync` | generated docs drift | `./scripts/runner_adapter.sh docs-generate` |
| `schema.registry_*` | registry/docs mismatch | `./scripts/runner_adapter.sh schema-registry-build` |
| `normalization.*` | canonical formatting/path drift | `./scripts/runner_adapter.sh normalize-check` |
| `runtime.*` | adapter/runner contract drift | `./scripts/runner_adapter.sh governance` |
| `runtime.api_http_*` | `api.http` verbs/CORS/scenario drift | `./scripts/runner_adapter.sh governance` |

## API HTTP Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| schema error for `request.method` | verb not in supported suite | use `GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS` |
| schema error for `request.cors.preflight` | method is not `OPTIONS` | set `method: OPTIONS` for preflight |
| schema error for `requests` scenario shape | invalid step id/order/fields | validate each `requests[*]` step has `id`, `method`, and `url` |
| chain reference/schema failure | invalid `harness.chain.steps[*].ref` or unresolved case | validate `path`/`case_id` resolution and run governance chain checks |
| chain template resolution failure | `{{chain.<step>.<export>}}` points to missing export | add explicit `exports` on prerequisite step and use exact export names |
| runtime error in deterministic mode | network URL used without live mode | set `harness.api_http.mode: live` |
| missing round-trip values | bad `{{steps.*}}` path | verify step `id` and `steps_json` structure |
| CORS assertion fails | raw headers differ from expectation | assert via normalized `cors_json` fields |

First command for API flow issues:

- `./scripts/runner_adapter.sh governance`
- `./scripts/runner_adapter.sh normalize-check`

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
