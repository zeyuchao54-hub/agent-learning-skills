# Local validation report

Date: 2026-10-05. Environment: Windows, Python 3.14.3.

- Initializer: 13 tests discovered, 12 passed, 1 skipped because creating directory symlinks requires an unavailable Windows privilege.
- A tutor skill copied to an isolated installation initialized a workspace successfully without the repository or notes skill.
- Dry-run, explicit directory selection, existing content preservation, no-notes mode, Unicode/quoted labels, and conflict refusal were exercised in temporary directories.
- Package checks passed: manifests, JSON, UTF-8, licenses, links, and whitespace. Template links are checked after rendering by initializer tests, rather than resolved against the skill source directory.

The creator's external quick validator could not run in either the system or bundled Python because PyYAML was absent. The package's stdlib validator passed; the external validator was not reported as passed, and no dependencies were installed for it.

No independent agent learning trial, actual student outcome evaluation, Obsidian rendering session, or remote CI run has been performed. The behavior scenarios in `validation.md` are a future evaluation plan, not passed tests.
