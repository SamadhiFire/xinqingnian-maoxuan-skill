#!/usr/bin/env python3
"""Validate this skill with Python's standard library only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


MAX_SKILL_NAME_LENGTH = 64
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(
    r"\[(?:[^\]\r\n]{0,60})"
    r"(?:可删|按需|待填|待替换|案例|摘要|判断|目标|对象|场景|阶段|路线|"
    r"动作|风险|约束|来源|时间点|事实|节点|说明)"
    r"(?:[^\]\r\n]{0,60})\]"
)


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"not valid UTF-8: {path}: {exc}") from exc


def parse_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has invalid YAML frontmatter")

    result: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"invalid frontmatter line: {raw_line}")
        key = key.strip()
        value = value.strip()
        if key in result:
            raise ValueError(f"duplicate frontmatter key: {key}")
        if value.startswith(('"', "'")) and value.endswith(value[0]):
            value = value[1:-1]
        result[key] = value
    return result


def validate_frontmatter(root: Path, errors: list[str]) -> str | None:
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md not found")
        return None

    try:
        frontmatter = parse_frontmatter(read_utf8(skill_md))
    except ValueError as exc:
        errors.append(str(exc))
        return None

    unexpected = set(frontmatter) - {"name", "description"}
    if unexpected:
        errors.append(f"unexpected SKILL.md frontmatter keys: {sorted(unexpected)}")

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()
    if not name:
        errors.append("missing frontmatter name")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"invalid skill name: {name}")
    elif len(name) > MAX_SKILL_NAME_LENGTH:
        errors.append(f"skill name exceeds {MAX_SKILL_NAME_LENGTH} characters")

    if root.name != name:
        errors.append(f"folder name '{root.name}' does not match skill name '{name}'")
    if not description:
        errors.append("missing frontmatter description")
    elif len(description) > 1024:
        errors.append("frontmatter description exceeds 1024 characters")
    elif "<" in description or ">" in description:
        errors.append("frontmatter description contains angle brackets")
    return name or None


def validate_openai_yaml(root: Path, skill_name: str | None, errors: list[str]) -> None:
    path = root / "agents" / "openai.yaml"
    if not path.exists():
        errors.append("agents/openai.yaml not found")
        return
    try:
        text = read_utf8(path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    for field in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s+{field}:\s+\".+\"\s*$", text, re.MULTILINE):
            errors.append(f"agents/openai.yaml missing quoted interface.{field}")
    if skill_name and f"${skill_name}" not in text:
        errors.append("agents/openai.yaml default_prompt does not reference the current skill name")
    if not re.search(r"^\s+allow_implicit_invocation:\s+false\s*$", text, re.MULTILINE):
        errors.append("agents/openai.yaml should set allow_implicit_invocation: false")


def validate_text_and_links(root: Path, errors: list[str]) -> None:
    text_suffixes = {".md", ".yaml", ".yml", ".py", ".html", ".txt"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        try:
            text = read_utf8(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if path.suffix.lower() != ".md":
            continue
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            destination = (path.parent / unquote(target)).resolve()
            if not destination.exists():
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"broken link: {path.relative_to(root)}:{line} -> {target}")


def validate_legacy_references(root: Path, errors: list[str]) -> None:
    old_invocation = "$" + "maozedong-maoxuan-skill"
    for path in list(root.rglob("*.md")) + list(root.rglob("*.yaml")):
        text = read_utf8(path)
        if old_invocation in text:
            errors.append(f"legacy skill invocation remains in {path.relative_to(root)}")


def validate_html(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"HTML file not found: {path}")
        return
    try:
        text = read_utf8(path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    lowered = text.lower()
    for marker in ("<!doctype html", "<html", "<head", "<body", "</html>"):
        if marker not in lowered:
            errors.append(f"HTML missing {marker}: {path}")
    title = re.search(r"<title>\s*(.*?)\s*</title>", text, re.IGNORECASE | re.DOTALL)
    if not title or not title.group(1).strip():
        errors.append(f"HTML has no non-empty title: {path}")

    placeholders = sorted(set(match.group(0) for match in PLACEHOLDER_RE.finditer(text)))
    if placeholders:
        preview = ", ".join(placeholders[:8])
        errors.append(f"HTML placeholder text remains in {path}: {preview}")
    if "交付前自查" in text or "默认做法：先复制本模板" in text:
        errors.append(f"HTML still contains template instructions: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_directory", nargs="?", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--html", action="append", default=[], help="Validate a generated HTML report")
    args = parser.parse_args()

    root = Path(args.skill_directory).resolve()
    errors: list[str] = []
    skill_name = validate_frontmatter(root, errors)
    validate_openai_yaml(root, skill_name, errors)
    validate_text_and_links(root, errors)
    validate_legacy_references(root, errors)
    for html_path in args.html:
        candidate = Path(html_path)
        if not candidate.is_absolute():
            candidate = (Path.cwd() / candidate).resolve()
        validate_html(candidate, errors)

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
