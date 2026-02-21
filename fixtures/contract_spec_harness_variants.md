# Contract-Spec Harness Variants (Examples)

The blocks below are complete `yaml contract-spec` examples showing different
`harness` variants in the v1 schema.

## 1) `contract.check` with `harness.check.profile: text.file`

```yaml contract-spec
id: EXAMPLE-HARNESS-TEXT-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: text.file profile example
purpose: Example contract.check using text.file profile with imported text artifact.
requires:
  capabilities:
  - text.file
  when_missing: fail
expect:
  portable:
    status: pass
    category: null
harness:
  check:
    profile: text.file
    config:
      path: /README.md
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: text}
      - data-contracts
```

## 2) `contract.check` with `harness.check.profile: cli.run`

```yaml contract-spec
id: EXAMPLE-HARNESS-CLI-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: cli.run profile example
purpose: Example contract.check using cli.run profile with explicit entrypoint and args.
requires:
  capabilities:
  - cli.run
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  env:
    EXAMPLE_FLAG: "1"
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - stdout
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: stdout}
      - usage
```

## 3) `contract.check` with `harness.check.profile: api.http`

```yaml contract-spec
id: EXAMPLE-HARNESS-API-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: api.http profile example
purpose: Example contract.check using api.http profile with deterministic local fixture input.
requires:
  capabilities:
  - api.http
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
harness:
  api_http:
    mode: deterministic
  check:
    profile: api.http
    config:
      request:
        method: GET
        url: /specs/conformance/cases/fixtures/api_http_ok.json
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - status
    - body_json
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: status}
      - "200"
  - id: assert_2
    assert:
      std.type.json_type:
      - {var: body_json}
      - dict
```

## 4) `contract.check` with `harness.check.profile: governance.scan`

```yaml contract-spec
id: EXAMPLE-HARNESS-GOV-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: governance.scan profile example
purpose: Example governance scan check wired through harness.check profile and config.
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.chain_fail_fast_default
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_assert
    symbols:
    - policy.assert.no_violations
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

## 5) `contract.job` with `harness.jobs`

```yaml contract-spec
id: EXAMPLE-HARNESS-JOB-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.job
title: contract.job harness example
purpose: Example contract.job using harness.jobs plus hook dispatch through when.fail/when.complete.
harness:
  use:
  - ref: /specs/libraries/policy/policy_job.spec.md
    as: lib_policy_job
    symbols:
    - policy.job.dispatch_ok
  spec_lang:
    capabilities:
    - ops.job
    - ops.helper
  jobs:
    main:
      mode: report
      helper: helper.report.emit
      inputs:
        report_name: example-report
        format: json
        out: .artifacts/example-report.json
    on_fail:
      mode: report
      helper: helper.report.emit
      inputs:
        report_name: example-fail
        format: json
        out: .artifacts/example-fail.json
    on_complete:
      mode: report
      helper: helper.report.emit
      inputs:
        report_name: example-complete
        format: json
        out: .artifacts/example-complete.json
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_1
    assert:
    - ops.job.dispatch:
      - main
    - call:
      - {var: policy.job.dispatch_ok}
      - {var: summary_json}
when:
  fail:
  - ops.job.dispatch:
    - on_fail
  complete:
  - ops.job.dispatch:
    - on_complete
```

## 6) `contract.export` with `harness.exports`

```yaml contract-spec
id: EXAMPLE-HARNESS-EXPORT-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
title: contract.export harness example
purpose: Example export case exposing reusable assertion function via harness.exports.
contract:
  defaults: {}
  steps:
  - id: __export__example.assert.text_contains
    assert:
      std.string.contains:
      - {var: subject}
      - {var: token}
harness:
  exports:
  - as: example.assert.text_contains
    from: assert.function
    path: /__export__example.assert.text_contains
    params:
    - subject
    - token
    required: true
    doc:
      summary: Returns true when subject contains token.
      description: Reusable helper for substring checks in policy/conformance cases.
      params:
      - name: subject
        type: string
        required: true
        description: Input text value.
      - name: token
        type: string
        required: true
        description: Required substring.
      returns:
        type: bool
        description: True when the substring exists.
      errors:
      - code: SCHEMA_ERROR
        when: Subject or token is not a string.
        category: schema
      examples:
      - title: positive
        input:
          subject: data contracts
          token: contracts
        expected: true
        notes: Basic containment check.
      portability:
        python: true
        php: true
        rust: true
        notes: Uses stdlib predicate only.
      see_also: []
      since: v1
