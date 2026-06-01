# Environment Adaptations

Differences between Claude Code, Cowork, and Claude.ai that affect skill engineering
workflows. Load when environment-specific behavior matters.

---

## Capability Matrix

| Capability | Claude Code | Cowork | Claude.ai |
|---|---|---|---|
| Subagents (Task tool) | Yes | Yes | No |
| File tools (Read/Write/Edit) | Yes | Yes (sandbox) | No |
| Shell (Bash) | Yes | Yes (sandbox) | No |
| Browser | No | No | No |
| MCP tools | Yes | Yes | No |
| Eval scripts | Yes | Yes (sandbox paths differ) | No |

## Claude Code

Full capabilities. All scripts, agents, and eval workflows available.

**Testing skills:** Install with `--plugin-dir` or place in `.claude/skills/`:
```bash
claude --plugin-dir /path/to/plugin
```

**Eval viewer:** Run `eval-viewer/generate_review.py` with HTTP server (default port 3117).
Auto-opens browser.

## Cowork

Subagents available. File tools work in sandbox. Shell runs in isolated Linux environment.

**Key differences:**
- File paths differ between file tools and bash (use path mapping).
- No browser; use `--static` flag for eval viewer to generate standalone HTML.
- Scripts execute in sandbox; install dependencies with `pip install --break-system-packages`.

**Eval viewer:** Use `--static` mode:
```bash
python3 eval-viewer/generate_review.py <workspace> --static
```
Generates self-contained HTML without starting an HTTP server.

## Claude.ai

No subagents, no file tools, no shell. Skill engineering is limited to:

- Reviewing skill content pasted into conversation
- Providing improvement suggestions as text
- Generating SKILL.md content for the user to copy

**Manual eval workflow:**
1. User describes what the skill should do
2. Generate test cases as a list in conversation
3. User tests manually and reports results
4. Iterate on description and content based on feedback

## Plugin-Specific Considerations

Plugin skills live in `plugin-name/skills/skill-name/` and are distributed as part of
the plugin. They do not need separate packaging.

**Auto-discovery:** Claude Code scans `skills/` directory, finds subdirectories containing
SKILL.md, loads metadata automatically, loads body when triggered, loads resources when
needed.

**Testing:** Use `--plugin-dir` flag to test plugins without installation.

**No init script needed:** Plugin skills can be created with a simple `mkdir -p` and
manual SKILL.md creation. The `init_skill.py` script is optional but useful for
generating a complete template.