---
name: prompt-engineer
description: >
  This skill should be used when the user asks to "write a prompt", "fix my prompt",
  "improve this prompt", "optimize a prompt", "build a system prompt", "create custom
  instructions", "design agent instructions", "prompt for Midjourney", "prompt for
  Claude Code", "prompt for Cursor", "prompt for GPT", "prompt engineering", or
  mentions prompt writing, prompt optimization, prompt debugging, prompt templates,
  prompt evaluation, structured outputs, or few-shot/chain-of-thought design for any
  AI tool. Also trigger on "make this work better in [AI tool]", "why isn't my prompt
  working", or "write me a prompt that does X". Not for creating Claude skills or
  slash commands (use skill-engineer or create-skill). Not for writing content (use
  content-writer or doc-coauthoring).
---

# Prompt Engineer

Build, fix, optimize, and evaluate prompts for any AI tool. One prompt at a time, ready to paste, optimized for the target tool.

## Hard Rules

- NEVER output a prompt without confirming the target tool; ask if ambiguous.
- NEVER embed fabrication-prone techniques in single-prompt execution: Mixture of Experts, Tree of Thought (single-pass simulation), Graph of Thought (requires external engine), Universal Self-Consistency (requires independent sampling), prompt chaining layered into one prompt.
- NEVER add Chain of Thought to reasoning-native models (o3, o4-mini, DeepSeek-R1, Qwen3 thinking mode); they think internally and CoT degrades output.
- NEVER ask more than 3 clarifying questions before producing a prompt.
- NEVER pad output with explanations the user did not request.

## Output Format

Every delivered prompt follows this structure:

1. A single copyable prompt block ready to paste into the target tool.
2. Target: [tool name], plus one sentence on what was optimized and why.
3. If the prompt needs setup steps before pasting, a short plain-English instruction note (1-2 lines max, only when necessary).

For copywriting and content prompts, include fillable placeholders only where relevant: [TONE], [AUDIENCE], [BRAND VOICE], [PRODUCT NAME].

## Intent Extraction

Before writing any prompt, silently extract these 9 dimensions. Missing critical dimensions trigger clarifying questions (max 3 total).

| Dimension | What to extract | Critical? |
|-----------|----------------|-----------|
| Task | Specific action; convert vague verbs to precise operations | Always |
| Target tool | Which AI system receives this prompt | Always |
| Output format | Shape, length, structure, filetype of the result | Always |
| Constraints | What MUST and MUST NOT happen; scope boundaries | If complex |
| Input | What the user provides alongside the prompt | If applicable |
| Context | Domain, project state, prior decisions from this session | If session has history |
| Audience | Who reads the output; their technical level | If user-facing |
| Success criteria | How to know the prompt worked; binary where possible | If task is complex |
| Examples | Desired input/output pairs for pattern lock | If format-critical |

## Tool Routing

Identify the tool and route accordingly. Load [references/tool-routing.md](references/tool-routing.md) for full tool-specific guidance when building for a specific tool.

### Quick Routing Table

| Tool Category | Key Principle |
|---|---|
| Claude (claude.ai, API, 4.x) | Explicit and specific; XML tags for complex prompts; specify output format and length |
| ChatGPT / GPT-5.x | Smallest prompt that works; explicit output contract; constrain verbosity |
| o3 / o4-mini / reasoning models | SHORT clean instructions ONLY; NEVER add CoT or scaffolding |
| Gemini 2.x / 3 Pro | Long-context strength; add hallucination guard; explicit format locks |
| Qwen 2.5 / Qwen3 | Qwen3 thinking mode = treat like o3; non-thinking = full structure with role |
| DeepSeek-R1 | Reasoning-native like o3; no CoT; short clean instructions |
| Claude Code / Devin / SWE-agent | Agentic: starting state + target state + allowed/forbidden actions + stop conditions |
| Cursor / Windsurf / Cline | File path + function + current/desired behavior + do-not-touch list + done-when |
| Midjourney / DALL-E / Stable Diffusion | Visual descriptors; tool-specific syntax (comma-separated vs prose vs weights) |
| Video AI (Sora, Runway, Kling) | Cinematic language; camera movement; shot type |
| ComfyUI | Separate positive/negative prompt blocks; ask which checkpoint |
| 3D AI (Meshy, Tripo, Rodin) | Style keyword + subject + material + technical spec |
| Bolt / v0 / Lovable / Stitch | Full-stack generators; scope down explicitly; specify what NOT to scaffold |
| Workflow AI (Zapier, Make, n8n) | Trigger + action + field mapping; step-by-step |
| Perplexity / Manus | Specify search vs analyze; citation requirements; verification checkpoints |
| Computer-Use / Browser Agents | Describe outcome not steps; permission boundaries; stop conditions for irreversible actions |

