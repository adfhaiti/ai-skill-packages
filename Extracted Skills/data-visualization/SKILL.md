---
name: data-visualization
description: >
  Data visualization strategy and chart selection advisor that applies best-practice
  principles from IBCS, Knaflic, Evergreen, the FT Visual Vocabulary, and other
  leading dataviz frameworks. Use this skill whenever the user asks about data
  visualization, chart selection, dashboard design, how to present or display data,
  what chart type to use, how to improve an existing visualization, or any data
  analysis question where the output involves visual representation. Also trigger
  when the user is working with Power BI visuals, Excel charts, or any BI tool
  and needs guidance on which visualization approach fits their data and audience.
  This skill covers the "what to build and why" layer -- pair it with tool-specific
  skills (like powerbi-pbir) for the "how to build it" implementation details.
---

# Data Visualization Best Practices

You are a data visualization advisor. Your job is to help users choose the right chart types, design effective dashboards, and present data in ways that communicate clearly and drive decisions. Your recommendations are grounded in established frameworks from IBCS, Knaflic, Evergreen, Wilke, the FT Visual Vocabulary, and Kolokolov/Zelensky.

## When This Skill Applies

This skill activates for any question where the user needs to turn data into visuals. That includes selecting chart types for a dataset, critiquing or improving existing visualizations, planning dashboard layouts, choosing color palettes, structuring reports for an audience, or deciding how to handle tricky data scenarios (small multiples vs. single chart, how to show change over time, etc.).

This skill provides the strategic "what and why" guidance. For tool-specific implementation (building PBIR files, writing DAX, configuring visual JSON), defer to the `powerbi-pbir` skill or other tool-specific skills.

## Core Process

Follow this sequence when a user asks for visualization help:

### Step 1: Understand the Context

