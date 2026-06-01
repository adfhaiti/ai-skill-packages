# Description Optimization

Trigger eval queries, the optimization loop, train/test split, and overfitting prevention.
Load when optimizing a skill's trigger description.

---

## Overview

The optimization loop iteratively improves a skill's frontmatter description by testing
whether it causes Claude to trigger on a set of eval queries, then using Claude to improve
the description based on failures.

## Eval Set Design

An eval set contains queries labeled as should-trigger or should-not-trigger:

```json
{
  "skill_name": "my-skill",
  "queries": [
    { "text": "create a hook for me", "should_trigger": true },
    { "text": "help me write a Python script", "should_trigger": false }
  ]
}
```

### Query Guidelines

- 10-20 queries minimum for reliable signal
- Balance: ~60% should-trigger, ~40% should-not-trigger
- Include naive phrasings, technical phrasings, and edge cases
- Include queries from adjacent skill domains (should NOT trigger)
- Use `assets/eval_review.html` for interactive editing

## Running the Optimization Loop

```bash
python3 scripts/run_loop.py \
  --skill-path <path-to-skill> \
  --eval-set <path-to-eval-set.json> \
  --max-iterations 10 \
  --trigger-threshold 0.9
```

### How It Works

1. Split eval set into train (70%) and test (30%) using stratified holdout
2. Run baseline evaluation on train set
3. Use Claude to improve description based on train failures
4. Evaluate improved description on train set
5. Repeat until threshold met or max iterations reached
6. Select best description by TEST score (not train score)

### Train/Test Split

The test set is hidden from the improvement model. This prevents overfitting:
descriptions that score well on train but poorly on test are rejected. The best
description is selected by test performance.

### Overfitting Prevention

- Never show test results to the improvement model
- Track history of previous attempts to prevent repetition
- Enforce 1024-character hard limit with fallback rewrite if exceeded
- If train score improves but test score degrades, stop iterating

## Standalone Evaluation

To evaluate a description without improving it:

```bash
python3 scripts/run_eval.py \
  --skill-path <path-to-skill> \
  --eval-set <path-to-eval-set.json>
```

Returns trigger rates and pass/fail status for each query.