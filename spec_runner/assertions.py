import json
import re
from pathlib import Path
from typing import Any


def parse_json(text: str) -> Any:
    return json.loads(text)


def first_nonempty_line(text: str) -> str:
    for ln in (text or "").splitlines():
        if ln.strip():
            return ln.strip()
    return ""


def assert_stdout_path_exists(stdout: str, *, suffix: str | None = None) -> Path:
    line = first_nonempty_line(stdout)
    p = Path(line)
    assert line, "expected stdout to contain a path"
    assert p.exists(), f"expected path to exist: {p}"
    if suffix:
        assert p.name.endswith(str(suffix))
    return p


_TEXT_OPS = {"contains", "regex"}


def assert_text_op(subject: str, op: str, value: Any, *, is_true: bool = True) -> None:
    """
    Shared implementation for text-match ops across harnesses.

    Keeping this centralized avoids subtly different semantics in different kinds.
    """
    if op == "contains":
        ok = str(value) in subject
    elif op == "regex":
        ok = re.search(str(value), subject) is not None
    else:
        raise ValueError(f"unsupported text op: {op}")
    assert ok is bool(is_true)


def is_text_op(op: str) -> bool:
    return op in _TEXT_OPS


def iter_leaf_assertions(leaf: Any):
    """
    Yield (target, op, value, is_true) tuples from a leaf assertion mapping.

    Canonical leaf shape:

    - target: stderr
      contains: ["WARN:"]
      regex: ["traceback"]
      is: false

    Rules:
    - `target` is required.
    - Each op key's value MUST be a list.
    - Duplicate keys are not allowed by YAML; multi-checks use lists.
    """
    if not isinstance(leaf, dict):
        raise TypeError("assert leaf must be a mapping")
    target = str(leaf.get("target", "")).strip()
    if not target:
        raise ValueError("assertion missing required key: target")
    if "op" in leaf or "value" in leaf:
        raise ValueError("legacy assertion shape (op/value) is not supported")
    if "any" in leaf or "all" in leaf:
        raise ValueError("leaf assertion must not include 'any' or 'all'")
    default_is_true = leaf.get("is", True)
    if not isinstance(default_is_true, bool):
        raise TypeError("assertion key 'is' must be a bool")

    known_ops = {
        "exists",
        "contains",
        "not_contains",
        "regex",
        "not_regex",
        "json_type",
        "is",
    }

    any_found = False
    for op, raw in leaf.items():
        if op in ("target", "is"):
            continue
        if op not in known_ops:
            raise ValueError(f"unsupported op: {op}")
        any_found = True
        if not isinstance(raw, list):
            raise TypeError(f"assertion op '{op}' must be a list")
        canonical = op
        is_true = default_is_true
        if op == "not_contains":
            canonical = "contains"
            if "is" in leaf:
                raise ValueError("do not combine 'is' with not_contains; use contains + is: false")
            is_true = False
        elif op == "not_regex":
            canonical = "regex"
            if "is" in leaf:
                raise ValueError("do not combine 'is' with not_regex; use regex + is: false")
            is_true = False
        for v in raw:
            yield target, canonical, v, is_true
    if not any_found:
        raise ValueError("assertion missing an op key (e.g. contains:, regex:, ...)")


def eval_assert_tree(assert_spec: Any, *, eval_leaf) -> None:
    """
    Evaluate an assertion tree.

    Supported shapes:
    - list: implicit AND across items (top-level `assert:` is typically a list)
    - mapping with `all:`: AND across child nodes
    - mapping with `any:`: OR across child nodes (at least one must pass)
    - leaf mapping with `target:` plus op keys
    """

    def _eval_node(node: Any) -> None:
        if node is None:
            return
        if isinstance(node, list):
            for child in node:
                _eval_node(child)
            return
        if not isinstance(node, dict):
            raise TypeError("assert node must be a mapping or a list")

        has_all = "all" in node
        has_any = "any" in node
        if has_all or has_any:
            if "target" in node:
                raise ValueError("assert group node must not include 'target'")
            extra = [k for k in node.keys() if k not in ("all", "any")]
            if extra:
                bad = sorted(str(k) for k in extra)[0]
                raise ValueError(f"unknown key in assert group: {bad}")

            if has_all:
                children = node.get("all")
                if not isinstance(children, list):
                    raise TypeError("assert.all must be a list")
                for child in children:
                    _eval_node(child)

            if has_any:
                children = node.get("any")
                if not isinstance(children, list):
                    raise TypeError("assert.any must be a list")
                # any: pass if at least one child passes; if all fail, raise a helpful message.
                failures: list[BaseException] = []
                for child in children:
                    try:
                        _eval_node(child)
                        return
                    except AssertionError as e:
                        failures.append(e)
                msg = "all 'any' branches failed"
                if failures:
                    details = "\n".join(f"- {str(e) or e.__class__.__name__}" for e in failures[:5])
                    msg = f"{msg}:\n{details}"
                raise AssertionError(msg)

            return

        # Leaf
        eval_leaf(node)

    _eval_node(assert_spec)
