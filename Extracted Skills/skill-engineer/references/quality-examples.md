# Quality Examples

Annotated good and bad skill patterns. Load when reviewing or auditing skills.

---

## Exemplary Descriptions

### Example 1: Hook Development (Score: 95/100)

```yaml
description: >
  This skill should be used when the user asks to "create a hook",
  "add a PreToolUse/PostToolUse/Stop hook", "validate tool use",
  "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}",
  "set up event-driven automation", "block dangerous commands",
  or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop,
  SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification).
  Provides comprehensive guidance for creating and implementing Claude
  Code plugin hooks with focus on advanced prompt-based hooks API.
```

**Why it scores well:**
- 7 specific trigger phrases covering diverse scenarios
- Includes naive phrasings ("block dangerous commands") and technical terms
- Third-person format with scope clarity
- Lists supported events (routing disambiguates from similar skills)
- Under 200 tokens

### Example 2: Skill Repair (Score: 90/100)

```yaml
description: >
  This skill should be used when the user asks to "fix my skill" or "audit this skill".
  Make sure to use this skill whenever the user mentions skill quality, structural issues,
  broken skills, or skill diagnostics — even if they don't explicitly say "repair-skill".
  Not for adding features or improving effectiveness — use improve-skill. Not for agents
  — use repair-agent.
```

**Why it scores well:**
- Natural trigger phrases ("fix my skill")
- Routing directive ("Make sure to use this skill whenever...")
- Negative triggers sharpen boundaries ("Not for agents")
- Clear domain distinction from sibling skills

### Example 3: Plugin Structure (Score: 88/100)

```yaml
description: >
  This skill should be used when the user asks to "create a plugin",
  "scaffold a plugin", "understand plugin structure", "organize plugin
  components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}",
  "add commands/agents/skills/hooks", "configure auto-discovery",
  or needs guidance on plugin directory layout, manifest configuration,
  component organization, file naming conventions, or Claude Code plugin
  architecture best practices.
```

**Why it scores well:**
- Mix of specific actions and conceptual queries
- Covers both creation and understanding use cases
- Technical terms alongside plain language

---

## Poor Descriptions

### Anti-Pattern 1: Vague Trigger (Score: 15/100)

```yaml
description: Provides guidance for working with hooks.
```

**Problems:**
- No trigger phrases at all
- Not third-person format
- No scope boundaries
- Would never trigger because no matching user speech patterns

### Anti-Pattern 2: Second-Person (Score: 25/100)

```yaml
description: Use this skill when you want to create a hook or need help with event handling.
```

**Problems:**
- Second-person ("you want", "you need")
- Only 2 vague scenarios
- No routing directive

### Anti-Pattern 3: Token-Wasting (Score: 40/100)

```yaml
description: >
  This is a comprehensive skill designed to help users with all aspects of
  hook development in Claude Code plugins. It covers the creation, testing,
  debugging, and optimization of hooks including PreToolUse, PostToolUse,
  and Stop events. The skill provides detailed guidance on prompt-based
  hooks, command hooks, and HTTP hooks with examples and best practices
  for each type.
```

**Problems:**
- Meta-commentary ("comprehensive skill designed to help")
- Explains what hooks are (wastes tokens on every session)
- No verbatim trigger phrases
- 70+ words for what could be said in 30

### Anti-Pattern 4: Over-Broad (Score: 35/100)

```yaml
description: This skill should be used when the user needs help with code,
  programming, development, engineering, or technical tasks.
```

**Problems:**
- Would trigger on virtually every technical request
- No domain specificity
- No negative boundaries
- Collides with every other technical skill

---

## Exemplary SKILL.md Body Patterns

### Pattern: Lean Workflow Hub

```markdown
# Skill Name

Brief objective statement (1-2 sentences).

## Core Workflow

### Step 1: Load Context
[3-5 lines]

### Step 2: Analyze
[5-10 lines with reference to detailed guidance]
Load `references/analysis-guide.md` for detailed criteria.

### Step 3: Execute
[5-10 lines]

### Step 4: Verify
[3-5 lines]

## Reference Files
- `references/analysis-guide.md`: detailed criteria and examples
- `references/edge-cases.md`: known edge cases and workarounds

## Scripts
- `scripts/validate.py <path>`: structural validation
```

**Why it works:** Under 200 lines. Clear phases. Detail deferred. Every resource referenced.

### Anti-Pattern: Kitchen Sink

SKILL.md that is 800+ lines with inline examples, API documentation, edge case catalogs,
and copy-paste code blocks. No references directory despite having deferrable content.

**Why it fails:** Loads 800+ lines on every invocation. Most content only needed for
specific sub-tasks. Exceeds 5,000-token compaction threshold.