library:
  id: example.assertions
  module: example
  stability: alpha
  owner: data-contracts
  tags:
  - example
  - assertions
doc:
  summary: Example assertion export library.
  description: Demonstrates minimum contract.export metadata plus harness.exports docs.
  audience: spec-authors
  since: v1
  tags:
  - examples
  see_also:
  - /specs/libraries/policy/policy_assertions.spec.md
```

## 7) Maximal Optional-Field Example (`contract.check` + `api.http`)

This example supplies all optional fields that can be combined in one valid
`contract.check` case. Note that `harness.spec_lang.includes` is intentionally
omitted because executable cases must not declare it.

```yaml contract-spec
id: EXAMPLE-HARNESS-OPTIONAL-ALL-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: maximal optional-field example
purpose: Demonstrates a single contract.check case with all compatible optional fields supplied.
domain: conformance
assert_health:
  mode: warn
requires:
  capabilities:
  - api.http
  - ops.job
  - ops.helper
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
    message_tokens:
    - optional-example
  impl:
    rust:
      status: skip
      category: null
    python:
      status: skip
      category: null
    php:
      status: skip
      category: null
doc:
  summary: Maximal optional contract.check example.
  description: Includes optional top-level metadata plus optional harness/contract branches.
  audience: spec-authors
  since: v1
  tags:
  - examples
  - optional-fields
  see_also:
  - /specs/schema/schema_v1.md
  - /specs/contract/02_case_shape.md
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  env:
    API_TOKEN: null
    EXAMPLE_MODE: optional
  stdin_isatty: false
  stdin_text: "{\"ping\":\"pong\"}\n"
  block_imports:
  - requests
  stub_modules:
  - local_fake_module
  setup_files:
  - path: fixtures/input.json
    text: "{\"ok\":true}\n"
  hook_before: hooks.example.before
  hook_after: hooks.example.after
  hook_kwargs:
    trace: true
    source: optional-example
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_assert
    symbols:
    - policy.assert.no_violations
  spec_lang:
    max_steps: 200
    max_nodes: 5000
    max_literal_bytes: 100000
    timeout_ms: 2000
    exports:
    - example.symbol.allowed
    imports:
    - from: std.string
      names:
      - contains
      as:
        contains: str_contains
    references:
      mode: allow
      providers:
      - github
      rules:
        github:
          allow_orgs:
          - data-contracts
    capabilities:
    - ops.helper
    - ops.job
  api_http:
    mode: live
    auth:
      oauth:
        grant_type: client_credentials
        token_url: https://auth.example.test/oauth/token
        client_id_env: EXAMPLE_CLIENT_ID
        client_secret_env: EXAMPLE_CLIENT_SECRET
        scope: contracts:read
        audience: https://api.example.test
        auth_style: body
        token_field: access_token
        expires_field: expires_in
        refresh_skew_seconds: 15
    scenario:
      setup:
        command:
        - ./scripts/control_plane.sh
        - governance
        cwd: /specs
        env:
          READY_WAIT_MS: "5000"
        ready_probe:
          url: https://api.example.test/healthz
          method: GET
          expect_status_in:
          - 200
          - 204
          timeout_ms: 8000
          interval_ms: 250
      teardown:
        command:
        - ./scripts/control_plane.sh
        - docs-generate-check
        cwd: /specs
        env:
          CLEANUP: "1"
      fail_fast: false
  chain:
    fail_fast: false
    steps:
    - id: run_fixture
      class: must
      ref: /specs/conformance/cases/core/api_http.spec.md#DCCONF-API-001
      allow_continue: true
    - id: check_fixtures_doc
      class: can
      ref: /specs/conformance/cases/core/api_http.spec.md
      allow_continue: false
    exports:
    - as: chain.example.export
      from: assert.function
      path: /contract/steps/assert_1/assert
      params:
      - summary
      required: false
    imports:
    - from: chain.example.export
      as: imported_chain_symbol
  check:
    profile: api.http
    config:
      requests:
      - id: create
        method: POST
        url: https://api.example.test/items
        headers:
          content-type: application/json
        query:
          dry_run: "true"
        body_json:
          name: sample
      - id: preflight
        method: OPTIONS
        url: https://api.example.test/items
        cors:
          origin: https://docs.example.test
          request_method: POST
          request_headers:
          - content-type
          preflight: true
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - status
    - body_json
    - steps_json
    - summary_json
    as:
      status: http_status
  steps:
  - id: assert_1
    imports:
    - from: artifact
      names:
      - cors_json
    assert:
    - std.string.contains:
      - {var: http_status}
      - "200"
    - std.type.json_type:
      - {var: body_json}
      - dict
    - std.type.json_type:
      - {var: steps_json}
      - list
    - std.type.json_type:
      - {var: cors_json}
      - dict
