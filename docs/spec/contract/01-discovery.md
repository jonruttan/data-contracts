# Discovery Contract (v1)

## Inputs

- Input is a directory path.
- Runner scans `*.md` files in that directory (non-recursive).

## Fence Extraction

- Extract fenced blocks with opening line exactly: ```` ```yaml spec-test ````.
- Closing fence is: ```` ``` ````.
- Fence body is parsed as YAML.

## Case Shapes

- Fence body MUST decode to either:
  - a mapping (one case), or
  - a list of mappings (many cases).
- Each case MUST include `id` and `type`.
- Legacy `kind` is accepted and normalized to `type`.
