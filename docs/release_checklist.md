# Release Contract

Release readiness is defined by executable gates, not manual checklists.
Sequential "do X, then inspect Y" checklist choreography is an anti-pattern in
this repo.

## Gate Entry Points

Optional fast preflight (developer convenience, not release criterion):

```sh
make ci-smoke
```

Normative merge/publish gate:

```sh
./scripts/ci_gate.sh
```

Passing `./scripts/ci_gate.sh` satisfies the release contract for this repo.
`make ci-smoke` is a subset preflight to catch issues earlier; it is not a
separate release requirement.

## Why This Exists

- Keep release criteria deterministic.
- Avoid process drift from manual checklist text.
- Push quality rules into governance/spec tests where they are executable.

## If A Gate Fails

Use:

- `docs/development.md` (CI/docs triage section)
- governance failure IDs (for example `SRGOV-*`) as the source of truth

When a failure requires repeated human steps, convert it into an executable
check rather than expanding manual procedure docs.
