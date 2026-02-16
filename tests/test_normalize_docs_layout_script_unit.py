# SPEC-OPT-OUT: Verifies filesystem layout normalization script behavior that is not representable as stable .spec.md fixtures.
from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/normalize_docs_layout.py"
    spec = importlib.util.spec_from_file_location("normalize_docs_layout_script", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load normalize_docs_layout.py module")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _seed_profile(tmp_path: Path) -> Path:
    profile = tmp_path / "docs/spec/schema/docs_layout_profile_v1.yaml"
    _write(
        profile,
        """version: 1
canonical_roots: [/docs/book, /docs/spec, /docs/impl, /docs/history/reviews]
forbidden_roots: [/docs/reviews]
index_filename: index.md
required_index_dirs:
  - /docs/book
  - /docs/spec
forbidden_filenames: [README.md, .DS_Store]
filename_policy:
  lowercase_only: true
  forbid_spaces: true
  allow_extensions: [.md, .yaml, .yml, .json, .txt]
""",
    )
    return profile


def test_docs_layout_check_passes_for_clean_layout(tmp_path, monkeypatch):
    mod = _load_script_module()
    profile = _seed_profile(tmp_path)
    _write(tmp_path / "docs/book/index.md", "# book\n")
    _write(tmp_path / "docs/spec/index.md", "# spec\n")
    (tmp_path / "docs/impl").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/history/reviews").mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(mod, "ROOT", tmp_path)
    code = mod.main(["--check", "--profile", str(profile)])
    assert code == 0


def test_docs_layout_check_fails_on_readme_and_legacy_reviews(tmp_path, monkeypatch):
    mod = _load_script_module()
    profile = _seed_profile(tmp_path)
    _write(tmp_path / "docs/book/README.md", "# book\n")
    _write(tmp_path / "docs/spec/index.md", "# spec\n")
    (tmp_path / "docs/reviews").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/history/reviews").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/impl").mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(mod, "ROOT", tmp_path)
    code = mod.main(["--check", "--profile", str(profile)])
    assert code == 1


def test_docs_layout_write_rewrites_readme_to_index(tmp_path, monkeypatch):
    mod = _load_script_module()
    profile = _seed_profile(tmp_path)
    _write(tmp_path / "docs/book/README.md", "# book\n")
    _write(tmp_path / "docs/spec/README.md", "# spec\n")
    (tmp_path / "docs/history/reviews").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/impl").mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(mod, "ROOT", tmp_path)
    code = mod.main(["--write", "--profile", str(profile)])
    assert code == 0
    assert (tmp_path / "docs/book/index.md").exists()
    assert (tmp_path / "docs/spec/index.md").exists()
