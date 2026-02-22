# Schema Registry Contract (v2)

## Purpose

The schema registry under `specs/schema/registry/v2/` is the machine source of truth for executable case-shape constraints.

## Normative Rules

- Runtime schema validation MUST be driven from compiled registry data.
- Unknown top-level case keys MUST fail with `schema`.
- Suite top-level validation MUST enforce `spec_version`, `schema_ref`, and non-empty `contracts`.
- Contract-item validation MUST enforce per-item `id` and `clauses` shape.
- Registry profiles MUST use `specs/schema/registry_schema_v1.yaml` shape.
- `specs/schema/schema_v2.md` MUST contain generated registry snapshot
  content and stay synchronized.
- Runtime expectation overrides MUST use `expect.overrides[]` (no `expect.impl.*` wildcard keys).
- Suite runtime metadata MUST define root `harness` (`type`, `profile`, optional `config`).
- Suite runtime services are optional at root.
- When `services` is present, it MUST define non-empty `services.actions[]`.
- Suite MAY declare root `bindings[]` to bind service imports to contracts for
  predicate piping (`service_id.import_name`).
- Contract-job metadata MUST use `services.actions[].config.jobs[]` rows keyed by explicit `id`.
- `contracts[].harness` is invalid in v2 (hard cut).
- `contracts[].clauses.profile` and `contracts[].clauses.config` are invalid in v2 runtime ownership.
- `services.actions[].type` MUST resolve to an entry in `/specs/schema/service_contract_catalog_v1.yaml`;
  unknown service types are hard-fail schema errors.
- `services.actions[].imports` MUST accept canonical list[mapping] rows and
  compact list[string] aliases, normalized to canonical mapping rows before
  runtime evaluation.
- Mixed string/mapping item kinds in one `services.actions[].imports` list are
  invalid.
- Effective declared service import names MUST be unique per service entry and
  MUST exist in catalog `available_imports_by_profile` for resolved
  `type/profile`.
- `services.actions[].config` MUST NOT include direct locator keys (`path`,
  `url`, `token_url`, `template_path`, `output_path`, `ref`).
- Any external locator consumed by service config MUST be declared in
  `artifacts[]` and referenced by `*_artifact_id` (or
  `*_artifact_ids[]`) fields that resolve to `artifacts[].id`.
- `bindings[].contract` MUST resolve to `contracts[].id`; `bindings[].service`
  MUST resolve to `services.actions[].id`.
- `bindings[].inputs[].from` MUST resolve to `artifacts[].id` where `io` is
  `input` or `io`.
- `bindings[].outputs[].to` MUST resolve to `artifacts[].id` where `io` is
  `output` or `io`.
- `from: artifact` imported names MUST resolve to suite-declared artifact ids
  and MUST NOT rely on implicit runtime target injection.
- If `bindings[]` or any `from: service` assertion import is present,
  `services` MUST be declared and valid.
- Suite artifact references MUST be declared only under `artifacts[]`.
- Root `exports[]` MUST be function-only declarations using
  `as` + `from: assert.function` + `path`.
- Documentation metadata surfaces MUST use `docs[]` entry arrays with required
  `summary|audience|status`; singular `doc` is invalid in v2.
- `docs[].id` and `docs[].owners[].id` are optional metadata keys.
- When optional docs/docs-owner ids are omitted, runtimes may emit
  deterministic synthetic labels for diagnostics only.
- Synthetic labels are not schema identity and must not be accepted as
  reference targets.
- `contracts[].clauses.predicates[].id` is required and must be explicitly
  authored.
- Suite defaults and clause defaults are optional compression surfaces; empty
  defaults mappings are non-canonical.

## Profile Types

- `core`
- `assertions`
- `harness`
- `path_model`
- `deprecated type overlays` (migration-only; non-normative)

## Runtime Catalogs

Runtime catalog entries define service additions over common suite/contract keys:

- required suite runtime fields (`harness`; `services.actions[]` when services are used)
- optional service-contract binding field (`bindings[]`)
- service type/profile/io compatibility and available function names
- allowed function operation prefixes per service type

## Determinism

Registry compilation and validation diagnostics must be deterministic and stable
for the same repository state.
