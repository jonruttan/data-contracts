import json
import inspect
from pathlib import Path
from typing import Any, Callable, Mapping

from spec_runner.internal_model import GroupNode, InternalAssertNode, PredicateLeaf
from spec_runner.spec_lang import SpecLangLimits, eval_predicate

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


def _raise_with_assert_context(
    exc: BaseException,
    *,
    case_id: str,
    assert_path: str,
    target: str | None = None,
    op: str | None = None,
) -> None:
    ctx = f"[case_id={case_id} assert_path={assert_path}"
    if target is not None:
        ctx += f" target={target}"
    if op is not None:
        ctx += f" op={op}"
    ctx += "]"
    detail = str(exc).strip()
    msg = ctx if not detail else f"{ctx} {detail}"
    if isinstance(exc, AssertionError):
        raise AssertionError(msg) from exc
    if isinstance(exc, TypeError):
        raise TypeError(msg) from exc
    if isinstance(exc, ValueError):
        raise ValueError(msg) from exc
    raise RuntimeError(msg) from exc


def iter_leaf_assertions(leaf: Any, *, target_override: str | None = None):
    """
    Yield (target, op, value, is_true) tuples from a leaf assertion mapping.

    Canonical leaf shape:

    - target: stderr
      evaluate:
        - contains: [{var: subject}, "WARN:"]

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
    if any(k in leaf for k in ("must", "can", "cannot")):
        raise ValueError("leaf assertion must not include group keys")
    if "evaluate" in leaf:
        raise ValueError("explicit evaluate leaf is not supported; use expression mapping directly")
    if not leaf:
        raise ValueError("assertion leaf must be a non-empty expression mapping")
    yield target, "evaluate", leaf, True


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
    accepts_kwargs = "**" in str(leaf_sig)
    accepts_inherited_target = "inherited_target" in leaf_sig.parameters or accepts_kwargs
    accepts_assert_path = "assert_path" in leaf_sig.parameters or accepts_kwargs

    def _call_leaf(node: dict, *, inherited_target: str | None, assert_path: str) -> None:
        kwargs = {}
        if accepts_inherited_target:
            kwargs["inherited_target"] = inherited_target
        if accepts_assert_path:
            kwargs["assert_path"] = assert_path
        if kwargs:
            eval_leaf(node, **kwargs)
        else:
            eval_leaf(node)

    def _eval_node(node: Any, *, inherited_target: str | None = None, path: str = "assert") -> None:
        if node is None:
            return
        if isinstance(node, list):
            for idx, child in enumerate(node):
                _eval_node(child, inherited_target=inherited_target, path=f"{path}[{idx}]")
            return
        if not isinstance(node, dict):
            raise TypeError("assert node must be a mapping or a list")
        step_class = str(node.get("class", "")).strip() if "class" in node else ""
        if step_class in {"must", "can", "cannot"} and "checks" in node:
            step_id = str(node.get("id", "")).strip()
            if not step_id:
                raise ValueError(f"{path}.id must be a non-empty string")
            extra = [k for k in node.keys() if k not in ("id", "class", "target", "checks")]
            if extra:
                bad = sorted(str(k) for k in extra)[0]
                raise ValueError(f"unknown key in assert step: {bad}")
            node_target = str(node.get("target", "")).strip() or inherited_target
            children = node.get("checks")
            if not isinstance(children, list):
                raise TypeError("assert step checks must be a list")
            if not children:
                raise ValueError("assert step checks must not be empty")
            step_path = f"{path}<{step_id}>"
            if step_class == "must":
                for idx, child in enumerate(children):
                    _eval_node(child, inherited_target=node_target, path=f"{step_path}.checks[{idx}]")
                return
            if step_class == "can":
                failures: list[BaseException] = []
                any_passed = False
                for idx, child in enumerate(children):
                    try:
                        _eval_node(child, inherited_target=node_target, path=f"{step_path}.checks[{idx}]")
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
                return
            if step_class == "cannot":
                passed = 0
                for idx, child in enumerate(children):
                    try:
                        _eval_node(child, inherited_target=node_target, path=f"{step_path}.checks[{idx}]")
                        passed += 1
                    except AssertionError:
                        continue
                if passed:
                    raise AssertionError(f"'cannot' failed: {passed} branch(es) passed")
                return

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
                for idx, child in enumerate(children):
                    _eval_node(child, inherited_target=node_target, path=f"{path}.must[{idx}]")

            if group_key == "can":
                children = node.get("can")
                if not isinstance(children, list):
                    raise TypeError("assert.can must be a list")
                if not children:
                    raise ValueError("assert.can must not be empty")
                # can: pass if at least one child passes; if all fail, raise a helpful message.
                failures: list[BaseException] = []
                any_passed = False
                for idx, child in enumerate(children):
                    try:
                        _eval_node(child, inherited_target=node_target, path=f"{path}.can[{idx}]")
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
                for idx, child in enumerate(children):
                    try:
                        _eval_node(child, inherited_target=node_target, path=f"{path}.cannot[{idx}]")
                        passed += 1
                    except AssertionError:
                        continue
                if passed:
                    raise AssertionError(f"'cannot' failed: {passed} branch(es) passed")

            return

        # Leaf
        _call_leaf(node, inherited_target=inherited_target, assert_path=path)

    _eval_node(assert_spec)


def evaluate_internal_assert_tree(
    assert_tree: InternalAssertNode,
    *,
    case_id: str,
    subject_for_key: Callable[[str], Any],
    limits: SpecLangLimits,
    symbols: Mapping[str, Any] | None = None,
    imports: Mapping[str, str] | None = None,
) -> None:
    """
    Evaluate compiled internal assertion tree nodes.

    Harnesses provide target -> subject resolution; all predicate checks run
    through spec-lang expressions.
    """

    def _eval_node(node: InternalAssertNode) -> None:
        if isinstance(node, PredicateLeaf):
            try:
                subject = subject_for_key(node.subject_key)
                ok = eval_predicate(
                    node.expr,
                    subject=subject,
                    limits=limits,
                    symbols=symbols,
                    imports=imports,
                )
                assert ok, "evaluate assertion failed"
            except BaseException as e:  # noqa: BLE001
                _raise_with_assert_context(
                    e,
                    case_id=case_id,
                    assert_path=node.assert_path,
                    target=node.target,
                    op=node.op,
                )
            return

        if not isinstance(node, GroupNode):
            raise TypeError("internal assert node must be GroupNode or PredicateLeaf")

        if node.op == "must":
            for child in node.children:
                _eval_node(child)
            return

        if node.op == "can":
            failures: list[BaseException] = []
            for child in node.children:
                try:
                    _eval_node(child)
                    return
                except AssertionError as e:
                    failures.append(e)
            msg = "all 'can' branches failed"
            if failures:
                details = "\n".join(f"- {str(e) or e.__class__.__name__}" for e in failures[:5])
                msg = f"{msg}:\n{details}"
            raise AssertionError(msg)

        if node.op == "cannot":
            passed = 0
            for child in node.children:
                try:
                    _eval_node(child)
                    passed += 1
                except AssertionError:
                    continue
            if passed:
                raise AssertionError(f"'cannot' failed: {passed} branch(es) passed")
            return

        raise ValueError(f"unknown internal assert group op: {node.op}")

    _eval_node(assert_tree)
