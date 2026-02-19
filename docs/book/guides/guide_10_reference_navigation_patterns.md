# Guide 10: Reference Navigation Patterns

```yaml doc-meta
doc_id: DOC-GUIDE-210
title: Guide 10 Reference Navigation Patterns
status: active
audience: reviewer
owns_tokens:
- guide_reference_navigation_patterns
requires_tokens:
- normative_reference_map
commands:
- run: ./scripts/control_plane.sh docs-generate-check
  purpose: Confirm reference navigation surfaces are synchronized.
examples:
- id: EX-GUIDE-10-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Navigate quickly from narrative guidance to normative contracts and generated references.

## Inputs

- chapter 90 reference map
- `docs/book/reference_manifest.yaml`
- generated appendices `91..99`

## Outputs

- deterministic path to authoritative source
- reduced review latency for contract questions

## Failure Modes

- using appendix text as normative source
- skipping manifest linkage while reviewing changes
- citing stale generated references

## Do This Now

```bash
./scripts/control_plane.sh docs-generate-check
rg -n "contract_refs" docs/book/reference_manifest.yaml
```

## How To Verify Success

- [ ] every narrative chapter points to contract refs
- [ ] generated reference index resolves chapter links
- [ ] docs freshness check passes

## Common Failure Signatures

| Signature | Likely Cause | Action |
| --- | --- | --- |
| missing `contract_refs` entry | manifest drift | add normative mapping for the chapter/guide |
| broken link in reference index | manifest path typo | correct path and regenerate reference index |
| outdated appendix content | generation skipped | rebuild docs and commit outputs |