when:
  required: []
  optional: []
  fail: []
  complete: []
```

## 8) Step-By-Step Explanation Of Each Element

This walkthrough explains the maximal example by section. Each section includes
the intent, key fields, and a copyable snippet.

### A) Identity And Routing

What it does:
- Declares the case identity and binds it to a schema + type contract.

Fields:
- `id`: stable, unique identifier.
- `spec_version`: schema major.
- `schema_ref`: canonical schema document path.
- `type`: execution contract (`contract.check` here).
- `title` and `purpose`: human-readable metadata.
- `domain`: optional grouping tag.

Example:

```yaml
id: EXAMPLE-HARNESS-OPTIONAL-ALL-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: maximal optional-field example
purpose: Demonstrates a single contract.check case with all compatible optional fields supplied.
domain: conformance
```

### B) Quality/Policy Metadata

What it does:
- Controls assertion-health behavior and capability gating.
- Defines expected outcome overlays for portability and per-runner deltas.

Fields:
- `assert_health.mode`: `ignore|warn|error`.
- `requires.capabilities`: required runtime capabilities.
- `requires.when_missing`: `skip|fail`.
- `expect.portable.*`: baseline expected result.
- `expect.impl.<runner>.*`: runtime-specific expected result.

Example:

```yaml
assert_health:
  mode: warn
requires:
  capabilities:
  - api.http
  - ops.job
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
    message_tokens:
    - optional-example
  impl:
    rust:
      status: skip
      category: null
```

Compound field guidance:

1. `expect.portable.*` (baseline contract)
   - Purpose: declare the default expectation for all runners unless overridden.
   - Typical keys:
     - `status`: `pass|fail|skip`
     - `category`: `schema|assertion|runtime|null`
     - `message_tokens`: optional list of expected diagnostic fragments
   - Good pattern:
     - Keep `portable` as the canonical truth for shared behavior.
     - Add `impl` only for intentional, documented runtime deltas.

Minimal example:

```yaml
expect:
  portable:
    status: pass
    category: null
```

Strict failure example:

```yaml
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - request.url is required
    - api.http
```

2. `expect.impl.<runner>.*` (runtime overlays)
   - Purpose: override `portable` when a specific runtime is intentionally different.
   - Runner keys commonly used in this repo: `rust`, `python`, `php`.
   - Overlay semantics:
     - If a runner key exists, its values override `portable` for that runner.
     - If a runner key is absent, runner inherits `portable`.

Mixed overlay example:

```yaml
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: skip
      category: null
    python:
      status: fail
      category: runtime
      message_tokens:
      - capability missing
```

Practical decision rule:
- Use `portable` only when behavior should be identical everywhere.
- Use `impl` only to capture known compatibility-lane differences.
- Avoid redundant overlays that exactly duplicate `portable`.

### C) Documentation Metadata

What it does:
- Adds generated-doc friendly description and cross-links.

Fields:
- `doc.summary`, `doc.description`
- `doc.audience`, `doc.since`
- `doc.tags`, `doc.see_also`

Example:

```yaml
doc:
  summary: Maximal optional contract.check example.
  description: Includes optional top-level metadata plus optional harness/contract branches.
  audience: spec-authors
  since: v1
  tags: [examples, optional-fields]
  see_also:
  - /specs/schema/schema_v1.md
```

Compound field guidance:

- `doc.tags`:
  - Use concise indexing terms (`examples`, `optional-fields`).
  - Keep stable over time for searchability.
- `doc.see_also`:
  - Prefer canonical virtual-root paths.
  - Point to schema/type contracts, not transient files.

Example with richer links:

```yaml
doc:
  summary: API HTTP scenario conformance fixture.
  description: Verifies live OAuth setup and teardown orchestration behavior.
  audience: runner-authors
  since: v1
  tags: [api, oauth, conformance]
  see_also:
  - /specs/contract/types/api_http.md
  - /specs/schema/schema_v1.md
