# Current Spec Snapshot

Spec-Version: 1
Date: 2026-02-12

Notes:

- The canonical assertion DSL is `must` / `can` / `cannot` with `contain`,
  `regex`, and `evaluate` (spec-lang v1 operator-keyed mapping AST).
- `target` is defined on group nodes; leaf assertions are op-only.
- Execution is internal-IR based: external cases compile to spec-lang-backed
  internal predicates before runtime evaluation.
- Spec-lang remains pure; adapter layers perform side effects and feed
  normalized subjects into evaluation.
- Runtime profiling is opt-in and cross-runner via
  `--profile-level off|basic|detailed|debug`, producing deterministic
  `run_trace_v1` artifacts at `/.artifacts/run-trace.json` and
  `/.artifacts/run-trace-summary.md` with span/event timeout diagnostics.
- Governance hang handling is liveness-first: no-progress stall detection
  (`--liveness-*` / `SPEC_RUNNER_LIVENESS_*`) is primary with emergency
  hard-cap fallback; legacy governance timeout env vars are deprecated and
  mapped to hard-cap behavior.
- Gate orchestration now defaults to fail-fast in `ci-gate-summary` with
  deterministic skipped-tail rows (`skip_reason: fail_fast.after_failure`)
  and profile-on-fail diagnostics (`--profile-on-fail`,
  `SPEC_RUNNER_PROFILE_ON_FAIL`) that emit `/.artifacts/run-trace.json` and
  `/.artifacts/run-trace-summary.md` for failing runs.
- Local drift prevention is parity-default: `make prepush` routes to
  `scripts/local_ci_parity.sh` and runs rust core plus python parity lanes by
  default; explicit fast mode uses `SPEC_PREPUSH_MODE=fast` (`make prepush-fast`).
- Repository-managed git hook enforcement is canonical via
  `.githooks/pre-push` and installer `make hooks-install`
  (`scripts/install_git_hooks.sh`), with emergency bypass only through
  `SPEC_PREPUSH_BYPASS=1`.
- Rust local adapter target selection now supports preferred-target fallback to
  host cargo execution when platform target is unavailable; strict hard-fail
  remains opt-in through `SPEC_RUNNER_RUST_TARGET_STRICT=1`.
- Subject projection now follows JSON-core profile envelopes
  (`profile_id`, `profile_version`, `value`, `meta`, optional `context`);
  evaluator subjects are JSON-only.
- `api.http` now supports harness-scoped OAuth client-credentials auth via
  env-ref inputs only (`harness.api_http.auth.oauth`) with deterministic mode
  default and explicit live-mode opt-in for network token/request fetches.
- `api.http` v2 supports practical REST verbs (`GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS`),
  CORS preflight/actual projection via `cors_json`, and scenario round-trip
  execution (`requests` + `harness.api_http.scenario`) with `steps_json`.
- Cross-spec chaining is universal across executable case types via
  `harness.chain` with required step classes (`must|can|cannot`), explicit
  target-derived exports/imports, and scalar refs (`[path][#case_id]`).
- Chain export shape is hard-cut to list-only entries under
  `harness.chain.steps[*].exports`; legacy mapping-form exports are rejected.
- Executable symbol loading is chain-first: `harness.chain` library-symbol
  exports/imports replace `harness.spec_lang.includes` in executable cases.
- `api.http` request templating supports chain state lookups in `url`, header
  values, and `body_text` using `{{chain.<step_id>.<export_name>...}}`.
- all executable harnesses expose chain payload assertions through `chain_json`
  (`state`, `trace`, `imports`) alongside existing type targets.
- Markdown assertion helpers now use expanded domain library surface under
  `domain.markdown.*` with dual-input semantics (raw markdown text or markdown
  profile envelope with structured `context`).
- Hard-cut markdown namespace enforcement is active for governed surfaces:
  legacy `md.*` usage is rejected by governance and conformance fixtures.
