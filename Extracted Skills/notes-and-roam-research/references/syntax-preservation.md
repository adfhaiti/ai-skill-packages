# Roam Research: Syntax Preservation Reference

This file is the authoritative catalog of Roam-specific syntax that MUST be preserved
verbatim during note optimization. Read this file before performing any Mode 1 (Note
Optimization) task.

---

## 1. Page References and Tags

Page references and tags are the foundation of Roam's bidirectional linking system. They
create nodes in the knowledge graph. NEVER add new ones; NEVER remove existing ones.

| Syntax | Example | Notes |
|--------|---------|-------|
| `[[Page Name]]` | `[[Roam Research]]` | Inline page reference; creates page if it doesn't exist |
| `#Tag` | `#idea` | Single-word tag; functionally identical to `[[idea]]` |
| `#[[Multi Word Tag]]` | `#[[Meeting Notes]]` | Multi-word tag; functionally identical to `[[Meeting Notes]]` |
| Namespaced pages | `[[Projects/ADF]]` | Pages with `/` separators for hierarchical organization |

**Key rule**: `[[Page Link]]` and `#Hashtag` serve the same structural purpose (both create pages). The difference is stylistic. Preserve whichever form the user chose.

---

## 2. Block References and Embeds

Block references create live links to specific blocks elsewhere in the graph. Block embeds
render the referenced block's content inline. Both update dynamically if the source changes.

| Syntax | Example | Notes |
|--------|---------|-------|
| Block reference | `((block-uid))` | Live link to a specific block; the UID is an alphanumeric string like `((PWRiHAsEv))` |
| Block embed | `{{[[embed]]: ((block-uid)) }}` | Renders the referenced block's full content inline |
| `{{embed:((uid))}}` | `{{embed:((PWRiHAsEv)) }}` | Alternate embed syntax (older format); preserve as-is |

**Preservation rule**: Block UIDs are opaque identifiers. Never modify, "fix," or question them. Even if they look like random strings, they are valid references.

---

## 3. Attributes (Double-Colon Syntax)

Attributes are Roam's key-value metadata system. They are used extensively in templates, CRM pages, book notes, and structured data.

| Syntax | Example | Notes |
|--------|---------|-------|
| `AttributeName:: value` | `Author:: [[Conor White-Sullivan]]` | The `::` is the critical delimiter |
| | `Tags:: #topic #research` | Values can contain page refs and tags |
| | `Status:: In Progress` | Values can be plain text |
| | `Date:: [[January 15th, 2026]]` | Values can be date references |

**Preservation rule**: The double-colon `::` is syntactically significant. Do not normalize to single colon or other formats. Preserve the attribute name, the `::`, and the value exactly.

---

## 4. TODO/DONE Markers

| Syntax | Example | Notes |
|--------|---------|-------|
| `{{[[TODO]]}}` | `{{[[TODO]]}} Write proposal` | Renders as an unchecked checkbox |
| `{{[[DONE]]}}` | `{{[[DONE]]}} Submit report` | Renders as a checked checkbox |

**Preservation rule**: These are component syntax, not plain text. The double-bracket-inside-double-curly-brace format is required. Do not simplify to `[ ]` or `[x]`.

---

## 5. Emphasis and Highlights

| Syntax | Example | Renders As |
|--------|---------|------------|
| `**bold**` | `**important**` | **important** |
| `__italics__` | `__emphasis__` | _emphasis_ |
| `^^highlight^^` | `^^key point^^` | Highlighted text (yellow background in Roam) |
| `**^^combined^^**` | `**^^critical^^**` | Bold + highlighted |
| `~~strikethrough~~` | `~~old idea~~` | ~~old idea~~ |

**Strikethrough preservation rule**: Strikethroughs are intentional records of the user's thinking process (revisions, rejected ideas, corrections). NEVER remove them or "clean them up." They carry meaning.

---

## 6. Queries

Roam has two query systems. Both MUST be preserved verbatim.

### 6.1 Legacy Query Syntax

```
{{[[query]]: {and: [[Page A]] [[Page B]] {not: [[Page C]]}}}}
```

Operators: `{and: ...}`, `{or: ...}`, `{not: ...}`, `{between: [[date1]] [[date2]]}`

### 6.2 New Datalog Query Syntax (`:q` blocks)

Introduced in March 2026. These are full Datalog queries using Roam-specific symbols and rules.

```
:q "Query title"
[:find ?b
 :where
 (refs-dnp-between dnp/this-week-start dnp/this-week-end ?b)
 (not (in-dnp-between dnp/this-week-start dnp/this-week-end ?b))
 [?b :create/time ?t]]
```

**Key elements to preserve**:
- The `:q` prefix and quoted title string
- Datalog `[:find ... :where ...]` structure
- Roam-specific symbols: `ms/*` (millisecond timestamps like `ms/today-start`, `ms/next-week-end`), `dnp/*` (Daily Note Page references like `dnp/this-week-start`)
- Roam-specific rules: `(refs-dnp-between ...)`, `(in-dnp-between ...)`, `(created-by ...)`, `(in-or-refs-dnp-between ...)`
- All Datalog clauses, bindings, and aggregation functions

**Preservation rule**: Treat `:q` blocks like code blocks. Do not reorganize their internal structure, rename variables, or "improve" the query syntax.

---

## 7. Component Syntax (`{{...}}`)

These are interactive components rendered by Roam's engine.

