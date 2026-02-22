# Spec-Test Schema (v2)

This schema defines the stable shape of executable spec tests embedded in
Markdown files selected by case-file pattern (default `*.spec.md`) as fenced blocks:

```text
```yaml contract-spec
...
```

Related docs/reference schemas:

- `specs/schema/docs_schema_v2.md`
- `specs/schema/reference_manifest_v2.md`
- `specs/schema/objective_metrics_schema_v2.md`
- `specs/schema/docs_generator_registry_v2.yaml`
- `specs/schema/docs_layout_profile_v2.yaml`
- `specs/schema/runner_api_catalog_v2.yaml`
- `specs/schema/harness_type_catalog_v2.yaml`
- `specs/schema/spec_lang_builtin_catalog_v2.yaml`
- `specs/schema/spec_lang_stdlib_profile_v2.yaml`
- `specs/schema/subject_profiles_v2.yaml`
- `specs/schema/run_trace_v2.yaml`
- `specs/schema/orchestration_result_v2.yaml`
- `specs/schema/registry_schema_v2.yaml`
- `specs/schema/registry/v2/*.yaml`
- `specs/contract/19_spec_lang_stdlib_profile_v2.md`
- `specs/contract/20_subject_profiles_v2.md`
- `specs/contract/21_schema_registry_contract.md`
- `specs/contract/24_runtime_profiling_contract.md`
```

## Suite Fields

- Machine source of truth for case-shape constraints lives in
  `specs/schema/registry/v2/*.yaml`; this document includes a generated
  registry snapshot section.

- `spec_version` (int, required): schema major used by this suite
- `schema_ref` (string, required): canonical virtual-root schema path
- `contracts` (list, required): non-empty list of executable contract items
- `defaults` (mapping, optional): shallow defaults merged into each contract
  item; defaults should be used only for measurable duplication reduction and
  empty defaults mappings are non-canonical
- `artifact` (mapping, optional): suite-level artifact reference declarations
  - `artifact.imports` (list, optional): artifact import declarations
    - `id` (string, required)
    - `ref` (string, required): supports moustache template expressions (`{{...}}`)
      resolved from suite context
    - `type` (string, optional): expected MIME type for resolved `ref`
    - `inputs` (mapping, optional)
    - `options` (mapping, optional)
    - `docs` (list, optional): documentation metadata entries
  - `artifact.exports` (list, optional): artifact export declarations
    - `id` (string, required)
    - `ref` (string, required): supports moustache template expressions (`{{...}}`)
      resolved from suite context
    - `type` (string, optional): expected MIME type for resolved `ref`
    - `options` (mapping, optional)
    - `docs` (list, optional): documentation metadata entries
- `exports` (list, optional): function export declarations only
  - `exports[].as` (string, required): exported function symbol name
  - `exports[].from` (string, required): must be `assert.function`
  - `exports[].path` (string, required): producer function body path
  - `exports[].params` (list, optional): ordered parameter names
  - `exports[].required` (bool, optional): export requirement flag
  - `exports[].docs` (list, optional): function documentation metadata entries
- `domain` (string, optional): suite-level domain hint
- `title` (string, optional): suite-level label
- `purpose` (string, optional): suite-level description
- `docs` (list, optional): suite-level documentation metadata entries
  - required entry keys: `id`, `summary`, `audience`, `status`
  - optional entry keys: `description`, `type`, `since`, `updated_at`, `tags`, `owners`, `links`, `examples`
  - `docs[].type` enum: `overview|reference|howto|policy|contract|changelog`
  - unknown entry keys are invalid in v2
  - `docs[].id` MUST be unique within each containing `docs[]` array scope

Bundle/package management is not part of `contract-spec` suite shape in v2.
Bundle taxonomy, lock, and package semantics are defined at package-contract
level in:

- `specs/contract/32_contract_bundle_taxonomy.md`
- `specs/contract/33_bundle_package_management.md`
- `specs/contract/34_runner_implementation_spec_bundles.md`
- `specs/schema/bundle_manifest_v1.yaml`
- `specs/schema/resolved_bundle_lock_v1.yaml`
- `specs/schema/project_bundle_lock_v1.yaml`
- `specs/schema/implementation_bundle_overlay_v1.yaml`
- `specs/schema/implementation_bundle_build_lock_v1.yaml`

Each `contracts[]` item:

- `id` (string, required): stable identifier like `CK-CLI-001`
- `clauses` (mapping, required)
- `title`/`purpose`/`domain` (optional overrides)
- `expect`/`requires`/`when` (optional)

Suite runtime surfaces:

- `harness` (mapping, required): suite orchestration surface
  - `harness.type` (string, required)
  - `harness.profile` (string, required)
  - `harness.config` (mapping, required)
- `services` (mapping, required): suite system service bindings with defaults and concrete entries
  - `services.entries[].id` (string, required; unique in suite)
  - `services.entries[].type` (string, required; resolved by `/specs/schema/service_contract_catalog_v1.yaml`)
  - `services.entries[].io` (string, required): `input|output|io`
  - `services.entries[].profile` (string, required)
  - `services.entries[].config` (mapping, required)
  - `services.entries[].default` (bool, optional; at most one `true`)
  - `services.entries[].functions` (list, optional): declarative callable function surface

Parser behavior:

- discovery scans files matching case-file pattern (default `*.spec.md`) in
  the provided directory (non-recursive)
- default discovery is Markdown-only (`*.spec.md`)
- runners MAY opt in additional external case formats via explicit format
  selection (`yaml`, `json`)
- canonical executable spec trees (`specs/conformance/cases`,
  `specs/governance/cases`, `runner-owned implementation specs`) are markdown-only and must
  not include runnable `.spec.yaml`/`.spec.yml`/`.spec.json` files
- fence extraction accepts Markdown fences using either backticks or tildes
  (3+), with info tokens including `contract-spec` and `yaml`/`yml`
- closing fences must use the same fence character and at least the opener
  length
- `contracts` is required and must be non-empty
- `spec_version` is required
- `schema_ref` is required
- each `contracts[]` item requires `id`
- suite `harness` mapping is required
- suite `services.entries[]` list is required and must be non-empty via `services.entries`
- `schema_ref` MUST resolve in `/specs/schema/schema_catalog_v2.yaml`
- `spec_version` MUST match the schema major encoded by `schema_ref`
- root `imports` is invalid in v2
- `artifact.imports[].ref` and `artifact.exports[].ref` MUST be strings
- `artifact.imports[].ref` and `artifact.exports[].ref` template expressions
  use moustache syntax and resolve from suite context only
- unresolved `artifact.imports[].ref`/`artifact.exports[].ref` template
  expressions are schema/runtime failures
- root `exports[]` is function-only:
  - `exports[].from` MUST be `assert.function`
  - `exports[].mode` is invalid
  - `exports[].id` is invalid
  - `exports[].ref` is invalid
- singular `doc` surfaces are invalid in v2; use `docs[]`
- `contracts[].harness` is invalid in v2 (hard cut)
- `contracts[].clauses.profile` and `contracts[].clauses.config` are invalid in v2 runtime ownership
- unknown `services.entries[].type` MUST hard-fail during schema validation
- invalid `services.entries[].io` MUST hard-fail during schema validation
- legacy `type` on contract items is invalid in v2

`expect` (conformance metadata):

- `portable` (mapping): shared expectation baseline
- `overrides` (list, optional): runtime-specific overlays with explicit `runner`
- expected keys in `portable`/`overrides[]`:
  - `status`: `pass`, `fail`, or `skip`
  - `category`: `schema` / `assertion` / `runtime` / `null`
  - `message_tokens`: optional list of expected message tokens
- for conformance fixture cases, `expect.portable` with `status` is required

`requires` (metadata):

- `capabilities` (list[string], optional): declared capabilities for the case
- `when_missing` (string, optional): `skip` or `fail` (default `fail`)

## Portable Authoring Profile

For implementation-independent conformance specs:

- Canonical case set lives in `specs/conformance/cases/**/*.spec.md`.
- Portable expectations are defined in `expect.portable`.
- Runtime deltas are expressed via `expect.overrides[]`.
- Portable cases SHOULD be deterministic and avoid ambient dependency on:
  - time/date/timezone
  - randomness without explicit seeded input
  - network access
  - undeclared environment variables

Normative contract details:

- `specs/contract/06_conformance.md`
- `specs/contract/07_portable_spec_authoring.md`

## Harness-Profile Fields

### `harness.type: unit.test` with `services.entries[].profile: text.file`

`text.file` asserts against file content.

- If `path` is omitted, the runner asserts against the spec document that
  contains the `yaml contract-spec` block.
- If `path` is provided, it MUST be a relative path and is resolved relative to
  contract root (virtual `/`) and normalized to canonical `/...`.
- Resolved `path` MUST remain within the implementation's configured contract
  root/workspace boundary (path traversal outside that boundary is invalid).

Fields:

- `path` (string, optional): virtual-root path (`/docs/...`) or root-relative
  path string normalized to `/...`

Assertion targets for `text.file`:

- `text`
- `context_json`: JSON subject profile envelope
- `meta_json`: runtime metadata envelope

Markdown library authoring guidance:

- markdown helper predicates SHOULD target `context_json` when asserting
  structured document properties (headings, links, token ownership/dependencies)
- text-only assertions SHOULD be limited to literal text obligations
- markdown domain helpers accept dual input:
  - raw markdown string
  - markdown profile envelope (`value` + optional `context`)

## Harness Dispatch

Harness dispatch is selected by suite-root `harness` and service execution/binding is selected by suite-root `services.entries[]`. Runtime profile/config data is declared in `harness.profile`/`harness.config` and `services.entries[].profile`/`services.entries[].config`.

Governance assertion contract:

- For governance check profiles, decision obligations MUST be encoded in
  `clauses` blocks.
- ad-hoc service evaluate surfaces are forbidden.
- Extractors may emit candidate violations and subject payloads, but MUST NOT
  be the source of final decision truth.

Assertion targets for `governance.check`:

- `text`: human-readable PASS/FAIL summary output
- `summary_json`: structured summary target; `evaluate` receives summary mapping
  with `passed`, `check_id`, `case_id`, `violation_count`
- `violation_count`: integer violation count target
- `context_json`: optional JSON subject profile envelope
- `meta_json`: runtime metadata envelope

Security model:

- Spec tests are trusted inputs. `cli.run` and hook entrypoints can execute
  project code/commands with runner process privileges.
- Running untrusted spec documents is unsafe and out of scope for v2.
- Implementations MAY pass process environment variables to `cli.run`; keep
  sensitive env values out of runner contexts where possible.
- `data-contracts` is not a sandbox and MUST NOT be presented/documented as one.

For `harness.type: unit.test` with `services.entries[].profile: cli.run`, supported `services.entries[].config` keys include:

- `entrypoint` (string, recommended): CLI entrypoint to call (e.g. `myproj.cli:main`)
- `env` (mapping): env vars to set/unset before running the CLI
- `stdin_isatty` (bool): simulate TTY vs piped stdin
- `stdin_text` (string): text to provide on stdin
- `block_imports` (list[string]): make imports fail with `ModuleNotFoundError`
- `stub_modules` (list[string]): pre-populate `sys.modules` with stubs
- `setup_files` (list[{path, text}]): write files under the runner temp dir
- `hook_before` (string): hook entrypoint invoked before running the CLI
- `hook_after` (string): hook entrypoint invoked after running the CLI
- `hook_kwargs` (mapping): keyword arguments passed through to the hook
- `spec_lang` (mapping): evaluator budgets for `evaluate` leaves
- `orchestration` (mapping): orchestration tool dispatch contract for
  orchestration profiles

For `harness.type: unit.test` with `services.entries[].profile: api.http`, supported `services.entries[].config` keys include:

- `api_http.mode` (string): `deterministic` (default) or `live`
- `api_http.scenario` (mapping, optional):
  - `setup.command` (list[string])
  - `setup.cwd` (virtual-root path, optional)
  - `setup.env` (mapping, optional)
  - `setup.ready_probe` (mapping, optional)
  - `teardown.command` (list[string])
  - `teardown.cwd` (virtual-root path, optional)
  - `teardown.env` (mapping, optional)
  - `fail_fast` (bool, default `true`)
- `api_http.auth.oauth` (mapping):
  - `grant_type`: `client_credentials`
  - `token_url`: token endpoint URL or contract path
  - `client_id_env`: env var name for OAuth client id
  - `client_secret_env`: env var name for OAuth client secret
  - `scope` (optional)
  - `audience` (optional)
  - `auth_style`: `basic` (default) or `body`
  - `token_field`: token field in token response (default `access_token`)
  - `expires_field`: expiry field in token response (default `expires_in`)
  - `refresh_skew_seconds`: cache skew (default `30`)

OAuth and execution rules:

- credentials MUST be env references (`*_env`) only; inline secrets are invalid
- network `http(s)` token/request URLs require `api_http.mode: live`
- deterministic mode forbids network token/request fetches
- context profile metadata MUST redact secret/token values

`api.http` request shape:

- `request` (mapping) for single-request cases, or `requests` (non-empty list) for scenario cases
- request fields:
  - `method`: `GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS`
  - `url`
  - `headers` (optional mapping)
  - `query` (optional mapping; merged into URL deterministically)
  - `body_text` / `body_json` (mutually exclusive)
  - `cors` (optional mapping):
    - `origin`
    - `request_method` (required when `preflight=true`)
    - `request_headers` (optional list)
    - `preflight` (optional bool, default `false`)

`api.http` additional assert targets:

- `cors_json` (normalized CORS projection for final response)
- `steps_json` (ordered step envelopes in scenario mode)

For `harness.type: unit.test` with `services.entries[].profile: docs.generate`, supported `services.entries[].config` keys include:

- `docs_generate.surface_id` (required)
- `docs_generate.mode` (required): `write|check`
- `docs_generate.output_mode` (required): `markers|full_file`
- `docs_generate.template_path` (required): virtual-root path
- `docs_generate.output_path` (required): virtual-root path
- `docs_generate.marker_surface_id` (required when `output_mode=markers`)
- `docs_generate.data_sources` (required list):
  - `id`
  - `source_type`: `json_file|yaml_file|generated_artifact|command_output`
  - `path` for file/artifact source types
  - `command` for `command_output` source type
- `docs_generate.strict` (optional bool, default `true`)

`setup_files[*].path` constraints:

- MUST be relative
- MUST resolve within the runner temp directory (no path escape)

`clauses.config.spec_lang` fields:

- `max_steps` (int, >=1)
- `max_nodes` (int, >=1)
- `max_literal_bytes` (int, >=1)
- `timeout_ms` (int, >=0, `0` disables timeout)
- `includes` (list[string], optional): library include files (library docs only)
- `exports` (list[string], optional): symbol allowlist exposed to this case
- `imports` (list[mapping], optional): case-scoped stdlib imports
  - `from` (string, required): `std.*` namespace prefix
  - `names` (list[string], required): symbols imported from namespace
  - `as` (mapping, optional): alias map `symbol -> local_name`
- `references` (mapping, optional): external reference policy
  - `mode` (string): `deny` (default) or `allow`
  - `providers` (list[string]): allowlisted provider names
  - `rules` (mapping, optional): provider-specific rule payloads for adapters
- `capabilities` (list[string], optional): explicit evaluator capabilities
  (for example `ops.os`).

`clauses.config.spec_lang.includes` format scope:

- library include paths MAY target `.spec.md`, `.spec.yaml`, or `.spec.yml`
  files
- library include paths use virtual-root semantics (`/` means contract root);
  root-relative values normalize to canonical `/...`
- external references use `external://provider/id` and are deny-by-default
  unless capability and harness policy explicitly allow provider access
