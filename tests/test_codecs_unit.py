# SPEC-OPT-OUT: Unit coverage for multi-format external codecs and discovery policy defaults.
from __future__ import annotations

import json
from pathlib import Path

from spec_runner.codecs import discover_case_files, load_external_cases


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_load_external_cases_defaults_to_md_only(tmp_path: Path) -> None:
    _write(
        tmp_path / "a.spec.md",
        """```yaml spec-test
id: A
 type: text.file
```
""".replace("\n ", "\n"),
    )
    _write(tmp_path / "b.spec.yaml", "id: B\ntype: text.file\n")

    loaded = load_external_cases(tmp_path)
    assert [(p.name, c["id"]) for p, c in loaded] == [("a.spec.md", "A")]


def test_load_external_cases_can_opt_in_yaml_and_json(tmp_path: Path) -> None:
    _write(
        tmp_path / "a.spec.md",
        """```yaml spec-test
id: A
type: text.file
```
""",
    )
    _write(tmp_path / "b.spec.yaml", "id: B\ntype: text.file\n")
    (tmp_path / "c.spec.json").write_text(json.dumps({"id": "C", "type": "text.file"}), encoding="utf-8")

    loaded = load_external_cases(tmp_path, formats={"md", "yaml", "json"})
    assert sorted((p.name, c["id"]) for p, c in loaded) == [
        ("a.spec.md", "A"),
        ("b.spec.yaml", "B"),
        ("c.spec.json", "C"),
    ]


def test_discover_case_files_respects_default_md_pattern(tmp_path: Path) -> None:
    _write(tmp_path / "x.md", "# no")
    _write(tmp_path / "ok.spec.md", "# yes")
    found = discover_case_files(tmp_path)
    assert [p.name for p, _fmt in found] == ["ok.spec.md"]