| Syntax | Purpose |
|--------|---------|
| `{{[[table]]}}` | Creates a table; rows and columns are indented children |
| `{{[[kanban]]}}` | Creates a Kanban board; columns are indented children |
| `{{[[diagram]]}}` | Creates a diagram canvas |
| `{{[[slider]]}}` | Creates an interactive slider |
| `{{[[calculator]]}}` | Creates a calculator block |
| `{{[[encrypt]]}}` | Creates an encrypted/password-protected block |
| `{{[[POMO]]: N}}` | Creates a Pomodoro timer for N minutes |
| `{{[[video]]: URL}}` | Embeds a video player (YouTube, Loom, etc.) |
| `{{date}}` | Date picker component |

**Preservation rule**: Component syntax is the double-curly-brace wrapper `{{ }}` containing a double-bracket keyword `[[ ]]` and optional parameters. Preserve the entire expression including whitespace patterns.

---

## 8. Callouts and Blockquotes

Added/improved in February 2026.

| Syntax | Example |
|--------|---------|
| Blockquote | `> quoted text` |
| Callout (tip) | `> [!TIP] helpful information` |
| Callout (warning) | `> [!warning] be careful` |
| Callout (note) | `> [!NOTE] additional context` |

**Preservation rule**: The `> [!TYPE]` prefix is syntactically significant. Do not strip the `>` prefix or the `[!TYPE]` marker. Multi-line blockquotes (consecutive `>` lines) should remain grouped.

---

## 9. Date References

| Syntax | Example | Notes |
|--------|---------|-------|
| Date page ref | `[[January 15th, 2026]]` | Links to a Daily Note page |
| Date picker | `{{date}}` | Interactive date selection component |
| `/current time` | Inserts `HH:MM` timestamp | Slash command |

**Preservation rule**: Date references use Roam's specific date format (`[[Month Dayth, Year]]`). Do not normalize to ISO 8601 or other date formats.

---

## 10. Slash Commands

Slash commands are typed as `/command` in a block to insert components or formatting.

Common slash commands (preserve if found in source text):
- `/current time` (timestamp)
- `/Pomo` (Pomodoro timer)
- `/table` (table component)
- `/kanban` (Kanban board)
- `/diagram` (diagram canvas)
- `/TODO` (TODO checkbox)
- `/inline` (inline calculation reference)

---

## 11. Code Blocks

````
```language-identifier
code content here
```
````

**Preservation rule**: NEVER modify anything inside code blocks. This includes:
- The language identifier (e.g., `javascript`, `clojure`, `plain text`)
- All whitespace, indentation, and line breaks
- All content, even if it appears to contain errors
- Roam-specific code like `roam/js`, `roam/css`, or `roam/render` blocks

---

## 12. Images

Images MUST be preserved with exact URLs on their own bullets.

**Source formats to normalize**:
- HTML `<img src="URL">` → `![image](URL)`
- Reference-style `![alt][ref]` → `![image](URL)` (resolve reference)
- Already `![alt](URL)` → preserve as-is

**Common Roam image hosts** (all URLs from these hosts are valid; do not modify):
- `firebasestorage.googleapis.com` (Roam's primary image storage)
- `s3.amazonaws.com/cdn.freshdesk.com` (help documentation)
- `camo.githubusercontent.com` (GitHub proxy)
- `raw.githubusercontent.com` (GitHub raw)
- Any CDN, cloud storage, or image hosting URL

**Placement rule**: Each image gets its own bullet. Place images adjacent to the text they illustrate.

---

## 13. Extension-Specific Syntax

Roam Depot extensions may introduce custom syntax. Preserve all of the following verbatim.

### Better Bullets Markers
Prefix markers at the start of blocks (e.g., `-> `, `=> `, `?? `, `... `, `= `, `! `, `+ `, `~ `, `^ `, `@ `, `<- `). These trigger custom bullet glyphs. The space after the marker is significant when "Require a space after marker" is enabled.

### Roam Toolkit Vim Mode
Settings references, keybinding notation. Preserve as-is.

### roam/js, roam/css, roam/render
These are special pages/blocks containing executable code. Treat their contents as code blocks (never modify).

### Template Markers
`;;` followed by a template name inserts a template. Preserve the `;;` prefix.

### SRS (Spaced Repetition) Markers
`AGAIN`, `HARD`, `GOOD`, `EASY` scheduling markers. Preserve as-is.

---

## 14. CSS Classes and Grid Syntax

| Syntax | Example | Purpose |
|--------|---------|---------|
| `#.rm-grid` | `# **Components** #.rm-grid` | Applies CSS grid layout to children |
| `#.rm-g` | Block-level CSS class | Group display styling |

**Preservation rule**: These are Roam CSS class annotations. They look like tags but serve a layout function. Preserve them exactly, including their position relative to other content on the same line.

---

## 15. Personal Notation Conventions

Users develop their own shorthand. Common patterns to watch for and preserve:
- `[*]` markers (personal annotation)
- `??` or `?` prefixes (open questions)
- Custom emoji prefixes
- Inline marginal notes
- Any consistent notation pattern visible in the source

**Rule**: If it looks intentional and you're unsure what it is, preserve it.

---

## 16. Multilingual Content

Roam users often write in multiple languages within the same graph or even the same page.

**Rules**:
- Preserve all text in its original language (English, Haitian Creole, French, Spanish, or any other)
- NEVER translate between languages
- NEVER "correct" spelling in non-English languages (what looks like a typo may be correct Kreyo`l or regional spelling)
- NEVER consolidate content across languages (e.g., do not merge an English summary with its Kreyo`l original)

---

## 17. Soft Line Breaks

Within a single Roam block, `Ctrl+Shift+V` pastes content with soft line breaks (multiple
lines rendered inside one block, not as separate blocks). These appear as newlines within
a single bullet.

**Preservation rule**: If the source shows multi-line content that belongs to a single block, keep it as a single block with the line breaks intact. Do not split into separate bullets unless the content clearly represents distinct ideas that should be separate blocks.
