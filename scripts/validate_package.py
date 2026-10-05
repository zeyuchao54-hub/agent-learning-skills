#!/usr/bin/env python3
"""Validate this package's simple manifests, UTF-8 files, and local links.

This stdlib check deliberately supports the simple one-line YAML frontmatter
used by this package; it is not a general YAML or educational-quality validator.
"""

from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent


def validate(root: Path = ROOT) -> list[str]:
    errors = []
    for required in ("README.md", "README.zh-CN.md", "LICENSE", "NOTICE"):
        if not (root / required).is_file():
            errors.append(f"Missing package file: {required}")
    for name in ("learning-tutor", "study-notes"):
        folder = root / "skills" / name
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            errors.append(f"Missing skill: {name}")
            continue
        text = manifest.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"Bad frontmatter: {name}")
            continue
        fields = {}
        for line in match.group(1).splitlines():
            key, sep, value = line.partition(":")
            if not sep or key in fields:
                errors.append(f"Unsupported/duplicate manifest field: {name}: {line}")
            fields[key] = value.strip()
        if fields.get("name") != name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"Invalid skill name: {name}")
        if not 1 <= len(fields.get("description", "")) <= 1024:
            errors.append(f"Missing/long description: {name}")
        if fields.get("license") != "MIT" or not (folder / "LICENSE").is_file():
            errors.append(f"Missing per-skill license: {name}")
        if re.search(r"XJTLU|[A-Z]{3}\d{3}|_课程总览|[CD]:[\\/]", text):
            errors.append(f"Personal repository dependency in {name}")
        if "[TODO:" in text:
            errors.append(f"Unfinished scaffold in {name}")

    for path in root.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__", "workspaces", "_build"} for part in path.relative_to(root).parts):
            continue
        if path.suffix not in {".md", ".py", ".json", ".yaml", ".yml"} and path.name not in {"LICENSE", "NOTICE", ".gitignore", ".gitattributes"}:
            errors.append(f"Unexpected distributable file: {path.relative_to(root)}")
            continue
        raw = path.read_bytes()
        if not raw or raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"Empty file or UTF-8 BOM: {path.relative_to(root)}")
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"Not UTF-8: {path.relative_to(root)}")
            continue
        if any(line.rstrip() != line for line in content.splitlines()):
            errors.append(f"Trailing whitespace: {path.relative_to(root)}")
        if path.suffix == ".json":
            try:
                json.loads(content)
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON: {path.relative_to(root)}: {exc}")
        if path.suffix == ".md":
            # Exclude code fences before checking real Markdown links.
            prose = re.sub(r"```.*?```", "", content, flags=re.S)
            prose = re.sub(r"`[^`\n]*`", "", prose)
            # These links resolve in the generated workspace, not the package.
            # Initializer tests check them after rendering the assets.
            if path.parent == root / "skills" / "learning-tutor" / "assets":
                continue
            for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", prose):
                target = target.strip().strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("#") or "{{" in target:
                    continue
                dest = (path.parent / unquote(parsed.path)).resolve()
                if not dest.is_relative_to(root.resolve()) or not dest.exists():
                    errors.append(f"Broken/escaping link: {path.relative_to(root)} -> {target}")
    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        raise SystemExit(1)
    print("Package checks passed: manifests, licenses, UTF-8, JSON, local links, and whitespace.")
