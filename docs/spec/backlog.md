# Spec Backlog

Lightweight queue of spec work to draft next for `spec_runner`.

- Decide which `kind`s are part of `spec_runner` core vs adapters.
- Version the `harness:` namespace and define compatibility rules.
- Define a public plugin API for third-party harnesses (if desired).
- Add a breaking-change release spec for assertion DSL removals:
  require major-version bump policy and explicit upgrade notes when removing
  supported keys (e.g. `all`/`any`/`contains`/`is`).
- Add a migration-guide spec for assertion DSL transitions:
  document old-to-new rewrites (especially `is: false` to `cannot`) with
  copy/paste examples and expected semantics.
- Add a diagnostics spec for legacy assertion keys:
  parser errors SHOULD include direct replacement hints (e.g. `contains` ->
  `contain`, `all` -> `must`, `is: false` -> `cannot`).
- Resolve stale draft conflicts in `docs/spec/drafts/`:
  mark superseded assertion drafts clearly and align all examples to current
  canonical DSL.
- Normalize test naming to canonical DSL terms:
  rename remaining `contains`/`negation`-era test names to `contain`/`cannot`
  for clearer failure triage.
