# Customization

The learner's current request wins over saved settings. Settings are agent-readable preferences, not enforcement by an application server. The initializer writes schema version 1; it is not a general-purpose validator or migrator for subsequently edited config.

## Tutor settings

Edit `.learning/config.json` within one learner/topic workspace.

| Field | Default | Meaning |
| --- | --- | --- |
| `schema_version` | `1` | Document format version |
| `topic` | Required display label | Not a path or an institutional course code requirement |
| `language` | `auto` | Infer from the learner; otherwise a language name or tag |
| `assessment_language` | `null` | Use teaching language unless explicitly set |
| `path` | `auto` | `curriculum`, `assignment`, `lab`, `project`, `exam`, or `self-study` |
| `evidence` | `auto` | A string or list of `recognition`, `explanation`, `derivation`, `artifact` |
| `practice_sources` | `[]` | Register supplied paths/locators or approved external sources |
| `pass_threshold` | `0.8` | Fraction in [0, 1] for scored checks; not a substitute for required evidence |
| `max_retries_before_replan` | `3` | Suggest changing the approach rather than endlessly retesting |
| `review_intervals_days` | `[1, 3, 7, 21]` | Positive day intervals from the last successful check; `[]` disables automatic proposals |
| `notes` | See below | Optional note output settings |

An agent should flag invalid values or an unfamiliar `schema_version`, and ask only when that setting affects the task. Do not silently discard custom settings. Put stage-specific rubrics and outcomes in `plan.md`; keep this config small.

## Notes settings

| Field inside `notes` | Default | Meaning |
| --- | --- | --- |
| `enabled` | `true` | Whether tutoring automatically maintains local notes |
| `directory` | `notes` | Relative to the learning workspace, or an explicitly selected absolute collection path |
| `format` | `markdown` | `markdown` for relative links, `obsidian` for wikilinks |
| `style` | `cards` | `cards`, `reference`, or `layered`; preserve existing structure |
| `languages` | `[]` | Follow the learner; specify one or more languages for explicit heading/terminology preference |
| `source_policy` | `attributed` | Distinguish sources and supplements; `source-only` restricts to supplied material |

For standalone `study-notes`, optionally put `notes.config.json` in the notes root, with `{"notes": {...}}`. Here `directory` is relative to that root and can be `.`. Local format guides and explicit user choices remain authoritative. The skill also works without a config file.

See [a bilingual tutor configuration](../examples/bilingual-config.json) and [standalone notes settings](../examples/notes.config.json). These use fictional topics, not actual learner data.

## Adaptation examples

- **Programming:** project or lab path; artifact plus explanation; record the actual language/runtime standard in each stage. Test the learner's code when execution is available.
- **Mathematics:** curriculum or self-study path; explanation and derivation; accept shorthand or a photographed solution if the host can read it. Recognition is useful practice but not proof of derivation.
- **Humanities:** explanation, interpretation, or essay rubric; capture quotations and arguments with locators. Do not force numerical grading when a rubric is more informative.
- **Language learning:** add performance evidence appropriate to reading, speaking, or listening. If the host cannot assess audio, keep pronunciation unverified rather than passing it from a text response.
- **Exam review:** question-family path, actual assessment language if desired, gap remediation, and transfer practice. Use available papers without inferring unpublished exam details.
- **Chat-only:** no scripts or required files; provide a copyable handoff. Persistence exists only when the host or learner actually stores it.

Institution-specific policies can live in the learner's local course-information note or format guide. They should not become universal instructions in the distributed skill.
