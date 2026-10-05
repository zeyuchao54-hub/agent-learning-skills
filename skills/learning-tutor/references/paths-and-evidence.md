# Paths and evidence

The learning sequence (`path`), assessment method (`evidence`), and practice source (`practice_sources`) solve different problems. Set them independently in `.learning/config.json`; `auto` means infer from the goal and record the decision in `plan.md`, not default to a lecture-plus-quiz workflow.

| Path | Stage unit | Planning constraint |
| --- | --- | --- |
| Curriculum | Coherent lesson or concept group | Preserve required prerequisites and published sequence |
| Assignment | Transferable skill needed for a deliverable | Work backward from its actual deadline; question numbers are examples, not skills |
| Lab | Experiment or exercise group | Preserve dependencies, environment, measurement, and output requirements |
| Project | Working capability or milestone | Specify acceptance evidence; teach prerequisites as they become relevant |
| Exam | Question family and underlying skills | Diagnose gaps, then repair them; past papers are not the entire syllabus |
| Self-study | Learner-chosen capability | Build prerequisites around the goal; do not invent an institutional syllabus |

For each stage, record the outcome, prerequisites, source locators, practice task, evidence criteria, and current status. Replanning should preserve demonstrated capabilities and their evidence; split or merge stages without resetting the learner's work. Keep `STATE.md` pointing to the current stage, with stage statuses maintained only in `plan.md`.

## Matching evidence to outcomes

| Outcome | Suitable evidence | Insufficient evidence by itself |
| --- | --- | --- |
| Recognize terminology | Well-constructed selection or matching | Exposure to a glossary |
| Explain a mechanism | Explain-back plus a new situation | Repeating the tutor's wording |
| Calculate or derive | Independent work with method and boundary checks | Selecting the final number |
| Program or simulate | Build/run under the required standard and representative tests | Code that looks plausible |
| Write or analyze | Artifact evaluated against an explicit rubric | A factual vocabulary quiz |
| Speak or perform | Actual performance or an agreed observable substitute | Text-only evidence when pronunciation or physical skill is the goal |

For artifacts, verify the criteria actually stated by the task. Exact output matching is appropriate only when exact formatting is required; use numeric tolerances, semantic checks, or a qualitative rubric when those match the specification. Report compilation, execution, and rubric review as distinct checks. An unavailable tool leaves a check pending.

## Sources and revisions

Choose authority by claim: an assessment policy governs deadlines, a corrected assignment governs its output, and a technical source governs a definition. Record source edition/revision and page, section, exercise, or URL. For stable fundamentals, tutor-created explanation is allowed but should not masquerade as a quotation from a document.

When a source changes, compare relevant old and new passages if the old version is available. Correct affected notes and plan entries, preserve still-valid reasoning and examples, and flag unresolved conflicts. With no old version, disclose that a historical comparison was impossible. A file hash can detect byte changes but cannot explain them; use it only when revision tracking is useful. Ingesting new materials does not establish that the learner has studied them.