```

### D) Harness Root

What it does:
- Contains runner-only inputs.
- Keeps runtime configuration separated from assertion logic.

Common optional roots used in the maximal example:
- `entrypoint`, `env`, `stdin_isatty`, `stdin_text`
- `block_imports`, `stub_modules`, `setup_files`
- `hook_before`, `hook_after`, `hook_kwargs`
- `use`, `spec_lang`, `api_http`, `chain`, `check`

Example:

```yaml
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  env:
    EXAMPLE_MODE: optional
  stdin_isatty: false
  stdin_text: "{\"ping\":\"pong\"}\n"
```

Compound field guidance:

- `harness.env`:
  - Values can be strings or `null` (unset semantics in adapters that support it).
  - Keep secrets referenced by env name; do not inline secret literals in case YAML.
- `harness.setup_files`:
  - `path` should stay relative to sandbox/temp workspace.
  - `text` should be deterministic fixture content.

Example:

```yaml
harness:
  env:
    EXAMPLE_MODE: "ci"
    SECRET_TOKEN: null
  setup_files:
  - path: fixtures/request.json
    text: "{\"name\":\"sample\"}\n"
```

### E) Harness: Runtime Setup Helpers

What it does:
- Shapes runtime environment and pre/post execution behavior.

Fields:
- `harness.block_imports`: force import failures for modules.
- `harness.stub_modules`: inject fake modules.
- `harness.setup_files[].path` and `harness.setup_files[].text`: create files in temp workspace.
- `harness.hook_before` and `harness.hook_after`: lifecycle hook entrypoints.
- `harness.hook_kwargs`: kwargs passed to hooks.

Example:

```yaml
harness:
  block_imports: [requests]
  stub_modules: [local_fake_module]
  setup_files:
  - path: fixtures/input.json
    text: "{\"ok\":true}\n"
  hook_before: hooks.example.before
  hook_after: hooks.example.after
  hook_kwargs:
    trace: true
```

### F) Harness: Library Imports (`use`)

What it does:
- Pulls exported symbols from other case files.

Fields:
- `harness.use[].ref`: source case path (optional `#case_id` fragment).
- `harness.use[].as`: local namespace alias.
- `harness.use[].symbols`: symbol names to import.

Example:

```yaml
harness:
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_assert
    symbols:
    - policy.assert.no_violations
```

Compound field guidance:

- `harness.use[].ref`:
  - Can include fragment `#CASE-ID` for single-case import source.
  - Without fragment, target file-level exported symbols.
- `harness.use[].symbols`:
  - Import only symbols actually used by assertions to keep intent clear.

Example with fragment ref:

```yaml
harness:
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md#LIB-POLICY-ASSERT-001
    as: policy_lib
    symbols:
    - policy.assert.scan_pass
```

### G) Harness: Spec-Lang Runtime Controls

What it does:
- Sets evaluator limits and import/reference policy.

Fields:
- Limits: `max_steps`, `max_nodes`, `max_literal_bytes`, `timeout_ms`.
- `exports`: optional visible symbol allowlist.
- `imports`: std namespace imports + aliases.
- `references`: external reference allow/deny and provider rules.
- `capabilities`: explicit evaluator capabilities.

Example:

```yaml
harness:
  spec_lang:
    max_steps: 200
    max_nodes: 5000
    timeout_ms: 2000
    imports:
    - from: std.string
      names: [contains]
      as:
        contains: str_contains
    references:
      mode: allow
      providers: [github]
```

Compound field guidance:

- `harness.spec_lang.imports[]`:
  - `from` is namespace (`std.string`), `names` is imported symbols, `as` is optional alias map.
  - Keep aliases explicit when name collisions are possible.
- `harness.spec_lang.references`:
  - Default safe posture is `mode: deny`.
  - Enable `allow` only with bounded `providers` and rules.

Example with alias + rules:

```yaml
harness:
  spec_lang:
    imports:
    - from: std.object
      names: [get]
      as:
        get: obj_get
    references:
      mode: allow
      providers: [github]
      rules:
        github:
          allow_orgs: [data-contracts]
```

### H) Harness: API HTTP Transport/Auth/Scenario

What it does:
- Configures HTTP execution mode, OAuth behavior, and optional setup/teardown flow.

