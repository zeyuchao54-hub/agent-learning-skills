# Validation and its limits

Run from this distribution's root with Python 3.10+:

```shell
python scripts/validate_package.py
python -m unittest discover -s tests -v
```

The package validator checks this package's simple skill frontmatter, folder/name agreement, licenses, UTF-8 without BOM, JSON syntax, internal Markdown file links, unfinished entry-point scaffolds, and trailing whitespace. It is deliberately not a general YAML parser, semantic source checker, Obsidian renderer, or proof of good teaching.

The initializer tests check explicit output targeting, honest initial state, existing-content preservation, disabled notes, language/format settings, dry-run behavior, Unicode labels, invalid inputs, parent-file conflicts, and use with the tutor skill copied out of this repository. A symlink-escape check runs when the OS grants directory-symlink creation; otherwise it is reported as skipped.

CI is configured to run these checks on Linux, Windows, and macOS with Python 3.10 and 3.14. A configured workflow is not evidence of a successful remote run. Initial local verification is recorded in [the local validation report](validation-report.md).

## Behavioral evaluation prompts

These are scenarios for future real agent sessions, not claims that an independent agent or learner trial has been run. Use fictional materials in temporary workspaces. Inspect actual responses and files; do not grade only by matching wording.

| Scenario | Request and supplied context | Observable behavior to evaluate |
| --- | --- | --- |
| New self-study | “Teach me probability for data analysis in Spanish. I have no syllabus.” | Uses the chosen language, sets capability goals, and diagnoses relevant prerequisites without inventing school requirements |
| Existing long notes | “Correct the example in this 200-line reference page; preserve my derivation.” | Changes the affected portion while retaining valid explanation and annotations |
| Practical programming | “Prepare me for this coding lab; the task specifies a compiler standard.” | Uses the task's actual standard and execution evidence; a quiz cannot substitute for the artifact |
| Two active topics | “Continue learning.” Both workspaces have unfinished stages and no clear conversational topic | Shows short choices rather than silently picking a topic or reading entire vaults |
| Source revision | Supplied old/new policy changes the published assessment date | Updates source-grounded information and pending work, without inventing a passed learning stage |
| Input accessibility | “I cannot type equations. Let me answer with shorthand.” | Accepts workable input, chooses evidence that still tests the goal, and avoids mandatory LaTeX |
| User bypass | “Skip the quiz; I just need the full explanation today.” | Provides the requested explanation and keeps ability unverified |
| Missing execution | Artifact check requires unavailable runtime | Reports the unexecuted criterion and avoids claiming the artifact passed |
| Faulty answer key | Issued options and stored answer index conflict | Re-solves the issued question, corrects grading with an audit entry, and preserves original attempt |
| Standalone notes | Only study-notes installed; request source-only Markdown notes | Writes notes without asking for a tutor installation or creating unrelated learner state |

Host discovery, file permissions, rendering, assessment quality, and sustained learning outcomes remain areas for broader evaluation. New evidence should drive changes; avoid adding universal constraints for every unusual example.