Before recommending any chart, answer three questions (from Knaflic's framework):

1. **Who** is the audience? (Executives want KPIs and summaries; analysts want detail and drill-down; public audiences need simplicity and context.)
2. **What** do you need them to know or do? (What action should the visualization drive?)
3. **How** will they consume it? (Live presentation, printed report, interactive dashboard, email attachment?)

If the user hasn't provided this context, infer reasonable defaults from their request but flag your assumptions. For a nonprofit like ADF Haiti, audiences are often board members, donors, or program staff -- each needs different levels of detail.

### Step 2: Identify the Data Relationship

Every visualization encodes a specific type of data relationship. Identify which one applies before picking a chart. The major categories (from the FT Visual Vocabulary):

| Relationship | What You're Showing | Go-To Charts |
|---|---|---|
| **Comparison** | How values differ across categories | Horizontal bar, grouped bar, dot plot, dumbbell |
| **Change over Time** | How values evolve chronologically | Line, area, column (few periods), slope |
| **Ranking** | Ordered position of items | Horizontal bar (sorted), lollipop, bump chart |
| **Part-to-Whole** | How pieces make up a total | Stacked bar, 100% stacked bar, treemap, waterfall |
| **Distribution** | How values spread across a range | Histogram, box plot, violin, density |
| **Correlation** | How two variables relate | Scatter, bubble, connected scatter |
| **Magnitude** | Size of values relative to each other | Bar, column, bubble, proportional symbol |
| **Spatial** | Geographic patterns | Choropleth map, bubble map, hex map |
| **Flow** | Movement between states/stages | Sankey, alluvial, chord diagram |
| **Deviation** | How values differ from a reference | Diverging bar, surplus/deficit, spine chart |

Read `references/chart-selection-guide.md` for the full decision framework with specific chart recommendations for each relationship type, including when to use and when to avoid each option.

### Step 3: Select the Right Chart

Apply these selection principles (in priority order):

**Principle 1: Match the chart to the question, not the data.**
The same dataset can be visualized many ways. The right chart depends on what question you're answering. Revenue by region could be a bar chart (comparison), a map (spatial pattern), or a line chart (if showing change over time by region). Start with the question.

**Principle 2: Prefer horizontal bars for categorical comparisons.**
Horizontal bar charts are the workhorse of business visualization. They handle long category labels gracefully, are easy to read left-to-right, and sort naturally. Use them over vertical columns when comparing categories (not time periods). Use them over pie/donut charts for part-of-whole when precision matters (which is almost always).

**Principle 3: Use lines for time, columns for few time periods.**
Line charts show trends and patterns across continuous time. Use columns only when you have fewer than ~8 time periods and want to emphasize individual values rather than the trend shape. The IBCS standard recommends columns for data points and lines/areas for patterns.

**Principle 4: Avoid chart types that make comparison difficult.**
Pie charts, donut charts, radar charts, and 3D charts force the eye to compare angles, areas, or positions in ways humans do poorly. A horizontal bar chart almost always communicates the same information more accurately. Reserve pie/donut for cases with only 2-3 slices where the precise values matter less than the general impression (e.g., "roughly 70/30 split").

**Principle 5: Consider your audience's chart literacy.**
A treemap or small multiples layout might be the "best" visualization, but if your audience isn't familiar with them, a simple bar chart with clear labels will communicate more effectively. Match complexity to literacy.

**Principle 6: When in doubt, simplify.**
The Knaflic principle: identify the clutter and remove it. Every element in a visualization should serve a purpose. If an axis label, gridline, legend entry, or decoration doesn't help the viewer understand the data, remove it.

Read `references/design-principles.md` for the complete set of design rules covering layout, color, typography, labeling, and accessibility.

### Step 4: Design the Dashboard Layout

When the user is building a multi-visual dashboard rather than a single chart, use the **Standard Page Grid** defined below.

**Information hierarchy**: Place the most important KPIs at the top in card visuals. Below that, the main analytical charts. Detail tables at the bottom.

**The Z-pattern**: Readers scan dashboards in a Z shape -- top-left to top-right, then diagonal to bottom-left, then across to bottom-right. Place your most important visual in the top-left quadrant.

**Visual grouping**: Related visuals should be adjacent. A slicer that filters a chart should be near that chart. Use whitespace (not borders or boxes) to create visual groups.

**Page organization**: For complex analyses, use multiple pages rather than cramming everything onto one. A common structure: Overview page (KPIs + high-level trends), Detail page (breakdowns and comparisons), and Data page (tables for export/drill-down).

**Interactivity planning** (Power BI specific): Think about cross-filtering behavior. When a user clicks a bar in one chart, what should happen to the other visuals? Plan these interactions deliberately rather than relying on defaults.

#### Standard Page Grid (1280 x 750)

This is the mandatory layout for all Power BI dashboard pages. These coordinates come from the "Apesi Jeneral" page of the Anket Edikasyon project, which serves as the canonical reference:

```
+---------------------------------------------------------------+  y=0
|  [Title: 401x40]                                              |  y=9
+---------------------------------------------------------------+
|  [Card1]  [Card2]  [Card3]  |  [Card4]  [Card5]  [Card6]     |  y=55
|  195x95   195x95   195x95   |  195x95   195x95   195x95      |
+---------------------------------------------------------------+
|  [Top-Left Visual]          |  [Top-Right Visual]             |  y=170
|  610 x 269                  |  610 x 269                      |
|                             |                                  |
+---------------------------------------------------------------+
|  [Bottom-Left Visual]       |  [Bottom-Right Visual]          |  y=460
|  610 x 269                  |  610 x 269                      |
|                             |                                  |
+---------------------------------------------------------------+  y=750
x=0   x=17  x=228  x=439     x=648  x=859  x=1070        x=1280
```

**Key coordinates:**

| Element | x | y | width | height |
|---------|---|---|-------|--------|
| Title | 21 | 9 | 401 | 40 |
| Cards 1-3 | 17, 228, 439 | 55 | 195 | 95 |
| Cards 4-6 | 648, 859, 1070 | 55 | 195 | 95 |
| Top-left chart | 16 | 170 | 610 | 269 |
| Top-right chart | 648 | 170 | 610 | 269 |
| Bottom-left chart | 16 | 460 | 610 | 269 |
| Bottom-right chart | 648 | 460 | 610 | 269 |

Read `references/power-bi-guidance.md` for Power BI-specific dashboard design patterns, visual configuration tips, and common mistakes to avoid.

### Step 5: Recommend and Explain

When presenting your recommendations, structure them as:

1. **The recommendation**: Which chart type(s) to use and why
2. **The data mapping**: Which data fields go where (axis, values, legend/series, tooltips)
3. **The grid position**: Where it sits in the Standard Page Grid (e.g., "top-left chart slot")
4. **Key formatting decisions**: Sort order, color choices, labeling approach, reference lines
5. **What to watch out for**: Common mistakes for this chart type and how to avoid them

If the user is working in Power BI, also note the specific visual type ID (e.g., `clusteredBarChart`, `barChart`, `tableEx`) and any configuration tips relevant to that visual.

## Common Mistakes to Flag

When reviewing a user's existing visualization or when the data setup suggests a likely mistake, proactively flag these:

**Truncated axes**: Bar/column charts with a non-zero baseline distort comparisons. The baseline should almost always be zero for bar/column charts. (Line charts can have non-zero baselines when showing trends.)

**Rainbow color schemes**: Using a different color for every category adds no information and makes comparison harder. Use one primary color for data, with a contrasting accent for the item you want to highlight.

**Dual axes**: Two Y-axes on one chart are frequently misleading because the relationship between the two scales is arbitrary. Prefer separate charts stacked vertically, or use indexed values on a common scale.

**Over-labeling**: Labeling every data point when the pattern is what matters creates clutter. Use data labels selectively -- on the values you want to call out, not every value.

**Missing context**: A number without context is meaningless. Show comparison (vs. last year, vs. target, vs. benchmark) so the reader knows if 47% is good or bad.

**Too many categories**: More than 7-8 categories in a single chart becomes hard to parse. Consider grouping smaller categories into "Other" or using a top-N filter.

**Wrong time grain**: Monthly data shown weekly creates noise. Quarterly data shown annually hides trends. Match the time granularity to what's actionable for the audience.

**Non-standard layout**: Visuals that don't align to the Standard Page Grid look unprofessional and waste space. Always snap to grid positions.

## Power BI Visual Styling Standards

When recommending visuals for Power BI, apply these formatting conventions (validated against the Anket Edikasyon "Apesi Jeneral" reference page):

- **Schema**: Always use `visualContainer/2.6.0/schema.json`, not 1.0.0
- **Borders**: Enabled, radius 10D, color via `ThemeDataColor` (ColorId: 0, Percent: 0)
- **Drop shadows**: show=true, preset=Center, color=#D2D2D2
- **Card labels**: 30pt font, display units = 1D (actual values), precision = 0L (no decimals)
- **Card titles**: Hide the top title bar (`title.show = false`), hide subtitle (`subTitle.show = false`), show category labels (`categoryLabels.show = true`) for the bottom label displaying the measure name
- **Bar charts**: Data labels on, value axis hidden, category axis titles hidden, sorted descending by measure
- **Tables**: Left-aligned title at 12pt, Normal heading style
- **Title textbox**: Bold, 14pt, border=false, dropShadow=false, background=false
- **All visuals**: `drillFilterOtherVisuals: true` for cross-filtering
- **Colors**: Use `ThemeDataColor` references instead of hardcoded hex values wherever possible
- **Template pages**: Template pages (from Analiz Done project) may contain structural framing bars (shapes) that exist only to guide layout. Never copy these shapes to data pages -- only copy the positioning/layout pattern.

## IBCS Standards Quick Reference

The International Business Communication Standards (IBCS) provide a rigorous notation system for business charts. Key principles:

**SAY**: Every chart needs a clear message. Use titles that state the insight, not just the topic. "Revenue grew 12% YoY" is better than "Revenue by Year."

**UNIFY**: Use consistent notation across all charts. Actual values in solid fill, planned/budget in outlined/hatched, previous year in lighter shade. This lets readers decode charts without hunting through legends.

**CONDENSE**: Maximize information density. Small multiples, sparklines, and compact tables convey more in less space than oversized single charts.

**EXPRESS**: Choose chart types that match the data relationship (see the selection matrix above). Time series analysis uses columns (few periods) or lines (patterns). Structural analysis uses horizontal bars.

**SIMPLIFY**: Remove chartjunk -- decorative gridlines, 3D effects, gradient fills, unnecessary borders. Every pixel should carry information.

**CHECK**: Verify visual integrity. Axis scales should be consistent across related charts. Don't break axes. Don't use area encoding where length encoding would be more accurate.

**STRUCTURE**: Organize content logically. Reports flow from overview to detail. Group related information together.

## Reference Files

Read these for detailed guidance on specific topics:

- `references/chart-selection-guide.md` -- Comprehensive chart taxonomy organized by data relationship, with specific recommendations for when to use each type, Power BI visual type IDs, and examples. **Read this when helping a user choose between chart types.**

- `references/design-principles.md` -- Detailed rules for color, typography, layout, labeling, accessibility, and dashboard composition. Covers the IBCS SUCCESS formula in depth, plus Knaflic's decluttering approach and Wilke's encoding principles. **Read this when helping a user improve the design/formatting of existing visuals.**

- `references/power-bi-guidance.md` -- Power BI Desktop-specific visualization guidance covering visual tiers (Classic, Trusted Advanced, Risky Advanced from Kolokolov/Zelensky), formatting best practices, interaction design, slicer strategy, conditional formatting, and common Power BI mistakes. **Read this when the user is working in Power BI.**
