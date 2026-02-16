# SPEC-OPT-OUT: Exercises pure ops symbol parser/validator helper functions not represented as executable spec cases yet.
from __future__ import annotations

import pytest

from spec_runner.ops_namespace import is_legacy_underscore_form
from spec_runner.ops_namespace import parse_ops_symbol
from spec_runner.ops_namespace import validate_ops_symbol


def test_parse_ops_symbol_accepts_deep_dot() -> None:
    parsed = parse_ops_symbol("ops.fs.file.read")
    assert parsed.raw == "ops.fs.file.read"
    assert parsed.segments == ("ops", "fs", "file", "read")


def test_parse_ops_symbol_rejects_bad_forms() -> None:
    with pytest.raises(ValueError, match=r"start with 'ops\.'"):
        parse_ops_symbol("fs.file.read")
    with pytest.raises(ValueError, match="at least three segments"):
        parse_ops_symbol("ops.x")
    with pytest.raises(ValueError, match="must not contain empty segments"):
        parse_ops_symbol("ops..file.read")


def test_validate_ops_symbol_rejects_legacy_underscore() -> None:
    assert is_legacy_underscore_form("ops.fs.read_file") is True
    diags = validate_ops_symbol("ops.fs.read_file", context="x")
    assert any(d.code == "ORCHESTRATION_OPS_UNDERSCORE_LEGACY_FORBIDDEN" for d in diags)


def test_validate_ops_symbol_rejects_invalid_segment_chars() -> None:
    diags = validate_ops_symbol("ops.fs.file.Read", context="x")
    assert any(d.code == "ORCHESTRATION_OPS_DEEP_DOT_REQUIRED" for d in diags)
