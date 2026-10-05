# Format and collection styles

Prefer existing conventions. For a new collection, select a style that serves the task:

- **Concept cards:** focused pages connected through a small overview; split when multiple distinct ideas compete, not at a universal line limit.
- **Reference:** longer explanations and worked examples; update the relevant section without compressing the entire page.
- **Layered:** overview, detailed lessons, quick references, and mistakes. Do not duplicate the same derivation across layers.

Folder names can follow topic, chapter, week, project, or another established sequence. Filenames can use any learner-preferred language. Avoid characters unsupported by the target filesystem. A collection opened as an Obsidian vault benefits from a distinctive folder name, but `notes/` is valid and should not be renamed without a reason.

## Minimal metadata

For new pages, use `title`, `type`, `topic`, `sources`, and optional `tags`. Examples are in `assets/`. Sources may be plain strings with precise locators; complex schemas are unnecessary unless the collection already has one. Quote YAML strings containing punctuation, escape quotes, and keep tags as text without leading `#`. Use ISO dates only when the relevant creation/revision date is known. The examples in `assets/` are templates: substitute their `{{title}}` and `{{topic}}` placeholders with the real values as you adapt them.

Optional fields include aliases and translations. Do not require an English translation for a single-language learner. `status` should distinguish source coverage from demonstrated ability. If a learning plan owns progress, link to that plan instead of copying mutable scores into frontmatter.

Use one H1 title. Organize H2 headings around the content, omitting sections that would be empty. For bilingual mode use the configured languages; a separator such as ` · ` is convenient, not compulsory. Do not translate code identifiers or alter official wording whose exact form matters.

## Links and math

For plain Markdown use `[label](relative-path.md)` with percent-encoded spaces or angle-bracket destinations when needed. Resolve links from the page's directory. For Obsidian use `[[path/to/Page|label]]` for ambiguous basenames and normal external URL links. Link new concept pages from an overview and make prerequisites identifiable.

Use math syntax supported by the target renderer. LaTeX with `$...$` and `$$...$$` is suitable for Obsidian; other Markdown renderers vary. In a terminal or inaccessible math renderer, use readable plain text. Match chat notation to the host's rendering capability rather than banning LaTeX everywhere.

## Final checks

Check YAML syntax if frontmatter is used, balanced code/math fences, valid definitions and assumptions, accurate citations, and relevant internal links. Newly created content pages must contain substantive material. Reference sheets need applicability constraints and links to fuller explanations. A template intentionally stored under `assets/` is not a learner note; do not copy its blank fields as a finished page. No `{{...}}` placeholder may survive into a saved note: substitute every one, including those inside quoted frontmatter.
