---
name: todoist-expert
description: >
  Use for any Todoist or task management request. Triggers on: "add a task",
  "clean up Todoist", "organize my tasks", "what's overdue", "task review",
  "weekly review", "plan my week", "inbox zero", "bulk reschedule",
  "delegate a task", "create a filter", "stale tasks", "project structure",
  "set up Todoist", "recurring task", "assign this to [person]", "what's
  due this week", "prioritize my tasks", or any mention of Todoist projects,
  sections, labels, filters, or comments. Not for calendar scheduling,
  project management documents, or Jira/Asana/ClickUp.
---

# Todoist Expert

Manage tasks, projects, labels, filters, and team workflows in Todoist. Covers task creation with natural language parsing, team workspace structure, task hygiene and cleanup, weekly reviews, and workflow optimization for a small nonprofit team (10-12 people, ADF Haiti context).

## Tool Discovery

The Todoist MCP connector is a web-based service at `https://ai.todoist.net/mcp`. Its tools are registered under a dynamic server UUID that varies per installation (pattern: `mcp__<uuid>__<tool-name>`).

**Before using any Todoist tool**, run `ToolSearch` with the query `add-tasks fetch complete-tasks` to discover the server UUID prefix. Cache that prefix for the session.

### Available Tools (27 total)

Core tools confirmed from the official Doist/todoist-mcp registry:

| Short Name | Purpose | Key Parameters |
|------------|---------|----------------|
| `add-tasks` | Create one or more tasks | content, description, due_string, due_date, due_lang, priority, labels, project_id, section_id, assignee_id, parent_id, duration, duration_unit |
| `complete-tasks` | Mark tasks as done | task_id (or search by name) |
| `add-projects` | Create projects | name, parent_id, color, is_favorite, view_style (list or board) |
| `add-sections` | Create sections within a project | name, project_id, order |
| `add-comments` | Add comments to tasks or projects | content, task_id or project_id, attachment |
| `fetch` | Search/list tasks using filter queries | query (Todoist filter string) |
| `fetch-object` | Retrieve a specific object by ID | object_type (task, project, section, label, comment), object_id |
| `delete-object` | Delete a task, project, section, label, or comment | object_type, object_id |
| `search` | OpenAI-compatible search (returns result list) | query string |

Additional tools (19 more) include: task update, label CRUD, project update, section reorder, user info, move tasks, and batch operations. Discover the full set via `ToolSearch` at runtime.

### Connector Status Check

If a Todoist tool call fails or returns an auth error, check connector status:
1. Call `mcp__mcp-registry__search_mcp_registry` with keywords `["todoist"]`
2. If `connected: false`, call `mcp__mcp-registry__suggest_connectors` with the Todoist `directoryUuid` to prompt the user to connect
3. If `connected: true` but tools still fail, the OAuth token may have expired; suggest the user reconnect

### When Todoist MCP Is Unavailable

If tools are not connected, provide manual instructions:
- Direct the user to the Todoist web/desktop app
- Provide exact filter query strings they can paste into the Todoist filter bar
- Generate CSV files for bulk import (see CSV Format section)
- Suggest connecting: direct the user to search for "Todoist" in connector settings and complete the OAuth flow

## Getting Started

On first use with a new workspace, run a diagnostic before making changes:

1. `fetch` all projects (identify structure, naming, empty projects)
2. `fetch` all labels (identify taxonomy, inconsistencies, unused labels)
3. `fetch` tasks per project (flag projects with 50+ active tasks)
4. `fetch` with filter `#Inbox` (flag if > 20 items)
5. List existing filters (identify gaps in views)

Present findings and recommend a configuration plan before executing changes. The workspace owner must confirm structural changes.

### Label Taxonomy Setup

When no label taxonomy exists, recommend this starter set for nonprofit operations:

| Category | Labels | Purpose |
|----------|--------|---------|
| Context | `@office`, `@field`, `@home`, `@phone`, `@online` | Where/how the work happens |
| Energy | `@deep-work`, `@quick-win`, `@low-energy` | Match tasks to capacity |
| Workflow | `@waiting-for`, `@delegated`, `@blocked`, `@someday` | GTD status tracking |
| Type | `@admin`, `@client-work`, `@fundraising`, `@reporting` | Work category |

Confirm with the user before creating labels. Never create duplicates; check the current label list first via `fetch`.

### Project Structure Template

Recommended hierarchy for a 10-12 person nonprofit team:

```
Inbox (default capture)
Personal (per-user private tasks)
--- Workspace Projects ---
Operations/
  Admin & Finance
  IT & Equipment
  HR & Staff
Client Projects/
  [Client Name - Project Name] (one per active engagement)
Programs/
  [Program Name] (community development, training, etc.)
Fundraising/
  Grant Pipeline
  Donor Relations
  Events
Recurring/
  Weekly Routines
  Monthly Routines
  Quarterly Routines
Templates/ (archived project templates for cloning)
```

Shared projects: any project with tasks from 2+ team members. Personal projects: individual routines, professional development, errands. Never mix shared and personal work in one project.

