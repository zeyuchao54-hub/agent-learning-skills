# Learning Skills

[中文说明](README.zh-CN.md)

Two portable agent skills for learning with evidence and keeping useful notes:

- **learning-tutor** diagnoses the starting point, plans around a goal, teaches in small steps, checks independent performance, repairs gaps, and preserves a resumable checkpoint.
- **study-notes** creates and maintains source-grounded concept pages, reference sheets, mistake records, and course information in Markdown or Obsidian.

Use either skill alone or both together. There is no required university, course code, language pair, note app, MCP server, paid service, or multi-agent setup. Core instructions need a host that can load skill Markdown; local persistence needs file access. The optional initializer and validation tools need Python 3.10+ and only its standard library.

This is a 0.1 release candidate. File initialization and package structure have automated checks; learning effectiveness and all host integrations have not been established by those checks.

## Install

Copy the complete skill folders, including their references, assets, and licenses, into your host's skill directory. Do not overwrite an existing installation without inspecting it.

| Host | Project-local destination | Personal destination |
| --- | --- | --- |
| Codex | `.agents/skills/learning-tutor/` and `.agents/skills/study-notes/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/learning-tutor/` and `.claude/skills/study-notes/` | `~/.claude/skills/` |
| Other Agent Skills hosts | Host-defined skill directory | Consult the host documentation |

Paths and loading behavior are documented in [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills) and [Claude Code's skill guide](https://code.claude.com/docs/en/skills). The package follows the [Agent Skills directory format](https://agentskills.io/specification). Optional `agents/openai.yaml` files provide Codex UI labels; other hosts can ignore them. No universal cross-host execution guarantee is implied.

In Codex, mention `$learning-tutor` or `$study-notes`. In Claude Code, use `/learning-tutor` or `/study-notes`. Other hosts may require a different invocation syntax. If discovery is unavailable, provide the relevant `SKILL.md` and let the agent read its linked references.

## Try it

```text
Use learning-tutor to teach me probability for data analysis.
I have 30 minutes per session. Teach in Spanish; check explanations and calculations.
Save my progress only in the workspace I specify.

Use study-notes to organize these chapters in my existing Markdown collection.
Preserve my long reference pages and use relative Markdown links.
```

To initialize local files, run from this package directory:

```shell
python skills/learning-tutor/scripts/init_workspace.py --workspace ./workspaces/python-basics --topic "Python basics" --notes-format markdown
```

For bilingual study with Obsidian:

```shell
python skills/learning-tutor/scripts/init_workspace.py --workspace ./workspaces/circuits --topic "Circuit analysis" --language zh-CN --assessment-language en --notes-format obsidian
```

For chat plus progress files without note output, use `--notes-format none`. Add `--dry-run` to preview files or `--date YYYY-MM-DD` to use a specific local date. `--style cards`, `reference`, or `layered` sets a writing preference; it does not create empty concept folders or restructure existing notes. Generated administration pages are in English; the tutor can translate their prose to the chosen language while preserving filenames and pointers.

The initializer targets only the explicitly supplied workspace. If `.learning/` already exists, it makes no changes; resume or edit settings there instead. A conflicting notes overview causes it to stop before writing. To use a preexisting vault, initialize with notes disabled, then set `notes.enabled` and `notes.directory` deliberately. No installer or automatic migration runs in the background.

```text
workspaces/python-basics/
  .learning/
    config.json    explicit settings
    STATE.md       current pointer and next action
    plan.md        stage outcomes, criteria, and statuses
    memory.md      confirmed preferences and observations
    attempts.md    append-only evidence and corrections
  notes/
    Overview.md    entry point; actual concepts are added while studying
```

The initializer creates honest “not yet assessed” administration pages, not a course curriculum or claims of mastery. It can be copied with the tutor skill alone; it does not depend on the notes skill or this repository's layout.

## Configure and contribute

Read [customization](docs/customization.md) for settings and examples, [migration](docs/migration.zh-CN.md) for adapting a personal setup, and [the assessment](docs/open-source-assessment.zh-CN.md) for the project's intended value and related work. [Validation](docs/validation.md) explains tested behavior and realistic prompts for future evaluations.

```shell
python scripts/validate_package.py
python -m unittest discover -s tests -v
```

Contributions should improve an observable learning or note-maintenance failure. Keep host-specific integration optional, include a minimal reproduction for a fix, and use fictional examples rather than learner histories. The GitHub Actions workflow runs the same checks on Linux, Windows, and macOS when this directory is published as its own repository.

## License and data

MIT; see [LICENSE](LICENSE) and [NOTICE](NOTICE). The license covers the skill instructions and helper code, not a learner's source materials. Store learner workspaces separately from the published skill repository. Review dates in a file do not send reminders, and these skills do not automatically publish notes, submit coursework, or contact anyone.