Fields:
- `harness.api_http.mode`: `deterministic|live`.
- `harness.api_http.auth.oauth.*`: client credentials and token parsing.
- `harness.api_http.scenario.setup.*`: pre-run command and readiness probing.
- `harness.api_http.scenario.teardown.*`: post-run cleanup.
- `harness.api_http.scenario.fail_fast`: stop after first failed request step.

Example:

```yaml
harness:
  api_http:
    mode: live
    auth:
      oauth:
        grant_type: client_credentials
        token_url: https://auth.example.test/oauth/token
        client_id_env: EXAMPLE_CLIENT_ID
        client_secret_env: EXAMPLE_CLIENT_SECRET
    scenario:
      setup:
        command: [./scripts/control_plane.sh, governance]
      teardown:
        command: [./scripts/control_plane.sh, docs-generate-check]
      fail_fast: false
```

Compound field guidance:

- `harness.api_http.auth.oauth`:
  - Use env-ref keys (`client_id_env`, `client_secret_env`) for credentials.
  - `auth_style`, `token_field`, and `expires_field` document token-response parsing.
- `harness.api_http.scenario.setup.ready_probe`:
  - Add for services that need warm-up.
  - `expect_status_in` should include only healthy codes.

Example with explicit probe details:

```yaml
harness:
  api_http:
    auth:
      oauth:
        grant_type: client_credentials
        token_url: https://auth.example.test/oauth/token
        client_id_env: EXAMPLE_CLIENT_ID
        client_secret_env: EXAMPLE_CLIENT_SECRET
        auth_style: body
        token_field: access_token
        expires_field: expires_in
    scenario:
      setup:
        command: [./scripts/control_plane.sh, governance]
        ready_probe:
          url: https://api.example.test/healthz
          method: GET
          expect_status_in: [200, 204]
          timeout_ms: 8000
          interval_ms: 250
```

### I) Harness: Chain Composition

What it does:
- Composes other cases into an ordered chain with explicit continuation rules.
- Allows chain-level exports/imports for cross-step symbol sharing.

Fields:
- `harness.chain.fail_fast`
- `harness.chain.steps[].id|class|ref|allow_continue`
- `harness.chain.exports[]` and `harness.chain.imports[]`

Example:

```yaml
harness:
  chain:
    fail_fast: false
    steps:
    - id: run_fixture
      class: must
      ref: /specs/conformance/cases/core/api_http.spec.md#DCCONF-API-001
      allow_continue: true
```

Compound field guidance:

- `harness.chain.steps[].class`:
  - `must`: required pass.
  - `can`: optional/non-blocking.
  - `cannot`: expected to fail/prohibited condition.
- `harness.chain.exports[]` + `harness.chain.imports[]`:
  - Use when chaining symbol outputs into later steps.
  - Keep `from: assert.function` and explicit `params`.

Example with exports/imports:

```yaml
harness:
  chain:
    steps:
    - id: producer
      class: must
      ref: /specs/example/producer.spec.md#CASE-1
    exports:
    - as: chain.helper
      from: assert.function
      path: /contract/steps/assert_1/assert
      params: [subject]
      required: true
    imports:
    - from: chain.helper
      as: helper_fn
```

### J) Harness: Check Profile + Config Payload

What it does:
- Selects check adapter profile and passes profile-specific config.

Fields:
- `harness.check.profile`: one of `text.file|cli.run|api.http|governance.scan`.
- `harness.check.config`: shape depends on selected profile.
- In this example, `api.http` config uses `requests[]` scenario input.

Example:

```yaml
harness:
  check:
    profile: api.http
    config:
      requests:
      - id: create
        method: POST
        url: https://api.example.test/items
        body_json:
          name: sample
```

Compound field guidance:

- `harness.check.profile` chooses the schema for `harness.check.config`.
- For `api.http` config:
  - Use `request` for single-call cases.
  - Use `requests` (with per-step `id`) for multi-step scenarios.

Single-request example:

```yaml
harness:
  check:
    profile: api.http
    config:
      request:
        method: GET
        url: /specs/conformance/cases/fixtures/api_http_ok.json
```

Scenario example:

```yaml
harness:
  check:
    profile: api.http
    config:
      requests:
      - id: create
        method: POST
        url: https://api.example.test/items
      - id: fetch
        method: GET
        url: https://api.example.test/items/{{steps.create.body_json.id}}
```

### K) Contract Program

What it does:
- Encodes assertion logic and imported artifacts.

