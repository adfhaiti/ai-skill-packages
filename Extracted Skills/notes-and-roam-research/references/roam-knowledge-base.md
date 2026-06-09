# Roam Research: Knowledge Base Reference

This file is the authoritative reference for answering Roam Research documentation and
implementation questions (Mode 2). Read this file before answering any guidance query.

---

## Table of Contents

1. Core Architecture
2. Core Mechanics
3. Daily Notes
4. Workflows and Methodologies
5. Templates
6. Keyboard Shortcuts and Commands
7. Productivity Features
8. Design Principles
9. Extensions Ecosystem (Roam Depot)
10. Import, Export, and Graph Management
11. Query System (Legacy and Datalog)
12. Search (Classic and Semantic)
13. Limitations and Workarounds
14. AI Integrations (MCP, Chief of Staff, Deep Research)
15. Key Vocabulary

---

## 1. Core Architecture: Networks vs. Hierarchies

Traditional note tools (Evernote, Notion, Google Docs) use hierarchical structures:
folders, notebooks, stacks. This forces premature classification and silos information.

Roam uses a **network/graph** structure:
- No folders, no notebooks, no stacking
- Every page is a node; relationships form organically through linking
- Structure emerges bottom-up from content itself
- The more information added, the more powerful the system (connections compound)
- Analogous to how the brain connects through associations, not filing cabinets

### The Knowledge Graph
- All pages form a visual graph (the "Graph Overview")
- Each page is a node; each link is an edge
- Nodes grow larger as they accumulate inbound links
- Large nodes = ideas worth pursuing or writing about
- Pattern: "plant idea seeds, wait for nodes to grow, pick the ones that blossom"

### Roam's Technical Foundation
- Built on: React, Clojure/ClojureScript, Datalog
- Data model: directed graph with blocks as atoms and pages as named nodes
- Any block can occupy multiple positions simultaneously
- Changes propagate throughout the graph via references

---

## 2. Core Mechanics

### 2.1 Pages
- Created by typing `[[Page Name]]` or `#PageName`; auto-created on first reference
- Pages can exist as empty placeholders, collecting backlinks
- Every tag is a page, and every page is a tag (equivalent)
- Convention: `[[Page Links]]` for inline references; `#Hashtags` for out-of-context tags
- Pages have no inherent location; reachable from any linking page
- Case-sensitive: `[[Productivity]]` and `[[productivity]]` are different pages
  - Fix: navigate to unwanted page, change title to match correct one; Roam auto-merges

### 2.2 Blocks (Bullets)
- The fundamental unit of content (rendered as bullet points)
- Can nest inside other blocks (indentation via Tab)
- Can be referenced `((uid))`, embedded `{{embed}}`, or dragged to other pages
- Can be converted to TODOs via `/TODO` or `Cmd+Enter` / `Ctrl+Enter`
- Can contain inline calculations, Pomodoro timers, timestamps

### 2.3 Bidirectional Links
- When Page A links to Page B, Page B automatically knows about and displays the link
- Historical lineage: Vannevar Bush's Memex (1945) > Ted Nelson's Project Xanadu (1965) > WWW (mono-directional) > Roam (bi-directional in personal scope)
- Implementation: type `[[Topic]]` or `#Topic`; target page shows source in Linked References
- **Unlinked References**: Roam detects every occurrence of the page name string across the database, even without explicit links. Click "Link" to convert, or "Link All" for batch conversion.

### 2.4 Linked References and Filtering
- Every page has a "Linked References" section showing all pages/blocks linking to it
- Functions as automatic backlinks aggregator
- Creates a timeline when links originate from Daily Notes (which carry dates)
- Supports filtering: e.g., on `[[Mindfulness]]` page, filter to show only references also referencing `[[Books]]`