- producer cases define reusable symbols through root `exports[]` entries using
  `from: assert.function`; function
  bodies are sourced from producer contract-step `asserts` expression mappings
- Canonical export source marker is ``assert.function``.
- default executable case discovery remains Markdown-only (`*.spec.md`) unless
  explicit format opt-in is provided by the runner interface
- executable case types MUST NOT declare `clauses.config.spec_lang.includes`;
  executable symbol loading is chain-first via `harness.chain`

`harness.chain` fields:

- `fail_fast` (bool, optional, default `true`)
- `steps` (list, required when `harness.chain` is present; non-empty)
  - each step:
    - `id` (string, required, unique)
    - `required` (bool, optional, default `true`)
    - `priority` (int, optional, default `1`, minimum `1`)
    - `severity` (int, optional, default `1`, minimum `1`)
    - `purpose` (string, optional, non-empty when provided)
    - `ref` (string, required): `[path][#case_id]`
      - path may be virtual-absolute (`/...`) or relative
      - `#case_id` fragment is optional
      - `#case_id` with no preceding path is valid and resolves in current doc
      - case id fragment must match `[A-Za-z0-9._:-]+` when present
      - YAML authors should quote hash-only refs (for example `ref: "#CASE-1"`)
    - `imports` (forbidden non-canonical location)
    - `exports` (forbidden non-canonical location)
    - `allow_continue` (bool, optional, default `false`)
