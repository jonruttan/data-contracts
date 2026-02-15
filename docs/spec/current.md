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
- Canonical authoring remains `.spec.md`; `.spec.yaml/.spec.yml/.spec.json`
  are opt-in external adapter formats.
- Portability reporting includes a segmented self-containment metric across
  conformance/governance/impl `.spec.md` corpora.
- Portability governance enforces non-regression on configured spec-lang
  self-containment baseline metrics.
- Additional ratchet-only metrics track spec-lang adoption, runner
  independence, python dependency evidence, docs operability, and contract
  assertions quality.
- Objective scorecard reporting now composes all metric families into a single
  objective-aligned health view with tripwire hits and course-correction
  recommendations.
- Spec-lang now supports reusable library symbols via
  `harness.spec_lang.library_paths` and optional `exports` allowlists.
- Governance decision checks are now policy-engine first:
  check extractors emit deterministic subject payloads and
  `policy_evaluate` drives final verdicts.
- Governance assertions now validate structured result surfaces
  (`violation_count`, `summary_json`) so pass/fail contracts are not coupled to
  PASS text output tokens.
- Spec-lang utility surface now includes collection helpers for governance
  policy authoring (`sum`, `min`, `max`, `sort_by`, `pluck`, `distinct`,
  `is_empty`, `coalesce`, `matches_all`).
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
- Normalization tooling is unified under `scripts/normalize_repo.py` with
  profile-driven rules from `docs/spec/schema/normalization_profile_v1.yaml`;
  CI runs `normalize-check` and local workflow uses `normalize-fix`.
- Gate scripts now invoke CI summary orchestration through runner-interface
  subcommand `ci-gate-summary` (no direct gate-script Python summary call).
- Gate scripts default to Rust adapter (`scripts/rust/runner_adapter.sh`);
  Python runner lane remains explicit opt-in via `SPEC_RUNNER_BIN`.

Canonical spec docs:

- `docs/spec/schema/schema_v1.md`
- `docs/spec/contract/`
- `docs/spec/backlog.md`
