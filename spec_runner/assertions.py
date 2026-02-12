import json
import re
import inspect
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


_TEXT_OPS = {"contain", "regex"}


def assert_text_op(subject: str, op: str, value: Any, *, is_true: bool = True) -> None:
    """
    Shared implementation for text-match ops across harnesses.

    Keeping this centralized avoids subtly different semantics in different kinds.
    """
    if op == "contain":
        ok = str(value) in subject
    elif op == "regex":
        ok = re.search(str(value), subject) is not None
    else:
        raise ValueError(f"unsupported text op: {op}")
    assert ok is bool(is_true)


def is_text_op(op: str) -> bool:
    return op in _TEXT_OPS


def iter_leaf_assertions(leaf: Any, *, target_override: str | None = None):
    """
    Yield (target, op, value, is_true) tuples from a leaf assertion mapping.

    Canonical leaf shape:

    - target: stderr
      contain: ["WARN:"]
      regex: ["traceback"]
    - target: stderr
      cannot:
        - contain: ["ERROR:"]

    Rules:
    - `target` is required unless a non-empty `target_override` is provided.
    - Each op key's value MUST be a list.
    - Duplicate keys are not allowed by YAML; multi-checks use lists.
    """
    if not isinstance(leaf, dict):
        raise TypeError("assert leaf must be a mapping")
    target = str(leaf.get("target", "")).strip()
    if not target:
        target = str(target_override or "").strip()
    if not target:
        raise ValueError("assertion missing required key: target")
    if "op" in leaf or "value" in leaf:
        raise ValueError("legacy assertion shape (op/value) is not supported")
    if any(k in leaf for k in ("all", "any", "must", "can", "cannot")):
        raise ValueError("leaf assertion must not include group keys (all/any/must/can/cannot)")
    known_ops = {
        "exists",
        "contain",
        "contains",
        "regex",
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
        canonical = "contain" if op == "contains" else op
        default_is_true = leaf.get("is", True)
        if not isinstance(default_is_true, bool):
            raise TypeError("assertion key 'is' must be a bool")
        is_true = default_is_true
        for v in raw:
            yield target, canonical, v, is_true
    if "is" in leaf and not any_found:
        raise ValueError("assertion key 'is' requires at least one operator")
    if not any_found:
        raise ValueError("assertion missing an op key (e.g. contains:, regex:, ...)")


def eval_assert_tree(assert_spec: Any, *, eval_leaf) -> None:
    """
    Evaluate an assertion tree.

    Supported shapes:
    - list: implicit AND across items (top-level `assert:` is typically a list)
    - mapping with `must:` / `all:`: AND across child nodes
    - mapping with `can:` / `any:`: OR across child nodes (at least one must pass)
    - mapping with `cannot:`: NONE across child nodes (no child may pass)
    - group nodes may include `target:`; child leaves inherit that target
    - leaf mapping with `target:` plus op keys
    """

    leaf_sig = inspect.signature(eval_leaf)
    accepts_inherited_target = (
        "inherited_target" in leaf_sig.parameters
        or any(p.kind == inspect.Parameter.VAR_KEYWORD for p in leaf_sig.parameters.values())
    )

    def _call_leaf(node: dict, *, inherited_target: str | None) -> None:
        if accepts_inherited_target:
            eval_leaf(node, inherited_target=inherited_target)
        else:
            eval_leaf(node)

    def _eval_node(node: Any, *, inherited_target: str | None = None) -> None:
        if node is None:
            return
        if isinstance(node, list):
            for child in node:
                _eval_node(child, inherited_target=inherited_target)
            return
        if not isinstance(node, dict):
            raise TypeError("assert node must be a mapping or a list")

        has_all = "all" in node or "must" in node
        has_any = "any" in node or "can" in node
        has_cannot = "cannot" in node
        if has_all or has_any or has_cannot:
            node_target = str(node.get("target", "")).strip() or inherited_target
            extra = [k for k in node.keys() if k not in ("all", "any", "must", "can", "cannot", "target")]
            if extra:
                bad = sorted(str(k) for k in extra)[0]
                raise ValueError(f"unknown key in assert group: {bad}")

            if has_all:
                children = node.get("must", node.get("all"))
                if not isinstance(children, list):
                    raise TypeError("assert.must/all must be a list")
                for child in children:
                    _eval_node(child, inherited_target=node_target)

            if has_any:
                children = node.get("can", node.get("any"))
                if not isinstance(children, list):
                    raise TypeError("assert.can/any must be a list")
                # can/any: pass if at least one child passes; if all fail, raise a helpful message.
                failures: list[BaseException] = []
                any_passed = False
                for child in children:
                    try:
                        _eval_node(child, inherited_target=node_target)
                        any_passed = True
                        break
                    except AssertionError as e:
                        failures.append(e)
                if not any_passed:
                    msg = "all 'can/any' branches failed"
                    if failures:
                        details = "\n".join(f"- {str(e) or e.__class__.__name__}" for e in failures[:5])
                        msg = f"{msg}:\n{details}"
                    raise AssertionError(msg)

            if has_cannot:
                children = node.get("cannot")
                if not isinstance(children, list):
                    raise TypeError("assert.cannot must be a list")
                # cannot: pass only when every child assertion fails.
                passed = 0
                for child in children:
                    try:
                        _eval_node(child, inherited_target=node_target)
                        passed += 1
                    except AssertionError:
                        continue
                if passed:
                    raise AssertionError(f"'cannot' failed: {passed} branch(es) passed")

            return

        # Leaf
        _call_leaf(node, inherited_target=inherited_target)

    _eval_node(assert_spec)
