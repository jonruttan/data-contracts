# SPEC-OPT-OUT: Exercises schema validator error mapping and unknown-key hard-fail behavior before dispatch.
from __future__ import annotations

from spec_runner.schema_validator import validate_case_shape


def test_validate_case_shape_accepts_known_keys() -> None:
    diags = validate_case_shape(
        {
            "id": "X-1",
            "type": "text.file",
            "title": "ok",
            "contract": [],
        },
        "text.file",
        "sample.spec.md",
    )
    assert diags == []


def test_validate_case_shape_rejects_unknown_top_level_key() -> None:
    diags = validate_case_shape(
        {
            "id": "X-2",
            "type": "text.file",
            "contract": [],
            "unknown_field": True,
        },
        "text.file",
        "sample.spec.md",
    )
    assert any("unknown top-level key: unknown_field" in d.render() for d in diags)
