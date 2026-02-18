# SPEC-OPT-OUT: Unit-level path normalization/error behavior for virtual-root resolver internals.
from pathlib import Path

import pytest

from spec_runner.virtual_paths import VirtualPathError, normalize_contract_path, parse_external_ref, resolve_contract_path


def test_normalize_virtual_absolute_and_relative_equivalent() -> None:
    assert normalize_contract_path("/specs/schema/schema_v1.md", field="x") == "/specs/schema/schema_v1.md"
    assert normalize_contract_path("specs/schema/schema_v1.md", field="x") == "/specs/schema/schema_v1.md"


def test_rejects_contract_root_escape() -> None:
    with pytest.raises(VirtualPathError):
        normalize_contract_path("../../outside", field="x")


def test_resolve_contract_path_within_root(tmp_path: Path) -> None:
    root = tmp_path
    target = root / "specs/schema/schema_v1.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("ok", encoding="utf-8")
    resolved = resolve_contract_path(root, "/specs/schema/schema_v1.md", field="x")
    assert resolved == target.resolve()


def test_parse_external_ref() -> None:
    ref = parse_external_ref("external://catalog/id-123")
    assert ref is not None
    assert ref.provider == "catalog"
    assert ref.ref_id == "id-123"
