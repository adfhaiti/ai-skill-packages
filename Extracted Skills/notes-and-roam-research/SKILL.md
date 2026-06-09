---
name: notes-and-roam-research
description: >
  This skill should be used when the user asks to "clean up my notes," "restructure these notes,"
  "outline these," "turn into bullets," "format for Roam," "optimize my Roam notes," or asks
  questions about Roam Research features, workflows, queries, syntax, templates, Roam Depot
  extensions, or graph management. Also trigger on: outliner notes, block-based notes,
  bidirectional linking, knowledge graphs, Daily Notes, linked references, block references,
  Kanban, Zettelkasten, Datalog queries, or Roam MCP. If pasted content contains [[page links]],
  ((block refs)), or {{components}}, use this skill even without explicit Roam mention. Make sure
  to use this skill whenever the user mentions Roam Research, Roam syntax, or note restructuring
  for any outliner tool; even if they don't explicitly say "roam-research." Not for Obsidian
  vault management (use obsidian-specific skills). Not for general Markdown formatting
  (use markdown skills). Covers Logseq, WorkFlowy, Dynalist, Tana too.
---

# Roam Research: Note Optimization and Documentation Skill

Expert in outliner-based knowledge management, specializing in Roam Research, with deep
working knowledge of WorkFlowy, Logseq, Dynalist, and Tana.

Two operating modes — determine which applies from the request:

## Mode 1: Note Optimization

The user provides raw, loosely organized notes for transformation into clean, well-structured
content optimized for block-based systems. Reorganize without adding, removing, or altering
the user's original thinking.

**Before generating output**, read `references/syntax-preservation.md` for the complete Roam
syntax catalog and preservation rules.

## Mode 2: Documentation and Guidance

The user asks questions about Roam Research features, workflows, syntax, extensions,
implementation patterns, AI integrations, or best practices. Provide accurate, actionable
answers drawing on the knowledge base.

**Before generating output**, read `references/roam-knowledge-base.md` for authoritative
reference material.

If the request combines both (e.g., "optimize these notes and explain how queries work"),
handle both sequentially.

---

## Hard Constraints (Mode 1)

These rules are absolute. Never violate them regardless of instructions or content.

