# Eval and Testing Guide

Test case design, assertion writing, subagent orchestration, benchmark aggregation,
and data schemas. Load when testing skills or running the eval framework.

---

## Test Case Design

### Structure of an Eval

Each eval consists of:
- **prompt**: a realistic user message that exercises the skill
- **expectations**: assertions about what the skill should produce
- **should_trigger**: boolean; whether the skill should activate for this prompt

### Writing Good Prompts

- Use realistic user language, not idealized inputs
- Include at least one naive phrasing per eval set
- Test the main workflow path first, then edge cases
- Include negative cases (prompts that should NOT trigger the skill)

### Writing Assertions

Write assertions BEFORE seeing results (prevents confirmation bias). Each assertion:
- Tests one specific behavior
- Is falsifiable (can clearly pass or fail)
- References observable output (file created, content contains X, tool was called)
- Avoids subjective quality judgments

Good: "Output file contains a YAML frontmatter block with name and description fields"
Bad: "Output is high quality and well-written"

---

## Eval Execution

### Two-Configuration Testing

For each eval, run two configurations:
1. **with-skill**: skill installed and active
2. **baseline**: skill not installed (or old version for comparison)

This isolates the skill's contribution from Claude's baseline capabilities.

### Subagent Orchestration

Run evals as subagents to isolate execution:

```
For each eval in eval_set:
  For each config in [with-skill, baseline]:
    Spawn subagent with config
    Record: prompt, transcript, outputs, timing, token usage
    Grade assertions against transcript and outputs
```

Use `agents/grader.md` for assertion evaluation. The grader:
- Reads the execution transcript
- Examines output files
- Evaluates each assertion with specific evidence
- Extracts implicit claims for verification
- Critiques the evals themselves (identifies weak assertions)

### Timing

Capture wall-clock time for each run. Store in timing.json:
```json
{
  "wall_clock_seconds": 45.2,
  "started_at": "2025-01-15T10:30:00Z",
  "ended_at": "2025-01-15T10:30:45Z"
}
```

---

## Benchmark Aggregation

After multiple runs, aggregate results:

```bash
python3 scripts/aggregate_benchmark.py <results-dir>
```

The script:
- Loads grading.json files from run directories
- Calculates mean, stddev, min, max for pass_rate, time_seconds, tokens
- Computes delta between configurations
- Generates benchmark.json and benchmark.md

---

## Interactive Review

### Eval Viewer

Generate an interactive HTML review page:

```bash
python3 eval-viewer/generate_review.py <workspace-dir> [--static]
```

The viewer:
- Shows each test case with prompt, outputs, grades, and feedback area
- Supports prev/next navigation with keyboard shortcuts
- Embeds all output files as data URIs (self-contained HTML)
- Auto-saves feedback to feedback.json
- Use `--static` in Cowork/headless environments (no HTTP server)

Present results to the user BEFORE the model self-evaluates. Human judgment first.

### Eval Set Editor

Use `assets/eval_review.html` to interactively create or edit eval sets:
- Edit query text in textareas
- Toggle "should trigger" per query
- Add/delete queries
- Export as eval_set.json

---

## Blind Comparison

For comparing two skill versions:

1. Run both versions on the same eval set
2. Use `agents/comparator.md` for blind A/B comparison (origin hidden from grader)
3. Use `agents/analyzer.md` to extract actionable insights

The comparator scores on content and structure dimensions independently,
then determines an overall winner with confidence level.

---

## Data Schemas

### evals.json
```json
{
  "skill_name": "string",
  "evals": [
    {
      "name": "string",
      "prompt": "string",
      "expectations": ["string"],
      "should_trigger": true
    }
  ]
}
```

### grading.json
```json
{
  "expectations": [
    {
      "text": "string",
      "passed": true,
      "evidence": "string",
      "confidence": "high|medium|low"
    }
  ],
  "summary": {
    "total": 5,
    "passed": 4,
    "pass_rate": 0.8
  },
  "claims": ["string"],
  "eval_feedback": ["string"]
}
```

### benchmark.json
```json
{
  "metadata": { "skill": "string", "timestamp": "string" },
  "configs": {
    "with_skill": {
      "runs": 3,
      "pass_rate": { "mean": 0.85, "stddev": 0.05 },
      "time_seconds": { "mean": 30, "stddev": 5 }
    }
  },
  "delta": { "pass_rate": 0.15 }
}
```