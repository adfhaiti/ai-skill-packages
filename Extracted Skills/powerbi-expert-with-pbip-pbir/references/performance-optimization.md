# Performance Optimization Reference

## Table of Contents

1. [The Two Engines](#the-two-engines)
2. [VertiPaq Compression](#vertipaq-compression)
3. [Diagnostic Tools](#diagnostic-tools)
4. [DAX Optimization](#dax-optimization)
5. [Query Folding](#query-folding)
6. [Model Size Reduction](#model-size-reduction)
7. [Aggregations](#aggregations)
8. [Incremental Refresh](#incremental-refresh)
9. [Report Rendering Performance](#report-rendering-performance)
10. [Big Data Patterns](#big-data-patterns)
11. [Performance Checklist](#performance-checklist)

---

## The Two Engines

Power BI has two distinct engines. Nearly all performance issues fall into one camp or the other.

**Storage Engine**: Retrieves data from disk. In Import mode, this is VertiPaq (columnar, compressed, in-memory). In DirectQuery, it's the source database.

**Formula Engine**: Evaluates DAX expressions. CPU-bound. Evaluates iterators, FILTER calls, and complex business logic.

**How to diagnose**: Use Performance Analyzer to see query duration vs. rendering time. Long query times suggest a Storage Engine bottleneck. Long rendering times or slow interactivity suggest Formula Engine issues. DAX Studio's Server Timings tab breaks this down further.

---

## VertiPaq Compression

VertiPaq compresses data at the column level using two encoding methods.

**Dictionary Encoding**: Unique values are stored once, and rows store references (integers) to dictionary entries. Low-cardinality columns compress extremely well.

**Value Encoding**: For high-cardinality columns, values are stored with run-length or frequency encoding.

**Why it matters**: A column with 2 million rows but only 50 unique values compresses to roughly the size of a few KB, not MB.

**Practical optimization steps**:

- Use integer keys instead of text keys. `CustomerID` (int) compresses far better than `CustomerName`.
- Remove unnecessary columns. Every column in a fact table consumes memory, even if unused in reports.
- Split date-time columns. A single `DateTime` column has high cardinality. Split into separate `Date` and `Time` columns.
- Disable auto date/time tables. Power BI creates hidden date tables for every date column by default. Disable this in options (File > Options and settings > Options > Data Load > Time Intelligence > uncheck "Auto date/time").
- Remove audit/system columns like `CreatedBy`, `ModifiedDate`, `ETLBatchID`.
- Use summarization instead of detail where possible. If you only ever sum a column, don't store individual values.

**Example**: A fact table with 50 million rows and columns `OrderDate` (100K unique values), `OrderTime` (86K unique values) compresses poorly. Splitting to `Date` (5K unique) and `Hour` (24 unique) reduces memory by 60%+.

---

## Diagnostic Tools

### Performance Analyzer

Built into Power BI Desktop. Shows query time, render time, and visual-level breakdown.

**How to use**: Home tab > Performance Analyzer > Start recording > interact with the report. Logs milliseconds for each visual.

**What it tells you**: If query time dominates, the Storage Engine is the bottleneck. If render time is high, focus on Formula Engine or visual complexity.

### DAX Studio

External tool. Connects to Power BI Desktop or SSAS. Provides deep query analysis.

**Key features**:
- Server Timings tab: CPU time, query plan, formula evaluation time.
- VertiPaq Analyzer: See exactly how much memory each column consumes.
- Trace query execution.

**When to use**: Investigating slow DAX measures, understanding memory usage by column, tracing formula evaluation.

### Tabular Editor

External tool. Includes Best Practice Analyzer for model optimization.

**Key features**:
- Identifies unused columns, redundant relationships, missing aggregations.
- Shows calculated column vs. measure trade-offs.
- Bulk editing for multiple objects.

**When to use**: Model optimization, best practice enforcement, bulk updates.

### ALM Toolkit

Version control and deployment tool.

**When to use**: Comparing model changes across versions, identifying orphaned tables/columns.

---

## DAX Optimization

### Avoid Unnecessary FILTER Calls

**Slow (FILTER approach)**:
```dax
Total Sales := 
SUMX(
    FILTER(ALL(Sales), Sales[Year] = 2025),
    Sales[Amount]
)
```

**Fast (CALCULATE with direct predicate)**:
```dax
Total Sales 2025 := 
CALCULATE(
    SUM(Sales[Amount]),
    Sales[Year] = 2025
)
```

FILTER iterates every row. CALCULATE uses index lookups when possible.

### Use Variables to Prevent Re-evaluation

**Slow (evaluated twice)**:
```dax
Total := 
CALCULATE(SUM(Sales[Amount])) + 
CALCULATE(SUM(Sales[Amount])) * 0.1
```

**Fast (evaluated once)**:
```dax
Total := 
VAR BaseAmount = CALCULATE(SUM(Sales[Amount]))
RETURN BaseAmount + BaseAmount * 0.1
```

### Prefer SUMMARIZECOLUMNS over SUMMARIZE

**Slower**:
```dax
SUMMARIZE(Sales, Sales[Region], "Total", SUM(Sales[Amount]))
```

**Faster**:
```dax
SUMMARIZECOLUMNS(Sales[Region], "Total", SUM(Sales[Amount]))
```

SUMMARIZECOLUMNS is optimized for grouping and aggregation. SUMMARIZE adds unnecessary context rows.

### Avoid Nested Iterators

**Slow**:
```dax
Total := SUMX(Customers, SUMX(RELATEDTABLE(Orders), Orders[Amount]))
```

**Better**:
```dax
Total := SUMPRODUCT(Orders[Amount])
```

Or use CALCULATE to cross tables.

### KEEPFILTERS vs. Replacing Filters

**Replacing filters (default)**:
```dax
CALCULATE(SUM(Sales[Amount]), Sales[Region] = "West")
```

Clears all filters on Sales[Region], then applies the new one.

**Keeping filters**:
```dax
CALCULATE(SUM(Sales[Amount]), KEEPFILTERS(Sales[Region] = "West"))
```

Adds to existing filters. More efficient if a filter is already applied.

### DISTINCTCOUNT Optimization

DISTINCTCOUNT is one of the most expensive DAX operations. When VertiPaq evaluates DISTINCTCOUNT, it uses a mechanism called CallbackDataID to track unique values across filter intersections.

**Why it's slow:** Each filter combination requires a full distinct-value scan. A visual with 3 slicers and a matrix creates hundreds of filter combinations, each needing its own DISTINCTCOUNT evaluation.

**Optimization strategies:**

1. **Use integer keys instead of text:**
```dax
// Slow: text column with high cardinality
Unique Customers = DISTINCTCOUNT(Sales[CustomerName])

// Fast: integer key column
Unique Customers = DISTINCTCOUNT(Sales[CustomerID])
```

2. **Pre-aggregate when possible:**
```dax
// Instead of DISTINCTCOUNT in a complex context...
// Create an aggregation table with pre-computed distinct counts
// Then use SUM on the pre-aggregated column
```

3. **Avoid DISTINCTCOUNT inside iterators:**
```dax
// BAD: DISTINCTCOUNT inside SUMX
BadPattern = SUMX(Products, DISTINCTCOUNT(Sales[CustomerID]))

// BETTER: Use CALCULATE with appropriate filters
BetterPattern =
COUNTROWS(
    SUMMARIZE(Sales, Sales[CustomerID], Sales[ProductID])
)
```

4. **Consider APPROXIMATEDISTINCTCOUNT for DirectQuery:** Available only in DirectQuery mode, this function uses HyperLogLog for approximate counts with much better performance on very large datasets.

---

## Query Folding

Query folding is the ability of Power Query (M) to push transformations back to the source database. If folding breaks, the entire dataset is imported, then transformed in Power BI (expensive).

**Brief cross-reference**: See `power-query-m.md` for detailed M optimization.

**Operations that break folding**:
- Custom columns written in M without native SQL equivalents.
- Changing column data type after grouping.
- Adding index columns after filtering.
- UNION operations on tables from different sources.

**Impact**: A 500 million-row table with broken folding loads 500M rows into memory. With folding, the database returns only aggregated or filtered results.

**Quick win**: In Power Query, check the formula bar. If the step shows "Source" (or query name), folding is active. If it shows "Added Custom", "Merged", or similar, folding may be broken. Right-click the step and select "Delete Applied Steps" beyond where folding is active.

---

## Model Size Reduction

Smaller models load faster, refresh faster, and require less premium capacity.

**Priority actions**:

1. **Remove unused columns**. If a column isn't in a measure, slicer, or visual, delete it. Fact tables often have 50+ columns, but only 20 are used.

2. **Reduce cardinality**. Create a `DateKey` (integer) instead of `DateString` (text). Use lookups for descriptions in dimension tables.

3. **Use integer keys**. `CustomerID` (4 bytes) compresses better than `Customer_Name_Text` (50 bytes).

4. **Disable auto date/time tables**. These hidden tables balloon the model.

5. **Remove audit columns**: `CreatedDate`, `CreatedBy`, `ModifiedDate`, `ETLBatchID`, `SourceSystem`.

6. **Split date-time columns**. `2025-04-05 14:32:15` (high cardinality) becomes `Date: 2025-04-05` (5K unique) and `Time: 14:32` (1440 unique).

**Example**: A 500 MB model with 30 unused columns in a 100M-row fact table can drop to 250 MB by removing those columns.

---

## Aggregations

Aggregation tables are pre-calculated summaries that Power BI queries before hitting detail data. Critical for large datasets.

**Pattern**: Detail table in DirectQuery, aggregation table in Import.

**Setup steps**:

1. Create a summary table in your source database (e.g., `Sales_Monthly_Summary` with `Year`, `Month`, `Region`, `TotalAmount`, `TotalQuantity`).
2. Import the summary table into Power BI.
3. In Power BI, go to **Manage aggregations** (right-click table > Aggregations).
4. Map each aggregation column to its source column and aggregation function.
5. Set the aggregation table to have a DirectQuery relationship to the detail table.

**Automatic vs. user-defined**: Power BI can suggest aggregations based on your queries. Enable suggestions in Options > Power BI Desktop > Options > Preview features > Automatic aggregations. Review and accept/reject suggestions.

**Impact**: Queries against monthly data return in milliseconds instead of seconds. Drill-through to detail remains available.

---

## Incremental Refresh

Incremental refresh loads only new/changed data, skipping the full historical load.

**How it works**: You define a date column and two parameters: `RangeStart` (minimum date) and `RangeEnd` (maximum date). Power BI loads data where `DateColumn > RangeStart AND DateColumn <= RangeEnd`, then appends to existing partitions.

**Configuration steps**:

1. In Power Query, create a source query that accepts two parameters: `RangeStart` and `RangeEnd` (both datetime type, default to `Date.AddYears(Date.From(DateTime.LocalNow()), -10)` and `Date.From(DateTime.LocalNow())`).

2. Filter your data: `Table.SelectRows(Source, each [DateColumn] > RangeStart AND [DateColumn] <= RangeEnd)`.

3. In Power BI Desktop, go to **Refresh > Configure incremental refresh**.

4. Specify:
   - Date column (e.g., `OrderDate`).
   - Years to store historically (e.g., 3 full years).
   - Days to store incrementally (e.g., 10 days).

5. Publish to Power BI Premium. Scheduled refreshes now load only the last 10 days + append to the last 3 years' partitions.

**When to use**: Tables with 50M+ rows and a reliable date column. Not suitable for tables without a monotonic date.

**Partition management**: Power BI automatically creates partitions. You can view them in Tabular Editor > Partitions. Each partition has its own load range.

---

## Report Rendering Performance

Slow reports often have too many visuals or overly complex ones.

**Visual count**: Aim for 15-20 visuals per page maximum. Each visual queries the model and renders. 50+ visuals per page will feel sluggish.

**Complex visuals**:
- Scatter plots with 100K+ data points. Limit to 5K-10K points or use aggregation.
- Dendrograms with nested hierarchies. Flatten or use separate pages.
- Maps with thousands of individual markers. Use filled maps or clustering.

**Excessive cross-filtering**: If every slicer filters 10 visuals, the model recalculates 10x. Use page-level filters or grouped slicers instead.

**Visual-level vs. page-level filters**: Visual-level filters apply context only to one visual. Page-level filters apply to all visuals on the page. Page-level is slightly more efficient.

**Progressive rendering**: Enable in File > Options > Current file > Performance analyzer. Reports render visuals one at a time instead of waiting for all to compute.

**Visual calculations (preview):** Visual calculations let you add DAX-like expressions directly on a visual (running totals, percent of total, rankings) without creating model measures. They compute client-side and can reduce the number of model queries. Use them for visual-specific calculations that don't need to be reused across reports.

---

## Big Data Patterns

### Composite Models

Mix real-time DirectQuery data with cached Import data.

**Example**: Source system sales (DirectQuery, always current) + budget forecast (Import, calculated weekly).

```
Sales Table (DirectQuery)
    |
    +--- Relationship ---
    |
Budget Table (Import)
```

Query both in a single visual. Power BI handles joining and filtering.

### DirectQuery with Aggregation Tables

Pair a DirectQuery detail table with Import summary tables.

```
Sales Detail (DirectQuery, 1B rows)
    |
    +--- Aggregation ---
    |
Sales Monthly (Import, 12K rows)
```

Small queries go to the summary. Drill-through queries hit detail.

### Dataflows

Stage data transformation in a shared, reusable layer.

**Benefits**: Transform once, use in multiple datasets. Schedule independently from reports. Reduce refresh load on source systems.

### Partitioning Strategies

- **Time-based**: Partitions by year or month. Older partitions are read-only.
- **Range-based**: Numeric range (e.g., Customer IDs 1-100K, 100K-200K).
- **Hybrid**: Combine time and range.

Use in conjunction with Incremental Refresh for large fact tables.

### Direct Lake (Fabric)

Direct Lake is a Fabric-exclusive storage mode that reads Delta/Parquet files directly from OneLake without importing data into VertiPaq.

**Performance characteristics:**
- Near-Import speed for queries that fit in memory
- Automatic fallback to DirectQuery when data exceeds the SKU's memory limit
- V-Order optimization in Delta tables significantly improves read performance
- No refresh needed -- reads current data directly from the lakehouse

**Optimization tips:**
- Apply V-Order when writing to Delta tables (default in Fabric notebooks)
- Partition large tables by date for efficient pruning
- Monitor "Direct Lake fallback" events in capacity metrics -- frequent fallbacks indicate the data exceeds memory limits
- Consider upgrading SKU or reducing table size if fallbacks are frequent
- Row groups in Parquet files should be 1M rows for optimal performance

---

## Performance Checklist

1. [ ] Run Performance Analyzer on each report page. Identify visuals taking >1 second.
2. [ ] Reduce visual count to 15-20 per page.
3. [ ] Limit scatter plot data points to 5K-10K.
4. [ ] Disable auto date/time tables (File > Options > Data Load).
5. [ ] Remove unused columns (especially from fact tables).
6. [ ] Split date-time columns into separate Date and Time columns.
7. [ ] Use integer keys instead of text keys for relationships.
8. [ ] Remove audit/system columns (CreatedBy, ModifiedDate, ETLBatchID).
9. [ ] Run Tabular Editor Best Practice Analyzer and fix high-priority issues.
10. [ ] Check query folding in Power Query; delete steps that break it.
11. [ ] Use CALCULATE instead of FILTER where possible in DAX.
12. [ ] Use variables to avoid re-evaluation of expensive DAX expressions.
13. [ ] Replace SUMMARIZE with SUMMARIZECOLUMNS in new measures.
14. [ ] Open DAX Studio and check VertiPaq Analyzer for memory hogs.
15. [ ] Create aggregation tables for tables >100M rows.
16. [ ] Set up Incremental Refresh for large fact tables (>50M rows).
17. [ ] Enable progressive rendering for reports with many visuals.
18. [ ] Review and optimize DirectQuery data sources.
19. [ ] Test refresh times in a staging environment before production.
20. [ ] Document model design decisions and optimization rationale.
21. [ ] For DISTINCTCOUNT measures, verify the target column uses integer keys (not text).
22. [ ] If using Fabric Direct Lake, monitor fallback events and apply V-Order to Delta tables.
