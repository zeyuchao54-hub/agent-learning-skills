---
name: study-notes
description: Create, revise, and check source-grounded learning notes, concept pages, reference sheets, mistake records, and course information in Markdown or Obsidian. Use for organize study notes, update my learning vault, ingest course materials, or record a misconception; not for general writing or meeting minutes.
license: MIT
---

# Study Notes

Make knowledge retrievable and traceable while preserving the learner's existing work. This skill works independently of any tutoring skill.

## Establish the destination and conventions

Resolve the requested notes directory and read any local note-format guide. Use the explicit request first, then local conventions, then this skill's defaults. If the destination remains unclear, ask for it; do not silently reorganize the user's vault.

For paired tutoring, the `notes` object in workspace `.learning/config.json` supplies defaults. For standalone use, optionally read `notes.config.json` at the notes root, containing the same `notes` object. Neither file is required. If `notes.enabled` is false, honor it unless the current user explicitly requests a saved note. Read [format and styles](references/format-and-styles.md) before creating a collection or changing its structure.

Choose the language, Markdown or Obsidian link format, and detail level from the request or collection. Bilingual titles, LaTeX, Chinese filenames, fixed line counts, and week-number folders are optional. Read a representative existing page before editing. Do not replace long reference notes with short cards to enforce a new style.

## Use the page that serves the task

| Page | Purpose | Maintenance |
| --- | --- | --- |
| Overview | Navigate outcomes, topics, and knowledge pages | Link to canonical pages rather than duplicating them |
| Concept | Explain one coherent concept or mechanism | Revise affected sections; preserve valid derivations and annotations |
| Reference | Retrieve formulas, decisions, or procedures quickly | Brief rule, applicability warning, and concept link |
| Mistake record | Reconstruct an actual error and its correction | Preserve attempts; append later correction or retest |
| Course information | Track official outcomes, assessments, and dates | Attribute policy facts and record revisions |

Use the relevant templates in `assets/` as starting points, not mandatory section checklists. Fill useful sections and omit irrelevant ones; do not create empty content pages just to complete a directory tree. An overview explaining that no concepts have been recorded yet is a useful index, not evidence that content was studied.

## Write from evidence

Read [sources and revisions](references/sources.md) when ingesting or revising materials. Identify what each claim came from with a page, section, exercise, document revision, or URL. Keep source facts, tutor explanations, supplementary sources, and learner observations distinguishable. Do not invent source locators or assessment details. “Not stated in the supplied source” is preferable to a guessed deadline or rule.

For concepts, give the purpose or problem first when helpful, then the definition and conditions, a worked example or mechanism, concrete pitfalls, and related topics. Use the depth appropriate to the learner and subject. A formula without its assumptions is incomplete. Do not fabricate an observed mistake merely because it is a common pitfall.

Edit the current explanation where it is wrong or obsolete, preserving useful existing content and learner annotations. A whole-page rewrite is appropriate for a requested snapshot refresh, not the default for every edit. Mistake histories keep the original error and add corrections. Reference sheets should link to detailed derivations rather than become duplicate chapters.

## Connect and verify

Use relative Markdown links for plain collections and path-qualified wikilinks for Obsidian collections where names are ambiguous. Preserve existing backlinks on rename. Mark intentional future topics as planned; do not create empty files to make unresolved links appear valid. Do not delete existing empty files automatically—first establish their purpose.

Verify frontmatter, formulas/units, source fidelity, and changed links. Check the note is reachable from the overview or relevant parent page. Report intentional unresolved links and source gaps separately from accidental broken links. Preview in the target renderer when available; if not, state that rendering remains unchecked when it matters.

When notes are updated during tutoring, follow [the synchronization guide](references/teaching-sync.md). Keep progress in its canonical state/plan rather than treating “note exists” as “learner mastered concept.” Conclude with the pages changed, substantive correction, and any unresolved source question.
