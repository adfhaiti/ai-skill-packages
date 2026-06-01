# Chart Selection Guide

A comprehensive decision framework for choosing the right visualization. Organized by the type of data relationship you need to communicate.

## Table of Contents
1. [Comparison](#comparison)
2. [Change over Time](#change-over-time)
3. [Ranking](#ranking)
4. [Part-to-Whole](#part-to-whole)
5. [Distribution](#distribution)
6. [Correlation](#correlation)
7. [Deviation](#deviation)
8. [Magnitude](#magnitude)
9. [Spatial](#spatial)
10. [Flow](#flow)
11. [Single Values / KPIs](#single-values--kpis)
12. [Survey / Likert Data](#survey--likert-data)
13. [Quick Decision Matrix](#quick-decision-matrix)

---

## Comparison

**The question**: How do values differ across categories?

### Horizontal Bar Chart (preferred)
- **When to use**: Comparing values across categories. This is the default choice for categorical comparison -- use it unless you have a specific reason not to.
- **Why it works**: Easy to read, handles long labels, natural sort order, precise comparison via length (humans judge length more accurately than angle or area).
- **Power BI type**: `clusteredBarChart`
- **Tips**: Sort bars by value (largest to smallest or vice versa) unless the categories have a natural order (e.g., age groups). Always start the axis at zero.

### Grouped Bar / Grouped Column
- **When to use**: Comparing values across categories AND a second dimension (e.g., revenue by region and by year). Limited to 2-4 groups per category.
- **Power BI type**: `clusteredBarChart` or `clusteredColumnChart` with a Legend field
- **Tips**: Keep groups to 3-4 max. More than that and the chart becomes unreadable.

### Dot Plot
- **When to use**: Comparing values when you don't need to emphasize the magnitude from zero, or when the differences between values are small relative to the values themselves.
- **Power BI type**: Scatter chart or custom visual
- **Tips**: Good alternative to bars when the zero baseline would compress the differences.

### Dumbbell Chart
- **When to use**: Comparing two related values per category (e.g., before/after, male/female, plan/actual).
- **Power BI type**: Custom visual or built with error bars
- **Tips**: Great for showing gaps between two measures.

### Small Multiples
- **When to use**: When you have too many series for a single chart, or when you want to compare patterns across categories without the visual clutter of overlapping lines.
- **Power BI type**: Use the "Small multiples" field well in supported visuals (line, bar, column, area)
- **Tips**: Keep the same axis scale across all panels so comparisons are fair.

---

## Change over Time

**The question**: How do values evolve over a time period?

### Line Chart
- **When to use**: Showing trends, patterns, and rates of change over continuous time. The default for time series with more than ~8 periods.
- **Why it works**: The slope of the line encodes rate of change. Multiple lines allow trend comparison across series.
- **Power BI type**: `lineChart`
- **Tips**: Limit to 4-5 lines max. Use direct labeling (label the line itself) instead of legends when possible. Consistent line thickness; highlight one series with a bolder stroke if needed.

### Column Chart (Vertical)
- **When to use**: Showing values for discrete time periods (fewer than ~8). Emphasizes individual values rather than the trend shape. IBCS recommends columns for "data points" in time series.
- **Power BI type**: `clusteredColumnChart`
- **Tips**: Columns are appropriate for time because the left-to-right reading order matches chronological order. Always include all time periods (don't skip gaps).

### Area Chart
- **When to use**: Showing volume or cumulative totals over time. Works well for a single series where you want to emphasize the magnitude beneath the trend line.
- **Power BI type**: `areaChart`
- **Tips**: Avoid stacked areas with more than 3-4 series -- the middle layers become impossible to read because they don't share a common baseline.

### Stacked Column (over time)
- **When to use**: Showing how the total changes over time AND how the composition of that total shifts.
- **Power BI type**: `stackedColumnChart`
- **Tips**: The bottom segment is the only one that's easy to compare across periods (it has a consistent baseline). Put the most important category at the bottom.

### Sparkline
- **When to use**: Inline trend indicators within tables or KPI cards. Shows the shape of a trend in minimal space.
- **Power BI type**: Available in matrix/table visuals and some card visuals
- **Tips**: Great for IBCS-style condensed reporting where you need trend context without a full chart.

### Slope Chart / Slopegraph
- **When to use**: Comparing values at exactly two points in time (e.g., 2023 vs. 2024) across multiple categories. Shows direction and magnitude of change.
- **Power BI type**: Custom visual or line chart with exactly two x-axis values
- **Tips**: Effective for before/after comparisons.

---

## Ranking

**The question**: What is the relative position/order of items?

### Sorted Horizontal Bar
- **When to use**: Showing items ranked by a value. The default and best option for ranking.
- **Power BI type**: `clusteredBarChart` with Top N filter or sorted axis
- **Tips**: Sort descending (highest at top). Consider showing only top 10 or top 15 and grouping the rest into "Other."

### Lollipop Chart
- **When to use**: Same as sorted bar, but with less visual weight. Good when you have many items and full bars would be overwhelming.
- **Power BI type**: Custom visual
- **Tips**: Essentially a dot plot with a stem to the axis.

### Bump Chart
- **When to use**: Showing how rankings change over time (e.g., quarterly market share rankings).
- **Power BI type**: Custom visual
- **Tips**: Works well with 5-10 items. More than that and the crossings become tangled.

---

## Part-to-Whole

**The question**: How do components add up to a total?

### Stacked Bar (Horizontal)
- **When to use**: Showing composition across categories. Better than pie charts because length comparisons are more precise than angle comparisons.
- **Power BI type**: `stackedBarChart`
- **Tips**: Limit to 4-5 segments. Use consistent color coding across charts.

### 100% Stacked Bar
- **When to use**: Comparing proportional composition across categories when you care about the percentages, not the absolute values.
- **Power BI type**: `hundredPercentStackedBarChart`
- **Tips**: Good for survey data (% agree vs. disagree) or budget allocation comparisons.

### Waterfall Chart
- **When to use**: Showing how an initial value is affected by sequential positive and negative changes to arrive at a final value. Classic for P&L statements, bridge analyses.
- **Power BI type**: `waterfallChart`
- **Tips**: Use consistent colors for increases (one color) and decreases (another). The starting and ending totals should be visually distinct.

### Treemap
- **When to use**: Showing hierarchical part-of-whole relationships with many categories. The area encoding shows relative size.
- **Power BI type**: `treemap`
- **Tips**: Labels can be hard to read in small rectangles. Works best on large screens or when you have 15+ categories that would overwhelm a bar chart.

### Pie / Donut Chart
- **When to use**: Almost never. Reserve for showing a simple 2-3 category split where the precise values matter less than the general proportion (e.g., "about 70/30"). Many visualization experts advise against them entirely.
- **Power BI type**: `pieChart` / `donutChart`
- **Why to avoid**: Humans compare angles and areas poorly. Small differences between slices are nearly impossible to distinguish. A horizontal bar chart communicates the same information more accurately.

---

## Distribution

**The question**: How are values spread across a range?

### Histogram
- **When to use**: Showing the frequency distribution of a continuous variable. How many items fall into each bin?
- **Power BI type**: Column chart with binned data (use Power Query or DAX to create bins)
- **Tips**: Bin width matters. Too few bins hide patterns; too many create noise. Start with the square root of N as a guideline for bin count.

### Box Plot
- **When to use**: Comparing distributions across categories. Shows median, quartiles, and outliers compactly.
- **Power BI type**: Custom visual from AppSource
- **Tips**: Useful for technical audiences. For general audiences, consider a simpler alternative like a range chart.

### Violin Plot
- **When to use**: Like a box plot but also shows the shape of the distribution. Good for comparing multimodal distributions.
- **Power BI type**: Custom visual or R/Python visual
- **Tips**: Requires audience familiarity. Consider whether a histogram or density curve would be clearer.

---

## Correlation

**The question**: How do two variables relate to each other?

### Scatter Plot
- **When to use**: Showing the relationship between two continuous variables. Each point represents an observation.
- **Power BI type**: `scatterChart`
- **Tips**: Add a trend line if the correlation is the point. Use size encoding (bubble) for a third variable. Label outliers directly.

### Bubble Chart
- **When to use**: Scatter plot with a third variable encoded as bubble size. Classic example: Gapminder (income vs. life expectancy, bubble size = population).
- **Power BI type**: `scatterChart` with Size field
- **Tips**: Humans underestimate area differences, so use size as an approximate/supporting dimension, not for precise comparison.

---

## Deviation

**The question**: How do values differ from a reference point?

### Diverging Bar Chart
- **When to use**: Showing positive and negative deviations from a center point (zero, target, average). Common for variance analysis and survey net scores.
- **Power BI type**: Stacked bar with calculated positive/negative measures, or custom visual
- **Tips**: Use green/blue for positive and red for negative (or whatever your organization's convention is). Keep it consistent.

### Bullet Chart
- **When to use**: Showing a value against a target with qualitative ranges (poor/good/excellent). Compact alternative to gauges.
- **Power BI type**: Custom visual (OKViz Bullet Chart is popular)
- **Tips**: Much more informative than gauge charts because they show context (target + ranges) in less space.

### Variance Charts (IBCS style)
- **When to use**: Showing absolute or relative variance from plan/budget/prior year. A core IBCS pattern.
- **Tips**: Place variance charts adjacent to the actual-vs-plan chart they relate to. Use integrated variance (bars showing the delta) rather than separate charts when space allows.

---

## Magnitude

**The question**: How big are these values relative to each other?

Use the same charts as Comparison (horizontal bar is the default). The distinction is mainly conceptual: magnitude focuses on "how big" while comparison focuses on "which is bigger."

---

## Spatial

**The question**: Are there geographic patterns in the data?

### Choropleth Map (Filled Map)
- **When to use**: Showing values by geographic region using color intensity.
- **Power BI type**: `filledMap` or `map`
- **Tips**: Large regions get disproportionate visual weight. A bar chart sorted by region may actually communicate better for precise comparisons. Maps are best when the geographic pattern IS the insight.

### Bubble Map
- **When to use**: Showing point-level data (cities, locations) with bubble size proportional to a value.
- **Power BI type**: `map` with Size field
- **Tips**: Overlapping bubbles are a problem in dense areas. Consider a table with region groupings as an alternative.

---

## Flow

**The question**: How do things move between stages or categories?

### Sankey Diagram
- **When to use**: Showing flows between stages. Common for user journey analysis, budget allocation, material flows.
- **Power BI type**: Custom visual from AppSource
- **Tips**: Works well with 3-8 nodes per stage. More than that and it becomes spaghetti.

### Funnel Chart
- **When to use**: Showing sequential stages with decreasing values (sales pipeline, conversion funnel).
- **Power BI type**: `funnel`
- **Tips**: Only meaningful when the stages are sequential and values naturally decrease.

---

## Single Values / KPIs

**The question**: What is the current state of a key metric?

### Card Visual
- **When to use**: Displaying a single important number prominently. Revenue, headcount, completion rate.
- **Power BI type**: `card` or `multiRowCard`
- **Tips**: Include context! Show the comparison (vs. last period, vs. target) either in the card subtitle or with conditional formatting (green/red). A number alone is meaningless.

### Gauge
- **When to use**: Showing progress toward a specific target. Limited to a single metric.
- **Power BI type**: `gauge`
- **Tips**: Gauges waste a lot of space for one data point. A bullet chart or a card with a progress bar is usually more space-efficient. Kolokolov/Zelensky classify gauges as "Risky Advanced" visuals.

---

## Survey / Likert Data

**The question**: What did the survey respondents say?

### Diverging Stacked Bar
- **When to use**: Showing Likert scale responses (Strongly Disagree to Strongly Agree) centered on the neutral point.
- **Tips**: Center on neutral. Use a sequential color scheme from negative to positive.

### Stacked Bar with Percentages
- **When to use**: Showing response distributions when there's no natural center point (e.g., "Select all that apply" questions).
- **Power BI type**: `hundredPercentStackedBarChart`

---

## Quick Decision Matrix

Use this when you need a fast answer:

| Your Question | Best Chart | Power BI Visual Type |
|---|---|---|
| Compare values across categories | Horizontal bar | `clusteredBarChart` |
| Show trend over time (many periods) | Line chart | `lineChart` |
| Show values at few time points | Column chart | `clusteredColumnChart` |
| Rank items by value | Sorted horizontal bar | `clusteredBarChart` |
| Show composition of a total | Stacked bar or waterfall | `stackedBarChart` / `waterfallChart` |
| Show a distribution | Histogram | Column chart with bins |
| Show correlation between 2 variables | Scatter plot | `scatterChart` |
| Show geographic patterns | Filled map | `filledMap` |
| Display a single KPI | Card | `card` |
| Compare actual vs. target | Bullet chart | Custom visual |
| Show deviation from reference | Diverging bar | Custom visual or calculated measures |
| Show flows between stages | Sankey | Custom visual |
| Show change between exactly 2 periods | Slope chart | Line with 2 points or custom visual |
