#!/usr/bin/env python3
"""Initialize one explicit learner/topic workspace using only the stdlib.

An existing .learning directory is never changed or repaired automatically.
All templates live in this skill; no sibling skill or repository is needed.
"""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys


def render(text: str, values: dict[str, str]) -> str:
    return re.sub(r"\{\{([a-z_]+)\}\}", lambda match: values.get(match[1], match[0]), text)


def initialize(
    workspace: Path,
    topic: str,
    language: str = "auto",
    assessment_language: str | None = None,
    notes_format: str = "markdown",
    style: str = "cards",
    today: str | None = None,
    dry_run: bool = False,
) -> list[Path]:
    """Return created paths, or [] when already initialized; refuse conflicts."""
    if not topic.strip() or any(ord(char) < 32 for char in topic):
        raise ValueError("Topic must be nonempty and contain no control characters.")
    if notes_format not in {"markdown", "obsidian", "none"}:
        raise ValueError("Unsupported notes format.")
    if style not in {"cards", "reference", "layered"}:
        raise ValueError("Unsupported note style.")
    today = today or date.today().isoformat()
    date.fromisoformat(today)
    workspace = workspace.expanduser().resolve()
    if workspace.exists() and not workspace.is_dir():
        raise ValueError("Workspace must be a directory.")
    state_dir = workspace / ".learning"
    if state_dir.exists() or state_dir.is_symlink():
        if state_dir.is_symlink() or not state_dir.is_dir():
            raise ValueError("Existing .learning is not a regular directory.")
        print("Already initialized: no files or settings changed. Inspect existing state to resume.")
        return []

    config = {
        "schema_version": 1,
        "topic": topic.strip(),
        "language": language,
        "assessment_language": assessment_language,
        "path": "auto",
        "evidence": "auto",
        "practice_sources": [],
        "pass_threshold": 0.8,
        "max_retries_before_replan": 3,
        "review_intervals_days": [1, 3, 7, 21],
        "notes": {
            "enabled": notes_format != "none",
            "directory": "notes",
            "format": "markdown" if notes_format == "none" else notes_format,
            "style": style,
            "languages": [],
            "source_policy": "attributed",
        },
    }
    assets = Path(__file__).resolve().parent.parent / "assets"
    values = {
        "topic": topic.strip(),
        "topic_yaml": json.dumps(topic.strip(), ensure_ascii=False),
        "date": today,
        "notes_pointer": "../notes/Overview.md" if notes_format != "none" else "disabled",
    }
    planned = {
        state_dir / "config.json": json.dumps(config, ensure_ascii=False, indent=2) + "\n",
    }
    for name in ("STATE.md", "memory.md", "plan.md", "attempts.md"):
        planned[state_dir / name] = render((assets / name).read_text(encoding="utf-8"), values)
    if notes_format != "none":
        planned[workspace / "notes" / "Overview.md"] = render(
            (assets / "Overview.md").read_text(encoding="utf-8"), values
        )

    # Preflight everything before creating directories or files.
    for target in planned:
        resolved = target.resolve()
        if not resolved.is_relative_to(workspace):
            raise ValueError(f"Output would escape the workspace: {target}")
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Refusing to overwrite: {target}")
        for parent in target.parents:
            if parent == workspace:
                break
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"Output parent is not a directory: {parent}")
    if dry_run:
        for target in planned:
            print(f"Would create: {target}")
        return list(planned)

    for target, content in planned.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print(f"Created: {target}")
    return list(planned)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True, help="Explicit topic directory")
    parser.add_argument("--topic", required=True, help="Display label, not a directory name")
    parser.add_argument("--language", default="auto", help="Preferred teaching language")
    parser.add_argument("--assessment-language", default=None)
    parser.add_argument("--notes-format", choices=["markdown", "obsidian", "none"], default="markdown")
    parser.add_argument("--style", choices=["cards", "reference", "layered"], default="cards")
    parser.add_argument("--date", dest="today", help="ISO local date; defaults to the OS local date")
    parser.add_argument("--dry-run", action="store_true", help="Print proposed files without writing")
    args = parser.parse_args()
    try:
        initialize(**vars(args))
    except (OSError, ValueError) as exc:
        print(f"Initialization failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
