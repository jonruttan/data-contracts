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
- Contracts MAY declare `contracts[].bindings[]` to bind service imports for
  predicate piping (`service_id.import_name`).
- Root `bindings` is invalid in v2 (hard cut).
- Contract-job metadata MUST use `services.actions[].config.jobs[]` rows keyed by explicit `id`.
- `contracts[].harness` is invalid in v2 (hard cut).
- `contracts[].clauses.profile` and `contracts[].clauses.config` are invalid in v2 runtime ownership.
- `services.actions[].type` MUST resolve to an entry in `/specs/schema/service_contract_catalog_v1.yaml`;
  unknown service types are hard-fail schema errors.
- Runtime plugin manifest and lock contracts are defined by
  `/specs/schema/service_plugin_manifest_v1.yaml` and
  `/specs/schema/service_plugin_lock_v1.yaml`.
- Runtime-loaded service plugins MUST be lock-pinned and signature-verified.
- v2 service types are integration-only (`io.fs`, `io.http`, `io.system`,
  `io.mysql`, `io.docs`).
- legacy service types are hard-fail schema errors in v2:
  `assert.check`, `assert.export`, `ops.job`.
- legacy service profile tokens are hard-fail schema errors in v2:
  `text.file`, `api.http`, `cli.run`, `docs.generate`.
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
- `contracts[].bindings` supports canonical list rows (`contracts[].bindings[]`)
  and additive mapping form (`contracts[].bindings.defaults` +
  `contracts[].bindings.rows[]`), normalized to effective rows.
- Mixed list-form and mapping-form bindings in the same contract are invalid.
- Effective binding row = shallow merge(defaults, row), with row values
  overriding defaults.
- Effective binding rows MUST include `id`, `service`, and `import`.
- Effective `service` MUST resolve to `services.actions[].id`.
- `contracts[].clauses.imports` and `contracts[].clauses.predicates[].imports`
  MUST accept bare-string short alias rows that normalize to
  `from: service` rows.
- Bare-string clause/predicate alias rows MUST resolve `service` from
  `contracts[].bindings.defaults.service`; missing/empty defaults service is a
  schema hard-fail.
- Legacy binding row key `contract` is invalid in v2.
- `contracts[].bindings[].inputs[].from` MUST resolve to `artifacts[].id` where `io` is
  `input` or `io`.
- `contracts[].bindings[].outputs[].to` MUST resolve to `artifacts[].id` where `io` is
  `output` or `io`.
- `from: artifact` imported names MUST resolve to suite-declared artifact ids
  and MUST NOT rely on implicit runtime target injection.
- If any `contracts[].bindings[]` or any `from: service` assertion import is present,
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
- optional contract-local binding field (`contracts[].bindings[]`)
- service type/profile/io compatibility and available function names
- integration-mode profile compatibility (`type + profile`) from service catalog
- allowed function operation prefixes per service type

## Determinism

Registry compilation and validation diagnostics must be deterministic and stable
for the same repository state.