Fields:
- `contract.steps[].required`: optional step requiredness flag (default `true`).
- `contract.steps[].priority`: optional positive integer metadata (default `1`).
- `contract.steps[].severity`: optional positive integer metadata (default `1`).
- `contract.imports[]`: default imports from `artifact`.
- `contract.steps[].id`: ordered step key.
- `contract.steps[].imports[]`: step-level import overrides.
- `contract.steps[].assert`: expression list/mapping evaluated by spec-lang.

Example:

```yaml
contract:
  defaults: {}
  imports:
  - from: artifact
    names: [status, body_json]
    as:
      status: http_status
  steps:
  - id: assert_1
    assert:
    - std.string.contains:
      - {var: http_status}
      - "200"
```

Compound field guidance:

- `contract.imports[]`:
  - Use `from: artifact` with explicit `names`.
  - Use `as` to normalize artifact names across profiles.
- `contract.steps[].assert`:
  - Can be a single expression mapping or a list of expressions.
  - Prefer short, composable assertions over one large nested tree.

Multiple-assert list example:

```yaml
contract:
  imports:
  - from: artifact
    names: [status, body_json]
  steps:
  - id: assert_api
    assert:
    - std.string.contains:
      - {var: status}
      - "200"
    - std.type.json_type:
      - {var: body_json}
      - dict
```

### L) Lifecycle Hooks (`when`)

What it does:
- Declares optional lifecycle branches for must/may/forbidden/failure/completion actions.

Fields:
- `when.required`, `when.optional`, `when.fail`, `when.complete`

Example:

```yaml
when:
  required: []
  optional: []
  fail: []
  complete: []
```

Compound field guidance:

- `when.fail` and `when.complete` are commonly used for cleanup/report hooks.
- Keep lifecycle actions deterministic and side-effect scoped.
- If unused, empty lists communicate deliberate no-op behavior.

Hook dispatch example:

```yaml
when:
  fail:
  - ops.job.dispatch:
    - on_fail
  complete:
  - ops.job.dispatch:
    - on_complete
```

### M) Quick Variations You Can Apply

Use this to adapt the maximal example quickly:
- Convert to strict missing-capability failure:
  Change `requires.when_missing: fail`.
- Convert HTTP live -> deterministic:
  Change `harness.api_http.mode: deterministic` and use fixture `url` paths.
- Remove CLI runtime setup:
  Delete `entrypoint`, `stdin_*`, hooks, and setup file keys.
- Disable external references:
  Set `harness.spec_lang.references.mode: deny`.

### N) Execution Outcome Matrix

This matrix is the fastest way to reason about what changing `expect.*.status`
and `expect.*.category` means at execution time.

Source rules:
- `/specs/conformance/report_format.md`
- `/specs/contract/05_errors.md`

| `status` | `category` | Valid? | Pipeline stage signal | Interpretation | `message_tokens` guidance |
|---|---|---|---|---|---|
| `pass` | `null` | Yes | Assertion/check completed | Case succeeded | Usually omitted |
| `skip` | `null` | Yes | Capability/selection gate | Case intentionally not executed | Usually omitted |
| `fail` | `schema` | Yes | Schema validation / shape checking | Case payload/config was invalid | Include shape/type/key hints |
| `fail` | `assertion` | Yes | Assertion evaluation | Inputs were valid, assertion predicate failed | Include `case_id`, `assert_path`, `target`/`op` when available |
| `fail` | `runtime` | Yes | Harness/runner invocation | Execution fault outside assertion truth value | Include actionable runtime token |
| `pass` | `schema` | No | n/a | Contradiction: pass cannot carry failure category | Invalid combination |
| `pass` | `assertion` | No | n/a | Contradiction: pass cannot carry failure category | Invalid combination |
| `pass` | `runtime` | No | n/a | Contradiction: pass cannot carry failure category | Invalid combination |
| `skip` | `schema` | No | n/a | Contradiction: skip cannot carry failure category | Invalid combination |
| `skip` | `assertion` | No | n/a | Contradiction: skip cannot carry failure category | Invalid combination |
| `skip` | `runtime` | No | n/a | Contradiction: skip cannot carry failure category | Invalid combination |
| `fail` | `null` | No | n/a | Contradiction: failure must specify failure category | Invalid combination |

### O) Where Each Category Comes From

- `schema`
  Generated before or during early evaluation when case shape/config/type constraints are violated.
  Typical triggers: missing required field, bad enum, malformed request shape.