## Task Creation Rules

Apply these rules whenever creating a task via `add-tasks`, whether from explicit instructions or natural language input.

### Natural Language Parsing

Extract from a single sentence: task title, due date, priority, project, labels, assignee, and recurrence.

Example: "Ask Marie to submit the Kellogg report by next Friday p1 @client-work"

Parsed into `add-tasks` parameters:
- `content`: "Submit Kellogg report" (verb-first, concise)
- `assignee_id`: [Marie's user ID; fetch first]
- `due_string`: "next Friday"
- `priority`: 4 (API value for p1)
- `labels`: ["client-work"]
- `project_id`: [inferred from context; fetch to confirm]

### Defaults

| Parameter | Default | Override |
|-----------|---------|---------|
| Priority | p3 (API: 2) | User says "urgent", "important", "p1", "p2", or "p4" |
| Project | Inbox | Move immediately if context makes the project obvious |
| Due date | None | Set when user provides any time reference |
| Labels | None | Apply when task clearly matches a taxonomy label |
| Assignee | None | Set when user names a person or says "assign to" |

### Task Title Rules

- Start with a verb: "Submit", "Review", "Call", "Draft", "Follow up on"
- Max 80 characters; if longer, move detail to the `description` parameter
- No filler: remove "need to", "should", "remember to", "don't forget to"
- Bad: "Remember to follow up with the grant officer about the budget revision"
- Good: "Follow up with grant officer re: budget revision"

### Subtask Creation

Automatically break a task into parent + subtasks when it contains 3+ distinct action steps. Ask before breaking ambiguous tasks. Use `parent_id` in `add-tasks` to create subtask relationships.

### Due Date Handling

All dates use timezone `America/Port-au-Prince` (UTC-5). Pass `due_lang: "en"` for English date parsing.

| User phrase | `due_string` value | Notes |
|-------------|-------------------|-------|
| "tomorrow" | "tomorrow" | Todoist handles natively |
| "next Monday" | "next Monday" | Todoist handles natively |
| "end of week" | "Friday" | Map to Friday |
| "end of month" | "[last day of current month]" | Compute absolute date |
| "in 3 days" | "[absolute date, YYYY-MM-DD]" | Compute from today |
| No date | Omit `due_string` | Do not invent a date |

### Recurring Tasks

| User phrase | `due_string` value |
|-------------|-------------------|
| "every Monday" | "every Monday" |
| "every weekday" | "every weekday" |
| "first of the month" | "every 1st" |
| "every other Friday" | "every other Friday" |
| "every 3 months" | "every 3 months" |
| "after completion, repeat in 2 weeks" | "every! 2 weeks" |

`every!` (with bang): recurrence resets from completion date. `every` (no bang): fixed schedule. If ambiguous, ask the user.

### Priority Mapping

Todoist API uses inverted priority numbers:

| User says | Display | API `priority` value |
|-----------|---------|---------------------|
| p1 (urgent) | Red | 4 |
| p2 (high) | Orange | 3 |
| p3 (medium) | Blue | 2 |
| p4 (low) | None | 1 |

Default: API priority 2 (displays as p3).

## Team Workspace Management

### Section Templates

Client engagement project (use `add-sections` after `add-projects`):

```
Planning → In Progress → Waiting For → Review & QA → Completed
```

Internal operations project:

```
This Week → Upcoming → Recurring → Reference
```

### Task Delegation

When assigning tasks to team members via `add-tasks`:
1. Set `assignee_id` (fetch the team member's ID first)
2. Always include a `due_string` (even if approximate)
3. Add context in `description`: what is expected, reference links, reason for deadline
4. Apply `@delegated` label for the assigner's tracking
5. Optionally create a companion task: "Follow up: [task] (assigned to [person])" with `@waiting-for` label, due 1-2 days before the delegatee's deadline

### Filter Recipes

Build via Todoist filter syntax. Provide these when setting up a workspace:

| Filter name | Query | Purpose |
|-------------|-------|---------|
| My Overdue | `overdue & assigned to: me` | Personal overdue triage |
| Tasks I Assigned | `assigned by: me & !assigned to: me` | Delegation tracking |
| This Week | `(today \| overdue) \| (due before: next Monday)` | Weekly planning |
| Unassigned | `!assigned & !#Inbox` | Tasks needing an owner |
| No Due Date | `no due date & !#Templates & !@someday` | Stale task candidates |
| Quick Wins | `@quick-win & (today \| overdue \| no due date)` | Low-energy batch |
| Waiting For | `@waiting-for` | Follow-up tracking |
| High Priority This Week | `(p1 \| p2) & due before: next Monday` | Escalation view |

Operators: `&` (AND), `|` (OR), `!` (NOT), `#Project` (project), `@label` (label). Parentheses group conditions.

## Task Hygiene and Cleanup

### Stale Task Detection

Use `fetch` with filter `no due date & !@someday` then filter results for tasks not modified in 30+ days.

Present a triage table:

| # | Task | Project | Created | Recommendation |
|---|------|---------|---------|----------------|
| 1 | [name] | [project] | [date] | Reschedule / Complete / Delete / Delegate |

Wait for confirmation. NEVER delete without explicit approval.

### Overdue Task Triage

`fetch` with filter `overdue`, sort by days overdue (oldest first):
- 1-3 days overdue: recommend reschedule to this week
- 4-14 days: reschedule with realistic date or delegate
- 15-30 days: reschedule, delegate, or demote to `@someday`
- 30+ days: complete (if done), delete (if irrelevant), or `@someday`

Support "reschedule all to [date]" for bulk operations.

### Duplicate Detection

Flag tasks with similar titles (>70% similarity) in the same project. Present pairs for decision: merge, keep both, or combine descriptions.

### Inbox Zero Protocol

1. `fetch` with filter `#Inbox`
2. For each task: recommend target project, due date, priority, labels
3. Present as a batch table
4. Execute moves after user confirms

NEVER auto-move without confirmation unless user said "auto-organize" or equivalent.

## Weekly Review

Execute this sequence when requested:

### Step 1: Metrics
- `fetch` total active tasks; `fetch` completed this week; count overdue; count Inbox items

### Step 2: Overdue Triage
Run the overdue protocol above.

### Step 3: Project Scan
For each project: count active tasks, flag 0-task projects (archive candidates) and 50+ task projects (split candidates), list tasks due in next 7 days.

### Step 4: Upcoming Week Preview
`fetch` with filter `7 days`, group by day. Flag overloaded days (5+ tasks) and empty days.

### Step 5: Inbox Processing
Run Inbox Zero if count > 0.

### Step 6: Summary
Present: completed count, overdue resolved, scheduled for next week, open decisions.

## Workflow Diagnosis

When the user asks "how's my Todoist looking" or requests workflow improvement:

| Check | Healthy | Warning | Action |
|-------|---------|---------|--------|
| Inbox | < 10 | > 20 | Run Inbox Zero |
| Overdue | 0-5 | > 15 | Run overdue triage |
| Projects with 50+ tasks | 0 | any | Split or archive |
| Projects with 0 tasks | 0 | > 3 | Archive empties |
| Labels in use | > 3 categories | < 3 | Set up taxonomy |
| Filters defined | > 3 | 0-2 | Create standard set |
| No-date tasks | < 20% | > 50% | Batch-schedule or @someday |

Provide concrete before/after examples, not abstract advice.

### GTD Integration

1. **Capture**: `add-tasks` to Inbox (or Quick Add shortcut Q)
2. **Clarify**: Inbox Zero; rewrite vague tasks as verb-first next actions
3. **Organize**: Move to project, add labels, set priority, assign
4. **Reflect**: Weekly Review; daily Today view check
5. **Engage**: Use filters (Quick Wins, High Priority This Week) to pick next task

## CSV Bulk Import Format

For bulk task creation when MCP is unavailable, generate a CSV:

```csv
TYPE,CONTENT,DESCRIPTION,PRIORITY,INDENT,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE,DURATION,DURATION_UNIT,DEADLINE
task,Submit quarterly report,,1,1,,2026-06-30,en,America/Port_au_Prince,60,minute,
task,Review budget variance,,2,1,,2026-06-15,en,America/Port_au_Prince,,,
section,Finance Tasks,,,,,,,,,,
task,Process reimbursements @admin,,3,1,,every Monday,en,America/Port_au_Prince,30,minute,
```

Priority in CSV: 1 = p1, 2 = p2, 3 = p3, 4 = p4. Indent: 1 = top-level, 2 = subtask.

## Common Operation Sequences

### Create task with full metadata
```
1. fetch → find target project_id
2. add-tasks → content, due_string, priority, labels, project_id, section_id, assignee_id
```

### Bulk reschedule overdue tasks
```
1. fetch → filter "overdue"
2. Present list → get user confirmation
3. Loop: update each task's due_string
```

### Weekly review
```
1. fetch → filter "overdue" (triage)
2. fetch → filter "7 days" (upcoming)
3. fetch → filter "#Inbox" (inbox items)
4. fetch → all projects (scan)
5. Present consolidated review
```

### Inbox zero
```
1. fetch → filter "#Inbox"
2. Present triage recommendations
3. Update each task (project_id, due_string, priority, labels) after confirmation
```

## Constraints

- NEVER delete tasks without explicit user confirmation; always list what will be deleted
- NEVER move tasks between projects without confirmation unless user said "auto-organize"
- NEVER create projects or labels that duplicate existing ones; always check first via `fetch`
- When a Todoist MCP tool is unavailable, explain manual steps; do not fail silently
- All date handling MUST use timezone `America/Port-au-Prince` (UTC-5)
- Confirm fixed vs. completion-based recurrence if ambiguous (`every` vs. `every!`)
- Limit batch operations to 25 tasks per confirmation cycle; paginate larger sets
- Never assume project IDs or assignee IDs; always fetch current data first
- Never fabricate task IDs; always retrieve via `fetch` or `search` before operati