# Local state and handoff

All paths below are relative to one learner/topic workspace. The package has no global student database or automatic cross-topic profile. Do not combine different learners' evidence or preferences.

| File | Authority | Maintenance |
| --- | --- | --- |
| `.learning/config.json` | Explicit preferences and workflow settings | Change when the learner changes a setting |
| `.learning/STATE.md` | Current stage pointer, next action, pending tasks, current resources, review dates | Update at meaningful boundaries; aim for at most 120 lines |
| `.learning/plan.md` | Stage outcomes, prerequisites, criteria, and stage statuses | Update on advancement or replanning |
| `.learning/memory.md` | Confirmed preferences and evidence-backed teaching observations | Revise rather than endlessly append; aim for at most 90 lines |
| `.learning/attempts.md` | Actual attempts, grading evidence, and later corrections | Append only |
| Configured notes directory | Reusable knowledge, sources, examples, and misconception explanations | Follow the existing note style |

Budgets are defaults for keeping startup cheap, not reasons to delete unresolved issues. When a snapshot becomes large, move resolved historical context into an archive with a pointer, or link detailed records already stored in attempts. Never truncate answer logs to meet a snapshot budget. Preserve user-authored preferences and unresolved work while editing snapshots.

## Resume

Read config, state, memory, the current stage entry in plan, and the few resources the state points to. State files are indexes, not a reason to scan the entire vault. Summarize the checkpoint and proceed with the requested action. If the last question was unanswered, resume that question rather than inventing an answer. If substantial time has elapsed, offer a short retrieval check.

Existing notes without state do not mean a beginner. Inspect the overview and relevant pages, then diagnose only the capability needed now. When recorded status and evidence conflict, flag the conflict and use the actual dated evidence to reconcile it; do not silently certify mastery.

## Updating

Capture concept and mistake notes soon after the event, then keep state and plan pointers consistent. Mark completion only when the evidence in attempts supports the announced criteria. A progress dashboard may point to the plan, but should not maintain an independent editable copy of scores or stage statuses.

Write review dates in ISO format using the learner's date/timezone, record what is due, and update on actual review. Defaults of 1, 3, 7, and 21 days are adjustable intervals measured from the most recent successful check. These are local to-do dates, not scheduled notifications.

Record observed patterns with the evidence and uncertainty: “requested worked examples twice” is preferable to “is a visual learner.” Persistent memory should avoid unrelated personal facts. If asked to stop storing progress or remove it, respect that scope using the host's normal file permissions and data-preservation rules; append-only means ordinary learning updates do not rewrite history, not that the learner cannot delete their data.

## With no filesystem

Use the same separation in a short copyable handoff: topic/goal, current stage and demonstrated scope, next action, unanswered question, weak points, source locators, preferences, and due reviews. Never claim automatic cross-chat memory or file persistence when the host does not provide it.