- `assertion`
  Generated when the assertion program runs successfully but returns false for expected conditions.
  Typical triggers: regex mismatch, missing text token, JSON value mismatch.
- `runtime`
  Generated when harness/adapter execution fails outside schema validity and assertion truth.
  Typical triggers: hook/entrypoint failure, command invocation error, unavailable runtime dependency.
- `null`
  Non-failure category used only with `pass` and `skip`.

### P) Portable vs Impl Overlay Resolution

Resolution order:
1. Start from `expect.portable` as baseline.
2. If `expect.impl.<runner>` exists, overlay that runner's fields.
3. If no runner overlay exists, runner inherits baseline unchanged.

Mini-matrix:

| Runner | `portable` | `impl.<runner>` present? | Effective result |
|---|---|---|---|
| `rust` | `pass/null` | No | `pass/null` |
| `python` | `pass/null` | No | `pass/null` |
| `php` | `pass/null` | Yes (`fail/runtime`) | `fail/runtime` |

Overlay example:

```yaml
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: fail
      category: runtime
      message_tokens:
      - hook import failed
```

### Q) Runnable Scenario Set (Proof View)

Each snippet below demonstrates one primary execution outcome.

#### Q1) `pass + null`

Why this category:
- Inputs are valid and assertion passes.

Expected tuple:
- `(pass, null, [])`

```yaml contract-spec
id: EXAMPLE-EXPECT-PASS-NULL-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
expect:
  portable:
    status: pass
    category: null
harness:
  check:
    profile: text.file
    config: {}
contract:
  defaults: {}
  imports:
  - from: artifact
    names: [text]
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: text}
      - contract-spec
```

#### Q2) `skip + null` (capability gating)

Why this category:
- Capability gate intentionally skips execution.

Expected tuple:
- `(skip, null, [])`

```yaml contract-spec
id: EXAMPLE-EXPECT-SKIP-NULL-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
requires:
  capabilities: [api.http, api.http.nonexistent_capability]
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
harness:
  check:
    profile: api.http
    config:
      request:
        method: GET
        url: /specs/conformance/cases/fixtures/api_http_ok.json
contract:
  defaults: {}
  steps: []
```

#### Q3) `fail + schema`

Why this category:
- Case config shape is invalid (`request.url` missing).

Expected tuple:
- `(fail, schema, ["api.http", "request.url is required"])`

```yaml contract-spec
id: EXAMPLE-EXPECT-FAIL-SCHEMA-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - api.http
    - request.url is required
harness:
  check:
    profile: api.http
    config:
      request:
        method: GET
contract:
  defaults: {}
  steps: []
```

#### Q4) `fail + assertion`

Why this category:
- Assertion evaluated normally but predicate failed.

Expected tuple:
- `(fail, assertion, ["case_id=EXAMPLE-EXPECT-FAIL-ASSERTION-001", "assert_path"] )`

```yaml contract-spec
id: EXAMPLE-EXPECT-FAIL-ASSERTION-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
    - case_id=EXAMPLE-EXPECT-FAIL-ASSERTION-001
    - assert_path
harness:
  check:
    profile: text.file
    config: {}
contract:
  defaults: {}
  imports:
  - from: artifact
    names: [text]
  steps:
  - id: assert_1
    assert:
      std.string.regex_match:
      - {var: text}
      - \A\Z
```

#### Q5) `fail + runtime`

Why this category:
- Harness execution fails before a meaningful assertion verdict (hook import/invocation fault).

Expected tuple:
- `(fail, runtime, ["hook", "import failed"])`

```yaml contract-spec
id: EXAMPLE-EXPECT-FAIL-RUNTIME-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
requires:
  capabilities: [cli.run]
  when_missing: skip
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - hook
    - import failed
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  hook_before: missing.module.before
  check:
    profile: cli.run
    config:
      argv: [--help]
      exit_code: 0
contract:
  defaults: {}
  steps: []
```

#### Q6) Mixed overlay (`portable` + `impl.php` override)

Why this category:
- Baseline is pass for most runners, but php intentionally expects runtime failure.

Expected tuples:
- `rust -> (pass, null, [])`
- `python -> (pass, null, [])`
- `php -> (fail, runtime, ["hook import failed"])`

```yaml contract-spec
id: EXAMPLE-EXPECT-OVERLAY-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: fail
      category: runtime
      message_tokens:
      - hook import failed
harness:
  check:
    profile: text.file
    config: {}
contract:
  defaults: {}
  steps: []
```
