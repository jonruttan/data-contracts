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

    Rules:
    - leaf assertions MUST NOT define `target`; target is inherited from a
      parent group (`must` / `can` / `cannot`).
    - Each op key's value MUST be a list.
    - Duplicate keys are not allowed by YAML; multi-checks use lists.
    """
    if not isinstance(leaf, dict):
        raise TypeError("assert leaf must be a mapping")
    if "target" in leaf:
        raise ValueError("leaf assertion must not include key: target; move target to a parent group")
    target = str(target_override or "").strip()
    if not target:
        raise ValueError("assertion leaf requires inherited target from a parent group")
    if "op" in leaf or "value" in leaf:
        raise ValueError("legacy assertion shape (op/value) is not supported")
    if any(k in leaf for k in ("all", "any", "must", "can", "cannot")):
        raise ValueError("leaf assertion must not include group keys")
    if "is" in leaf:
        raise ValueError("leaf assertion key 'is' is not supported; use a 'cannot' group")
    known_ops = {
        "exists",
        "contain",
        "regex",
        "json_type",
    }

    any_found = False
    for op, raw in leaf.items():
        if op not in known_ops:
            raise ValueError(f"unsupported op: {op}")
        any_found = True
        if not isinstance(raw, list):
            raise TypeError(f"assertion op '{op}' must be a list")
        canonical = op
        is_true = True
        for v in raw:
            yield target, canonical, v, is_true
    if not any_found:
        raise ValueError("assertion missing an op key (e.g. contain:, regex:, ...)")


def eval_assert_tree(assert_spec: Any, *, eval_leaf) -> None:
    """
    Evaluate an assertion tree.

    Supported shapes:
    - list: implicit AND across items (top-level `assert:` is typically a list)
    - mapping with exactly one group key:
      - `must:`: AND across child nodes
      - `can:`: OR across child nodes (at least one must pass)
      - `cannot:`: NONE across child nodes (no child may pass)
    - group nodes may include `target:`; child leaves inherit that target
    - leaf mapping with op keys (target inherited from parent group)
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

        if "all" in node or "any" in node:
            raise ValueError("assert group aliases 'all'/'any' are not supported; use 'must'/'can'")

        present_groups = [k for k in ("must", "can", "cannot") if k in node]
        if present_groups:
            if len(present_groups) > 1:
                keys = ", ".join(present_groups)
                raise ValueError(f"assert group must include exactly one key (must/can/cannot), got: {keys}")
            node_target = str(node.get("target", "")).strip() or inherited_target
            group_key = present_groups[0]
            extra = [k for k in node.keys() if k not in (group_key, "target")]
            if extra:
                bad = sorted(str(k) for k in extra)[0]
                raise ValueError(f"unknown key in assert group: {bad}")

            if group_key == "must":
                children = node.get("must")
                if not isinstance(children, list):
                    raise TypeError("assert.must must be a list")
                if not children:
                    raise ValueError("assert.must must not be empty")
                for child in children:
                    _eval_node(child, inherited_target=node_target)

            if group_key == "can":
                children = node.get("can")
                if not isinstance(children, list):
                    raise TypeError("assert.can must be a list")
                if not children:
                    raise ValueError("assert.can must not be empty")
                # can: pass if at least one child passes; if all fail, raise a helpful message.
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
                    msg = "all 'can' branches failed"
                    if failures:
                        details = "\n".join(f"- {str(e) or e.__class__.__name__}" for e in failures[:5])
                        msg = f"{msg}:\n{details}"
                    raise AssertionError(msg)

            if group_key == "cannot":
                children = node.get("cannot")
                if not isinstance(children, list):
                    raise TypeError("assert.cannot must be a list")
                if not children:
                    raise ValueError("assert.cannot must not be empty")
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