### 2.5 The Sidebar
- `Shift+Click` any link to open in right-hand sidebar
- Main page stays in view; sidebar is fully navigable
- Multiple pages can be open simultaneously
- Critical for: writing (source notes alongside draft), research (compare pages), CRM (person's page during a call)

---

## 3. Daily Notes

- Auto-created date-stamped page for each day (default landing page)
- Functions as: inbox, journal, productivity log, capture surface
- Provides temporal anchor in an otherwise structureless graph

### Use Patterns
- **Journaling**: free-form writing in first bullets (5-10 min)
- **TODO tracking**: convert bullets to checkboxes; items appear on global `[[TODO]]` page
- **Capture**: fleeting ideas, meeting notes, article references, quotes
  - Tag ideas with `#idea`; tag questions with `#??`
- **Work logging**: each task block references `[[Client Name]]`, creating automatic activity log
- **Time stamping**: `/current time` inserts 24-hour timestamps for billing/productivity

### Daily Notes as Productivity Journal
- Pattern (Coleman McCormick): keep Roam open on second display; notes flow continuously
- Pattern (Ali Abdaal): use Daily Notes template with structured sections

---

## 4. Workflows and Methodologies

### 4.1 Capture > Connect > Create (Smart Notes / Zettelkasten)

Based on Luhmann's Zettelkasten as described in "How to Take Smart Notes" by So"nke Ahrens.

**Capture**: Daily Note for fleeting thoughts; dedicated pages for each consumed resource (book, article, video). Populate with metadata, highlights, and personal interpretation in your own words.

**Connect**: After capturing, review notes and create links to related concepts. Ask: "What does this remind me of?" "How does this relate to X?" The linking process is where insight happens.

**Create**: When a node accumulates enough connections, it signals readiness for synthesis. Open the page, review linked references, and draft new content combining multiple sources.

### 4.2 Research Workflow
- Create a page for each research question
- As you read sources, mention the question page with `[[Question]]` tag
- Over time, the question page accumulates all relevant evidence in its Linked References
- Filter and synthesize when ready

### 4.3 CRM Usage (Josh Ginter / Conor White-Sullivan pattern)
- Create a page for each person: `[[Person Name]]`
- During meetings, write notes on Daily Notes page and tag with `[[Person Name]]`
- Person's page automatically accumulates all interaction history
- Before next meeting: open person's page, review backlinks for context

### 4.4 Meeting Notes (Conor White-Sullivan pattern)
- On Daily Notes, create a block for the meeting
- Indent all notes under that block
- Tag with `[[Meeting]]`, `[[Attendee Names]]`, `[[Project]]`
- Action items get `{{[[TODO]]}}` with `[[Assigned Person]]` tags
- Result: meeting notes are automatically cross-referenced on every tagged page

### 4.5 Executive 1:1 Pattern
- Create query on your page that pulls all TODOs assigned to you
- Before each 1:1, review the person's page for context
- During meeting, add notes on Daily Notes tagged with person
- After meeting, update TODO statuses

---

## 5. Templates

### 5.1 Book Notes Template
```
- **Source**
    - Author:: [[Author Name]]
    - Type:: [[Book]]
    - Status:: Reading / Finished / Abandoned
    - Rating:: /5
    - Started:: [[Date]]
    - Finished:: [[Date]]
- **Summary**
    - (2-3 sentence overview in your own words)
- **Key Ideas**
    - Idea 1 (linked to relevant concept pages)
    - Idea 2
- **Highlights & Notes**
    - Chapter/section reference
        - Quote or paraphrase
        - Your interpretation
```

### 5.2 Article/Paper Notes Template
```
- **Source**
    - Author:: [[Author Name]]
    - Type:: [[Article]] / [[Paper]]
    - URL:: [Title](URL)
    - Tags:: #topic1 #topic2
    - Date Read:: [[Date]]
- **Summary**
    - (Your summary)
- **Key Takeaways**
    - Takeaway 1
    - Takeaway 2
- **Quotes & Notes**
    - "Quote" (with your annotation)
```

### 5.3 Meeting Notes Template
```
- **Meeting: [Topic]** [[Meeting]]
    - Date:: [[Date]]
    - Attendees:: [[Person 1]] [[Person 2]]
    - Project:: [[Project Name]]
    - **Discussion**
        - Point 1
        - Point 2
    - **Decisions**
        - Decision 1
    - **Action Items**
        - {{[[TODO]]}} Task [[Assigned Person]] [[Due Date]]
```

### 5.4 Daily Note Template (Ali Abdaal pattern)
```
- **Morning Pages**
    - Free-form journaling (5-10 min)
- **Today's Priorities**
    - {{[[TODO]]}} Priority 1
    - {{[[TODO]]}} Priority 2
    - {{[[TODO]]}} Priority 3
- **Work Log**
    - /current time: Task description for [[Client/Project]]
- **Capture**
    - Random ideas, links, quotes
    - Tag with #idea or relevant page links
```

### 5.5 Weekly Plan Template (Nat Eliason pattern)
```
- **Week of [[Date Range]]**
    - **Goals This Week**
        - Goal 1 (linked to [[Project]])
        - Goal 2
    - **Monday**
        - {{[[TODO]]}} Task 1
        - {{[[TODO]]}} Task 2
    - **Tuesday**
        - {{[[TODO]]}} Task 1
    - (continued for each day)
    - **Other Tasks** (to be scheduled or deferred)
```

### 5.6 Using Templates
- Create a page called `[[roam/templates]]`
- Each template is a block with children containing the template structure
- Insert templates with `;;` followed by the template name
- Templates can also be triggered via the `/` command menu

---

## 6. Keyboard Shortcuts and Commands

### Essential Shortcuts

| Action | macOS | Windows/Linux |
|--------|-------|---------------|
| Create/find page | `Cmd+U` | `Ctrl+U` |
| Toggle TODO | `Cmd+Enter` | `Ctrl+Enter` |
| Open in sidebar | `Shift+Click` | `Shift+Click` |
| Indent block | `Tab` | `Tab` |
| Outdent block | `Shift+Tab` | `Shift+Tab` |
| Search | `Cmd+U` | `Ctrl+U` |
| Command Palette | `Cmd+P` | `Ctrl+P` |

### Inline Syntax
| Action | Syntax |
|--------|--------|
| Page reference | `[[Page Name]]` |
| Tag | `#Tag` or `#[[Multi Word]]` |
| Block reference | `((` then search |
| Bold | `**text**` |
| Italic | `__text__` |
| Highlight | `^^text^^` |
| Strikethrough | `~~text~~` |
| Code inline | `` `code` `` |
| LaTeX inline | `$$formula$$` |

### Slash Commands
| Command | Result |
|---------|--------|
| `/current time` | Insert timestamp |
| `/Pomo` | Pomodoro timer |
| `/table` | Table component |
| `/kanban` | Kanban board |
| `/diagram` | Diagram canvas |
| `/TODO` | TODO checkbox |

### Block Operations
- `Option+Drag` (Mac): drag block while preserving live link to source
- Right-click page title: expand/collapse all blocks
- `Ctrl+Shift+V`: paste with soft line breaks (multi-line single block)

---

## 7. Productivity Features

- **Inline Calculator**: type math expression; use `/inline` to compute results
- **Pomodoro Timer**: `/Pomo` inserts clickable timer (bell sounds only if page is open; workaround: keep timer page in sidebar)
- **Tables**: `/table` command; rows and columns as indented children; sortable columns and improved drag-and-drop scrolling (May 2026)
- **Kanban Boards**: `/kanban` command; columns as indented children
- **Diagrams**: `/diagram` for visual diagrams
- **Queries**: aggregate blocks matching criteria across database (both legacy `{{query}}` and new `:q` Datalog)
- **Encrypted Blocks**: `{{[[encrypt]]}}` for sensitive content
- **Slider**: `{{[[slider]]}}` for interactive value selection

---

## 8. Design Principles for Effective Use

1. **Link liberally**: err on creating too many links; unused links cost nothing, missed links cost discoverability
2. **Don't pre-organize**: let structure emerge from usage; resist folder-like hierarchies
3. **Use Daily Notes as home base**: capture everything there first, refine and connect over time
4. **Write in your own words**: restate ideas in your language for better comprehension and retrieval
5. **Tag people, places, ideas**: the more entities tagged, the richer the graph
6. **Use metadata templates consistently**: standardized metadata makes pages comparable and filterable
7. **Review Graph Overview periodically**: identify large nodes as candidates for deep exploration
8. **Use the sidebar constantly**: parallel viewing is one of Roam's most powerful features
9. **Embrace the mess**: designed to be messy at micro level, organized at macro level through links
10. **Don't duplicate; link**: use block references to maintain single source of truth

---

## 9. Extensions Ecosystem (Roam Depot)

Extensions are installed via **Roam Depot** (Settings > Roam Depot > Community Extensions).

### Notable Extensions (as of May 2026)

| Extension | Purpose |
|-----------|---------|
| Better Bullets | Custom bullet glyphs via prefix markers (`-> `, `=> `, `?? `, etc.) |
| Roam Toolkit Vim Mode | Vim-style navigation/editing for blocks |
| Chief of Staff | AI assistant connecting Roam to LLMs (Anthropic, OpenAI, Gemini, Mistral) via Composio |
| Roam Reader | Read-it-later with annotations synced to graph |
| Quick Capture | Hotkey-triggered capture to Daily Notes sidebar |
| Export with References | Export page + backlinks as markdown |
| Roam Deep Research | Long-form research jobs dispatched to external AI providers |
| YouTube Transcript Sync | Import YouTube transcripts with clickable timestamps |
| Object Metadata Autocomplete | Search OpenLibrary/Google Maps and create structured pages |
| DNP Default Filters | Auto-apply linked reference filters to Daily Notes |
| Better Command Palette | Pin favorite commands to top of palette |
| Nautilus Enhanced | Advanced navigation and block management |
| tldraw | Drawing/whiteboard integration |
| Stats | Graph statistics (page count, block count, word count, etc.) |
| Meta Type | Add a `Type` attribute to pages; inline chip appears next to title with configurable side panel and pinned fields |
| Discourse Graphs | Structured argumentation with custom sidebar commands, clipboard search, and modular node creation (v0.19.0+) |
| Roam Raycast Extension | Instant capture, capture templates, Windows support; works with encrypted graphs |

### Extension Syntax Patterns
- Extensions may use `;;` for template insertion
- Extensions store config in `extensionAPI.settings`
- Extensions can register command palette actions and slash commands
- Custom CSS variables may be exposed (e.g., `--bb-bullet-size` for Better Bullets)

---

## 10. Import, Export, and Graph Management

### Export Formats
- **Markdown**: good for portability to other tools
- **JSON**: preserves more Roam-specific metadata; recommended for Roam-to-Roam transfers
- **EDN**: highest fidelity; recommended for graph backup and restoration

### Import Formats
- **Markdown**: for importing from other tools
- **JSON**: for importing Roam exports

### Graph Management
- Graph names cannot be changed after creation (workaround: export EDN, create new graph, restore)
- Deleted graph names become available after 90 days
- Local graphs are device-specific; hosted graphs are accessible anywhere
- Merging graphs is not supported (workaround: manual copy-paste for small graphs, then EDN import)
- Maximum paste size: ~50KB of text at a time

### Hosted vs. Local Graphs
- **Hosted**: accessible from any device; supports sharing/collaboration
- **Local**: stored only on the creating device; ultra-secure (data never hits server)

---

## 11. Query System

### Legacy Query Syntax
```
{{[[query]]: {and: [[Page A]] [[Page B]] {not: [[Page C]]}}}}
```
- Operators: `{and:}`, `{or:}`, `{not:}`, `{between: [[date1]] [[date2]]}`
- Good for simple filtering; limited expressiveness

### New Datalog Query Syntax (`:q` blocks, March 2026+)
Full Datalog queries with Roam-specific extensions.

**Structure**:
```
:q "Human-readable title"
[:find ?b
 :where
 [?b :block/string ?s]
 [(clojure.string/includes? ?s "search term")]]
```

**Roam-specific symbols**:
- `ms/*` : millisecond timestamps (e.g., `ms/today-start`, `ms/next-week-end`)
- `dnp/*` : Daily Note Page references (e.g., `dnp/this-week-start`, `dnp/this-week-end`)

**Roam-specific rules**:
- `(refs-dnp-between ?start ?end ?b)` : blocks referencing DNPs in range
- `(in-dnp-between ?start ?end ?b)` : blocks inside DNPs in range
- `(in-or-refs-dnp-between ?start ?end ?b)` : either of the above
- `(created-by "Display Name" ?b)` : blocks created by user

**Context behavior**: When a `:q` query is on a Daily Note page, relative symbols (like `ms/today-start`) resolve to that Daily Note's date, not the actual current date. On non-DNP pages, they resolve to the actual current date.

**API access**: Custom symbols and rules are exposed via `roamAlphaAPI.data.q` for extension developers.

---

## 12. Search (Classic and Semantic)

### Classic Search
- `Cmd+U` (Mac) / `Ctrl+U` (PC) opens the find-or-create modal
- Searches page titles by default; results show reference counts
- Also serves as the page creation shortcut (type a new name and press Enter)

### Redesigned Search Bar (May 2026)
- Full redesign of the find-or-create modal with richer results:
  - Reference counts on page results
  - Path context and match highlighting on block-level results
  - Live preview window toggled with `Ctrl+O`
- Classic inline search box remains accessible for users who prefer the original interface
- Advanced search available from the right side of the search bar or via a keyboard shortcut

### Semantic Search (May 2026)
- Background search now indexes the resolved text of blocks, making `((block references))` findable by their content (not just the UID)
- Semantic search finds blocks by meaning, not just exact keyword match
- Integrated into the redesigned search bar alongside classic text search

### Background Indexing
- Roam performs background indexing for faster search across large graphs
- Resolved block reference text is included in the index, improving discoverability

---

## 13. Limitations and Workarounds

| Limitation | Workaround |
|------------|-----------|
| No native mobile app | Install as webapp via Chrome (Add to Homescreen); Capture for Roam (Android) for quick capture |
| Case-sensitive page names | Merge by renaming unwanted page to match correct one |
| No graph name changes | Export EDN, create new graph, restore |
| No graph merging | Manual copy-paste for small graphs + EDN import |
| Not ideal for long-form prose | Outline in Roam, draft in Google Docs; or use "view as document" mode |
| $15/month pricing | 31-day free trial; 50% scholar discount (students, under 22, financial hardship) |
| Learning curve | Several days of active use required to internalize paradigm shift |
| Pomodoro bell needs open page | Keep timer page in sidebar |
| 50KB paste limit | Split large imports into chunks |

---

## 14. AI Integrations (MCP, Chief of Staff, Deep Research)

### Roam MCP Server (Model Context Protocol)
- Official MCP server by Roam Research (v0.6.5+ as of May 2026, alpha software)
- Connects to Roam's local HTTP API (requires desktop app with "Enable Local API" in Settings)
- Enables AI agents (Claude, etc.) to read and write to a Roam graph programmatically
- **Available tools**: `create_page`, `update_page`, `delete_page`, `create_block`, `update_block`, `move_block`, `delete_block`, `search`, `search_templates`, `get_page`, `get_block`, `get_backlinks`, `get_focused_block`, `open_main_window`, `open_sidebar`, `file_get`
- **Graph guidelines**: create a `[[agent guidelines]]` page in the graph with instructions for AI agents; the MCP server retrieves these via `get_graph_guidelines`
- **Graph selection**: auto-detected with single graph open; specify `graph` parameter for multiple
- **Safety warning**: grants full read/write access — recommend backups and starting with test graphs
- Installation: `git clone`, `npm install`, `npm run build`; configured via `.mcp.json` or Claude Desktop config
- CLI also available: `npm run cli -- <tool-name> [options]`

### Chief of Staff (Roam Depot Extension)
- AI assistant extension connecting Roam directly to LLMs (Anthropic, OpenAI, Gemini, Mistral) via Composio
- Enables in-graph AI interactions: summarize blocks, generate content, answer questions using graph context
- Installed via Roam Depot

### Roam Deep Research (Roam Depot Extension)
- Long-form research jobs dispatched to external AI providers
- Operates asynchronously: submit a research question, results populate into the graph
- Installed via Roam Depot

### Context Engineering with Roam
- Roam's graph structure is well-suited as a personal knowledge layer for AI agent pipelines
- Pattern: use Roam as the PKM layer feeding an AI agent harness; the graph provides context engineering for LLMs (referenced in Brookings Institution working paper on "context-maxxing," May 2026)
- The bidirectional link structure and block-level granularity enable precise context retrieval

---

## 15. Key Vocabulary

| Term | Definition |
|------|-----------|
| Block | Atomic unit of content (a bullet point); can be nested, referenced, linked, TODO'd |
| Page | Named entity in the graph; auto-created on first `[[]]` or `#` reference |
| Linked Reference (Backlink) | Automatic reverse-link showing all pages/blocks referencing the current page |
| Unlinked Reference | Detected occurrence of page name string without explicit link |
| Graph Overview | Visual map of all pages (nodes) and links (edges) |
| Daily Note | Auto-created date-stamped page; default home screen |
| Sidebar | Secondary pane for parallel viewing |
| Block Reference | Live link to a specific block `((uid))`; updates if source changes |
| Block Embed | Renders referenced block's content inline `{{embed}}` |
| Bidirectional Link | Link where both source and target are mutually aware |
| Attribute | Key-value metadata using `::` syntax |
| PKM | Personal Knowledge Management |
| Zettelkasten | Interconnected atomic notes method (Niklas Luhmann) |
| PARA | Projects, Areas, Resources, Archive (Tiago Forte) |
| Progressive Summarization | Layered highlighting: bold > highlight > extract (Tiago Forte) |
| Roam Depot | Extension marketplace for Roam |
| Graph | A Roam database (all your pages and blocks) |
| Namespace | Hierarchical page organization via `/` (e.g., `[[Projects/ADF]]`) |
| View as Document | Right-click title to toggle bullet-free prose view |
| Semantic Search | Search by meaning (not just keywords); indexes resolved block reference text |
| MCP (Model Context Protocol) | Standard protocol for AI agents to interact with tools; Roam has an official MCP server |
| Agent Guidelines | A `[[agent guidelines]]` page in the graph with instructions for AI agents working via MCP |
| Meta Type | Extension adding typed pages with inline attribute chips and side panels |
| Discourse Graph | Extension for structured argumentation and modular claim/evidence nodes |
