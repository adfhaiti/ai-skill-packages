# Power BI Visualization Guidance

Power BI-specific best practices for visualization, covering visual tiers, formatting, interactivity, slicers, and common mistakes. Based on Kolokolov/Zelensky (2024), Knight et al. (2022), and Sinha (2021).

## Table of Contents
1. [Visual Tiers](#visual-tiers)
2. [Formatting Best Practices](#formatting-best-practices)
3. [Slicer Strategy](#slicer-strategy)
4. [Cross-Filtering and Interactions](#cross-filtering-and-interactions)
5. [Conditional Formatting](#conditional-formatting)
6. [KPI Cards Done Right](#kpi-cards-done-right)
7. [Table and Matrix Design](#table-and-matrix-design)
8. [Common Power BI Mistakes](#common-power-bi-mistakes)
9. [Dashboard Design Checklist](#dashboard-design-checklist)
10. [Visual Type Quick Reference](#visual-type-quick-reference)

---

## Visual Tiers

Kolokolov and Zelensky organize Power BI visuals into three tiers based on reliability and audience familiarity:

### Classic Visuals (Tier 1 -- Use Freely)
These are well-understood, battle-tested, and appropriate for any audience:

- **Column chart** (`clusteredColumnChart`): Time series with few periods
- **Bar chart** (`clusteredBarChart`): Categorical comparison and ranking (horizontal)
- **Line chart** (`lineChart`): Trends over time
- **Table** (`tableEx`): Detailed data display
- **Matrix** (`pivotTable`): Cross-tabulated data with drill-down
- **Card** (`card`): Single KPI display
- **Treemap** (`treemap`): Hierarchical part-of-whole
- **KPI Cards** (`multiRowCard`): Multiple KPI values
- **Slicer** (`slicer`): Interactive filter

These visuals are what 90% of business reports need. Master them before reaching for advanced options.

### Trusted Advanced Visuals (Tier 2 -- Use with Purpose)
These serve specific use cases and have well-established best practices:

- **Funnel chart** (`funnel`): Sequential stage conversion
- **Map** (`map`, `filledMap`): Geographic data
- **Tornado chart**: Comparing two categories back-to-back
- **Waterfall chart** (`waterfallChart`): Bridge/build-up analysis
- **Bullet chart** (custom visual): Actual vs. target with ranges
- **Gantt chart** (custom visual): Project timelines
- **Sankey diagram** (custom visual): Flow between categories
- **Advanced KPI cards**: Multi-target KPIs

Use these when the data relationship specifically calls for them, not just because they look interesting.

### Risky Advanced Visuals (Tier 3 -- Use with Caution)
These can impress but can also confuse. Use only when you're sure the audience can interpret them:

- **Gauge** (`gauge`): Wastes space, consider bullet chart instead
- **Scatterplot** (`scatterChart`): Requires statistical literacy
- **Word cloud** (custom visual): Low analytical value, consider alternatives
- **Decomposition tree** (custom visual): AI-driven drill-down
- **Radar/Aster plot**: Uncommon, hard to read
- **Chord diagram**: Dense flow visualization

The principle: if you have to explain how to read the chart, choose a simpler one.

---

## Formatting Best Practices

### Chart Anatomy (Power BI Specific)

Every Power BI chart has configurable elements. Here's what to adjust:

**Title**: Turn on. Write an insight-driven title (see Design Principles). Set to 12-14pt, left-aligned, bold.

**Legend**: Turn off when possible. Use direct labeling (data labels or text boxes) instead. If you must use a legend, place it at the top of the chart, not to the side (side legends steal chart width).

**Axis labels**: Keep on for orientation. Reduce font size to 9-10pt. Turn off axis title if the chart title already includes the unit/dimension. Turn off axis lines if gridlines provide reference.

**Gridlines**: Use horizontal gridlines only (for column charts) or vertical only (for bar charts). Make them thin and light gray. Remove the other axis's gridlines.

**Data labels**: Use selectively. For bar charts with few bars, label each bar and remove the value axis entirely. For dense charts, skip data labels and rely on the axis.

**Background**: White or transparent. Never use colored backgrounds.

**Borders**: Use subtle rounded borders (10px radius) with the theme primary color to give visuals a polished, cohesive look. When working in PBIR, use `ThemeDataColor` references for border color rather than hardcoded hex values.

**Drop shadows**: Apply a centered drop shadow (#D2D2D2) to all visuals. This gives depth to the dashboard without being heavy-handed. In PBIR, set `visualContainerObjects.dropShadow` with `position: "'Center'"`.

**Visual spacing**: Use whitespace between visuals -- the shadow provides enough visual separation without needing additional borders or dividers.

### Color Configuration

Power BI's default color palette is not bad, but can be improved:

- Assign a consistent color to each key dimension across all pages (e.g., "East Region" is always blue, "West Region" is always orange)
- Use the theme editor (View > Themes > Customize) to set a palette that matches your organization's brand
- For single-series charts, use one color. Reserve multi-color for when color encodes a dimension
- Use conditional formatting to highlight values above/below thresholds rather than manual color assignment

---

## Slicer Strategy

Slicers are Power BI's primary user interaction mechanism. Use them deliberately:

### Slicer Types
- **Dropdown**: Best for dimensions with many values (20+). Compact.
- **List**: Best for dimensions with few values (3-8). All options visible.
- **Between (range)**: Best for dates and numeric ranges.
- **Relative date**: Best for dynamic time filtering ("Last 30 days").

### Placement
- Place slicers at the top or left side of the page, not scattered between charts
- Group all slicers together so users know where to find filters
- If a slicer applies to the whole page, put it in a prominent position
- If a slicer applies to specific visuals only, place it near those visuals and configure interaction settings

### Common Slicer Mistakes
- Too many slicers (more than 4-5 per page overwhelms users)
- No default selection (page loads with all data, which may be too much)
- Slicers that affect each other in confusing ways (cascade carefully)
- Missing "Select All" option for multi-select slicers

---

## Cross-Filtering and Interactions

Power BI's default cross-filtering behavior (clicking a bar in one chart filters all other charts on the page) is powerful but needs deliberate management.

### Edit Interactions
Use Format > Edit Interactions to control how each visual affects others. Options per pair:

- **Filter**: The target visual shows only the filtered data
- **Highlight**: The target visual dims unrelated data but keeps the full context
- **None**: The target visual ignores the interaction

### Best Practices
- KPI cards should usually be set to "Filter" (so they update to show the filtered metric)
- Context charts (overall trend lines) should be set to "Highlight" (so users don't lose the overall pattern)
- Unrelated charts should be set to "None"
- Test every interaction by clicking through the dashboard. Unexpected cross-filtering is the most common complaint from dashboard users

---

## Conditional Formatting

Use conditional formatting to embed analytical value directly into the visual:

### When to Use
- Heatmap coloring in tables/matrices (color scales on numeric columns)
- Icon sets (arrows, traffic lights) for status indicators in tables
- Background color on KPI cards to indicate above/below target
- Font color for positive (green) vs. negative (red) variance values
- Data bars in table cells as inline mini-charts

### When Not to Use
- Don't apply conditional formatting to every column in a table (visual overload)
- Don't use traffic light colors (red/yellow/green) without defining what the thresholds mean
- Don't use conditional formatting as a substitute for a proper chart (if the pattern matters, show a chart)

---

## KPI Cards Done Right

KPI cards are the first thing dashboard users look at. Make them count.

### Essential Elements of a Good KPI Card
1. **The metric value** (large, prominent -- 30pt font)
2. **The metric name** as a bottom category label (clear, unambiguous -- this is the only label needed)
3. **Comparison context** (vs. last period, vs. target, vs. benchmark -- when available)

### Card Styling in PBIR
- Hide the top title bar (`visualContainerObjects.title.show = false`). The title bar is redundant when the category label already names the metric.
- Show the bottom category label (`objects.categoryLabels.show = true`). This displays the measure name below the number.
- Set `nativeQueryRef` and `displayName` on the projection to the actual measure name (e.g., "Total Revenue"), never a generic placeholder like "Card Label".
- Standard card size: 195w x 95h. Position 6 cards in a row at y=55.

### Example Layout
```
   ┌─────────────────┐
   │                  │
   │      $2.4M       │   <-- large value (labels object, 30pt)
   │   Total Revenue  │   <-- category label (bottom)
   └─────────────────┘
```

### Common KPI Mistakes
- Showing a number without context (is $2.4M good or bad?)
- Using the "new card" visual without customizing it (defaults are too plain)
- Leaving the top title bar visible AND the category label -- this creates redundant labeling
- Cramming too many metrics into one card (keep it to 1-2 values per card)
- Leaving `nativeQueryRef`/`displayName` as generic placeholder text like "Card Label"
- Not updating the comparison period dynamically (hardcoded "vs. 2024" breaks next year)

---

## Table and Matrix Design

Tables and matrices are underrated. They're the most information-dense visual and the best choice when users need exact numbers or want to export data.

### Formatting for Readability
- Use alternating row shading (very light gray, not heavy banding)
- Right-align numeric columns, left-align text columns
- Use consistent number formatting within each column
- Bold totals and subtotals
- Freeze header rows

### Matrix-Specific Tips
- Enable stepped layout for hierarchies (makes drill-down obvious)
- Use conditional formatting (data bars, background color) to add visual dimension to the numbers
- Consider sparklines in matrix rows for trend context
- Keep row and column headers short; use tooltips for full descriptions

### When to Use Tables vs. Charts
- Use a table when the audience needs exact values for many items
- Use a table when there are more than 15-20 categories (too many for a bar chart)
- Use a chart when the pattern/trend is the message, not the individual values
- Use both: chart for the overview, table below for the drill-down detail

---

## Common Power BI Mistakes

### Design Mistakes
1. **Using default colors without thought**: Power BI's default palette assigns different colors to bars in a single-series chart. Override this: use one color for single-series charts.
2. **Pie charts for everything**: Horizontal bar charts are almost always better. Use pie/donut only for 2-3 category splits where precision doesn't matter.
3. **Too many visuals per page**: 6-8 visuals is a good upper limit for a dashboard page. More than that, and nothing stands out.
4. **No visual hierarchy**: If everything is the same size and prominence, nothing is important. Make KPIs big, supporting charts medium, detail tables small.
5. **Ignoring mobile layout**: If users will view the dashboard on mobile, use the mobile layout editor (View > Mobile Layout) to create a vertical-scroll version.

### Data Mistakes
6. **No date table**: Always create a proper date/calendar table for time intelligence. Don't rely on auto date/time hierarchy.
7. **Measures in the wrong table**: Put measures in a dedicated "Measures" table or in the fact table they most logically belong to. Don't scatter measures across dimension tables.
8. **Implicit measures**: Always create explicit DAX measures. Don't drag numeric fields directly onto visuals (this creates implicit SUM/COUNT that's harder to control and reuse).
9. **Too many data points**: A line chart with 10,000 daily data points is unreadable. Aggregate to weekly or monthly.
10. **Not handling nulls/blanks**: Blank values can distort averages and counts. Use CALCULATE with appropriate filters, or handle with IF/ISBLANK.

### Interaction Mistakes
11. **Default cross-filtering left unconfigured**: Test every cross-filter interaction. Unexpected behavior confuses users.
12. **No bookmarks for common views**: If users frequently filter to the same view (e.g., "My Region"), create bookmarks for one-click access.
13. **Missing drill-through pages**: If a dashboard shows summary metrics, create drill-through pages so users can click to see the detail behind a number.

---

## Dashboard Design Checklist

Before publishing a Power BI dashboard, verify:

### Content
- [ ] Every visual answers a specific question
- [ ] KPI cards include comparison context (vs. target, vs. prior period)
- [ ] Titles state insights or clearly describe the content with units and time period
- [ ] A date/time slicer is available if the data is temporal
- [ ] The "last refreshed" date is visible somewhere on the page

### Design
- [ ] Visual hierarchy is clear (KPIs prominent at top, detail at bottom)
- [ ] Consistent color usage across all pages
- [ ] No unnecessary legends (direct labels used where possible)
- [ ] Whitespace separates visual groups
- [ ] All visuals have drop shadows (Center position, #D2D2D2) and rounded borders
- [ ] Font sizes are readable (nothing below 8pt)
- [ ] Charts use horizontal bars for categorical comparison (not pie/donut)
- [ ] Card visuals show only the bottom category label (top title bar hidden)

### Interactions
- [ ] Cross-filtering tested for every visual pair
- [ ] Slicers have sensible defaults
- [ ] Drill-through pages available for detail behind summary metrics
- [ ] Bookmarks created for common filter combinations
- [ ] Tooltip pages configured for contextual detail (if applicable)

### Technical
- [ ] All measures are explicit DAX (no implicit measures)
- [ ] A proper date table exists for time intelligence
- [ ] Data model relationships are correct
- [ ] Performance is acceptable (page loads in < 3 seconds)
- [ ] Row-level security is configured if needed

---

## Visual Type Quick Reference

| Visual | Power BI Type ID | Best For |
|---|---|---|
| Horizontal bar | `clusteredBarChart` | Category comparison, ranking |
| Vertical column | `clusteredColumnChart` | Time series (few periods) |
| Stacked bar | `stackedBarChart` | Part-of-whole across categories |
| Stacked column | `stackedColumnChart` | Composition over time |
| 100% stacked bar | `hundredPercentStackedBarChart` | Proportion comparison |
| Line | `lineChart` | Trends over time |
| Area | `areaChart` | Volume/cumulative over time |
| Combo (line + column) | `lineClusteredColumnComboChart` | Trend + value overlay |
| Scatter | `scatterChart` | Correlation, clustering |
| Pie | `pieChart` | Avoid; use stacked bar |
| Donut | `donutChart` | Avoid; use stacked bar |
| Treemap | `treemap` | Hierarchical composition |
| Waterfall | `waterfallChart` | Bridge / build-up analysis |
| Funnel | `funnel` | Sequential stage conversion |
| Card | `card` | Single KPI |
| Multi-row card | `multiRowCard` | Multiple KPIs |
| Table | `tableEx` | Exact values, many items |
| Matrix | `pivotTable` | Cross-tabulated drill-down |
| Map | `map` | Point-level geographic data |
| Filled map | `filledMap` | Choropleth by region |
| Slicer | `slicer` | Interactive filter |
| Gauge | `gauge` | Caution: low info density |
| KPI | `kpi` | Metric with trend indicator |
