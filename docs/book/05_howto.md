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
2. Add `yaml spec-test` case with `id`, `type`, `assert`.
3. Prefer `evaluate` for policy logic.
4. Run:
   - `./scripts/runner_adapter.sh normalize-check`
   - `./scripts/runner_adapter.sh governance`

## Add Or Reuse A Library Function

1. Add function in a `type: spec_lang.library` file.
2. Keep mapping-AST canonical form.
3. Export symbol through `defines.public`.
4. Import via `harness.spec_lang.includes` and call with `call`.

## Add Markdown Structure Assertions

1. Include markdown helpers:
   - `/docs/spec/libraries/domain/markdown_core.spec.md`
2. Prefer `target: context_json` for structural checks.
3. Use `md.*` helpers for heading/link/token checks.

Example:

```yaml
harness:
  spec_lang:
    includes:
    - /docs/spec/libraries/domain/markdown_core.spec.md
    exports:
    - md.required_sections_present
    - md.link_targets_all_resolve
assert:
- target: context_json
  must:
  - evaluate:
    - call:
      - {var: md.required_sections_present}
      - {var: subject}
      - lit:
        - Purpose
        - Inputs
        - Outputs
    - call:
      - {var: md.link_targets_all_resolve}
      - {var: subject}
```

## Add A Governance Check

1. Add scanner/check implementation and check id.
2. Add governance case under `/docs/spec/governance/cases/core/`.
3. Wire policy + traceability entries.
4. Run full governance pass.

## Run Local Gate Subsets

- Docs only: `./scripts/runner_adapter.sh docs-generate-check`
- Governance only: `./scripts/runner_adapter.sh governance`
- Full local gate: `./scripts/runner_adapter.sh ci-cleanroom`

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
          from_target: body_json
          path: /id
    imports:
    - from_step: preload
      names:
      - item_id
      as:
        item_id: seed_id
request:
  method: POST
  url: /docs/spec/conformance/cases/fixtures/api_http_item_{{chain.preload.item_id}}.json
```

For chained state sharing:

- keep `harness.spec_lang.includes` for library imports only
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
