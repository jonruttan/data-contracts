# SPEC-OPT-OUT: Unit checks for moustache-core rendering semantics and strict missing-key diagnostics.
from __future__ import annotations

import pytest

from spec_runner.docs_template_engine import TemplateRenderError, render_moustache


def test_render_moustache_interpolates_variables() -> None:
    out = render_moustache("hello {{name}}", {"name": "world"})
    assert out == "hello world"


def test_render_moustache_sections_and_inverted() -> None:
    tpl = "{{#rows}}- {{name}}\n{{/rows}}{{^rows}}none\n{{/rows}}"
    out = render_moustache(tpl, {"rows": [{"name": "a"}, {"name": "b"}]})
    assert out == "- a\n- b\n"
    out_empty = render_moustache(tpl, {"rows": []})
    assert out_empty == "none\n"


def test_render_moustache_missing_key_strict_error() -> None:
    with pytest.raises(TemplateRenderError, match="missing template key"):
        render_moustache("{{missing}}", {"ok": 1}, strict=True)
