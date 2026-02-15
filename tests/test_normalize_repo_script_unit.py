# SPEC-OPT-OUT: Exercises normalization script orchestration and diagnostics not yet representable as stable .spec.md fixtures.
from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/normalize_repo.py"
    spec = importlib.util.spec_from_file_location("normalize_repo_script", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load normalize_repo.py module")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _seed_profile(tmp_path: Path) -> Path:
    profile = tmp_path / "docs/spec/schema/normalization_profile_v1.yaml"
    _write(
        profile,
        """version: 1
paths:
  specs: [docs/spec]
  contracts: [docs/spec/contract, docs/spec/schema]
  tests: [tests]
expression:
  expression_fields: [evaluate, policy_evaluate]
spec_style:
  conformance_max_block_lines: 120
docs_token_sync:
  rules:
    - id: TOKEN
      file: docs/spec/schema/schema_v1.md
      must_contain: ["mapping AST"]
      must_not_contain: ["list S-expression"]
replacements:
  rules:
    - id: REWRITE
      file: docs/spec/schema/schema_v1.md
      edits:
        - old: "old token"
          new: "new token"
""",
    )
    return profile


def test_normalize_check_passes_when_tools_and_tokens_are_clean(tmp_path, monkeypatch):
    mod = _load_script_module()
    profile = _seed_profile(tmp_path)
    _write(tmp_path / "docs/spec/schema/schema_v1.md", "mapping AST\n")

    monkeypatch.setattr(mod, "ROOT", tmp_path)
    monkeypatch.setattr(mod, "PROFILE_PATH", profile)
    monkeypatch.setattr(mod, "_run", lambda _cmd: (0, ""))

    code = mod.main(["--check"])
    assert code == 0


def test_normalize_check_fails_on_token_drift(tmp_path, monkeypatch):
    mod = _load_script_module()
    profile = _seed_profile(tmp_path)
    _write(tmp_path / "docs/spec/schema/schema_v1.md", "list S-expression\n")

    monkeypatch.setattr(mod, "ROOT", tmp_path)
    monkeypatch.setattr(mod, "PROFILE_PATH", profile)
    monkeypatch.setattr(mod, "_run", lambda _cmd: (0, ""))

    code = mod.main(["--check"])
    assert code == 1


def test_normalize_write_applies_replacements(tmp_path, monkeypatch):
    mod = _load_script_module()
    profile = _seed_profile(tmp_path)
    p = tmp_path / "docs/spec/schema/schema_v1.md"
    _write(p, "old token\nmapping AST\n")

    monkeypatch.setattr(mod, "ROOT", tmp_path)
    monkeypatch.setattr(mod, "PROFILE_PATH", profile)
    monkeypatch.setattr(mod, "_run", lambda _cmd: (0, ""))

    code = mod.main(["--write"])
    assert code == 0
    assert "new token" in p.read_text(encoding="utf-8")
