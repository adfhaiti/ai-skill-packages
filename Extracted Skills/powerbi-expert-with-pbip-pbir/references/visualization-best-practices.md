# Power BI Visualization Best Practices

## Perception Accuracy Hierarchy (Cleveland & McGill)

Before choosing a chart, understand how accurately humans interpret different visual encodings. This ranking is based on decades of perception research (Cleveland & McGill, 1984; Evergreen, 2017; Wilke, 2019):

```
Most Accurate
  1. Position on a common scale (dot plots, bar charts)
  2. Position on non-aligned scales (small multiples)
  3. Length (bar/column height)
  4. Direction/Slope (line charts, slopegraphs)
  5. Angle (pie charts) -- error rate increases here
  6. Area (bubble charts, treemaps)
  7. Volume (3D charts) -- avoid entirely
  8. Curvature (donuts at scale)
Least Accurate
```

**Practical takeaway:** Prioritize position-based and length-based charts (bars, dots, lines) over area-based (bubbles, treemaps) and angle-based (pies). When stakeholders ask "why not a pie chart?", this hierarchy is your answer.

---

## Chart Selection Guide

### Decision Tree for Choosing the Right Chart

```
What's your primary question?
  |
  +---> Compare values across categories?
  |     Yes: Clustered bar/column (up to 5-7 categories)
  |          Grouped bar (multiple series comparison)
  |          Small multiples (many categories)
  |
  +---> Show change over time?
  |     Yes: Line chart (trends, forecasts)
  |          Area chart (magnitude + trend)
  |          Column chart (discrete time periods)
  |
  +---> Show parts of a whole?
  |     Yes: Donut chart (single series)
  |          Stacked bar 100% (multiple series)
  |          Treemap (hierarchical, many categories)
  |          Waterfall (flow from one value to another)
  |
  +---> Show distribution?
  |     Yes: Histogram (frequency distribution)
  |          Box plot (quartiles, outliers)
  |          Dot plot (individual values)
  |
  +---> Show relationship between two variables?
  |     Yes: Scatter plot (correlation)
  |          Bubble chart (add third dimension)
  |
  +---> Show geographic data?
  |     Yes: Filled map (by country/region)
  |          Shape map (custom regions)
  |          ArcGIS map (coordinates, routes)
  |
  +---> Show single metric or KPI?
        Yes: Card (single number)
             Multi-row card (multiple metrics)
             Gauge (progress to target)
             KPI visual (current vs. target)
```

### Visualization Compass: Simplified Three-Category Approach (Kolokolov)

For 90% of corporate dashboard decisions, classify your data into one of three buckets:

**RANKING** (comparing categories by magnitude):
- Under 10 categories: Column chart (vertical)
- 10+ categories: Bar chart (horizontal, so labels are readable)
- Never use line charts for ranking data (lines imply a continuous relationship that doesn't exist between categories)

**DYNAMICS** (change over time):
- 12 or fewer time periods: Column chart works well
- 13+ periods: Line chart (easier to spot trends)
- Time axis is ALWAYS horizontal, reading left to right
- Max 4 lines on a single line chart; beyond that, use small multiples

**STRUCTURE** (parts of a whole):
- Up to 6 categories: Pie or donut
- 7-12 categories: Treemap
- 13+ categories: Table with conditional formatting (group into "Other" where possible)

### Chart Type Details

**Comparison Charts**
- Clustered bar: Best for 5-7 categories, easy to compare values
- Grouped bar: Compare multiple series within categories
- Don't use: Pie charts (humans misjudge angles; donut is minimally better)

**Time Series Charts**
- Line chart: Show trends, smooth lines for cleaner look
- Area chart: When you need to emphasize magnitude
- Column chart: Discrete periods (monthly, quarterly)
- Combination: Line for trend, column for volume

**Part-of-Whole**
- Donut: One series, up to 5-6 slices (over 6, use treemap)
- Stacked bar 100%: Multiple series, emphasize proportions
- Treemap: Hierarchical data, many categories, area represents value
- Waterfall: Show how values accumulate (starting value, changes, ending value)

**Distribution**
- Histogram: Frequency distribution of one variable
- Box plot: Quartiles, median, outliers (built via R/Python or custom visual)
- Dot plot: Individual data points, small datasets

**Relationship**
- Scatter: Two continuous variables, shows correlation
- Bubble: Scatter plus third dimension via bubble size
- Small multiples: Show relationship across groups

**Key Performance Indicators**
- Card: Single metric, large text for visibility
- Multi-row card: 3-4 related metrics
- Gauge: Progress toward target (0-100 scale ideal)
- KPI visual: Current value, status indicator, trend

**Geography**
- Filled map: Countries, states, provinces (built-in shapes)
- Shape map: Custom regions (requires map definition file)
- ArcGIS map: Latitude/longitude, satellite imagery

---

## Dashboard Layout and Design

### Reading Patterns

Most users scan dashboards in one of two patterns:

**Z-Pattern** (default for most dashboards)
- Top-left to top-right (headline KPIs, summary)
- Diagonally down and back to bottom-left
- Bottom-right acts as secondary info
- Best for: Executive dashboards with multiple KPIs

**F-Pattern** (for detailed dashboards)
- Horizontal scan across top (filters, main KPI)
- Left-hand column for navigation or secondary filters
- Rest of page for detailed visuals
- Best for: Operational dashboards with drill-downs

### Four-Level Information Hierarchy (Kolokolov)

Organize dashboards top-to-bottom using explicit hierarchy levels:

```
Level 0 - HEADER
  Title, navigation buttons, slicers, logo, report date

Level 1 - KPI CARDS (max 6)
  Most critical metrics. Users see these first.
  Never mix KPI cards with charts on the same row.

Level 2 - TREND/SUBTOTAL CHARTS
  High-level charts by category, region, or time
  Often serve as interactive filters for Level 3

Level 3 - DETAIL TABLES
  Granular data with conditional formatting
  Tables, matrices, or detailed breakdowns
```

### Grid Systems for Professional Alignment (Kolokolov)

Use symmetric grids as the foundation, not free placement:

- **2x2 Grid (4 modules):** Simplest balanced layout. Good for focused pages with 4 visuals.
- **3x2 Grid (6 modules):** Most common corporate layout. Allows flexible merging (e.g., tall chart spanning 2 modules on the left, two stacked charts on the right).

Align ALL elements (KPIs, charts, tables) to this invisible grid. Consistent proportions and spacing create professionalism automatically.

### Layout Principles

1. **Above the Fold**: Place critical KPIs and filters in the top 400 pixels
2. **Summary First**: Show overview visuals before detail
3. **Visual Hierarchy**: Use size, color, position to guide attention
4. **Consistent Grid**: Align all visuals to an invisible grid (5-pixel or 10-pixel)
5. **White Space**: Use breathing room; don't cram visuals. More white space = more professional and readable. (Evergreen)
6. **Visual Density**: 15-20 visuals per page maximum (prefer 8-12)
7. **Chunking**: Group related visuals that tell one story together. Create visual breaks between unrelated data stories. (Evergreen)

### Page Structure

**KPI/Summary Page**
- Row 1: 3-5 headline KPIs as cards/gauges
- Row 2: 2-3 trend lines or area charts
- Row 3: Comparison bar chart or breakdown treemap
- Add drill-through buttons to detail pages

**Detail Pages**
- Filters at top (slicers for date range, category, region)
- Main visual (large, 60% of page width)
- Supporting visuals (30% width on right)
- Table or matrix below for raw data export

**Operational Dashboard**
- Real-time metrics (top-left, red/yellow/green)
- Alerts or exceptions (prominent color)
- Trend charts (right side)
- Recent transactions table (bottom)

### Color and Accessibility

Use a limited palette (3-5 colors) for consistency:
- Primary color: Most important data (KPIs, main insights)
- Secondary color: Supporting data
- Accent color: Alerts, exceptions (red for negative, green for positive)
- Neutral gray: Background, deemphasis

**Colorblind-Friendly Palettes**
- Deuteranopia (red-green): Use blue, orange, purple instead
- Protanopia (red-green, more severe): Similar to deuteranopia
- Tritanopia (blue-yellow): Use red, green, pink instead
- Gray for neutral (works for all types)

Example accessible palette:
```
Primary blue: #0173B2
Secondary orange: #DE8F05
Accent red: #CC78BC
Neutral gray: #999999
Background: #FFFFFF
```

### Three Core Uses of Color (Wilke)

Color is not decorative. It serves exactly three purposes, and mixing them confuses viewers:

**1. Color to Distinguish (Qualitative/Categorical)**
- Use for categories with no inherent order (regions, product types, departments)
- Colors should look clearly distinct but visually equivalent (no color should "shout")
- Colors should NOT create an impression of order or hierarchy
- Good palettes: ColorBrewer Dark2, Okabe-Ito scale

**2. Color to Represent Data Values (Sequential)**
- Use for quantitative data (revenue heatmaps, growth rates)
- Must vary uniformly across the entire range (no sudden jumps)
- Can be monochromatic (dark blue to light blue) or multihue
- Multihue should follow natural gradients (dark red to light yellow = natural; purple to green = unnatural)

**3. Color to Highlight (Accent)**
- Use to emphasize specific data points carrying the key narrative
- Accent = subdued base colors + one stronger/darker accent color
- Alternative: Remove all color except highlighted elements (the "gray everything else" technique from Knaflic)
- Most effective when used sparingly

### Diverging Color Scales (Wilke)

For positive/negative deviations from a neutral midpoint (variance from budget, YoY change):
- Structure: Two sequential scales meeting at center (usually white or light gray)
- Must be balanced: left-to-dark matches right-to-dark in intensity
- Natural gradient: dark red | white | dark blue
- Avoid unbalanced: dark red | white | light blue (underrepresents positive side)

### Conditional Formatting Strategy (Kolokolov)

Four methods available, each with a specific purpose:

**Data Bars** (most popular): Highlight leaders in numeric columns. Use lighter bar colors so the numbers remain readable against the bar background.

**Icons with Rules**: Show deviation from plan. Example: green circle (>= 0% deviation), yellow circle (-5% to 0%), red circle (< -5%). Use the same shape (circle) for all -- let color alone convey status.

**Font Color**: Highlight extreme values. Example: >= $300 = green font, < $100 = red font. Good for drawing attention without changing cell backgrounds.

**Cell Color / Heat Map**: Matrix visualization of intersecting dimensions. Gradient: central value = white, negative = red, positive = green.

**Restraint Rules:**
- Apply one formatting rule per column (not multiple)
- Don't format the entire table (target 1-2 columns max)
- Maintain data label contrast (numbers are primary, formatting is secondary)
- Boundaries should reflect business logic, not arbitrary percentiles

### Proportional Ink Principle (Wilke, Evergreen)

The area of a shaded region must be directly proportional to the data value it represents. This is the most commonly violated principle in corporate dashboards.

**Rule: Bar charts on a linear scale must start at zero.** When a y-axis starts at $50,000 instead of $0, differences appear 2-3x larger than reality. Research by Pandey et al. (2015) found distorted charts produced responses 58-130% larger than control charts with correct axes.

**Exceptions:**
- Line charts can use non-zero baselines (because perception is based on slope, not area)
- Logarithmic scales: use dots instead of bars (bars have no meaningful zero on log scale)
- Explicit deviation/change charts labeled as such

**Power BI action:** Verify axis settings after every edit. When custom axis ranges are set, document the business reason. Default axis behavior varies by chart type.

### Cognitive Science Principles

Understanding how the brain processes visual information helps you build dashboards that communicate faster and more accurately.

**Preattentive Attributes** -- visual properties processed in under 250ms (before conscious thought):
- **Color hue**: Stands out instantly. Use for categories or alerts.
- **Color intensity/saturation**: Draws attention to important values.
- **Size**: Larger elements are seen first. Use for primary KPIs.
- **Position**: Items at top-left get attention first (in LTR cultures).
- **Orientation**: A tilted element among straight ones pops out.
- **Shape**: Different shapes stand out, but use sparingly (shapes are weaker than color).

**Practical application:** If you want executives to notice a KPI immediately, make it large, colorful, and top-left. Don't rely on them reading labels.

**Gestalt Principles** -- how the brain groups visual elements:
- **Proximity**: Items close together are perceived as related. Group related visuals.
- **Similarity**: Items that look alike (same color, shape) are perceived as belonging together. Use consistent formatting for the same data type.
- **Enclosure**: Items inside a border/box are seen as a group. Use card backgrounds or subtle borders to group related metrics.
- **Connection**: Lines connecting items show relationships. Use sparingly for flow diagrams.
- **Continuity**: The eye follows smooth paths. Align visuals on a grid.

**Cognitive Load**:
- Limit working memory: 7 +/- 2 items is the practical limit for categories in a legend
- Reduce chart junk: Remove unnecessary gridlines, borders, 3D effects, and decorations
- Use direct labels instead of legends when possible (label the line, not the legend)
- Progressive disclosure: Show summary first, let users drill into detail

### Redundant Encoding for Accessibility (Wilke)

Never rely on color alone to distinguish data. 8% of males have red-green color blindness.

**Redundant coding strategies:**
- Scatterplots: Encode groups by BOTH color AND point shape
- Line charts: Label lines directly at their endpoints with colored text, rather than using a separate legend
- Match legend order to visual order (top-to-bottom in legend = top-to-bottom in chart)
- All critical distinctions must work in grayscale

**Direct labeling** (Wilke, Knaflic): Place category names directly next to data elements rather than using a separate legend box. This eliminates the cognitive cost of looking back and forth between the legend and the chart. In Power BI, use data labels positioned at line endpoints.

**Colorblind testing protocol:**
- View all dashboards in grayscale before publishing
- Use colorblind simulation tools (Coblis, Color Oracle)
- Use colorblind-safe palettes (Okabe-Ito, ColorBrewer "colorblind safe")

---

## Interactivity and Navigation

### Cross-Highlighting vs. Cross-Filtering

**Cross-Highlighting** (default)
- Click a bar, related data points highlight elsewhere
- Other visuals stay visible, nothing hides
- Use for exploratory analysis, showing relationships
- Less intrusive, users can see context

**Cross-Filtering**
- Click a bar, other visuals show only related data
- Isolates the selected segment
- Use when you want to focus on one thing
- Risk: Users forget they're filtered

Set interaction between visuals in the View ribbon:
- Select chart, go to Visual interactions
- For each other visual, choose Highlight, Filter, or None

### Drill-Through Pages

Create detail pages, then set drill-through:
1. Create a detail page (e.g., "Customer Details")
2. On summary page, right-click a visual field
3. Select "Add drill-through filter" (field becomes the drill-through field)
4. Add context fields to the detail page for the drilled value
5. Users right-click a data point and select "Drill through"

Example: Click a product in a sales chart, drill to product performance detail page with filters for that product.

### Bookmarks for Storytelling

Bookmarks capture the state of a report (filters, selections, visual state):
1. Set up your desired view (filters applied, visual highlighted)
2. View ribbon > Bookmarks pane > Add current state as bookmark
3. Name it descriptively ("Q4 Focus", "Top 10 Regions")
4. Add shapes or buttons that navigate to bookmarks
5. Create guided narratives: "Click here to see regional breakdown"

Use bookmarks for:
- Scenario analysis (What-if views)
- Guided narratives (step through a story)
- Report navigation (buttons to different views)

### Slicers: Placement and Types

**Placement**
- Top or left: Most visible, users expect filters there
- Float above visuals: Use for frequently changed filters
- Dedicated filter panel: Create a filter page, link others via bookmarks

**Types**
- Dropdown: Space-efficient, all values visible
- List: Quick scanning, good for small lists (5-10 items)
- Between/After: For date ranges or numeric ranges
- Relative date slicer: "Last 30 days", "Year to date"
- Buttons: One-click filters, good for binary choices

**Best Practice**: Hide "All" initially; let users select specific values.

### Tooltips

**Default tooltips** show field names and values on hover.

**Custom report page tooltips**:
1. Create a small page with visuals showing detail
2. Go to slicer/visual > Format > Tooltip > Tooltip page (set it)
3. When users hover, your custom page appears
4. Great for: Adding context, showing KPI benchmarks

Example: Hover over a sales number, see that month's top 5 customers.

---

## Advanced Analytics Visuals

### Decomposition Tree
Shows what drives a metric, by drilling into dimensions.

When to use:
- Root cause analysis (why did sales drop?)
- Feature importance (what matters most?)
- Hierarchical drill-down

Example: Drag "Total Sales" to value, add Reason, Region, Product to analyze. Click a node to split by next dimension.

Limitation: Works best with 3-4 levels, not suitable for exploration without hypotheses.

### Key Influencers
Identifies what factors have the strongest relationship with an outcome.

When to use:
- Identify drivers of high/low values
- Customer segmentation (what makes customers churn?)
- Marketing analysis (what influences conversion?)

Steps:
1. Analyze field: your metric (e.g., Sales)
2. Explain by: dimensions that might influence it
3. Power BI calculates statistical influence

Output: Left side shows top influencers; right side shows distribution for each influencer.

### Q&A Visual (DEPRECATED - Retiring December 2026)

The Q&A visual allowed users to type natural language questions about data. **It is now officially deprecated** and will be retired in December 2026.

**Migration path:** Copilot replaces Q&A functionality with richer natural-language capabilities including:
- Generating DAX formulas from natural language
- Creating entire report pages from descriptions
- Explaining what a visual shows
- Suggesting insights from data

**Action required:** If you have existing reports using the Q&A visual, plan to replace them with Copilot-powered alternatives before December 2026. Copilot requires F2+ capacity (or existing P1+ Premium capacity until P-SKU retirement in December 2026).

### Smart Narrative
Auto-generates text insights about your data.

When to use:
- Executive summaries (what changed month-over-month?)
- Accessibility (screen reader friendly)
- Quick takeaways without manual writing

Customize: Set which metrics to focus on, tone, language level.

---

## Custom Visuals

### AppSource Marketplace

Power BI AppSource offers hundreds of custom visuals. Access via Insert > Get More Visuals > From Organization or AppSource.

Popular Custom Visuals:

**Bullet Chart by OKViz**
- Shows actual vs. target vs. range
- Better than gauges for KPIs with ranges
- Example: Sales actual 80k vs. target 100k vs. range 60-120k

**Gantt by MAQ Software**
- Project timeline visualization
- Shows task duration, dependencies, milestones
- Use for: Project tracking, roadmaps, critical path

**Sankey by MAQ Software**
- Shows flow from one dimension to another
- Width of path represents volume
- Use for: Customer journeys, budget allocation, funnel analysis

**Zebra BI (by Zebra)**
- Variance analysis and planning
- Compact display of actual, plan, variance
- Use for: Financial reporting, budget vs. actual

**Sparkline by OKViz**
- Mini line chart in table cell
- Shows trend without cluttering dashboard
- Use for: Tables with trend context

### R and Python Visuals

Enable R/Python scripts in Power BI:
1. File > Options > Script visuals
2. Select R/Python home directories
3. In Insert, choose R script visual or Python script visual

Example R code:
```r
plot(dataset$Sales, dataset$Quantity,
     main="Sales vs Quantity",
     xlab="Sales", ylab="Quantity")
```

Use cases:
- Statistical plots (ggplot2 for R, matplotlib for Python)
- ML model predictions (scikit-learn)
- Custom analytics not available in standard visuals

---

## Paginated Reports

Paginated reports are pixel-perfect, table-driven reports. Use Power BI Report Builder (separate from Desktop).

### When to Use

**Choose Paginated Reports If**:
- You need exact page layouts (invoice printing, compliance documents)
- Reports are operational (run daily, export to files)
- Large datasets (table with 100k+ rows)
- Complex formatting (multi-column layouts, page headers/footers)

**Choose Interactive Reports (Desktop) If**:
- Users explore data interactively
- Reports are strategic (dashboards, KPIs)
- Visuals and interactivity are priorities
- Users access via Power BI Service

### Power BI Report Builder Basics

1. **Data Source**: Connect to Power BI datasets or direct database
2. **Tables/Matrices**: Drag fields to create tabular reports
3. **Expressions**: Use expressions like `=Fields!Sales.Value` for formulas
4. **Formatting**: Pixel-level control over fonts, spacing, borders
5. **Parameters**: Add user prompts (date range, region filter)
6. **Export**: Built for PDF, Excel, Word export

Example: Monthly statement report, one page per customer, printed/emailed automatically.

---

## Data Storytelling (Knaflic, Evergreen, Berinato)

### The "What's Your Point?" Principle (Evergreen)

The single most important question before designing any visualization. Write down your point BEFORE opening Power BI.

**Test:** Show the dashboard to someone unfamiliar with the data. Can they state the main insight in one sentence? If not, redesign.

### Insight-Driven Titles (Knaflic, Evergreen)

Replace generic titles with your actual finding:

- Bad: "Monthly Sales" or "Chart 1"
- Good: "Sales Dropped 15% in Q3 After Price Increase"
- Bad: "Student Survey Results"
- Good: "Students' College Expectations Trail Parent Expectations by 20 Points"

The title does the heavy lifting. A viewer who reads only the title should understand the key message.

### Narrative Structure (Knaflic)

Structure dashboards and presentations as stories:

1. **Setup/Hook**: What is the current situation? (KPIs, context)
2. **Conflict/Rising Action**: What changed or what's wrong? (trends, variances)
3. **Resolution/Call to Action**: What should we do about it? (recommendations, drill-throughs to detail)

### The "Gray Everything Else" Technique (Knaflic)

To draw attention to a specific data point: color that element in a strong accent color and set everything else to gray. This exploits preattentive processing -- the colored element pops out before conscious thought.

### When NOT to Visualize (Evergreen)

Sometimes the best visualization is no visualization:
- Data is highly variable with no clear pattern -- a chart adds noise, not clarity
- The message is a single number -- use a KPI card, not a chart
- A simple table communicates faster than a chart would
- The visualization obscures the point rather than clarifying it (e.g., a pie chart with 20 slices)

---

## Small Multiples Best Practices (Evergreen, Wilke)

Small multiples (the same chart repeated for each category) are one of the most powerful and underused techniques in Power BI.

**When to use:** When a single chart would have too many overlapping lines or bars (more than 4 series).

**Critical rules:**
- ALL panels must use the SAME axis ranges. Different scales per panel misrepresents relationships. (Wilke)
- Arrange panels in a logical order (alphabetical, by magnitude, or chronological)
- Label each panel clearly; don't rely on viewers to decode

**Power BI implementation:** Use the "Small multiples" field well on supported visuals (bar, column, line, area charts). Or use field parameters to let users toggle between categories.

---

## Slopegraph for Before/After Comparison (Evergreen)

A slopegraph shows paired values across exactly two time points or conditions, with lines connecting each pair.

**When to use:** Comparing rankings or values between two periods (e.g., donor retention rates 2024 vs. 2025 by program area). Shows both absolute values AND direction of change.

**Power BI implementation:** Not a native visual. Approximate using a line chart with exactly two X-axis data points, or use a custom visual from AppSource.

---

## Dashboard Construction Workflow (Kolokolov)

Step-by-step process for building professional dashboards:

1. **Define the grid** (2x2 or 3x2) before placing any visuals
2. **Place KPI cards on top** (max 6; these are key indicators, not all summary values)
3. **Add trend charts** in the middle zone (Level 2)
4. **Add detail tables** at the bottom (Level 3)
5. **Apply consistent font styling** across all elements
6. **Add conditional formatting** to deviation columns and key metrics
7. **Set page background color** (subtle off-white or light gray reduces eye strain vs. pure white)
8. **Add header shape block** to visually separate the title/filter area
9. **Test at actual display size** -- responsive mode auto-adjusts fonts, sometimes poorly

**Key principle:** Don't sacrifice overall logic for artistic finesse. A clear, well-organized dashboard with basic formatting beats a visually stunning one that's hard to navigate.

---

## Visual Calculations

Visual calculations (GA) let you add calculations directly on a visual without creating measures in the data model. They reference the visual's own data matrix.

### When to Use
- Running totals, percent of grand total, or rankings that are specific to one visual
- Calculations that depend on the visual's sort order or axis
- Quick ad-hoc analysis without modifying the shared data model

### How to Add
1. Select a visual
2. In the visual's value well, click **New visual calculation** (or use the icon)
3. Write a DAX-like expression using visual calculation functions

### Key Functions
- `RUNNINGSUM([Measure])` -- cumulative total along the axis
- `MOVINGAVERAGE([Measure], 3)` -- 3-period moving average
- `RANK([Measure])` -- rank within the visual
- `PERCENTOF([Measure])` -- percentage of grand total
- `PREVIOUS([Measure])` -- value from the previous row in the visual

### Limitations
- Cannot be used outside the visual they're defined on
- Not available for slicers, filters, or conditional formatting based on model
- More limited than full DAX measures -- no CALCULATE, no table functions

---

## Field Parameters for Dynamic Visuals

Field parameters let users dynamically swap measures or dimensions in a visual using a slicer.

### Setup
1. **Modeling > New Parameter > Fields**
2. Select the measures or columns to include
3. Power BI creates a slicer and a special table

### Use Cases
- Let users toggle a chart between Revenue, Cost, and Profit
- Let users switch the X-axis between Region, Product, and Sales Rep
- Dynamic legends that change what the color grouping represents

### Best Practices
- Limit to 5-7 options per parameter
- Label the slicer clearly so users understand what it controls
- Field parameters + calculation groups = very powerful combinations for financial reporting

---

## Visualization for Nonprofits and Development Context (Wolvius, Sosulski)

Visualization for nonprofits and international development organizations has specific considerations that differ from corporate BI.

### Audience Awareness
- Board members and donors need high-level impact stories, not granular data
- Field staff need operational detail they can act on immediately
- Government partners need evidence-based summaries for policy decisions
- Build different report pages (or apps) for each audience rather than one dashboard for all

### The Data Journey for Development (Wolvius)
1. **Design**: Define what you need to measure BEFORE collecting data
2. **Capture**: Collect with quality in mind (tools like KoboToolbox, ODK)
3. **Understand**: Clean and analyze (Power Query is ideal here)
4. **Act**: Present findings that drive decisions

### Impact Visualization Patterns
- Use before/after comparisons (baseline vs. current) to show program impact
- Geographic maps showing intervention coverage vs. need
- Trend lines showing progress toward program targets (with target line overlaid)
- Diverging bar charts showing actual vs. planned for each indicator
- Simple KPI cards for headline metrics (beneficiaries served, completion rates)

### Data Quality First (Wolvius)
Bad data produces misleading visualizations. The GIGO (Garbage In, Garbage Out) principle:
- Clean data in Power Query BEFORE building visuals
- Document data quality issues visibly (e.g., a "Data Quality" indicator on the dashboard)
- Missing data should be shown as gaps, not zeros (zeros imply measurement of zero, not absence of data)

---

## Mobile Layout

Power BI automatically creates a phone-optimized view. Customize it in Desktop.

### Design for Phone View

1. View > Mobile layout (shows phone-sized canvas)
2. Drag visuals onto phone canvas (limited space, 1-2 per screen)
3. Stack vertically (users scroll down)
4. Hide non-essential visuals
5. Make text large (users hold phone at arm's length)

### Mobile-Optimized Visuals

- Cards: Single metric, large text
- Small bar chart: 5-7 categories max
- Line chart: Trends, simplified
- Avoid: Complex matrices, small text, hover interactions

### Testing on Device

- Power BI Mobile app (iOS/Android)
- Emulator: Use browser dev tools (Ctrl+Shift+I, toggle device toolbar)
- Test all interactions: filters, drill-through, bookmarks

### Best Practices

- Phone view first, then desktop
- Remove filters on mobile (space-constrained)
- Use drill-through for detail instead of multiple pages
- Test with actual users on their phones