- Spec-lang stdlib completeness and parity are contract-defined by
  `docs/spec/schema/spec_lang_stdlib_profile_v1.yaml` and
  `docs/spec/contract/19_spec_lang_stdlib_profile_v1.md`.
- Canonical executable authoring is `.spec.md` only across conformance,
  governance, impl, and spec-lang library surfaces; machine data artifacts
  remain YAML/JSON non-executable files.
- Case-shape contract is now registry-backed under
  `docs/spec/schema/registry/v1/*.yaml`; runtime validation uses compiled
  registry constraints and hard-fails unknown top-level keys.
- `docs/spec/schema/schema_v1.md` includes generated schema-registry snapshot
  content and is checked for synchronization in governance/CI.
- Portability reporting includes a segmented self-containment metric across
  conformance/governance/impl `.spec.md` corpora.
- Conformance and governance assertion authoring is evaluate-only for
  decision semantics; sugar assertion operators are not allowed in these
  assertion trees.
- Impl fixture suites are now evaluate-first with shared impl helper libraries;
  non-evaluate sugar is reserved for explicit, allowlisted schema-behavior
  fixtures only.
- Portability governance enforces non-regression on configured spec-lang
  self-containment baseline metrics.
- Additional ratchet-only metrics track spec-lang adoption, runner
  independence, python dependency evidence, docs operability, and contract
  assertions quality.
- Objective scorecard reporting now composes all metric families into a single
  objective-aligned health view with tripwire hits and course-correction
  recommendations.
- Spec-lang library files remain reusable via include paths in library
  authoring contexts, while executable cases load symbols through chain.
- Case-scoped import bindings are declared through
  `harness.spec_lang.imports` (`from`/`names` with optional `as` aliases).
- Spec-lang mapping-AST authoring now uses explicit subject reference node
  `{var: subject}`.
- Library producer authoring uses `type: spec.export` with producer-owned
  `harness.chain.exports` entries (`from: assert.function`) sourced from
  assert-step `checks` expression mappings.
- Canonical reusable libraries now include `path_core`, `policy_core`, and
  `policy_metrics` under `docs/spec/libraries/`, with domain helper libraries
  under `docs/spec/libraries/domain/`.
- Governance decision checks are now policy-engine first:
  check extractors emit deterministic subject payloads and
  `policy_evaluate` drives final verdicts.
- Governance assertions now validate structured result surfaces
  (`violation_count`, `summary_json`) so pass/fail contracts are not coupled to
  PASS text output tokens.
- Spec-lang utility surface now includes collection helpers for governance
  policy authoring (`sum`, `min`, `max`, `sort_by`, `pluck`, `distinct`,
  `is_empty`, `coalesce`, `matches_all`).
- Spec-lang now includes pure filesystem utility helpers under `ops.*`:
  `ops.fs.path.*` (normalize/join/split/dirname/basename/ext/stem,
  relativize/common_prefix/parents/within/compare/sort) and
  `ops.fs.file.*` metadata predicates/getters (`exists`, `is_file`, `is_dir`,
  `size_bytes`, `path`, `name`, `parent`, `ext`, `get`).
- Spec-lang now includes pure JSON helpers under `ops.fs.json.*`:
  `parse`, `get`, `get_or`, and `has_path` for deterministic JSON/path lookup.
- Spec-lang now includes pure glob helpers under `ops.fs.glob.*`:
  `match`, `filter`, `any`, and `all` for deterministic path pattern checks.
- Spec-lang now includes Ramda-style deep equality, set algebra
  (`union`, `intersection`, `difference`, `symmetric_difference`,
  `is_subset`, `is_superset`, `set_equals`), expanded collection transforms
  (`reduce`, `reject`, `find`, `partition`, `group_by`, `uniq_by`, `flatten`,
  `concat`, `append`, `prepend`, `take`, `drop`), and automatic builtin
  currying by arity.