- `exports` (list, optional): producer-owned export declarations
  - each entry:
    - `as` (string, required)
    - `from` (string, required; must be `assert.function`)
    - `path` (string, required for `from: assert.function`)
    - `params` (list[string], optional; non-empty when provided)
    - `required` (bool, optional; default `true`)
  - non-canonical key `from_target` is forbidden
- `imports` (list[mapping], optional)
  - each import:
    - `from` (string, required): source step id
    - `names` (list[string], required): exported names from that step
    - `as` (mapping, optional): alias map `name -> local_name`
  - local imported names and aliases must be unique
  - local imported names and aliases must not shadow reserved names:
    `subject`, `if`, `let`, `fn`, `call`, `var`

Chain reference resolution:

- `#case_id`: resolve one exact case within current `.spec.md` document.
- `path#case_id`: resolve one exact case in referenced document.
- `path`: execute all cases in referenced document in order.
- relative paths resolve from current `.spec.md` document directory.

Chain execution model:

- all executable case types may declare `harness.chain`.
- chain state sharing is explicit via step-level `imports` + `harness.chain.imports`.
- top-level `chain` and type-specific `*.chain` aliases are forbidden.
- scalar `ref` is the only supported reference format; non-canonical mapping refs are
  invalid.

Chain template interpolation:

- `api.http` request `url`, header values, and `body_text` support
  `{{chain.<step_id>.<export_name>}}` lookups from exported chain state.
- unresolved chain template references are schema/runtime failures.

Documentation generator model:

- docs generation surfaces are declared in
  `specs/schema/docs_generator_registry_v2.yaml`.
- generator-owned markdown sections MUST use read-only markers:
  - `<!-- GENERATED:START surface_id -->`
  - `<!-- GENERATED:END surface_id -->`
- CI/governance check mode MUST verify generated docs artifacts are synchronized.

Implementation note:

- `clauses.config.entrypoint` is required for `cli.run` execution.
- Conformance fixtures SHOULD always set explicit entrypoint config.
- Runners MAY provide a safe mode (for example `SPEC_RUNNER_SAFE_MODE=1`) that
  disables hook execution for `cli.run`.
- Runners MAY provide environment allowlisting for subprocess execution (for
  example `SPEC_RUNNER_ENV_ALLOWLIST=K1,K2`).

Assertion targets for `cli.run`:

- `stdout`: text output from command stdout
- `stderr`: text output from command stderr
- `stdout_path`: path printed on first non-empty stdout line
- `stdout_path_text`: UTF-8 text from file at `stdout_path`
- `chain_json`: shared chain state/trace/imports envelope
- `context_json`: JSON subject profile envelope
- `meta_json`: runtime metadata envelope

## Profiles

Currently supported `services.entries[].profile` values include:

- `cli.run` (core)
- `text.file` (core)
- `docs.generate` (core extension)
- `orchestration.run` (core extension)

Profile contracts live under:

- `specs/contract/types/`

Domain-specific adapters are expected to publish a matching profile contract doc
before portable conformance usage.

Published extension profile contracts:

- `api.http` (see `specs/contract/types/api_http.md`)

## Assertion Capability Model (Universal Core)

Universal core assertion model:

- every leaf assertion is a spec-lang mapping AST expression.
- every leaf assertion is represented with operator-keyed mappings.
- universal core operator semantics are evaluate-only at runtime.
- evaluator subjects MUST be JSON values only (`null`, boolean, number, string,
  list, object with string keys).

## Assertion Predicate Shape

`clauses` is a mapping with:

- `defaults` (optional mapping)
- `predicates` (required list)

Each `predicates[]` entry requires:

- `id` (string, unique per case)
- `assert` (non-empty expression mapping or list)
- `imports` (optional list)
- `purpose` (optional string)
- `required` (optional bool, default `true`)
- `priority` (optional int, default `1`, must be `>=1`)
- `severity` (optional int, default `1`, must be `>=1`)

Forbidden prior forms:

- `clauses` list form
- predicate key `asserts`
- predicate keys `target` and `on`

Import binding shape:

- `imports` is a list of mapping items
- each item requires `from` and `names`, with optional `as`
- canonical assertion imports are artifact-only (`from: artifact`)
- `names` must be a non-empty list of artifact keys
- `as` is optional mapping `source_name -> local_name`

Import merge behavior:

- effective predicate imports = `clauses.imports` merged with
  `clauses.predicates[].imports`
- predicate imports override defaults on key collision

Symbol resolution:

