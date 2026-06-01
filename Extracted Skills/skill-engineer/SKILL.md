---
name: skill-engineer
description: >
  This skill should be used when the user asks to "create a skill", "make a skill",
  "build a skill", "write a skill", "improve a skill", "make this skill better",
  "fix my skill", "repair this skill", "audit this skill", "review skill quality",
  "check my skill", "optimize the trigger description", "run evals on my skill",
  "test my skill", "package my skill", "what's wrong with this skill",
  "apply the improvement plan", "batch audit my skills", or mentions skill creation,
  skill quality, skill testing, skill packaging, or skill diagnostics.
  Make sure to use this skill whenever the user mentions anything about creating,
  improving, repairing, reviewing, testing, or packaging Claude skills or slash
  commands; even if they don't explicitly say "skill-engineer".
  Not for agents (use repair-agent or create-agent). Not for plugin scaffolding
  (use plugin-structure).
argument-hint: "[create|improve|repair|review|audit|test|package] [path-or-name]"
allowed-tools:
  - Read
  - Glob
  - Grep
  - Edit
  - Write
  - Bash
  - WebSearch
  - WebFetch
  - Task
  - AskUserQuestion
---

# Skill Engineer

Full-lifecycle skill engineering: create, review, improve, repair, test, optimize, audit,
and package Claude skills and slash commands.

## Philosophy

- One skill = one durable job.
- Frontmatter description is the primary trigger surface; treat every token there as budget.
- SKILL.md contains workflow and boundaries only; defer detail to `references/`.
- Never mention files that do not exist. Never inherit stale references without verifying.
- Local environment is the authority; inspect before writing.

## Decision Routing

Parse user intent from their request and `$ARGUMENTS`, then branch:

