# Skill Writing Guide

Reference for skill anatomy, progressive disclosure, writing patterns, frontmatter
catalog, and directory conventions. Load when creating new skills or repairing existing ones.

## Table of Contents

- [The Three-Level Loading Model](#three-level-loading-model)
- [Directory Anatomy](#directory-anatomy)
- [Frontmatter Reference](#frontmatter-reference)
- [Body Structure Conventions](#body-structure-conventions)
- [Progressive Disclosure](#progressive-disclosure)
- [Degrees of Freedom](#degrees-of-freedom)
- [Naming Conventions](#naming-conventions)
- [Dynamic Content Syntax](#dynamic-content-syntax)
- [Skill Content Lifecycle](#skill-content-lifecycle)

---

## The Three-Level Loading Model

This model governs every progressive disclosure and verbosity decision.

| Level | What loads | When | Budget impact |
|-------|-----------|------|---------------|
| **Metadata** | Frontmatter `description` | Every session, whether or not the skill triggers | Highest: every token costs on every session |
| **Skill body** | SKILL.md below the `---` | Only when the skill triggers | Medium: costs on every invocation of this skill |
| **Resources** | `references/`, `examples/`, `scripts/` | Only when Claude explicitly reads them | Lowest: free until needed |

Implication: justify every word in the description. Defer detail from SKILL.md to references aggressively. Scripts can execute without being loaded into context.

---

## Directory Anatomy

### Simple skill (no subdirectories)

```
skill-name/
└── SKILL.md    # Single file; body under 200 lines
```

Use when: one clear workflow, no reusable code, no domain-specific reference data.

### Standard skill

```
skill-name/
├── SKILL.md          # Core instructions; 200-400 lines
└── references/
    └── topic.md      # Detail deferred from SKILL.md
```

Use when: SKILL.md would exceed ~300 lines, or the skill has sections only needed for
specific sub-tasks.

### Complex skill

```
skill-name/
├── SKILL.md          # Navigation + core flow; under 500 lines
├── scripts/          # Deterministic operations
├── references/       # Documentation Claude reads while working
├── examples/         # Complete, runnable artifacts users can copy
└── assets/           # Output-only files (templates, images, fonts)
```

### Directory Type Definitions

**`scripts/`**: Executable code (Python, Bash). Defining characteristic: scripts run without
being loaded into context. Use when: the same code appears more than once across invocations,
the operation is fragile or must produce identical output, or a utility benefits multiple
workflow phases. Every script must have an explicit reference in SKILL.md with usage context.

**`references/`**: Documentation Claude reads while working. Defining characteristic: loaded
only when Claude decides it needs them. Use when: a SKILL.md section would exceed ~100 lines,
information is needed only for specific sub-tasks, or domain-specific data (lookup tables,
option catalogs) is involved. Include a TOC at the top of any reference file over 100 lines.

**`examples/`**: Complete, runnable artifacts users copy directly. Distinct from references
(docs to read) and scripts (utilities to invoke). Use when: the skill produces output users
adapt, working examples disambiguate ambiguous instructions, or the skill teaches by
demonstration.

**`assets/`**: Files used in output but never loaded into context. Consumed by other tools or
included in deliverables: templates, images, fonts, boilerplate, starter projects.

---

## Frontmatter Reference

### Required Fields

#### `name` (string)
Lowercase letters, digits, and hyphens only. Max 64 characters. Omit to use directory name.
Prefer short, verb-led names for commands. Namespace by tool when it aids routing:
`gh-address-comments`, `linear-close-issue`.

#### `description` (string)
The primary triggering mechanism. Always in context. Use `>` folded scalar (not `|` literal;
`|` preserves newlines that produce unexpected whitespace).

**Token budget:** Under 150 tokens (200 absolute max). Hard limit: 1024 characters (~250
tokens). Descriptions over 250 characters are truncated in the skill listing.

**Format rules:**
- Skills: third-person ("This skill should be used when the user asks to...")
- Commands: verb-first, under 60 chars

**Trigger phrase rules:**
- 3-5 varied trigger phrases minimum. Single-phrase descriptions have high miss rates.
- Phrases must be verbatim user speech (the exact words someone would type), not formalized
  paraphrases. "fix my skill" triggers better than "skill remediation workflow."
- Include at least one naive phrasing from a user who has never heard of the skill.
- Add negative triggers ("Not for X") in crowded domains to sharpen routing boundaries.
- Consider a routing directive suffix: "Make sure to use this skill whenever the user
  mentions [X, Y, Z]; even if they don't explicitly say '[skill name]'." The routing suffix
  uses intent categories (broad, anti-overfit); the core uses verbatim phrases (recall).

### Optional Fields

#### `allowed-tools` (list)
Restricts available tools. Default: unrestricted. Must be a YAML list (block `- Tool` or
flow `[Tool, Tool]`); a comma-separated string parses as a single scalar, not a list.

Tool selection framework:

| Tier | Tools | When to restrict |
|------|-------|------------------|
| Always allow | `Read`, `Grep`, `Glob` | Only if skill must be strictly read-only |
| Usually allow | `Edit`, `Write`, `WebSearch`, `WebFetch`, `Task` | Restrict if deliberately non-modifying |
| Scope Bash | `Bash(git:*)`, `Bash(npm:*)`, etc. | Never allow unrestricted `Bash` unless scope is unknown |
| Require if interactive | `AskUserQuestion` | Omit only if fully automated |
| Require if delegating | `Skill` | Omit if no delegation |
| Require if notebook | `NotebookEdit` | Omit unless `.ipynb` |
| Require if plan-gated | `EnterPlanMode`, `ExitPlanMode` | Omit unless plan/execute split |

Complete tool list: Read, Write, Edit, Glob, Grep, Bash, Bash(git:*), Bash(npm:*),
Bash(pytest:*), WebFetch, WebSearch, Task, AskUserQuestion, Skill, NotebookEdit,
EnterPlanMode, ExitPlanMode, mcp__<server>__<tool>.

#### `argument-hint` (string)
Shown in autocomplete. Documents expected argument syntax. Values containing `[...]` must
be quoted (YAML treats unquoted `[` as flow sequence start).

#### `hooks` (object)
Scoped to skill lifetime. Supports PreToolUse, PostToolUse, Stop, SessionStart, etc.
Each entry: optional `matcher` (filter by tool name), `hooks` array with handlers
(type: command/http/prompt/agent, command, timeout, statusMessage, once).
`once: true` is valid for skills only, not agents.

#### `user-invocable` (boolean)
Default `true`. Set `false` to hide from `/` menu while keeping automatic routing.

#### `disable-model-invocation` (boolean)
Commands only. Prevents auto-loading via description routing. Forces manual invocation.

#### `context` (string)
Set to `fork` to run in an isolated subagent. Pair with `agent`.

#### `agent` (string)
Subagent type when `context: fork` is set. Options: `Explore`, `Plan`, `general-purpose`,
or custom agents. `agent` without `context: fork` is dead config.

#### `effort` (string)
Override effort level: `low`, `medium`, `high`, `max` (max = Opus 4.6 only).

#### `paths` (string or list)
Glob patterns limiting auto-activation to matching files. Skills with `paths` should have
descriptions matching the narrowed scope.

#### `shell` (string)
Shell for inline execution blocks: `bash` (default) or `powershell`.

---

## Body Structure Conventions

### Voice and Framing

- **Imperative voice throughout**: "Analyze", "Generate", "Identify"
- **No first-person**: Never "I will", "I am", "I'll then check"
- **No second-person**: Never "you should", "you can", "your"
- **No hedging**: Remove "you might want to", "consider possibly", "generally speaking"
- **Intensional over extensional**: State rules directly with reasoning, not examples that
  imply the rule. An intensional rule generalizes to every input; an extensional approach
  requires reverse-engineering the rule from examples.

### Header Depth

- H2 (`##`) for major phases or top-level sections
- H3 (`###`) for sub-topics within a phase
- No H4+ (`####`): content this granular belongs in `references/`

### Routing Guidance Placement

Routing guidance ("when to use this skill") belongs exclusively in frontmatter description.
Never in the body. The body loads only after triggering; routing guidance there is never read
by the routing decision and wastes context.

### Size Invariants

| SKILL.md lines | Interpretation |
|----------------|----------------|
| Under 200 | Simple skill; likely no `references/` needed |
| 200-400 | Standard; check for invocation-frequency-selective sections |
| 400-500 | Approaching limit; audit for deferrable content |
| Over 500 | Requires `references/` deferral |

Target: 1,500-2,000 words. Absolute max: 5,000 words.

### Variable Bindings in Code Blocks

Code blocks serve two purposes: illustrating an operation and establishing workflow state.
When collapsing a code block to prose, preserve variable bindings (`BASE=...`, `BRANCH=...`)
that later steps reference. Add a "derive working variables" preamble before steps that use them.

---

## Progressive Disclosure

### What Goes in SKILL.md (always loaded when skill triggers)

- Core concepts and overview
- Essential procedures and workflows
- Quick reference tables
- Pointers to references/examples/scripts with file paths and usage context
- Most common use cases

### What Goes in references/ (loaded as needed)

- Detailed patterns and advanced techniques
- Comprehensive API documentation
- Migration guides, edge cases, troubleshooting
- Extensive examples and walkthroughs
- Large reference files (>10k words): include grep search patterns in SKILL.md

### What Goes in examples/ (complete, copyable artifacts)

- Configuration files, template code, structured prompts
- Working demonstrations that disambiguate ambiguous instructions

### What Goes in scripts/ (executable utilities)

- Validation tools, testing helpers, parsing utilities, automation scripts
- Must be executable and documented
- Must be referenced in SKILL.md

---

## Degrees of Freedom

Match instruction specificity to the task's fragility and variability:

| Level | When to use | Format |
|-------|-------------|--------|
| High freedom | Multiple valid approaches; context determines best path | Text heuristics, principles, criteria |
| Medium freedom | Preferred pattern exists; some variation acceptable | Pseudocode, parameterized scripts |
| Low freedom | Fragile operations, exact sequence required | Exact scripts, minimal parameters |

A step described vaguely that must produce consistent output is under-constrained.
A step with exact scripts for a judgment-heavy task is over-constrained.

---

## Naming Conventions

| Element | Rule |
|---------|------|
| Skill name | Lowercase letters, digits, hyphens; max 64 chars |
| Command name | Verb-led: `fix-issue`, `review-pr`, `deploy-staging` |
| Namespace | Tool prefix when it aids routing: `gh-address-comments` |
| Reference files | Lowercase, hyphens, descriptive: `frontmatter-options.md` |
| Script files | Lowercase, hyphens or underscores: `init_skill.py` |

---

## Dynamic Content Syntax

Substitutions processed before the skill body reaches Claude:

| Syntax | Resolves to |
|--------|-------------|
| `$ARGUMENTS` | All arguments passed as a single string |
| `$1`, `$2`, `$3` | Individual positional arguments |
| `@path/to/file` | Contents of the file, loaded inline |
| `@$1` | Contents of file whose path was passed as first argument |
| `` `!command` `` | Output of executing the command, injected inline |
| `${CLAUDE_SKILL_DIR}` | Path to the skill's own directory |
| `${CLAUDE_SESSION_ID}` | Current session ID |

Skills accepting a file path should use `@$1` to load inline rather than requiring a Read
tool call. The bang-backtick pattern is underused: git branch, file tree, env vars can be
injected without tool calls.

---

## Skill Content Lifecycle

When invoked, the rendered SKILL.md enters the conversation as a single message and stays
for the session. Claude Code does not re-read on later turns; write guidance as standing
instructions, not one-time steps.

Auto-compaction retains the first 5,000 tokens of each skill. All recently invoked skills
share a 25,000-token budget (most-recent-first). Skills exceeding 5,000 tokens lose their
tail after compaction. Critical instructions appearing after ~5,000 tokens will be lost;
front-load critical content or move reference material to separate files.

---

## Gap Analysis Checklist

**Would `scripts/` help?**
- Is there a code block that appears more than once across invocations?
- Is there a fragile operation that must produce consistent output?
- Is there a setup/validation/cleanup step that could be scripted?

**Would `references/` help?**
- Does SKILL.md exceed 300 lines with sections only needed for specific sub-tasks?
- Does the skill have domain-specific lookup data?
- Does the skill have multiple variants that could be split?

**Would `examples/` help?**
- Does the skill produce output users will adapt?
- Are there ambiguous instructions a working example would clarify?

**Would additional frontmatter fields help?**
- Skill accepts a file path but lacks `argument-hint`?
- Skill needs user decisions but lacks `AskUserQuestion` in `allowed-tools`?
- Skill writes files but `Edit`/`Write` not in `allowed-tools`?
- Skill has unrestricted `Bash` when a scoped pattern would work?