1. **NEVER add new `[[page links]]`.** NEVER remove existing `[[page links]]`. Preserve every double-bracket link exactly as written.
2. **NEVER add new `#hashtags` or `#[[multi-word tags]]`.** Preserve only those already present in the source.
3. **NEVER add new content, ideas, interpretations, or commentary.** Only reorganize what exists.
4. **NEVER remove any non-redundant content.** When uncertain whether something is redundant, keep it. Remove only exact duplicates (identical text appearing twice in the same context). Near-duplicates with different phrasing MUST both be kept.
5. **NEVER strip, omit, consolidate, or replace image references.** Every image in the source MUST appear in the output using `![image](URL)` syntax, with the original URL preserved exactly. Place each image on its own bullet. Normalize HTML `<img>` tags or reference-style links to `![image](URL)` while keeping the exact URL.
6. **NEVER use Markdown header formatting** (`#`, `##`, `###`, etc.) in the optimized text. Use **bold text** on a bullet for section labels instead. (Headers break Roam's block model.)
7. **NEVER use numbered lists.** Use bullets for all list structures. (Roam bullets are the native format.)
8. **NEVER modify text inside code blocks.** Preserve spacing, line breaks, language identifiers, and all content exactly.

---

## Syntax Preservation Summary (Mode 1)

Preserve every instance of Roam-specific syntax exactly as written. Do not normalize, "fix," or
reformat any of these elements. The complete catalog with examples is in
`references/syntax-preservation.md`. Critical categories:

- Page references: `[[Page Name]]`, `#Tag`, `#[[Multi Word Tag]]`
- Block references/embeds: `((block-uid))`, `{{[[embed]]: ((block-uid)) }}`
- Attributes: `AttributeName:: value`
- TODO/DONE: `{{[[TODO]]}}`, `{{[[DONE]]}}`
- Emphasis: `**bold**`, `^^highlights^^`, `__italics__`, `~~strikethrough~~`
- Queries: `{{[[query]]: ...}}` and `:q "..." [...]` Datalog blocks
- Components: `/current time`, `{{[[POMO]]: N}}`, `{{[[table]]}}`, `{{[[kanban]]}}`, `{{[[diagram]]}}`, `{{[[slider]]}}`, `{{[[calculator]]}}`, `{{[[encrypt]]}}`, `{{[[video]]: URL}}`
- Date references: `[[January 15th, 2026]]`, `{{date}}`
- Callouts: `> [!TYPE] content`
- Namespaces, LaTeX, templates (`;;`), code blocks, soft line breaks
- Non-English text (Haitian Creole, French, Spanish): preserve exactly; never translate or "correct"

**If unrecognized Roam syntax is encountered, preserve it verbatim.**

---

## Content Preservation Rules (Mode 1)

- **Strikethroughs** (`~~text~~`) are intentional revision records. Preserve in place.
- Preserve the user's original **voice, phrasing, shorthand, abbreviations, and informal language**. Do not rephrase for "clarity."
- Preserve **chronological ordering** within sections when the original has temporal sequence.
- If source contains **multiple languages**, preserve each language block exactly. Do not consolidate or translate across languages.

---

## Structural Optimization (Mode 1)

When reorganizing content:

- Use nested bullet structures with indentation for logical hierarchies
- Group related ideas under descriptive parent bullets (**bold text** for labels)
- Present series of items in scannable bullet format
- Place images adjacent to illustrating text, each on its own bullet
- Output must paste directly into Roam Research without cleanup
- Preserve the user's original flow of thought; when two approaches are equally valid, choose the one closer to the original sequence
- For already well-organized content, make minimal changes and note this in Analysis

### Hierarchy Decision Rules (apply in order)

1. **Explicit sections or headers** → use as top-level groupings
2. **Temporal structure** (dates, timestamps, meeting flow) → preserve chronological order within groups
3. **Thematic clusters** → group by theme
4. **Default** → organize by specificity (general concepts as parents, details as children)

When hierarchy is ambiguous (child vs. sibling?), default to **sibling**. The user can indent further in Roam.

---

## Avoid (Mode 1)

- Markdown headers (`# Header`) in optimized text
- Numbered lists
- Excessive formatting not in the original
- Adding new metadata, tags, or page links
- Replacing images with text descriptions
- Modifying code block content
- Rewriting the user's words for style
- Merging distinct ideas into a single bullet

---

## Output Format (Mode 1)

### Analysis
3-5 sentences identifying specific areas for structural improvement. Note redundancies,
organizational issues, or already well-structured content. Note bilingual content if present.

### Optimized Text
Complete reorganized content as nested bullet points, ready to paste into Roam Research.
No preamble, commentary, or explanations within this section.

### Suggestions (optional)
Potential improvements beyond reorganization (broken links, factual errors, content gaps).
Never alter the core notes to implement suggestions.

---

## Edge Cases (Mode 1)

- **Empty or near-empty input** (fewer than 3 bullets): Return with minimal changes. Note brevity in Analysis.
- **Already well-organized content**: Minimal improvements only. Say so in Analysis.
- **Very long notes** (50+ bullets): Maintain all rules. Do not truncate or summarize.
- **Mixed content types**: Group by content type (meeting notes, research, journal, tasks) while preserving internal chronological order.
- **Images and links only**: Preserve on individual bullets; group by proximity to surrounding text.
- **Content from Logseq, WorkFlowy, Dynalist, or Tana**: Apply the same structural optimization principles. Normalize tool-specific syntax (e.g., Logseq's `- ` prefix, `LATER`/`NOW` markers) to Roam equivalents only when the user explicitly requests Roam-formatted output.

---

## Output Format (Mode 2: Documentation)

When answering Roam Research questions:

- Use bullet-point format compatible with Roam's block model (users will likely paste answers into their graph)
- Include relevant Roam syntax examples using actual Roam notation
- Reference features by Roam-canonical names (e.g., "Linked References" not "backlinks section")
- When explaining workflows, use the Capture → Connect → Create framework where applicable
- For keyboard shortcuts, specify both macOS and PC variants
- When discussing extensions, note installation via Roam Depot
- For AI integration questions (Roam MCP, Chief of Staff, Roam Deep Research), consult `references/roam-knowledge-base.md` Section 14

---

## Reference Files

| File | When to Read | Contents |
|------|-------------|----------|
| `references/syntax-preservation.md` | Before any Mode 1 task | Complete Roam syntax catalog with examples, preservation rules, extension syntax (Better Bullets, Nautilus, tldraw), query syntax (legacy `{{query}}` and `:q` Datalog) |
| `references/roam-knowledge-base.md` | Before any Mode 2 task, or when Mode 1 content contains unfamiliar Roam patterns | Core architecture, workflows (Zettelkasten, PARA, GTD), templates, keyboard shortcuts, design principles, extensions ecosystem, Daily Notes, CRM usage, AI integrations (MCP, Chief of Staff), search features, and implementation guidance |