| User Intent | Branch | Key Reference |
|---|---|---|
| Create a new skill from scratch | [Create](#create) | `references/skill-writing-guide.md` |
| Review quality or score a skill | [Review](#review) | `references/quality-rubric.md` |
| Improve effectiveness of a skill | [Improve](#improve) | `references/quality-rubric.md` (effectiveness section) |
| Fix structural issues in a skill | [Repair](#repair) | `references/skill-writing-guide.md` (anatomy section) |
| Optimize trigger description | [Optimize](#optimize) | `references/description-optimization.md` |
| Run evals or benchmark a skill | [Test](#test) | `references/eval-and-testing.md` |
| Batch audit multiple skills | [Audit](#audit) | `references/quality-rubric.md` |
| Package skill for distribution | [Package](#package) | (none needed) |
| Execute an improvement plan | [Execute Plan](#execute-plan) | `examples/improvement-plan-example.md` |

If intent is ambiguous, use AskUserQuestion with options matching the branches above.

## Reference Loading Table

Load references on-demand, not upfront. Each branch specifies which files to load.

| File | Content | Load When |
|---|---|---|
| `references/skill-writing-guide.md` | Anatomy, progressive disclosure, writing patterns, style rules, frontmatter catalog, directory conventions | Create, Repair |
| `references/quality-rubric.md` | 4-dimension scoring (description 25%, organization 30%, style 20%, integrity 25%), grade mapping, severity framework, effectiveness sub-analyses | Review, Improve, Audit |
| `references/quality-examples.md` | Exemplary and poor skill descriptions, annotated good/bad patterns | Review, Audit |
| `references/eval-and-testing.md` | Test case design, assertion writing, subagent orchestration, benchmark aggregation, schemas | Test |
| `references/description-optimization.md` | Trigger eval queries, optimization loop, train/test split, overfitting prevention | Optimize |
| `references/environment-adaptations.md` | Claude Code vs Cowork vs Claude.ai differences, plugin-specific considerations | Any (when env context needed) |

---

<a id="create"></a>
## Branch: Create

Load `references/skill-writing-guide.md` before starting.

### Step 1: Gather Requirements

Use AskUserQuestion to collect:
1. Primary objective: what should this skill do?
2. Trigger scenarios: what would a user say to activate it?
3. Inputs/outputs: what does it receive and produce?
4. Complexity: simple (SKILL.md only), standard (+ references), or complex (+ scripts/assets)?
5. Execution needs: isolated context? Delegated to an agent?

Proceed when objective and trigger scenarios are established.

### Step 2: Inspect Environment

Before writing anything:
- Inspect the target directory (or parent directory if creating fresh).
- Check for neighboring skills that overlap.
- Verify which agents, commands, and sibling skills exist locally.
- Identify the operating context (Claude Code, Cowork, or Claude.ai); load
  `references/environment-adaptations.md` if plugin-specific behavior applies.

### Step 3: Initialize

For new skills, run the init script:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/init_skill.py <name> --path <dir> [--resources scripts,references,assets] [--examples]
```

For plugin skills where init is unnecessary, create the directory manually:
`mkdir -p skills/<name>/{references,scripts}` (only directories actually needed).

### Step 4: Write Frontmatter

Apply rules from `references/skill-writing-guide.md` (frontmatter section):
- Third-person trigger description with 3-5 verbatim user phrases.
- Include at least one naive phrasing from a user who has never heard of the skill.
- Add negative triggers ("Not for X") if the skill is in a crowded domain.
- Keep under 150 tokens (200 absolute max).
- Use `>` folded scalar.

### Step 5: Validate Description Discoverability

Before writing the body, mentally generate:
1. 3 should-trigger prompts (realistic user messages including naive phrasings).
2. 3 should-NOT-trigger prompts (adjacent domains that should not activate).

Revise the description until coverage is adequate.

### Step 6: Write Body

- State objective in first sentence.
- Imperative voice throughout ("Analyze", "Generate"); no first-person, no second-person.
- No "When to Use" section in body (routing is in frontmatter; body loads only after trigger).
- No headers deeper than H3; content that granular belongs in `references/`.
- Target 1,500-2,000 words. Absolute max 5,000 words.
- Reference all bundled resources with file paths and usage context.

### Step 7: Write Bundled Resources

Create `scripts/`, `references/`, `examples/`, `assets/` only as needed:
- `scripts/`: deterministic operations that would be rewritten each invocation.
- `references/`: detail deferred from SKILL.md; loaded selectively.
- `examples/`: complete artifacts users copy and adapt.
- `assets/`: output files (templates, images) not loaded into context.

Delete placeholder directories and files not actually used.

### Step 8: Validate and Package

Run `scripts/validate_skill.py <path>` to check structure.
Run quality gates (see [Quality Gates](#quality-gates)).
Optionally package: `scripts/package_skill.py <path> [output-dir]`.

---

<a id="review"></a>
## Branch: Review

Load `references/quality-rubric.md` and `references/quality-examples.md`.

Three review modes:

1. **score-only**: fast first-pass grading for one skill.
2. **structural-audit**: deep 7-dimension structural inspection (frontmatter quality,
   execution modifiers, instruction style, agentic split, verbosity, workflow clarity,
   anatomy completeness).
3. **effectiveness-audit**: deep 5-sub-analysis effectiveness inspection (mental simulation,
   doc validation, feature adjacency, UX flow, edge cases).

Default to score-only unless the user asks for a deep review or uses words like "audit",
"what's wrong", or "thorough review".

### Score-Only Workflow

1. Load the skill directory. Verify SKILL.md exists.
2. Parse YAML frontmatter.
3. Score across 4 dimensions (description 25%, organization 30%, style 20%, integrity 25%).
4. Compute weighted total, assign letter grade (A-F).
5. List top 3 findings with priority and estimated point impact.
6. Optionally generate `improvement-plan-<name>.md` if score < B.

### Structural Audit

Run all 7 dimensions from the rubric. For each finding record: dimension code, what is
wrong or missing, which principle it violates, severity (critical/major/minor), and the
specific change required. Output a structured improvement plan.

### Effectiveness Audit

Run all 5 sub-analyses. For each finding: what the issue is, why it reduces effectiveness,
the concrete improvement, and severity/effort calibration. Output a prioritized improvement
list ranked by value/effort ratio.

---

<a id="improve"></a>
## Branch: Improve

Load `references/quality-rubric.md` (effectiveness section).

### Step 1: Understand User Intent

Use AskUserQuestion: "What specifically does this skill not do well?" Offer options:
- A specific gap they've noticed
- "Run a full effectiveness audit"
- "It works but I want new capabilities"
- "The workflow feels clunky"

### Step 2: Run Effectiveness Analysis

Execute the 5 sub-analyses from the rubric:
- **Mental simulation**: walk through the skill with a concrete representative request.
- **Doc validation**: verify every referenced file exists, every script runs, no dead links.
- **Feature adjacency**: identify capabilities users would naturally expect but are missing.
- **UX flow**: trace the user experience; flag clunky handoffs, excessive questions, unclear output.
- **Edge cases**: identify inputs that would break or confuse the workflow.

### Step 3: Rank and Present Findings

Rank findings by value/effort ratio. Present as a table: finding, severity, effort,
recommended change. Get user confirmation before applying changes.

### Step 4: Apply Changes

Apply confirmed improvements using Edit/Write tools. Run quality gates after changes.

---

<a id="repair"></a>
## Branch: Repair

Load `references/skill-writing-guide.md`.

Quick structural fix workflow for broken or malformed skills:

1. Load skill directory; catalog what exists.
2. Parse YAML frontmatter; fix syntax errors.
3. Check: description is third-person with trigger phrases? Fix if not.
4. Check: all referenced files exist? Remove dead references or create missing files.
5. Check: SKILL.md size appropriate? Defer excess content to `references/`.
6. Check: imperative voice throughout? Fix second-person/first-person instances.
7. Check: no H4+ headers? Refactor deep nesting into reference files.
8. Run quality gates.
9. Report changes made.

For deep structural analysis, redirect to [Review (structural-audit)](#review).

---

<a id="optimize"></a>
## Branch: Optimize

Load `references/description-optimization.md`.

Iterative loop to improve a skill's trigger description using automated evaluation:

1. Load or create an eval set (should-trigger and should-not-trigger queries).
   Use `assets/eval_review.html` for interactive editing if in a browser environment.
2. Run baseline eval: `scripts/run_eval.py --skill-path <path> --eval-set <file>`.
3. Start optimization loop: `scripts/run_loop.py --skill-path <path> --eval-set <file>
   --max-iterations <N>`. (Internally calls `scripts/improve_description.py` per iteration.)
4. Review results in the generated HTML report or via `eval-viewer/generate_review.py`
   (which embeds `eval-viewer/viewer.html` as the interactive template).
5. Present the best description to the user before applying.

---

<a id="test"></a>
## Branch: Test

Load `references/eval-and-testing.md`.

### Design Test Cases

For each eval, define: a user prompt, expected behavior (assertions), and whether the
skill should trigger. Write assertions while runs are in progress (not after seeing results).

### Run Evals

Execute test cases using subagents. Two configurations per eval:
- **with-skill**: skill installed and active.
- **without-skill** (or old-skill): baseline for comparison.

### Grade and Benchmark

Use `agents/grader.md` to evaluate assertions against execution transcripts.
Use `scripts/aggregate_benchmark.py` to compute summary statistics.
Use `eval-viewer/generate_review.py` to generate an interactive review page.

Present results to the user BEFORE the model self-evaluates. Human judgment comes first.

Use `scripts/generate_report.py` to create an HTML optimization report from loop results.
See `examples/sample-analysis.md` for an annotated example of effectiveness analysis output.

### Blind Comparison (optional)

Use `agents/comparator.md` for blind A/B comparison between skill versions.
Use `agents/analyzer.md` to extract actionable insights from comparison results.

---

<a id="audit"></a>
## Branch: Audit

Load `references/quality-rubric.md` and `references/quality-examples.md`.

Batch portfolio review of multiple skills:

1. Discover skills: `scripts/skill-audit.py <directory>` to scan and inventory.
2. Score each skill using the score-only workflow.
3. Cluster repeated issues across the portfolio.
4. Produce a prioritized shortlist: which skills to fix first, which issues are systemic.
5. Optionally generate improvement plans for the lowest-scoring skills.

---

<a id="execute-plan"></a>
## Branch: Execute Plan

Apply an improvement plan generated by the Review or Improve branches.

1. Load the `improvement-plan-<name>.md` file. Validate it has priority sections.
2. Parse improvement items; group changes by target file.
3. Detect conflicts (multiple changes to same content). Resolution: high priority wins;
   same priority preserves first change; flag unresolvable conflicts for user review.
4. Sort by priority (High → Medium → Low).
5. Backup original files: `scripts/backup-skill.sh <skill-dir>`.
6. Apply changes using Edit/Write tools, one file at a time.
7. Verify results: `scripts/verify-update.sh <skill-dir>`.
8. Generate update report. See `examples/update-report-example.md` for format.

---

<a id="package"></a>
## Branch: Package

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/package_skill.py <path/to/skill> [output-dir]
```

The script validates the skill first, then creates a distributable `.skill` zip.
Plugin skills do not need packaging (distributed as part of the plugin).

**Shared utilities:** `scripts/utils.py` provides `parse_skill_md()` used by other scripts.

---

<a id="quality-gates"></a>
## Quality Gates

Run before closing any skill-engineering session:

1. **YAML parse**: frontmatter parses without error.
2. **Dead reference scan**: every file referenced in SKILL.md exists in the directory.
3. **Orphan scan**: every file in the directory is referenced or has a clear purpose.
4. **Word count check**: SKILL.md body under 5,000 words (target 1,500-2,000).
5. **Voice check**: no second-person ("you"), no first-person ("I will"), imperative throughout.
6. **Header depth**: no H4+ in SKILL.md.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/validate_skill.py <path>
```

If issues found, fix them before reporting completion.

---

## Environment Awareness

Three operating contexts affect available capabilities:

| Context | Subagents | Browser | File Tools | Shell |
|---|---|---|---|---|
| Claude Code | Yes | No | Yes | Yes |
| Cowork | Yes | No | Yes | Yes (sandbox) |
| Claude.ai | No | No | No | No |

Load `references/environment-adaptations.md` for context-specific workflow adjustments
(e.g., --static mode for eval viewer in Cowork, manual eval in Claude.ai).
