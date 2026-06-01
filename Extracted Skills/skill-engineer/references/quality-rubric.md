# Quality Rubric

Scoring criteria, grade mapping, structural audit dimensions, effectiveness sub-analyses,
and severity framework. Load when reviewing, improving, or auditing skills.

## Table of Contents

- [Quick Score: 4-Dimension Scoring](#4-dimension-scoring)
- [Grade Mapping](#grade-mapping)
- [Structural Audit: 7 Dimensions](#structural-audit)
- [Effectiveness Audit: 5 Sub-Analyses](#effectiveness-audit)
- [Severity Framework](#severity-framework)
- [Improvement Types](#improvement-types)
- [Audit Calibration](#audit-calibration)

---

## 4-Dimension Scoring

Use for quick quality assessment (score-only mode).

### Dimension 1: Description Quality (25%)

| Criterion | Points | Evaluation |
|-----------|--------|------------|
| Trigger phrases clarity | 0-25 | 5+ specific phrases = 25; 3-4 = 20; 2-3 = 15; 1-2 = 10; none = 0 |
| Third-person format | 0-25 | Consistent "This skill should be used when..." = 25; mixed = 10; second-person = 0 |
| Description length | 0-25 | 150-300 chars = 25; 100-150 or 300-400 = 20; under 50 or over 700 = 5 |
| Specific scenarios | 0-25 | Multiple concrete scenarios + scope boundaries = 25; vague = 10; none = 0 |

**Red flags:** vague triggers ("helps with tasks"), second-person descriptions, missing
trigger phrases, no scope boundaries.

### Dimension 2: Content Organization (30%)

| Criterion | Points | Evaluation |
|-----------|--------|------------|
| Progressive disclosure | 0-30 | SKILL.md <2k words with refs = 30; 2-3k = 25; 3-5k = 20; >7k = 0 |
| SKILL.md length control | 0-25 | 1,500-2,000 words = 25; 1-1.5k or 2-3k = 20; >5k = 5 |
| References usage | 0-25 | 3+ organized refs = 25; 1-2 refs = 20; none when needed = 5 |
| Resource referencing | 0-20 | All resources referenced with context = 20; some missing = 10; none = 0 |

### Dimension 3: Writing Style (20%)

| Criterion | Points | Evaluation |
|-----------|--------|------------|
| Imperative voice | 0-35 | Consistent imperative = 35; mostly = 25; mixed = 15; mostly second-person = 0 |
| Conciseness | 0-35 | Dense, no filler = 35; some padding = 25; verbose = 10 |
| Consistency | 0-30 | Uniform style = 30; minor variation = 20; inconsistent = 5 |

**Red flags:** "You should", "You can", hedging language, motivational padding,
first-person narrative.

### Dimension 4: Structural Integrity (25%)

| Criterion | Points | Evaluation |
|-----------|--------|------------|
| Valid YAML frontmatter | 0-25 | Parses, required fields present = 25; minor issues = 15; broken = 0 |
| File existence | 0-25 | All referenced files exist = 25; some missing = 10; many missing = 0 |
| No orphan files | 0-25 | All files referenced or purposeful = 25; some orphans = 15 |
| Header depth | 0-25 | No H4+ in SKILL.md = 25; occasional H4 = 15; H5+ = 5 |

---

## Grade Mapping

| Score | Grade | Interpretation |
|-------|-------|----------------|
| 90-100 | A | Excellent; ready for distribution |
| 80-89 | B | Good; minor improvements possible |
| 70-79 | C | Acceptable; several improvements needed |
| 60-69 | D | Below average; significant issues |
| Below 60 | F | Failing; major rework required |

Generate an improvement plan automatically for scores below B (80).

---

## Structural Audit

Deep inspection across 7 dimensions. Use for thorough structural review.

### D1: Frontmatter Quality

Audit the description (always-in-context cost):
- **Person and framing**: third-person required ("This skill should be used when...").
  First-person or imperative framing reads as an instruction to execute, not a triggering
  condition. Critical if wrong.
- **Scalar type**: `>` folded scalar required; `|` literal preserves newlines unexpectedly. Minor.
- **Trigger phrase authenticity**: phrases must be verbatim user speech, not paraphrases.
  "create a hook" triggers better than "hook creation tasks". Major if paraphrased.
- **Token density**: description restating the skill name, explaining what skills are, or
  including meta-commentary wastes budget. Minor per instance, major if systemic.
- **Negative triggers**: in crowded domains, absence of "Not for X" causes overtriggering. Major.
- **Routing directive**: absence of a "Make sure to use..." suffix may cause undertriggering. Minor.

### D2: Execution Modifiers

Audit `allowed-tools`, `hooks`, `context`, `agent`, `effort`, `paths`:
- `allowed-tools` as a string instead of list: critical (tools not recognized).
- Unrestricted `Bash` when scope is known: major.
- `AskUserQuestion` missing when skill asks the user anything: major.
- `agent` without `context: fork`: dead config, minor.
- `paths` set with broad description: contradiction, minor.

### D3: Instruction Style

- Second-person voice anywhere in body: major.
- First-person narrative: major.
- Hedging language: minor per instance.
- Headers deeper than H3: minor per instance, major if systemic.

### D4: Agentic Split

- Routing guidance in body (should be frontmatter only): major.
- "When to use this skill" section in body: major (never read by routing decision).
- Task delegation without `Task` in allowed-tools: critical.

### D5: Verbosity

- SKILL.md over 500 lines without references: major.
- Content that loads every invocation but is only needed for specific sub-tasks: major.
- Repeated instructions: minor per instance.

### D6: Workflow Clarity

- Ambiguous step ordering: major.
- Missing error handling for fragile operations: minor.
- Steps that require tools not in allowed-tools: critical.

### D7: Anatomy Completeness

Apply gap analysis checklist from skill-writing-guide.md:
- Scripts that would reduce redundancy: gap.
- References that would reduce SKILL.md size: gap.
- Examples that would clarify ambiguous instructions: gap.
- Missing frontmatter fields: gap.

---

## Effectiveness Audit

Deep analysis of whether the skill accomplishes what users need. Structural correctness
is a prerequisite; note obvious structural issues briefly and recommend the Repair branch.

### 2a: Mental Simulation

Walk through the skill as Claude executing it with a concrete representative request.
Choose a typical input (not an edge case). Track: where does the workflow stall, produce
wrong output, or require knowledge the skill doesn't provide?

### 2b: Doc Validation

- Verify every referenced file exists and is non-empty.
- Verify every script runs without syntax errors.
- Verify no dead links or orphan files.
- Verify examples are complete and current.

### 2c: Feature Adjacency

Identify capabilities users would naturally expect but are missing. If a skill handles
"create X" and "delete X", users will expect "update X" and "list X". Flag gaps.

### 2d: UX Flow

Trace the user experience end-to-end:
- How many questions does the skill ask before producing output?
- Are handoffs between steps clear?
- Does the output format match what users actually need?
- Are there unnecessary confirmations or redundant steps?

### 2e: Edge Cases

Identify inputs that would break or confuse the workflow:
- Empty or malformed input
- Very large or very small input
- Input that matches a sibling skill's domain
- Input in an unexpected format

---

## Severity Framework

### Finding Types

- **Violation**: something present that contradicts a rule.
- **Gap**: something absent that would improve the skill.
- **Improvement**: something that works but could be meaningfully tightened.

### Severity Levels

- **Critical**: breaks triggering or wastes significant context on every invocation.
- **Major**: degrades generalization, reliability, or workflow correctness.
- **Minor**: polish; the skill works but isn't as good as it could be.

### Effort Calibration

| Effort | Description |
|--------|-------------|
| Trivial | Single-line edit; under 2 minutes |
| Low | A few edits in one file; under 15 minutes |
| Medium | Edits across multiple files or new content; under 1 hour |
| High | New reference files, scripts, or significant restructuring; over 1 hour |

### Priority = Severity x Inverse Effort

Rank findings by value/effort ratio. A major finding with trivial effort ranks higher than
a critical finding with high effort for triage purposes.

---

## Improvement Types

| Type | Description | Typical Effort |
|------|-------------|----------------|
| Trigger expansion | Add missing trigger phrases to description | Trivial |
| Content deferral | Move detailed content from SKILL.md to references | Low-Medium |
| Voice correction | Fix second-person or first-person to imperative | Low |
| Dead reference cleanup | Remove references to non-existent files | Trivial |
| Script extraction | Create script for repeated code blocks | Medium |
| Feature addition | Add capability users naturally expect | Medium-High |
| Structural refactor | Reorganize skill directory and content flow | High |

---

## Audit Calibration

Known false-positive patterns that look like violations but are not:

**D2 (allowed-tools absent):** Omitting `allowed-tools` is valid when the skill genuinely
needs unrestricted access. Flag only when scope is clearly narrower than "everything."

**D4 (Task/Skill in prose):** Mentioning Task or Skill in instructional prose ("use Task
to spawn a subagent") is not a violation of the agentic split. The violation is routing
guidance in the body, not tool references.

**D5 (orientation sections):** A brief "Goal" or "Philosophy" section (under 5 lines) at
the top of SKILL.md is not verbosity; it grounds the skill's purpose. Only flag if it
exceeds ~100 words or duplicates the description.

**Reference file size:** Large reference files (500+ lines) are acceptable if they include
a TOC. The progressive disclosure principle applies to SKILL.md size, not reference file size.
