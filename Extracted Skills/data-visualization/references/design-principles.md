# Data Visualization Design Principles

Detailed guidance on color, typography, layout, labeling, accessibility, and decluttering. Drawn from IBCS v1.1, Knaflic (Storytelling with Data), Wilke (Fundamentals of Data Visualization), Evergreen (Effective Data Visualization), and Schwabish.

## Table of Contents
1. [The IBCS SUCCESS Formula](#the-ibcs-success-formula)
2. [Decluttering (Knaflic Method)](#decluttering-knaflic-method)
3. [Color](#color)
4. [Typography and Labels](#typography-and-labels)
5. [Axes and Scales](#axes-and-scales)
6. [Layout and Composition](#layout-and-composition)
7. [Titles and Annotations](#titles-and-annotations)
8. [Accessibility](#accessibility)
9. [Data-Ink Ratio](#data-ink-ratio)

---

## The IBCS SUCCESS Formula

The International Business Communication Standards organize visualization rules into seven principles:

### SAY (Convey a Message)
Every visualization should answer a question or communicate a finding. Write titles that state the insight, not just the topic.

- Bad title: "Revenue by Quarter"
- Good title: "Q4 revenue declined 8% after two quarters of growth"

The title is the first thing readers see. Use it to tell them what to take away. The subtitle can provide supporting detail (time period, data source, units).

### UNIFY (Apply Semantic Notation)
Create a consistent visual language across all reports. IBCS defines a notation system:

- **Actual (AC)**: Solid black/dark fill
- **Plan/Budget (PL)**: Outlined or hatched fill (not solid)
- **Previous Year (PY)**: Lighter shade of the actual color
- **Forecast (FC)**: Striped or dashed patterns
- **Variance**: Green for favorable, red for unfavorable (or up/down arrows for colorblind-safe alternatives)

When everyone in your organization uses the same notation, new reports are instantly understandable without hunting for legends.

### CONDENSE (Increase Information Density)
Pack more information into less space. A single well-designed page with sparklines, small multiples, and compact tables communicates more than ten separate full-page charts.

Techniques: small multiples, sparklines in tables, compact KPI grids, eliminating whitespace waste (not all whitespace -- just the wasted kind).

### EXPRESS (Choose Proper Visualization)
Select chart types that match the data relationship. The IBCS chart type matrix:

**Time series analysis**: Use columns for individual data points (few periods), lines for patterns and trends (many periods), areas for cumulative/volume emphasis. Stacked variants show composition over time.

**Structural analysis**: Use horizontal bars for comparisons across categories. Sorted by value unless the categories have a natural order.

**Variance analysis**: Show deviations from plan/budget/prior year using integrated variance bars (positive bars up, negative bars down, adjacent to the main chart).

### SIMPLIFY (Avoid Clutter)
Remove everything that doesn't convey information: decorative gridlines, 3D effects, gradient fills, shadows, unnecessary borders, redundant legends (use direct labeling instead), background colors, and ornamental clip art.

### CHECK (Ensure Visual Integrity)
Verify that your visualization doesn't distort the data:
- Bar/column charts start at zero
- Axis scales are consistent across related charts
- Area encoding is proportional (no misleading bubble sizes)
- Time axes have consistent intervals (no skipped months)
- Dual axes are avoided or clearly justified

### STRUCTURE (Organize Content)
Organize from overview to detail. Executive summaries first, supporting analysis second, raw data last. Group related content together. Use consistent page layouts across report sections.

---

## Decluttering (Knaflic Method)

Knaflic's approach to removing clutter, applied in sequence:

### 1. Remove chart borders and backgrounds
Default chart backgrounds (gray fills, borders) add visual noise without information. Use white or transparent backgrounds.

### 2. Remove or lighten gridlines
If gridlines help the reader trace values to the axis, make them thin and light gray. If the data labels make them unnecessary, remove them entirely.

### 3. Remove redundant data markers
Line charts don't need a dot on every data point unless the specific values matter more than the trend. If you keep markers, use them sparingly (endpoints only, or only on highlighted values).

### 4. Clean up axes
Remove axis lines if gridlines provide the reference. Remove tick marks. Reduce the number of axis labels to only what's needed for orientation (every other month, round numbers only).

### 5. Eliminate the legend (use direct labeling)
Place the series label directly on or next to the data (at the end of a line, above a bar) instead of forcing the reader to look back and forth between a legend and the chart.

### 6. Use strategic emphasis
Once the clutter is gone, use color, weight, and size to draw attention to the data that matters. Gray out the context; highlight the insight.

---

## Color

### Core Principles

**Use color purposefully.** Color should encode information or draw attention, never decorate. If a chart uses 7 different colors for 7 bars and the color doesn't represent anything, use one color for all bars.

**Highlight, don't rainbow.** The most effective approach: one neutral color (gray or muted blue) for most data, one accent color (bold blue, orange, or red) for the element you want to emphasize. This creates instant visual hierarchy.

**Sequential palettes for ordered data.** When color represents a continuous value (low to high, cold to hot), use a single-hue sequential palette (light blue to dark blue). Multi-hue sequential palettes (yellow to red) also work but can be confusing for colorblind readers.

**Diverging palettes for deviation.** When color shows positive vs. negative deviation from a center point, use a diverging palette with distinct colors on each side (blue for negative, red for positive) and a neutral middle.

**Categorical palettes for unordered groups.** When color distinguishes categories, limit to 5-7 distinct colors. More than that and the distinctions blur. Consider using shape or position to encode categories instead.

### Color and Meaning
- Red = negative, bad, danger, decrease
- Green = positive, good, growth, increase
- Gray = context, baseline, background
- Blue = neutral, professional (safe default)

Be aware of cultural context. In some financial contexts, red means loss and black means profit. In some cultures, red is positive.

### Color Don'ts
- Don't use pure red on pure blue (or vice versa) -- they vibrate visually
- Don't rely on color alone to convey information (add labels, patterns, or position for accessibility)
- Don't use more than 7 distinct colors in a single chart
- Don't use traffic light colors (red/yellow/green) unless you're encoding performance status

---

## Typography and Labels

### Font Choices
Use a clean sans-serif font for charts: Segoe UI (Power BI default), Calibri, Arial, or Helvetica. Save serif fonts for long-form text. Use one font family throughout a report.

### Hierarchy
- **Chart title**: 12-14pt, bold
- **Subtitle/description**: 10-11pt, regular, gray
- **Axis labels**: 9-10pt, regular
- **Data labels**: 8-10pt, matching the data color
- **Source/footnote**: 8pt, gray

### Data Labels
- Use them instead of gridlines when you want readers to know exact values
- Don't label every point in a dense chart -- label key points (max, min, first, last, highlighted)
- Position labels to avoid overlap (above bars, at line endpoints)
- Use consistent number formatting (1.2M not 1,200,000; 12% not 0.12)

### Number Formatting
- Use abbreviations for large numbers: K (thousands), M (millions), B (billions)
- Match decimal places to precision needed (board report: 0-1 decimals; analyst view: 2)
- Include units in axis titles or card labels, not in every data point
- Currency: show the symbol once (in the axis title), not on every label

---

## Axes and Scales

### Zero Baseline Rule
Bar and column charts should start at zero. Truncating the baseline exaggerates differences and misleads the reader. If the interesting variation is small relative to the total, consider a different chart type (dot plot, line chart) rather than truncating.

### Consistent Scales
When placing related charts side by side (revenue by region in two panels), use the same axis scale. Different scales make visual comparison meaningless.

### Axis Orientation
- Horizontal axis: time (left = past, right = present) or categories
- Vertical axis: values (up = more)
- If category labels are long, use horizontal bars (categories on Y-axis) for readability

### Log Scales
Use logarithmic scales when data spans multiple orders of magnitude AND the audience understands log scales. In general business reporting, avoid them. In analytical/technical contexts, they can reveal patterns hidden by linear scales.

---

## Layout and Composition

### Dashboard Layout Patterns

**KPI Row + Detail Grid**: 3-5 KPI cards across the top, 2-3 analytical charts below, optional detail table at the bottom. This is the most common and effective dashboard pattern.

**Left Sidebar Filters**: Slicers in a left column (about 20% of width), main content in the remaining 80%. Works well when you have 3+ filter dimensions.

**Narrative Flow**: Charts arranged in reading order (top to bottom) that tell a story. Works for presentations and printed reports. Each chart answers the next logical question.

### Spacing and Alignment
- Maintain consistent margins and gutters between visuals
- Align chart edges to an invisible grid
- Use 10-15px gaps between visuals in Power BI (enough to separate, not enough to waste space)
- Left-align titles across charts for a clean look

### Aspect Ratios
- Line charts: wider than tall (roughly 3:1 or 4:1 aspect ratio helps show trends without exaggerating slopes)
- Bar charts: taller than wide (enough room for category labels)
- Scatter plots: roughly square
- Dashboard page: 16:9 (1280x720 default in Power BI)

---

## Titles and Annotations

### Writing Effective Titles
A visualization title should answer "so what?" not just "what."

| Type | Bad Title | Good Title |
|---|---|---|
| Descriptive | "Sales by Region" | "East region leads sales by 23%" |
| Trend | "Monthly Revenue" | "Revenue recovered in Q4 after summer dip" |
| KPI | "Customer Count" | "Customer base grew 15% YoY to 12,400" |

If you can't state the insight in the title (e.g., for an exploratory dashboard where the user drives the analysis), use a clear descriptive title with units and time period: "Revenue by Product Category (USD, FY2025)."

### Annotations
Use annotations to call out important events, thresholds, or context that aren't visible in the data alone. Examples: "New pricing launched here" on a timeline, "Industry average: 34%" as a reference line, "Target: 95%" as a threshold.

---

## Accessibility

### Colorblind-Safe Design
Approximately 8% of men and 0.5% of women have some form of color vision deficiency. Design for them:

- Don't rely solely on color to distinguish categories. Also use shape, pattern, position, or direct labeling.
- Avoid red-green combinations as the only distinguishing feature. Use blue-orange instead, or add pattern fills.
- Test your palette with a colorblind simulator.
- IBCS notation (solid vs. hatched vs. outlined) is inherently colorblind-safe.

### Screen Reader Considerations
For digital dashboards:
- Write descriptive alt-text for charts
- Use table equivalents alongside visual charts where possible
- Ensure sufficient contrast ratios (WCAG AA: 4.5:1 for normal text, 3:1 for large text)

### Print Considerations
If the visualization might be printed in grayscale:
- Ensure categories are distinguishable without color (use patterns, direct labels)
- Use high contrast between data and background
- Test by printing a sample page in black and white

---

## Data-Ink Ratio

Tufte's data-ink ratio principle: maximize the share of ink (or pixels) that represents data. Everything else is non-data ink and should be minimized.

High data-ink ratio (good):
- Direct-labeled bars with no gridlines, no border, no background fill
- A sparkline embedded in a table cell
- A compact small multiples panel

Low data-ink ratio (wasteful):
- A 3D pie chart with gradient fills, drop shadows, and an exploded slice
- A gauge visual taking up 25% of the page to show one number
- Thick borders, dark gridlines, and patterned backgrounds

The goal isn't to strip everything to bare bones -- it's to make sure every visual element earns its place by conveying information or aiding comprehension.
