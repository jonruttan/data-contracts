# Spec-Lang Markdown Domain Library

## LIB-DOMAIN-MD-001

```yaml spec-test
id: LIB-DOMAIN-MD-001
title: markdown projection helper functions
type: spec_lang.library
definitions:
  public:
    md.has_heading:
      fn:
      - [subject, heading]
      - contains:
        - {get: [{var: subject}, value]}
        - {var: heading}
```
