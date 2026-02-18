# Chapter 5: How-To Workflows

```yaml doc-meta
doc_id: DOC-REF-008
title: Chapter 5 How-To Workflows
status: active
audience: author
owns_tokens:
- authoring_workflows
- governance_workflow_quickpath
requires_tokens:
- spec_lang_guide_patterns
commands:
- run: ./scripts/runner_adapter.sh governance
  purpose: Validate governance checks after workflow changes.
examples:
- id: EX-HOWTO-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide repeatable recipes for common contributor tasks.

## Inputs

- local checkout
- canonical runner entrypoint
- `.spec.md` authoring surface

## Outputs

- predictable task completion with contract/governance compliance

## Failure Modes

- using stale paths/names in docs or harness config
- adding non-canonical expression syntax
- skipping local gate commands before push

## Add A New Spec Case

1. Create `*.spec.md` in the correct domain tree.
2. Add `yaml contract-spec` case with `id`, `type`, `assert`.
3. Prefer `evaluate` for policy logic.
4. Run:
   - `./scripts/runner_adapter.sh normalize-check`
   - `./scripts/runner_adapter.sh governance`

## Add Or Reuse A Library Function

1. Add function in a `type: spec.export` case.
2. Define function logic in an `assert` step (`class: must`) and export from
   producer `harness.chain.exports` using `from: assert.function`.
3. Import symbols in consumers through `harness.chain.steps` + `harness.chain.imports`.
4. Prefer `domain.*` helpers in executable specs; keep raw `ops.*` usage inside
   domain libraries and stdlib primitive conformance cases.

## Add Markdown Structure Assertions

1. Chain-load markdown helpers:
   - `/docs/spec/libraries/domain/markdown_core.spec.md`
2. Prefer `target: context_json` for structural checks.
3. Use `domain.markdown.*` helpers for heading/link/token checks.

Example:

```yaml
harness:
  chain:
    steps:
    - id: lib_markdown
      class: must
      ref: /docs/spec/libraries/domain/markdown_core.spec.md
    imports:
    - from: lib_markdown
      names:
      - domain.markdown.required_sections_present
      - domain.markdown.link_targets_all_resolve
contract:
- target: context_json
  asserts:
  - must:
    - call:
      - {var: domain.markdown.required_sections_present}
      - {var: subject}
      - lit:
        - Purpose
        - Inputs
        - Outputs
    - call:
      - {var: domain.markdown.link_targets_all_resolve}
      - {var: subject}
```

## Prefer Domain FS Helpers Over Raw `ops.fs.*`

1. Chain-load:
   - `/docs/spec/libraries/domain/fs_core.spec.md`
2. Use domain wrappers in executable specs:
   - `domain.fs.json_get_text`
   - `domain.fs.json_get_or_text`
   - `domain.fs.json_path_eq_text`
   - `domain.fs.glob_filter`
   - `domain.fs.glob_all`

Example:

```yaml
harness:
  chain:
    steps:
    - id: lib_fs
      class: must
      ref: /docs/spec/libraries/domain/fs_core.spec.md
    imports:
    - from: lib_fs
      names:
      - domain.fs.json_path_eq_text
      - domain.fs.glob_filter
contract:
- id: assert_1
  class: must
  asserts:
  - must:
    - call:
      - {var: domain.fs.json_path_eq_text}
      - '{"meta":{"ok":true}}'
      - lit: [meta, ok]
      - true
    - std.logic.eq:
      - call:
        - {var: domain.fs.glob_filter}
        - lit: [/docs/a.md, /docs/a.spec.md]
        - '*.spec.md'
      - lit: [/docs/a.spec.md]
  target: context_json
```

## Add A Governance Check

1. Add scanner/check implementation and check id.
2. Add governance case under `/docs/spec/governance/cases/core/`.
3. Wire policy + traceability entries.
4. Run full governance pass.

## Run Local Gate Subsets

- Docs only: `./scripts/runner_adapter.sh docs-generate-check`
- Governance only: `./scripts/runner_adapter.sh governance`
- Governance triage (recommended first): `./scripts/governance_triage.sh --mode auto --impl rust`
- Full local gate: `./scripts/runner_adapter.sh ci-cleanroom`
- Required parity-default prepush gate: `make prepush`
- Fast opt-out mode: `make prepush-fast` or `SPEC_PREPUSH_MODE=fast make prepush`
- Install managed hook enforcement: `make hooks-install`
- Emergency push bypass: `SPEC_PREPUSH_BYPASS=1 git push`
- Triage artifacts: `/.artifacts/governance-triage.json`, `/.artifacts/governance-triage-summary.md`

## Configure Adapter Timeouts

Long-running adapter commands now have deterministic timeout guards. Override
defaults with environment variables when working on large repos or slower CI
workers.

- `SPEC_RUNNER_TIMEOUT_GOVERNANCE_SECONDS` (default `120`)
- `SPEC_RUNNER_TIMEOUT_GOVERNANCE_HEAVY_SECONDS` (default `180`)
- `SPEC_RUNNER_TIMEOUT_NORMALIZE_SECONDS` (default `120`)
- `SPEC_RUNNER_TIMEOUT_DOCS_SECONDS` (default `180`)
- `SPEC_RUNNER_TIMEOUT_CONFORMANCE_PARITY_SECONDS` (default `240`)

Example:

```bash
SPEC_RUNNER_TIMEOUT_GOVERNANCE_SECONDS=300 ./scripts/runner_adapter.sh governance
```

## Enable Runtime Profiling

Use opt-in profiling when diagnosing hangs or long-running checks:

```bash
./scripts/runner_adapter.sh --profile-level detailed \
  --profile-out .artifacts/run-trace.json \
  --profile-summary-out .artifacts/run-trace-summary.md \
  governance