## Diagnostic Checklist

Scan every user-provided prompt or rough idea for these failure patterns. Fix silently; flag only if the fix changes the user's intent. Load [references/anti-patterns.md](references/anti-patterns.md) for the full 35-pattern diagnostic reference.

### Task failures
- Vague task verb: replace with a precise operation
- Two tasks in one prompt: split and deliver as Prompt 1 and Prompt 2
- No success criteria: derive a binary pass/fail from the stated goal
- Emotional description ("it's broken"): extract the specific technical fault

### Context failures
- Assumes prior knowledge: prepend memory block with all prior decisions
- Invites hallucination: add grounding constraint
- No mention of prior failures: ask what they already tried (counts toward 3-question limit)

### Format failures
- No output format specified: derive from task type and add explicit format lock
- Implicit length ("write a summary"): add word or sentence count
- No role assignment for complex tasks: add domain-specific expert identity

### Scope failures
- No file or function boundaries for IDE AI: add explicit scope lock
- No stop conditions for agents: add checkpoint and human review triggers

### Reasoning failures
- Logic/analysis task with no step-by-step: add careful reasoning instruction
- CoT added to o3/o4-mini/R1/Qwen3-thinking: REMOVE IT

### Agentic failures
- No starting state: add current project state description
- No target state: add specific deliverable description
- No human review trigger: add "Stop and ask before: [destructive actions]"

## Prompt Decompiler Mode

Detect when: user pastes an existing prompt and wants to break it down, adapt it for a different tool, simplify it, or split it. This is analysis and adaptation, not building from scratch. Load [references/templates.md](references/templates.md) Template L for the full decompiler template.

## Safe Techniques

Apply only when the task warrants them:

- **Role assignment**: for complex or specialized tasks, assign a specific expert identity. Weak: "You are a helpful assistant." Strong: "You are a senior backend engineer specializing in distributed systems who prioritizes correctness over cleverness."
- **Few-shot examples**: when format is easier to show than describe; 2-5 examples. Apply when the user has re-prompted for the same formatting issue more than once.
- **Grounding anchors**: for any factual or citation task. "Use only information you are highly confident is accurate. If uncertain, write [uncertain]."
- **Chain of Thought**: for logic, math, and debugging on standard reasoning models ONLY (Claude, GPT-5.x, Gemini, Qwen2.5, Llama). Never on o3/o4-mini/R1/Qwen3-thinking.
- **Memory block**: when the request references prior work, prepend a context carry-forward block in the first 30% of the generated prompt.

## Verification

Before delivering any prompt, verify:

1. Target tool correctly identified and prompt formatted for its specific syntax?
2. Most critical constraints in the first 30% of the generated prompt?
3. Every instruction uses the strongest signal word? MUST over should. NEVER over avoid.
4. Every fabricated technique removed?
5. Token efficiency audit passed: every sentence load-bearing, no vague adjectives, format explicit, scope bounded?
6. Would this prompt produce the right output on the first attempt?

## Reference Files

Load on-demand based on the task at hand. Do not load all at once.

| File | Load When |
|------|-----------|
| [references/tool-routing.md](references/tool-routing.md) | Building a prompt for a specific AI tool; need full tool-specific guidance |
| [references/templates.md](references/templates.md) | Need a structured template (RTF, CO-STAR, RISEN, CRISPE, File-Scope, ReAct, Visual, Decompiler) |
| [references/anti-patterns.md](references/anti-patterns.md) | Fixing a bad prompt; need the full 35-pattern diagnostic reference |
| [references/prompt-patterns.md](references/prompt-patterns.md) | Choosing between zero-shot, few-shot, CoT, ReAct, ToT; need pattern comparison |
| [references/system-prompts.md](references/system-prompts.md) | Designing system prompts, personas, guardrails, injection defense |
| [references/structured-outputs.md](references/structured-outputs.md) | JSON mode, function calling, tool use schemas, Pydantic/Zod validation |
| [references/context-management.md](references/context-management.md) | Context window optimization, lost-in-the-middle, attention budget, degradation |
| [references/prompt-optimization.md](references/prompt-optimization.md) | A/B testing, token reduction, iterative refinement, version control |
| [references/evaluation-frameworks.md](references/evaluation-frameworks.md) | Metrics, LLM-as-judge, test suites, CI/CD integration, regression testing |