- `{var: subject}` is valid only when `subject` is explicitly imported
- implicit subject/target injection is forbidden in canonical authoring

Supported operators:

- universal core operator: spec-lang v2 operator-keyed mappings at each leaf

Core executable-surface rule:

- `specs/conformance/cases/**/*.spec.md` assertion trees MUST use
  direct spec-lang expression leaves.
- `specs/governance/cases/**/*.spec.md` assertion trees MUST use
  direct spec-lang expression leaves.

Operator constraints:

- all operator values MUST be lists
- each assertion leaf MUST be an expression node using an operator-keyed mapping
- subject reference node: `{var: subject}` resolves via explicit imports
- bare scalar `subject` is a literal string (not a reference)
- spec-lang semantics and budget model are defined in
  `specs/contract/03b_spec_lang_v2.md`
- spec-lang v2 includes deep-equality set algebra (`union`, `intersection`,
  `difference`, `symmetric_difference`, `is_subset`, `is_superset`,
  `set_equals`) and collection transforms (`map`, `filter`, `reduce`, etc.)
  with automatic builtin currying semantics
- spec-lang ramda-style utility surface includes strict numeric math
  (`mul`, `div`, `mod`, `pow`, `abs`, `negate`, `inc`, `dec`, `clamp`,
  `round`, `floor`, `ceil`), comparison/logical helpers (`compare`, `between`,
  `xor`), list utilities (`slice`, `reverse`, `zip`, `zip_with`, `range`,
  `repeat`), object helpers (`keys`, `values`, `entries`, `merge`, `assoc`,
  `dissoc`, `pick`, `omit`), and compositional predicates/combinators
  (`prop_eq`, `where`, `compose`, `pipe`, `identity`, `always`, `replace`,
  `pad_left`, `pad_right`) plus explicit JSON-type predicates (`is_null`,
  `is_bool`/`is_boolean`, `is_number`, `is_string`,
  `is_list`/`is_array`, `is_dict`/`is_object`)
- spec-lang shared library loading rules are defined in
  `specs/contract/14_spec_lang_libraries.md`
- runtime pass/fail decisions MUST execute through compiled spec-lang
  expressions
- orchestration effect symbol names use deep-dot `ops.*` hierarchy:
  `ops.<segment>(.<segment>)+` (for example `ops.fs.file.read`,
  `ops.proc.command.exec`)
- pure spec-lang utility symbols may also use `ops.*` namespaces
  (for example `ops.fs.path.normalize`, `ops.fs.file.exists`) and MUST remain
  deterministic with no evaluator side effects
- pure JSON helpers under `ops.fs.json.*` are allowed for parse/path lookup
  (`parse`, `get`, `get_or`, `has_path`) and remain evaluator-pure
- pure glob helpers under `ops.fs.glob.*` are allowed for deterministic
  pattern matching/filtering (`match`, `filter`, `any`, `all`)
- underscore shorthand ops symbols are invalid
- path fields in scoped harness/type config use virtual-root canonical `/...`
  form; `..` contract-root escapes are invalid
- regex portability guidance for spec-lang expressions is defined in
  `specs/contract/03a_regex_portability_v2.md`

Step metadata constraints:

- `clauses.predicates[].required` is optional and defaults to `true`
- `clauses.predicates[].priority` is optional integer metadata (`>=1`, default `1`)
- `clauses.predicates[].severity` is optional integer metadata (`>=1`, default `1`)
- `clauses.predicates[].purpose` is optional human-readable text
- optional predicates (`required: false`) are non-blocking for overall case verdict
- prohibition intent is expressed directly with negation operators
  (for example `std.logic.not`)

Canonical negation form:

```yaml
clauses:
  imports:
  - from: artifact
    names: [text]
    as:
      text: subject
  predicates:
  - id: assert_no_error
    required: true
    assert:
      std.logic.not:
      - std.string.contains:
        - {var: subject}
        - 'ERROR:'
```

Author in canonical form:

- use explicit assertion expressions; do not use step classes
- use `required: false` for non-blocking steps
- use `priority` / `severity` as metadata-only ranking hints
- use direct operator mappings in `assert` (no `evaluate` wrapper)
- put every operator value in a list

Example with defaults + step override imports:

```yaml
clauses:
  imports:
  - from: artifact
    names: [summary_json]
    as:
      summary_json: subject
  predicates:
  - id: assert_passed
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
  - id: assert_violation_count
    imports:
    - from: artifact
      names: [violation_count]
      as:
        violation_count: subject
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```

`when` lifecycle hooks:

- optional `when` mapping on executable cases
- non-canonical `harness.on` is forbidden (hard cut)
- allowed keys:
  - `required`
  - `optional`
  - `fail`
  - `complete`
- each hook key, when present, must be a non-empty list of mapping-AST expressions
- hook expressions evaluate with existing case spec-lang limits/imports/symbols/capabilities
- hook failures are runtime-fatal

Lifecycle order:

- `required` hook runs after successful required-step evaluation
- `optional` hook runs after successful optional-step evaluation
- `fail` runs once on first blocking step or hook failure
- `complete` runs only after all steps and hooks pass

`services.entries[].type: ops.job` executable profile (v2):

- `harness.type: unit.test` + `services.entries[].type: ops.job`
- required:
  - `clauses.config.jobs` (metadata list)
  - `clauses`
- optional:
  - `clauses.config.jobs[].mode`
  - `clauses.config.jobs[].inputs`
  - `clauses.config.jobs[].outputs`

Dispatch clauses:

- dispatch is contract-driven using `ops.job.dispatch`
- dispatch metadata is read from `clauses.config.jobs[]` matched by `id`
- `clauses.config.job` non-canonical singular form is forbidden
- `ops.job.dispatch` requires `clauses.config.spec_lang.capabilities` to include `ops.job`

Job ref grammar:

- absolute/virtual ref: `/path/to/file.spec.md#CASE-ID`
- same-doc ref: `#CASE-ID` (requires caller-provided document context)
- non-scalar refs are invalid
- missing path/case resolution is schema/runtime error

<!-- BEGIN GENERATED: SCHEMA_REGISTRY_V2 -->

## Generated Registry Snapshot

This section is generated from `specs/schema/registry/v2/*.yaml`.

- profile_count: 4
- top_level_fields: 221
- service_catalog: `/specs/schema/service_contract_catalog_v1.yaml`

### Top-Level Keys

