from pathlib import Path

import pytest

from spec_runner.doc_parser import iter_spec_doc_tests


def _write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def test_iter_spec_doc_tests_parses_single_mapping(tmp_path):
    _write(
        tmp_path / "a.md",
        """# Doc

```yaml spec-test
id: CK-CLI-001
title: Example
type: cli.example
```
""",
    )

    cases = list(iter_spec_doc_tests(tmp_path))
    assert len(cases) == 1
    assert cases[0].doc_path.name == "a.md"
    assert cases[0].test["id"] == "CK-CLI-001"
    assert cases[0].test["type"] == "cli.example"


def test_iter_spec_doc_tests_parses_list_of_mappings(tmp_path):
    _write(
        tmp_path / "a.md",
        """# Doc

```yaml spec-test
- id: CK-CLI-001
  title: One
  type: cli.one
- id: CK-CLI-002
  title: Two
  type: cli.two
```
""",
    )

    cases = list(iter_spec_doc_tests(tmp_path))
    assert [c.test["id"] for c in cases] == ["CK-CLI-001", "CK-CLI-002"]


def test_iter_spec_doc_tests_requires_id_and_type(tmp_path):
    _write(
        tmp_path / "a.md",
        """```yaml spec-test
title: Missing type
id: CK-CLI-001
```
""",
    )

    with pytest.raises(ValueError, match="must include 'id' and 'type'"):
        list(iter_spec_doc_tests(tmp_path))


def test_iter_spec_doc_tests_rejects_non_mapping_payload(tmp_path):
    _write(
        tmp_path / "a.md",
        """```yaml spec-test
42
```
""",
    )

    with pytest.raises(TypeError, match="must be a mapping or a list of mappings"):
        list(iter_spec_doc_tests(tmp_path))


def test_iter_spec_doc_tests_rejects_non_mapping_in_list(tmp_path):
    _write(
        tmp_path / "a.md",
        """```yaml spec-test
- id: CK-CLI-001
  title: ok
  type: cli.ok
- 123
```
""",
    )

    with pytest.raises(TypeError, match="contains a non-mapping test"):
        list(iter_spec_doc_tests(tmp_path))


def test_iter_spec_doc_tests_supports_tilde_fence_and_yml_token(tmp_path):
    _write(
        tmp_path / "a.md",
        """# Doc

~~~spec-test yml
id: CK-CLI-010
type: cli.example
~~~
""",
    )

    cases = list(iter_spec_doc_tests(tmp_path))
    assert len(cases) == 1
    assert cases[0].test["id"] == "CK-CLI-010"


def test_iter_spec_doc_tests_accepts_info_tokens_in_any_order(tmp_path):
    _write(
        tmp_path / "a.md",
        """# Doc

```spec-test yaml
id: CK-CLI-011
type: cli.example
```
""",
    )

    cases = list(iter_spec_doc_tests(tmp_path))
    assert len(cases) == 1
    assert cases[0].test["id"] == "CK-CLI-011"


def test_iter_spec_doc_tests_requires_matching_closing_fence_length(tmp_path):
    _write(
        tmp_path / "a.md",
        """# Doc

````yaml spec-test
id: CK-CLI-012
type: cli.example
note: |
  ```
````
""",
    )

    cases = list(iter_spec_doc_tests(tmp_path))
    assert len(cases) == 1
    assert cases[0].test["id"] == "CK-CLI-012"


def test_iter_spec_doc_tests_ignores_non_spec_fences(tmp_path):
    _write(
        tmp_path / "a.md",
        """# Doc

```yaml
id: CK-CLI-013
type: cli.example
```
""",
    )

    cases = list(iter_spec_doc_tests(tmp_path))
    assert cases == []
