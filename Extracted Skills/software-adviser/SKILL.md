---
name: software-adviser
description: >
  Research, evaluate, and recommend software tools with structured comparison tables and
  downloadable markdown files. Use this skill whenever the user asks to find, compare,
  recommend, evaluate, or research software, apps, tools, programs, utilities, or
  extensions for any platform. Also trigger when the user asks "what are alternatives to
  X," "what is the best tool for Y," "recommend software for Z," mentions a software
  category and wants options, asks for a replacement or upgrade for an existing tool,
  or says anything like "I need a tool that can..." Even if the user just names a
  software product and says "alternatives" or "competitors," use this skill. Trigger on
  keywords: software, app, tool, program, utility, extension, plugin, alternative,
  replacement, recommend, compare, evaluate, "best for," "what should I use," review,
  winget, install. Do NOT use for questions about how to USE software the user already
  has (that is support, not research).
---

# Software Adviser

Research and recommend software tools using structured comparison tables, web search
verification, and downloadable markdown deliverables.

## Context

The user is the director of ADF Haiti, a small Haitian-led nonprofit (10-12 staff).
Operations run on a Dell XPS 8950 (Windows 11, i7-12700, 16GB DDR5, 256GB SSD with
limited free space). The organization is budget-conscious and sells data collection,
GIS, and evaluation services to fund community development work.

### Current software stack (do not recommend tools the user already has)

- Power BI Desktop
- ArcGIS / ESRI tools
- R Statistics
- Zotero (citation/reference management)
- Roam Research, Typora (markdown note-taking)
- Microsoft 365 (Edge, Outlook, OneDrive, Office)
- Claude desktop app
- Fulcrum (mobile data collection)
- GitHub Desktop
- UniGetUI / winget (package management)
- PowerToys
- Camtasia (screen recording)

### Pricing preference hierarchy (apply this ranking to every recommendation)

1. **Free / Open Source**: always preferred when it meets functional requirements
2. **One-time / perpetual license**: strongly preferred over subscriptions
3. **Freemium with useful free tier**: acceptable if the free tier covers core needs
4. **Subscription with nonprofit discount**: acceptable only if no perpetual option exists; always note the discount availability and amount
5. **Full subscription**: list only if it is clearly the best-in-class tool with no comparable perpetual alternative; flag the ongoing cost prominently

When a subscription-only tool is included, explicitly state: "No perpetual license available" in the Pricing column.

### Platform requirements

- **Primary platform**: Windows 11 (x64)
- Note cross-platform support when available (macOS, Linux, iOS, Android, Web)
- Portable / no-install options are a plus for the constrained SSD
- winget availability is a plus; include `winget install <id>` when the package exists

## Workflow

### Step 1: Parse the request

Extract from the user's message:
- Software category or problem to solve
- Specific requirements or features mentioned
- Any budget constraints beyond the defaults
- Whether they are looking for alternatives to a named tool
- Whether a previous tool was evaluated and rejected (check memory and chat history)

If the user provides a `{{SOFTWARE_CATEGORY}}` and `{{USER_REQUIREMENTS}}` template
(from the project's system prompt), use those directly.

### Step 2: Research

Perform 3-6 targeted web searches. Search strategy:
1. Broad category search: `best [category] software Windows 2025 2026`
2. Per-candidate searches for pricing and current version: `[software name] pricing perpetual license 2026`
3. If the user named a specific tool to replace: `[tool name] alternative 2025 2026`

Prioritize sources in this order:
1. Official product homepages (pricing pages, feature lists)
2. Reputable review aggregators: G2, Capterra, AlternativeTo, TrustRadius
3. Tech journalism: TechRadar, PCMag, Wirecutter
4. Community sources: Reddit, Stack Overflow (for niche/developer tools)

Reject any candidate that:
- Has not been updated since 2023
- Has fewer than ~50 user reviews across major platforms (unless it is a niche open-source tool with active GitHub commits)
- Is primarily a mobile-only app with no desktop or web version

### Step 3: Select 3-5 candidates

Choose 3-5 options that best match the user's requirements. Ensure diversity:
- Include at least one free/open-source option if any credible one exists
- Include at least one perpetual-license option if any exists
- If all viable options are subscription-only, state this explicitly

### Step 4: Build the comparison table

Use this exact table structure in the output markdown file:

```markdown
# [Category Name] Software Comparison

**Category:** [Short description of what this category does]
**Date:** [Current date]
**Platform:** Windows 11 (Dell XPS 8950)

| Software | Platform | Pricing | Key Features | Reviews | Homepage |
|----------|----------|---------|--------------|---------|----------|
| **[Name]** | [Platforms] | [Model + price] | [3-5 bullet features] | [Link] | [Link] |
```

Column guidelines:
- **Software**: Bold the name. Include developer in parentheses for lesser-known tools.
- **Platform**: List OS support. Use abbreviations: Win, macOS, Linux, Web, iOS, Android.
- **Pricing**: State the model AND the price. Examples: "Free, Open Source (MIT)," "One-time $79," "Freemium (free tier: 3 projects)," "$12/mo (no perpetual option)." Flag nonprofit discounts.
- **Key Features**: 3-5 features most relevant to the user's stated requirements. Sentence fragments, comma-separated.
- **Reviews**: Link to AlternativeTo page (default), G2, or Capterra. Format: `[AlternativeTo](url)`.
- **Homepage**: Link to official site or GitHub. Format: `[Homepage](url)`.

### Step 5: Write the summary

After the table, write a 2-4 sentence summary that:
1. Names the top recommendation with a clear reason
2. States when each alternative would be the better pick (use-case differentiation)
3. Mentions the winget install command for the top pick if available

Do NOT pad with caveats, disclaimers, or generic advice. Be direct.

### Step 6: Deliver

1. Save the complete markdown file to `/mnt/user-data/outputs/[category-slug]-comparison.md`
2. Use `present_files` to deliver it
3. After the file link, provide a 1-2 sentence verbal summary with the top pick and install method

## Output quality checklist

Before delivering, verify:
- [ ] Every price is current (verified via web search, not from training data)
- [ ] Every URL resolves to a real page (do not fabricate URLs)
- [ ] No recommended tool duplicates something already in the user's stack
- [ ] At least one free or perpetual-license option is included (or absence is explained)
- [ ] The file is saved to `/mnt/user-data/outputs/` and presented via `present_files`
- [ ] No em dashes used anywhere (use colons, semicolons, or parentheses)
- [ ] Summary names a clear winner, not a wishy-washy "it depends"

## Handling edge cases

**User asks about a tool they already use**: Do not recommend it again. Instead, confirm
they already have it and ask if they want alternatives or complementary tools.

**User asks about a previously rejected tool**: Check memory for tools like Rocket Money,
Monarch Money, or others flagged as "evaluated and rejected." Do not re-recommend them
unless the user explicitly asks for a second look.

**Category has no good free/perpetual options**: State this upfront. Still rank
subscription options by value, and note any that offer annual billing discounts or
nonprofit pricing.

**User provides a very specific or niche request**: If fewer than 3 credible options
exist, present what is available and note the thin market. Do not pad with irrelevant
tools to hit a count.

## Reference

For the full output template with formatting examples, read
`references/output-template.md` in this skill's directory.