| key | type | required | since |
|---|---|---|---|
| `spec_version` | `int` | `true` | `v2` |
| `schema_ref` | `string` | `true` | `v2` |
| `defaults` | `mapping` | `false` | `v2` |
| `harness` | `mapping` | `true` | `v2` |
| `harness.type` | `string` | `true` | `v2` |
| `harness.profile` | `string` | `true` | `v2` |
| `harness.config` | `mapping` | `true` | `v2` |
| `harness.docs` | `list` | `false` | `v2` |
| `harness.docs[].id` | `string` | `true` | `v2` |
| `harness.docs[].summary` | `string` | `true` | `v2` |
| `harness.docs[].audience` | `string` | `true` | `v2` |
| `harness.docs[].status` | `string` | `true` | `v2` |
| `harness.docs[].description` | `string` | `false` | `v2` |
| `harness.docs[].type` | `string` | `false` | `v2` |
| `harness.docs[].since` | `string` | `false` | `v2` |
| `harness.docs[].updated_at` | `string` | `false` | `v2` |
| `harness.docs[].tags` | `list` | `false` | `v2` |
| `harness.docs[].owners` | `list` | `false` | `v2` |
| `harness.docs[].owners[].id` | `string` | `true` | `v2` |
| `harness.docs[].owners[].role` | `string` | `true` | `v2` |
| `harness.docs[].links` | `list` | `false` | `v2` |
| `harness.docs[].links[].rel` | `string` | `true` | `v2` |
| `harness.docs[].links[].ref` | `string` | `true` | `v2` |
| `harness.docs[].links[].title` | `string` | `false` | `v2` |
| `harness.docs[].examples` | `list` | `false` | `v2` |
| `harness.docs[].examples[].title` | `string` | `true` | `v2` |
| `harness.docs[].examples[].ref` | `string` | `true` | `v2` |
| `services` | `list` | `true` | `v2` |
| `services.entries[].id` | `string` | `true` | `v2` |
| `services.entries[].type` | `string` | `true` | `v2` |
| `services.entries[].io` | `string` | `true` | `v2` |
| `services.entries[].profile` | `string` | `true` | `v2` |
| `services.entries[].config` | `mapping` | `true` | `v2` |
| `services.entries[].default` | `bool` | `false` | `v2` |
| `services.entries[].functions` | `list` | `false` | `v2` |
| `services.entries[].functions[].name` | `string` | `true` | `v2` |
| `services.entries[].functions[].op` | `string` | `true` | `v2` |
| `services.entries[].functions[].params` | `list` | `false` | `v2` |
| `services.entries[].docs` | `list` | `false` | `v2` |
| `services.entries[].docs[].id` | `string` | `true` | `v2` |
| `services.entries[].docs[].summary` | `string` | `true` | `v2` |
| `services.entries[].docs[].audience` | `string` | `true` | `v2` |
| `services.entries[].docs[].status` | `string` | `true` | `v2` |
| `services.entries[].docs[].description` | `string` | `false` | `v2` |
| `services.entries[].docs[].type` | `string` | `false` | `v2` |
| `services.entries[].docs[].since` | `string` | `false` | `v2` |
| `services.entries[].docs[].updated_at` | `string` | `false` | `v2` |
| `services.entries[].docs[].tags` | `list` | `false` | `v2` |
| `services.entries[].docs[].owners` | `list` | `false` | `v2` |
| `services.entries[].docs[].owners[].id` | `string` | `true` | `v2` |
| `services.entries[].docs[].owners[].role` | `string` | `true` | `v2` |
| `services.entries[].docs[].links` | `list` | `false` | `v2` |
| `services.entries[].docs[].links[].rel` | `string` | `true` | `v2` |
| `services.entries[].docs[].links[].ref` | `string` | `true` | `v2` |
| `services.entries[].docs[].links[].title` | `string` | `false` | `v2` |
| `services.entries[].docs[].examples` | `list` | `false` | `v2` |
| `services.entries[].docs[].examples[].title` | `string` | `true` | `v2` |
| `services.entries[].docs[].examples[].ref` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs` | `list` | `false` | `v2` |
| `services.entries[].functions[].docs[].id` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].summary` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].audience` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].status` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].description` | `string` | `false` | `v2` |
| `services.entries[].functions[].docs[].type` | `string` | `false` | `v2` |
| `services.entries[].functions[].docs[].since` | `string` | `false` | `v2` |
| `services.entries[].functions[].docs[].updated_at` | `string` | `false` | `v2` |
| `services.entries[].functions[].docs[].tags` | `list` | `false` | `v2` |
| `services.entries[].functions[].docs[].owners` | `list` | `false` | `v2` |
| `services.entries[].functions[].docs[].owners[].id` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].owners[].role` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].links` | `list` | `false` | `v2` |
| `services.entries[].functions[].docs[].links[].rel` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].links[].ref` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].links[].title` | `string` | `false` | `v2` |
| `services.entries[].functions[].docs[].examples` | `list` | `false` | `v2` |
| `services.entries[].functions[].docs[].examples[].title` | `string` | `true` | `v2` |
| `services.entries[].functions[].docs[].examples[].ref` | `string` | `true` | `v2` |
| `artifact` | `mapping` | `false` | `v2` |
| `artifact.imports` | `list` | `false` | `v2` |
| `artifact.imports[].id` | `string` | `true` | `v2` |
| `artifact.imports[].ref` | `string` | `true` | `v2` |
| `artifact.imports[].type` | `string` | `false` | `v2` |
| `artifact.imports[].inputs` | `mapping` | `false` | `v2` |
| `artifact.imports[].options` | `mapping` | `false` | `v2` |
| `artifact.imports[].docs` | `list` | `false` | `v2` |
| `artifact.imports[].docs[].id` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].summary` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].audience` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].status` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].description` | `string` | `false` | `v2` |
| `artifact.imports[].docs[].type` | `string` | `false` | `v2` |
| `artifact.imports[].docs[].since` | `string` | `false` | `v2` |
| `artifact.imports[].docs[].updated_at` | `string` | `false` | `v2` |
| `artifact.imports[].docs[].tags` | `list` | `false` | `v2` |
| `artifact.imports[].docs[].owners` | `list` | `false` | `v2` |
| `artifact.imports[].docs[].owners[].id` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].owners[].role` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].links` | `list` | `false` | `v2` |
| `artifact.imports[].docs[].links[].rel` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].links[].ref` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].links[].title` | `string` | `false` | `v2` |
| `artifact.imports[].docs[].examples` | `list` | `false` | `v2` |
| `artifact.imports[].docs[].examples[].title` | `string` | `true` | `v2` |
| `artifact.imports[].docs[].examples[].ref` | `string` | `true` | `v2` |
| `artifact.exports` | `list` | `false` | `v2` |
| `artifact.exports[].id` | `string` | `true` | `v2` |
| `artifact.exports[].ref` | `string` | `true` | `v2` |
| `artifact.exports[].type` | `string` | `false` | `v2` |
| `artifact.exports[].options` | `mapping` | `false` | `v2` |
| `artifact.exports[].docs` | `list` | `false` | `v2` |
| `artifact.exports[].docs[].id` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].summary` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].audience` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].status` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].description` | `string` | `false` | `v2` |
| `artifact.exports[].docs[].type` | `string` | `false` | `v2` |
| `artifact.exports[].docs[].since` | `string` | `false` | `v2` |
| `artifact.exports[].docs[].updated_at` | `string` | `false` | `v2` |
| `artifact.exports[].docs[].tags` | `list` | `false` | `v2` |
| `artifact.exports[].docs[].owners` | `list` | `false` | `v2` |
| `artifact.exports[].docs[].owners[].id` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].owners[].role` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].links` | `list` | `false` | `v2` |
| `artifact.exports[].docs[].links[].rel` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].links[].ref` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].links[].title` | `string` | `false` | `v2` |
| `artifact.exports[].docs[].examples` | `list` | `false` | `v2` |
| `artifact.exports[].docs[].examples[].title` | `string` | `true` | `v2` |
| `artifact.exports[].docs[].examples[].ref` | `string` | `true` | `v2` |
| `exports` | `list` | `false` | `v2` |
| `exports[].as` | `string` | `true` | `v2` |
| `exports[].from` | `string` | `true` | `v2` |
| `exports[].path` | `string` | `true` | `v2` |
| `exports[].params` | `list` | `false` | `v2` |
| `exports[].required` | `bool` | `false` | `v2` |
| `exports[].docs` | `list` | `false` | `v2` |
| `exports[].docs[].id` | `string` | `true` | `v2` |
| `exports[].docs[].summary` | `string` | `true` | `v2` |
| `exports[].docs[].audience` | `string` | `true` | `v2` |
| `exports[].docs[].status` | `string` | `true` | `v2` |
| `exports[].docs[].description` | `string` | `false` | `v2` |
| `exports[].docs[].type` | `string` | `false` | `v2` |
| `exports[].docs[].since` | `string` | `false` | `v2` |
| `exports[].docs[].updated_at` | `string` | `false` | `v2` |
| `exports[].docs[].tags` | `list` | `false` | `v2` |
| `exports[].docs[].owners` | `list` | `false` | `v2` |
| `exports[].docs[].owners[].id` | `string` | `true` | `v2` |
| `exports[].docs[].owners[].role` | `string` | `true` | `v2` |
| `exports[].docs[].links` | `list` | `false` | `v2` |
| `exports[].docs[].links[].rel` | `string` | `true` | `v2` |
| `exports[].docs[].links[].ref` | `string` | `true` | `v2` |
| `exports[].docs[].links[].title` | `string` | `false` | `v2` |
| `exports[].docs[].examples` | `list` | `false` | `v2` |
| `exports[].docs[].examples[].title` | `string` | `true` | `v2` |
| `exports[].docs[].examples[].ref` | `string` | `true` | `v2` |
| `contracts` | `list` | `true` | `v2` |
| `contracts[].id` | `string` | `true` | `v2` |
| `title` | `string` | `false` | `v2` |
| `purpose` | `string` | `false` | `v2` |
| `docs` | `list` | `false` | `v2` |
| `docs[].id` | `string` | `true` | `v2` |
| `docs[].summary` | `string` | `true` | `v2` |
| `docs[].audience` | `string` | `true` | `v2` |
| `docs[].status` | `string` | `true` | `v2` |
| `docs[].description` | `string` | `false` | `v2` |
| `docs[].type` | `string` | `false` | `v2` |
| `docs[].since` | `string` | `false` | `v2` |
| `docs[].updated_at` | `string` | `false` | `v2` |
| `docs[].tags` | `list` | `false` | `v2` |
| `docs[].owners` | `list` | `false` | `v2` |
| `docs[].owners[].id` | `string` | `true` | `v2` |
| `docs[].owners[].role` | `string` | `true` | `v2` |
| `docs[].links` | `list` | `false` | `v2` |
| `docs[].links[].rel` | `string` | `true` | `v2` |
| `docs[].links[].ref` | `string` | `true` | `v2` |
| `docs[].links[].title` | `string` | `false` | `v2` |
| `docs[].examples` | `list` | `false` | `v2` |
| `docs[].examples[].title` | `string` | `true` | `v2` |
| `docs[].examples[].ref` | `string` | `true` | `v2` |
| `domain` | `string` | `false` | `v2` |
| `contracts[].title` | `string` | `false` | `v2` |
| `contracts[].purpose` | `string` | `false` | `v2` |
| `contracts[].domain` | `string` | `false` | `v2` |
| `contracts[].docs` | `list` | `false` | `v2` |
| `contracts[].docs[].id` | `string` | `true` | `v2` |
| `contracts[].docs[].summary` | `string` | `true` | `v2` |
| `contracts[].docs[].audience` | `string` | `true` | `v2` |
| `contracts[].docs[].status` | `string` | `true` | `v2` |
| `contracts[].docs[].description` | `string` | `false` | `v2` |
| `contracts[].docs[].type` | `string` | `false` | `v2` |
| `contracts[].docs[].since` | `string` | `false` | `v2` |
| `contracts[].docs[].updated_at` | `string` | `false` | `v2` |
| `contracts[].docs[].tags` | `list` | `false` | `v2` |
| `contracts[].docs[].owners` | `list` | `false` | `v2` |
| `contracts[].docs[].owners[].id` | `string` | `true` | `v2` |
| `contracts[].docs[].owners[].role` | `string` | `true` | `v2` |
| `contracts[].docs[].links` | `list` | `false` | `v2` |
| `contracts[].docs[].links[].rel` | `string` | `true` | `v2` |
| `contracts[].docs[].links[].ref` | `string` | `true` | `v2` |
| `contracts[].docs[].links[].title` | `string` | `false` | `v2` |
| `contracts[].docs[].examples` | `list` | `false` | `v2` |
| `contracts[].docs[].examples[].title` | `string` | `true` | `v2` |
| `contracts[].docs[].examples[].ref` | `string` | `true` | `v2` |
| `contracts[].when` | `mapping` | `false` | `v2` |
| `contracts[].when.required` | `list` | `false` | `v2` |
| `contracts[].when.optional` | `list` | `false` | `v2` |
| `contracts[].when.fail` | `list` | `false` | `v2` |
| `contracts[].when.complete` | `list` | `false` | `v2` |
| `contracts[].clauses` | `mapping` | `true` | `v2` |
| `contracts[].expect` | `mapping` | `false` | `v2` |
| `contracts[].expect.portable` | `mapping` | `false` | `v2` |
| `contracts[].expect.portable.status` | `string` | `false` | `v2` |
| `contracts[].expect.portable.category` | `string` | `false` | `v2` |
| `contracts[].expect.portable.message_tokens` | `list` | `false` | `v2` |
| `contracts[].expect.overrides` | `list` | `false` | `v2` |
| `contracts[].expect.overrides[].runner` | `string` | `true` | `v2` |
| `contracts[].expect.overrides[].status` | `string` | `false` | `v2` |
| `contracts[].expect.overrides[].category` | `string` | `false` | `v2` |
| `contracts[].expect.overrides[].message_tokens` | `list` | `false` | `v2` |
| `contracts[].requires` | `mapping` | `false` | `v2` |

### Runtime Surfaces

| surface | required keys | catalog |
|---|---|---|
| `harness` | `harness.type`, `harness.profile`, `harness.config` | n/a |
| `services.entries[]` | `services.entries[].id`, `services.entries[].type`, `services.entries[].io`, `services.entries[].profile`, `services.entries[].config` | `/specs/schema/service_contract_catalog_v1.yaml` |

<!-- END GENERATED: SCHEMA_REGISTRY_V2 -->
<!-- GENERATED:START spec_schema_field_catalog -->

## Generated Spec Schema Field Catalog

- top_level_field_count: 221
- harness_surface: suite-root `harness`
- service_catalog: `/specs/schema/service_contract_catalog_v1.yaml`

### Top-Level Fields

| key | type | required | since |
|---|---|---|---|
| `spec_version` | `int` | true | `v2` |
| `schema_ref` | `string` | true | `v2` |
| `defaults` | `mapping` | false | `v2` |
| `harness` | `mapping` | true | `v2` |
| `harness.type` | `string` | true | `v2` |
| `harness.profile` | `string` | true | `v2` |
| `harness.config` | `mapping` | true | `v2` |
| `harness.docs` | `list` | false | `v2` |
| `harness.docs[].id` | `string` | true | `v2` |
| `harness.docs[].summary` | `string` | true | `v2` |
| `harness.docs[].audience` | `string` | true | `v2` |
| `harness.docs[].status` | `string` | true | `v2` |
| `harness.docs[].description` | `string` | false | `v2` |
| `harness.docs[].type` | `string` | false | `v2` |
| `harness.docs[].since` | `string` | false | `v2` |
| `harness.docs[].updated_at` | `string` | false | `v2` |
| `harness.docs[].tags` | `list` | false | `v2` |
| `harness.docs[].owners` | `list` | false | `v2` |
| `harness.docs[].owners[].id` | `string` | true | `v2` |
| `harness.docs[].owners[].role` | `string` | true | `v2` |
| `harness.docs[].links` | `list` | false | `v2` |
| `harness.docs[].links[].rel` | `string` | true | `v2` |
| `harness.docs[].links[].ref` | `string` | true | `v2` |
| `harness.docs[].links[].title` | `string` | false | `v2` |
| `harness.docs[].examples` | `list` | false | `v2` |
| `harness.docs[].examples[].title` | `string` | true | `v2` |
| `harness.docs[].examples[].ref` | `string` | true | `v2` |
| `services` | `list` | true | `v2` |
| `services.entries[].id` | `string` | true | `v2` |
| `services.entries[].type` | `string` | true | `v2` |
| `services.entries[].io` | `string` | true | `v2` |
| `services.entries[].profile` | `string` | true | `v2` |
| `services.entries[].config` | `mapping` | true | `v2` |
| `services.entries[].default` | `bool` | false | `v2` |
| `services.entries[].functions` | `list` | false | `v2` |
| `services.entries[].functions[].name` | `string` | true | `v2` |
| `services.entries[].functions[].op` | `string` | true | `v2` |
| `services.entries[].functions[].params` | `list` | false | `v2` |
| `services.entries[].docs` | `list` | false | `v2` |
| `services.entries[].docs[].id` | `string` | true | `v2` |
| `services.entries[].docs[].summary` | `string` | true | `v2` |
| `services.entries[].docs[].audience` | `string` | true | `v2` |
| `services.entries[].docs[].status` | `string` | true | `v2` |
| `services.entries[].docs[].description` | `string` | false | `v2` |
| `services.entries[].docs[].type` | `string` | false | `v2` |
| `services.entries[].docs[].since` | `string` | false | `v2` |
| `services.entries[].docs[].updated_at` | `string` | false | `v2` |
| `services.entries[].docs[].tags` | `list` | false | `v2` |
| `services.entries[].docs[].owners` | `list` | false | `v2` |
| `services.entries[].docs[].owners[].id` | `string` | true | `v2` |
| `services.entries[].docs[].owners[].role` | `string` | true | `v2` |
| `services.entries[].docs[].links` | `list` | false | `v2` |
| `services.entries[].docs[].links[].rel` | `string` | true | `v2` |
| `services.entries[].docs[].links[].ref` | `string` | true | `v2` |
| `services.entries[].docs[].links[].title` | `string` | false | `v2` |
| `services.entries[].docs[].examples` | `list` | false | `v2` |
| `services.entries[].docs[].examples[].title` | `string` | true | `v2` |
| `services.entries[].docs[].examples[].ref` | `string` | true | `v2` |
| `services.entries[].functions[].docs` | `list` | false | `v2` |
| `services.entries[].functions[].docs[].id` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].summary` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].audience` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].status` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].description` | `string` | false | `v2` |
| `services.entries[].functions[].docs[].type` | `string` | false | `v2` |
| `services.entries[].functions[].docs[].since` | `string` | false | `v2` |
| `services.entries[].functions[].docs[].updated_at` | `string` | false | `v2` |
| `services.entries[].functions[].docs[].tags` | `list` | false | `v2` |
| `services.entries[].functions[].docs[].owners` | `list` | false | `v2` |
| `services.entries[].functions[].docs[].owners[].id` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].owners[].role` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].links` | `list` | false | `v2` |
| `services.entries[].functions[].docs[].links[].rel` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].links[].ref` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].links[].title` | `string` | false | `v2` |
| `services.entries[].functions[].docs[].examples` | `list` | false | `v2` |
| `services.entries[].functions[].docs[].examples[].title` | `string` | true | `v2` |
| `services.entries[].functions[].docs[].examples[].ref` | `string` | true | `v2` |
| `artifact` | `mapping` | false | `v2` |
| `artifact.imports` | `list` | false | `v2` |
| `artifact.imports[].id` | `string` | true | `v2` |
| `artifact.imports[].ref` | `string` | true | `v2` |
| `artifact.imports[].type` | `string` | false | `v2` |
| `artifact.imports[].inputs` | `mapping` | false | `v2` |
| `artifact.imports[].options` | `mapping` | false | `v2` |
| `artifact.imports[].docs` | `list` | false | `v2` |
| `artifact.imports[].docs[].id` | `string` | true | `v2` |
| `artifact.imports[].docs[].summary` | `string` | true | `v2` |
| `artifact.imports[].docs[].audience` | `string` | true | `v2` |
| `artifact.imports[].docs[].status` | `string` | true | `v2` |
| `artifact.imports[].docs[].description` | `string` | false | `v2` |
| `artifact.imports[].docs[].type` | `string` | false | `v2` |
| `artifact.imports[].docs[].since` | `string` | false | `v2` |
| `artifact.imports[].docs[].updated_at` | `string` | false | `v2` |
| `artifact.imports[].docs[].tags` | `list` | false | `v2` |
| `artifact.imports[].docs[].owners` | `list` | false | `v2` |
| `artifact.imports[].docs[].owners[].id` | `string` | true | `v2` |
| `artifact.imports[].docs[].owners[].role` | `string` | true | `v2` |
| `artifact.imports[].docs[].links` | `list` | false | `v2` |
| `artifact.imports[].docs[].links[].rel` | `string` | true | `v2` |
| `artifact.imports[].docs[].links[].ref` | `string` | true | `v2` |
| `artifact.imports[].docs[].links[].title` | `string` | false | `v2` |
| `artifact.imports[].docs[].examples` | `list` | false | `v2` |
| `artifact.imports[].docs[].examples[].title` | `string` | true | `v2` |
| `artifact.imports[].docs[].examples[].ref` | `string` | true | `v2` |
| `artifact.exports` | `list` | false | `v2` |
| `artifact.exports[].id` | `string` | true | `v2` |
| `artifact.exports[].ref` | `string` | true | `v2` |
| `artifact.exports[].type` | `string` | false | `v2` |
| `artifact.exports[].options` | `mapping` | false | `v2` |
| `artifact.exports[].docs` | `list` | false | `v2` |
| `artifact.exports[].docs[].id` | `string` | true | `v2` |
| `artifact.exports[].docs[].summary` | `string` | true | `v2` |
| `artifact.exports[].docs[].audience` | `string` | true | `v2` |
| `artifact.exports[].docs[].status` | `string` | true | `v2` |
| `artifact.exports[].docs[].description` | `string` | false | `v2` |
| `artifact.exports[].docs[].type` | `string` | false | `v2` |
| `artifact.exports[].docs[].since` | `string` | false | `v2` |
| `artifact.exports[].docs[].updated_at` | `string` | false | `v2` |
| `artifact.exports[].docs[].tags` | `list` | false | `v2` |
| `artifact.exports[].docs[].owners` | `list` | false | `v2` |
| `artifact.exports[].docs[].owners[].id` | `string` | true | `v2` |
| `artifact.exports[].docs[].owners[].role` | `string` | true | `v2` |
| `artifact.exports[].docs[].links` | `list` | false | `v2` |
| `artifact.exports[].docs[].links[].rel` | `string` | true | `v2` |
| `artifact.exports[].docs[].links[].ref` | `string` | true | `v2` |
| `artifact.exports[].docs[].links[].title` | `string` | false | `v2` |
| `artifact.exports[].docs[].examples` | `list` | false | `v2` |
| `artifact.exports[].docs[].examples[].title` | `string` | true | `v2` |
| `artifact.exports[].docs[].examples[].ref` | `string` | true | `v2` |
| `exports` | `list` | false | `v2` |
| `exports[].as` | `string` | true | `v2` |
| `exports[].from` | `string` | true | `v2` |
| `exports[].path` | `string` | true | `v2` |
| `exports[].params` | `list` | false | `v2` |
| `exports[].required` | `bool` | false | `v2` |
| `exports[].docs` | `list` | false | `v2` |
| `exports[].docs[].id` | `string` | true | `v2` |
| `exports[].docs[].summary` | `string` | true | `v2` |
| `exports[].docs[].audience` | `string` | true | `v2` |
| `exports[].docs[].status` | `string` | true | `v2` |
| `exports[].docs[].description` | `string` | false | `v2` |
| `exports[].docs[].type` | `string` | false | `v2` |
| `exports[].docs[].since` | `string` | false | `v2` |
| `exports[].docs[].updated_at` | `string` | false | `v2` |
| `exports[].docs[].tags` | `list` | false | `v2` |
| `exports[].docs[].owners` | `list` | false | `v2` |
| `exports[].docs[].owners[].id` | `string` | true | `v2` |
| `exports[].docs[].owners[].role` | `string` | true | `v2` |
| `exports[].docs[].links` | `list` | false | `v2` |
| `exports[].docs[].links[].rel` | `string` | true | `v2` |
| `exports[].docs[].links[].ref` | `string` | true | `v2` |
| `exports[].docs[].links[].title` | `string` | false | `v2` |
| `exports[].docs[].examples` | `list` | false | `v2` |
| `exports[].docs[].examples[].title` | `string` | true | `v2` |
| `exports[].docs[].examples[].ref` | `string` | true | `v2` |
| `contracts` | `list` | true | `v2` |
| `contracts[].id` | `string` | true | `v2` |
| `title` | `string` | false | `v2` |
| `purpose` | `string` | false | `v2` |
| `docs` | `list` | false | `v2` |
| `docs[].id` | `string` | true | `v2` |
| `docs[].summary` | `string` | true | `v2` |
| `docs[].audience` | `string` | true | `v2` |
| `docs[].status` | `string` | true | `v2` |
| `docs[].description` | `string` | false | `v2` |
| `docs[].type` | `string` | false | `v2` |
| `docs[].since` | `string` | false | `v2` |
| `docs[].updated_at` | `string` | false | `v2` |
| `docs[].tags` | `list` | false | `v2` |
| `docs[].owners` | `list` | false | `v2` |
| `docs[].owners[].id` | `string` | true | `v2` |
| `docs[].owners[].role` | `string` | true | `v2` |
| `docs[].links` | `list` | false | `v2` |
| `docs[].links[].rel` | `string` | true | `v2` |
| `docs[].links[].ref` | `string` | true | `v2` |
| `docs[].links[].title` | `string` | false | `v2` |
| `docs[].examples` | `list` | false | `v2` |
| `docs[].examples[].title` | `string` | true | `v2` |
| `docs[].examples[].ref` | `string` | true | `v2` |
| `domain` | `string` | false | `v2` |
| `contracts[].title` | `string` | false | `v2` |
| `contracts[].purpose` | `string` | false | `v2` |
| `contracts[].domain` | `string` | false | `v2` |
| `contracts[].docs` | `list` | false | `v2` |
| `contracts[].docs[].id` | `string` | true | `v2` |
| `contracts[].docs[].summary` | `string` | true | `v2` |
| `contracts[].docs[].audience` | `string` | true | `v2` |
| `contracts[].docs[].status` | `string` | true | `v2` |
| `contracts[].docs[].description` | `string` | false | `v2` |
| `contracts[].docs[].type` | `string` | false | `v2` |
| `contracts[].docs[].since` | `string` | false | `v2` |
| `contracts[].docs[].updated_at` | `string` | false | `v2` |
| `contracts[].docs[].tags` | `list` | false | `v2` |
| `contracts[].docs[].owners` | `list` | false | `v2` |
| `contracts[].docs[].owners[].id` | `string` | true | `v2` |
| `contracts[].docs[].owners[].role` | `string` | true | `v2` |
| `contracts[].docs[].links` | `list` | false | `v2` |
| `contracts[].docs[].links[].rel` | `string` | true | `v2` |
| `contracts[].docs[].links[].ref` | `string` | true | `v2` |
| `contracts[].docs[].links[].title` | `string` | false | `v2` |
| `contracts[].docs[].examples` | `list` | false | `v2` |
| `contracts[].docs[].examples[].title` | `string` | true | `v2` |
| `contracts[].docs[].examples[].ref` | `string` | true | `v2` |
| `contracts[].when` | `mapping` | false | `v2` |
| `contracts[].when.required` | `list` | false | `v2` |
| `contracts[].when.optional` | `list` | false | `v2` |
| `contracts[].when.fail` | `list` | false | `v2` |
| `contracts[].when.complete` | `list` | false | `v2` |
| `contracts[].clauses` | `mapping` | true | `v2` |
| `contracts[].expect` | `mapping` | false | `v2` |
| `contracts[].expect.portable` | `mapping` | false | `v2` |
| `contracts[].expect.portable.status` | `string` | false | `v2` |
| `contracts[].expect.portable.category` | `string` | false | `v2` |
| `contracts[].expect.portable.message_tokens` | `list` | false | `v2` |
| `contracts[].expect.overrides` | `list` | false | `v2` |
| `contracts[].expect.overrides[].runner` | `string` | true | `v2` |
| `contracts[].expect.overrides[].status` | `string` | false | `v2` |
| `contracts[].expect.overrides[].category` | `string` | false | `v2` |
| `contracts[].expect.overrides[].message_tokens` | `list` | false | `v2` |
| `contracts[].requires` | `mapping` | false | `v2` |

### Runtime Surface Matrix

| surface | required_keys | catalog |
|---|---|---|
| `harness` | `harness.type`, `harness.profile`, `harness.config` | n/a |
| `services.entries[]` | `services.entries[].id`, `services.entries[].type`, `services.entries[].io`, `services.entries[].profile`, `services.entries[].config` | `/specs/schema/service_contract_catalog_v1.yaml` |
<!-- GENERATED:END spec_schema_field_catalog -->