```

Optional controls:

- `--profile-heartbeat-ms <int>` (default `1000`)
- `--profile-stall-threshold-ms <int>` (default `10000`)

Environment equivalents:

- `SPEC_RUNNER_PROFILE_LEVEL`
- `SPEC_RUNNER_PROFILE_OUT`
- `SPEC_RUNNER_PROFILE_SUMMARY_OUT`
- `SPEC_RUNNER_PROFILE_HEARTBEAT_MS`
- `SPEC_RUNNER_PROFILE_STALL_THRESHOLD_MS`

## Domain-First Decision Flow

1. If a `domain.*` helper exists for your intent, use it.
2. If no `domain.*` helper exists, add one in the relevant domain library.
3. Use raw `ops.*` directly only in:
   - domain library implementation specs
   - primitive stdlib/conformance coverage specs

## REST API How-To (`api.http`)

Use `type: api.http` for endpoint tests. The practical method suite is:
`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.

### GET

```yaml
type: api.http
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
```

### POST

```yaml
type: api.http
request:
  method: POST
  url: /docs/spec/conformance/cases/fixtures/api_http_created.json
  body_json:
    name: example
```

### UPDATE (PUT and PATCH)

```yaml
type: api.http
request:
  method: PUT
  url: /docs/spec/conformance/cases/fixtures/api_http_item_abc-123.json
```

```yaml
type: api.http
request:
  method: PATCH
  url: /docs/spec/conformance/cases/fixtures/api_http_item_abc-123.json
```

### DELETE

```yaml
type: api.http
request:
  method: DELETE
  url: /docs/spec/conformance/cases/fixtures/api_http_deleted.json
```

### CORS Preflight (OPTIONS)

```yaml
type: api.http
request:
  method: OPTIONS
  url: https://api.example.invalid/items
  cors:
    preflight: true
    origin: https://client.example
    request_method: POST
    request_headers: [authorization, content-type]
```

### Round-Trip Scenario (`requests`)

```yaml
type: api.http
harness:
  api_http:
    scenario:
      fail_fast: true
requests:
- id: create
  method: POST
  url: /docs/spec/conformance/cases/fixtures/api_http_created.json
- id: get
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_item_{{steps.create.body_json.id}}.json
- id: cleanup
  method: DELETE
  url: /docs/spec/conformance/cases/fixtures/api_http_deleted.json
```

Use `steps_json` assertions to validate full round-trip order and output.

### Cross-Spec Chain (GET prerequisite -> POST dependent)

Use `harness.chain.steps` when the dependent case should run prerequisite
cases first and consume exported state.

Prerequisite case:

```yaml
id: API-GET-PREREQ
type: api.http
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_created.json
```

Dependent case:

```yaml
id: API-POST-WITH-CHAIN
type: api.http
harness:
  chain:
    steps:
    - id: preload
      class: must
      ref: '#API-GET-PREREQ'
      exports:
        item_id:
          from: body_json
          path: /id
    imports:
    - from: preload
      names:
      - item_id
      as:
        item_id: seed_id
request:
  method: POST
  url: /docs/spec/conformance/cases/fixtures/api_http_item_{{chain.preload.item_id}}.json
```

For chained state sharing:

- do not use `harness.spec_lang.includes` in executable cases
- keep executable prerequisites under `harness.chain.steps`
- set explicit step class (`must|can|cannot`) for every chain step
- export only target-derived values via explicit `exports`
- import only explicit exported names via `harness.chain.imports` (with
  optional renaming)

## Escalation Path

If a failure appears implementation-specific, move from book docs to:

- `/docs/impl/index.md`
- `/docs/impl/python.md`
- `/docs/impl/php.md`
