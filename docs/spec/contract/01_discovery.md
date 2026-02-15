# Discovery Contract (v1)

## Inputs

- Input is a directory path.
- Runner scans files matching configurable case-file pattern in that
  directory (non-recursive).
- Canonical executable case trees are markdown-only and MUST use `.spec.md`:
  - `docs/spec/conformance/cases`
  - `docs/spec/governance/cases`
  - `docs/spec/impl`
- Canonical executable case trees MUST NOT include runnable
  `.spec.yaml`/`.spec.yml`/`.spec.json` files.

## Fence Extraction

- Extract fenced blocks using Markdown fence syntax with either:
  - backticks: ```` ``` ```` (3+), or
  - tildes: `~~~` (3+).
- Opening fence info string MUST include:
  - `spec-test`
  - and one of: `yaml`, `yml`
- Info-string token order is not significant.
- Closing fence MUST use the same fence character as the opener and a fence
  length greater than or equal to the opener.
- Fence body is parsed as YAML.

## Case Shapes

- Fence body MUST decode to either:
  - a mapping (one case), or
  - a list of mappings (many cases).
- Each case MUST include `id` and `type`.
