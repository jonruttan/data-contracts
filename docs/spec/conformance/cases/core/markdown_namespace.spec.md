# Markdown Namespace Conformance Cases

## SRCONF-MARKDOWN-NS-001

```yaml contract-spec
id: SRCONF-MARKDOWN-NS-001
title: markdown namespace negative fixture file is present
purpose: Ensures the legacy markdown namespace fixture is available for script-level
  negative-path coverage.
type: text.file
path: /fixtures/markdown_namespace_negative/docs/book/index.md
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: must
  target: text
  asserts:
  - std.string.contains:
    - var: subject
    - legacy markdown alias tokens
```