- Spec-lang full-suite now adds strict numeric math (`mul`, `div`, `mod`,
  `pow`, `abs`, `negate`, `inc`, `dec`, `clamp`, `round`, `floor`, `ceil`),
  additional list/object utilities (`slice`, `reverse`, `zip`, `zip_with`,
  `range`, `repeat`, `keys`, `values`, `entries`, `merge`, `assoc`, `dissoc`,
  `pick`, `omit`), and compositional helpers (`prop_eq`, `where`, `compose`,
  `pipe`, `identity`, `always`, `replace`, `pad_left`, `pad_right`) with
  explicit JSON-type predicates (`is_null`, `is_bool`, `is_number`,
  `is_string`, `is_list`, `is_dict`).
- Docs quality v2 adds schema-backed `doc-meta`, manifest-driven reference
  generation, and governance checks for docs token ownership/dependencies and
  generated artifact freshness.
- Documentation generation is registry-first via
  `docs/spec/schema/docs_generator_registry_v1.yaml` and canonical orchestrator
  command `scripts/docs_generate_all.py` (`--build` / `--check`).
- Docs generation is now spec-driven through executable
  `type: docs.generate` cases (`docs/spec/impl/docs_generate/cases/*.spec.md`)
  and moustache-core templates under `docs/book/templates/`.
- Generated API catalogs now include runner interface commands, harness type
  profiles, and spec-lang builtin semantic references with machine artifacts in
  `.artifacts/*-catalog.json` and generated book pages under `docs/book/`.
- Spec-lang generated docs now include namespace chapters
  (`93a_std_core.md` through `93i_std_json_schema_fn_null.md`) with
  per-symbol signatures, parameters, returns, error conditions, and examples.
- Harness execution workflow is now hard-cut componentized around shared
  components (`build_execution_context`, `run_assertions_with_context`,
  `resolve_subject_for_target`) across `text.file`, `cli.run`,
  `orchestration.run`, `docs.generate`, and `api.http`.
- Governance enforces docs semantic completeness and minimum quality-score
  thresholds for runner/harness/stdlib generated references.
- Documentation catalog generation additionally includes policy rule,
  traceability, governance-check, metrics-field, and schema-field references
  with generated pages under `docs/book/91_appendix_*` through
  `docs/book/98_appendix_*` and synchronized machine artifacts in
  `.artifacts/`.
- Book chapter taxonomy is canonicalized to Learn -> Do -> Debug flow:
  `04_spec_lang_guide.md` appears before strict semantics in
  `07_spec_lang_reference.md`, while generated catalogs are appendices only.
- Normalization tooling is unified under `scripts/normalize_repo.py` with
  profile-driven rules from `docs/spec/schema/normalization_profile_v1.yaml`;
  CI runs `normalize-check` and local workflow uses `normalize-fix`.
- Docs layout now enforces canonical roots (`docs/book`, `docs/spec`,
  `docs/impl`, `docs/history/reviews`) with `index.md` as the only directory
  index filename under `docs/**`; legacy `docs/history/reviews` and docs-local
  `README.md` filenames are forbidden.
- Gate scripts now invoke CI summary orchestration through runner-interface
  subcommand `ci-gate-summary` (no direct gate-script Python summary call).
- Orchestration effect symbols now use deep-dot `ops.*` naming (for example
  `ops.fs.file.read`, `ops.proc.command.exec`) with underscore shorthand forms
  forbidden by governance.
- Gate scripts default to canonical adapter (`scripts/runner_adapter.sh`)
  in rust mode; Python runner lane remains explicit opt-in via
  `SPEC_RUNNER_IMPL=python` (or `--impl python`).
- Contract path model now uses virtual-root semantics (`/` = contract root)
  with canonical `/...` normalization and explicit deny-by-default
  `external://provider/id` references.
- Spec corpora now use domain-tree layout under `.../cases/<domain>/` and
  `.../libraries/<domain>/` with machine-checked `index.md` sync.

Canonical spec docs:

- `docs/spec/schema/schema_v1.md`
- `docs/spec/contract/`
- `docs/spec/backlog.md`
