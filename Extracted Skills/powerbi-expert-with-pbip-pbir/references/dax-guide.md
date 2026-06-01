# DAX Reference Guide: Power BI Expert

A practical, expert-level DAX reference for building performant Power BI models.

## 1. Evaluation Contexts

The foundation of DAX. Two contexts control value evaluation:

**Filter Context**: The set of filters applied (slicers, visual filters, CALCULATE arguments)
**Row Context**: Current row during iteration (SUMX, calculated columns)

### Filter Context Flow Diagram

```
Slicer: Year = 2024
    |
    v
[Dimension Table: Calendar]
    |
    v (Relationship:Foreign Key)
[Fact Table: Sales]
    |
    v
Filtered rows in fact table
ONLY rows matching Year = 2024
are available for aggregation
```

### Context Transition

When you reference a column from a row context inside an aggregation function, DAX transitions row context to filter context:

```dax
// Calculated Column (Row Context Active)
= [SalesAmount] * [Quantity]  // Simple math, no transition needed

// But inside an aggregator, transition occurs:
= SUM(Sales[Amount])  // DAX treats this as: CALCULATE(SUM(Sales[Amount]), ALL(Sales))
// The ALL() happens automatically - row context is LOST
```

### How CALCULATE Modifies Context

CALCULATE is the context modifier. It:
1. Removes existing filter context
2. Evaluates filter arguments
3. Applies new filters to the expression

```
CALCULATE(SUM(Sales[Amount]), Calendar[Year] = 2024)
    |
    +-- Removes all existing filters on Calendar table
    |
    +-- Evaluates Calendar[Year] = 2024 in the current context
    |
    +-- Applies ONLY this filter to Sales table
    |
    v
Aggregates Sales[Amount] where Year = 2024
(Previous slicers on Year are overridden, not combined)
```

## 2. CALCULATE and CALCULATETABLE

The most important function in DAX.

### Core Concept

```dax
CALCULATE(
    <expression>,
    <filter1>,
    <filter2>,
    ...
)

// What it does:
// 1. Modifies filter context for the expression
// 2. All filter arguments use AND logic (all must be true)
// 3. Filters override existing context (except with KEEPFILTERS)
```

### Filter Argument Evaluation Order

Critical for complex formulas:

```dax
VAR FilterValue = 100

CALCULATE(
    SUM(Sales[Amount]),
    Sales[Amount] > FilterValue    // Evaluated FIRST in current context
)
// Syntax: CALCULATE(expr, filter1, filter2, filter3...)
// Order: Filter1, Filter2, Filter3 evaluated left-to-right
// Each filter sees results of previous filters
```

### Override vs. Add Filters

```dax
// OVERRIDE (default behavior)
= CALCULATE(
    SUM(Sales[Amount]),
    Calendar[Year] = 2024          // Replaces Year filter
)
// If slicer already filters to 2023, this OVERRIDES to 2024

// ADD FILTERS (with KEEPFILTERS)
= CALCULATE(
    SUM(Sales[Amount]),
    KEEPFILTERS(Calendar[Year] = 2024)  // Combines with existing Year filter
)
// If slicer filters to 2023, result is empty (2023 AND 2024 = impossible)
```

### Common CALCULATE Patterns

```dax
// Year-to-date sales
YTDSales =
VAR CurrentDate = MAX(Calendar[Date])
VAR YearStart = DATE(YEAR(CurrentDate), 1, 1)
RETURN
    CALCULATE(
        SUM(Sales[Amount]),
        Calendar[Date] >= YearStart,
        Calendar[Date] <= CurrentDate
    )

// Sales for selected product, all time periods
ProductTotal =
CALCULATE(
    SUM(Sales[Amount]),
    ALL(Calendar)    // Remove all date filters
)

// Percent of total (combines contexts)
PercentOfTotal =
DIVIDE(
    SUM(Sales[Amount]),
    CALCULATE(
        SUM(Sales[Amount]),
        ALL(Dimension)   // All dimensions except current context
    )
)
```

## 3. Variables (VAR/RETURN)

Improves readability, debugging, and performance.

### Syntax and Behavior

```dax
MeasureName =
VAR IntermediateValue1 = <expression1>
VAR IntermediateValue2 = <expression2>
RETURN
    <expression_using_vars>

// Variables are lazy-evaluated:
// Each VAR is calculated ONLY when used in RETURN
// If a VAR is never used, it's never calculated
```

### Before/After Example

```dax
// WITHOUT variables (hard to debug, may calculate twice)
= DIVIDE(
    CALCULATE(SUM(Sales[Amount]), Calendar[Year] = 2024),
    CALCULATE(SUM(Sales[Amount]), Calendar[Year] = 2023)
)

// WITH variables (clean, calculates once each)
= 
VAR Sales2024 = CALCULATE(SUM(Sales[Amount]), Calendar[Year] = 2024)
VAR Sales2023 = CALCULATE(SUM(Sales[Amount]), Calendar[Year] = 2023)
RETURN
    DIVIDE(Sales2024, Sales2023)
```

### Performance Benefit

Variables prevent re-evaluation of identical expressions:

```dax
// This calculates the SUM four separate times (inefficient)
= SUM(...) + SUM(...) * SUM(...) / SUM(...)

// Variables ensure one calculation each (efficient)
VAR TotalSales = SUM(...)
RETURN
    TotalSales + TotalSales * TotalSales / TotalSales
```

## 4. Time Intelligence

Requires proper date table setup (marked as date table in Power BI).

### Date Table Requirements

```
Date column must:
- Be continuous (no gaps)
- Span entire analysis period
- Have no duplicate dates
- Be marked as "Date Table" in Power BI

Recommended columns:
- [Date] (primary key)
- [Year], [Quarter], [Month], [Day]
- [YearMonth] (for sorting)
- [IsCurrentMonth], [IsCurrentYear] (for highlighting)
```

### Year-to-Date, Quarter-to-Date, Month-to-Date

```dax
// Year-to-Date
SalesYTD =
VAR CurrentDate = MAX(Calendar[Date])
VAR YearStart = DATE(YEAR(CurrentDate), 1, 1)
RETURN
    CALCULATE(
        SUM(Sales[Amount]),
        Calendar[Date] >= YearStart,
        Calendar[Date] <= CurrentDate
    )

// Quarter-to-Date
SalesQTD =
VAR CurrentDate = MAX(Calendar[Date])
VAR QuarterStart = DATE(YEAR(CurrentDate), (QUARTER(CurrentDate) - 1) * 3 + 1, 1)
RETURN
    CALCULATE(
        SUM(Sales[Amount]),
        Calendar[Date] >= QuarterStart,
        Calendar[Date] <= CurrentDate
    )

// Month-to-Date
SalesMTD =
VAR CurrentDate = MAX(Calendar[Date])
VAR MonthStart = DATE(YEAR(CurrentDate), MONTH(CurrentDate), 1)
RETURN
    CALCULATE(
        SUM(Sales[Amount]),
        Calendar[Date] >= MonthStart,
        Calendar[Date] <= CurrentDate
    )
```

### Year-over-Year and Same Period Last Year

```dax
// Sales for same period last year
SalesLastYear =
VAR CurrentDate = MAX(Calendar[Date])
VAR LastYearDate = DATE(YEAR(CurrentDate) - 1, MONTH(CurrentDate), DAY(CurrentDate))
RETURN
    CALCULATE(
        SUM(Sales[Amount]),
        Calendar[Date] = LastYearDate
    )

// Year-over-Year comparison
YoYGrowth =
VAR CurrentSales = SUM(Sales[Amount])
VAR PriorSales = CALCULATE(
    SUM(Sales[Amount]),
    DATEADD(Calendar[Date], -1, YEAR)
)
RETURN
    DIVIDE(CurrentSales - PriorSales, PriorSales)
```

### Rolling Averages

```dax
// 12-month rolling average
RollingAverage12M =
VAR CurrentDate = MAX(Calendar[Date])
VAR Start12MBack = DATE(YEAR(CurrentDate) - 1, MONTH(CurrentDate), 1)
RETURN
    CALCULATE(
        AVERAGE(Sales[Amount]),
        Calendar[Date] >= Start12MBack,
        Calendar[Date] <= CurrentDate
    )
```

## 5. Iterator Functions

Create row context and iterate through tables. Each row evaluates independently.

### Common Iterators: SUMX, AVERAGEX, COUNTX

```dax
// SUMX: Sum with custom expression
TotalRevenue =
SUMX(
    Sales,                           // Table to iterate
    Sales[Quantity] * Sales[Price]   // Expression per row
)

// AVERAGEX: Average of expression
AverageOrderValue =
AVERAGEX(
    Sales,
    Sales[Amount] / Sales[Quantity]
)

// COUNTX: Count non-blank results
CountOrders =
COUNTX(
    Sales,
    Sales[OrderID]
)
```

### Context Transition in Iterators

```dax
// Row context is active inside iterator expression
// References to other tables cause context transition

ItemExtendedPrice =
SUMX(
    OrderItems,
    OrderItems[Quantity] * 
    RELATED(Products[UnitPrice])     // Context transition: gets price for THIS row's product
)
```

### Nested Iterators (Use Carefully)

```dax
// SLOW: Nested iterators create O(n^2) complexity
= SUMX(Customers, SUMX(Orders, Orders[Amount]))

// BETTER: Pre-filter the inner table
= SUMX(
    Customers,
    SUMX(
        FILTER(Orders, Orders[CustomerID] = Customers[CustomerID]),
        Orders[Amount]
    )
)
```

## 6. Table Functions

Return tables rather than scalars. Used with other functions or directly in visuals.

### Fundamental Table Functions

```dax
// FILTER: Return subset of table matching condition
TopProducts = FILTER(Products, Products[Sales] > 10000)

// ALL/ALLEXCEPT: Remove filters
// ALL: Return all rows, ignoring all filters
AllProductsSales = CALCULATE(SUM(Sales[Amount]), ALL(Products))

// ALLEXCEPT: All rows except specific columns
AllProductsExceptCategory = 
CALCULATE(
    SUM(Sales[Amount]),
    ALLEXCEPT(Products, Products[Category])
)

// VALUES: Unique values in current filter context
CurrentCategories = VALUES(Products[Category])

// DISTINCT: Unique values from expression
DistinctDates = DISTINCT(Calendar[Date])
```

### Advanced Table Functions

```dax
// SUMMARIZE: Group by columns, aggregate values
CategorySummary = 
SUMMARIZE(
    Sales,
    Products[Category],          // Group by
    "TotalSales", SUM(Sales[Amount]),
    "ItemCount", COUNTX(Sales, Sales[OrderID])
)

// ADDCOLUMNS: Add calculated columns to table
EnhancedSales =
ADDCOLUMNS(
    Sales,
    "ExtendedPrice", [Quantity] * [Price],
    "ProfitMargin", DIVIDE([Profit], [Sales])
)

// UNION: Combine tables with same structure
AllRevenue = UNION(
    SUMMARIZE(Sales, Products[Category], "Amount", SUM(Sales[Amount])),
    SUMMARIZE(Returns, Products[Category], "Amount", SUM(Returns[Amount]))
)
```

## 7. Calculated Columns vs. Measures

Know when to use each.

### The Rule

| | Calculated Columns | Measures |
|---|---|---|
| **When to use** | Dimension attributes, static lookup values | Dynamic aggregations based on filters |
| **Row context** | Yes - can reference current row | No - use SUMX if needed |
| **Filter context** | Weak - sees only table filters | Strong - sees all filters |
| **Performance** | Stored in model (memory cost) | Calculated on demand |
| **Use on fact tables** | NEVER (bloats model) | Always |
| **Example** | Product[Category], Customer[Segment] | Total Sales, Avg Order Value |

### Anti-Pattern: Calculated Columns on Fact Tables

```dax
// BAD: This calculated column stores a value for EVERY sales row
Sales[IsCurrentMonth] = 
MONTH(Sales[Date]) = MONTH(TODAY())
// If Sales has 10M rows, this wastes 10M boolean values in memory
// Same logic in a measure uses zero additional memory

// GOOD: Use a measure instead
IsCurrentMonth = 
CALCULATE(
    COUNTROWS(Sales),
    MONTH(Sales[Date]) = MONTH(TODAY())
) > 0
```

### Good Calculated Column Example

```dax
// Product[DisplayName] - Belongs on dimension table, small cardinality
Product[DisplayName] = 
Product[Name] & " (" & Product[SKU] & ")"
// Few hundred rows: acceptable memory cost
// Improves user experience and model clarity
```

## 8. Common Patterns

Ready-to-use patterns for frequent scenarios.

### Percentage of Total

```dax
PercentOfTotal =
VAR Total = CALCULATE(
    SUM(Sales[Amount]),
    ALL(Products),           // All products
    ALL(Customers)           // All customers
)
RETURN
    DIVIDE(SUM(Sales[Amount]), Total)
```

### Percentage of Parent (Hierarchical)

```dax
PercentOfCategory =
VAR CategoryTotal = CALCULATE(
    SUM(Sales[Amount]),
    ALL(Products[SubCategory])  // Same category only
)
RETURN
    DIVIDE(SUM(Sales[Amount]), CategoryTotal)
```

### Running Total

```dax
RunningTotal =
VAR CurrentDate = MAX(Calendar[Date])
RETURN
    CALCULATE(
        SUM(Sales[Amount]),
        Calendar[Date] <= CurrentDate,
        ALL(Calendar[Date])
    )
```

### ABC Analysis (Pareto)

```dax
// Rank products by sales
ProductRank = RANKX(
    ALL(Products),
    CALCULATE(SUM(Sales[Amount])),
    ,
    DESC
)

// Mark top 20% as "A", next 30% as "B", rest as "C"
ABCCategory =
VAR Rank = [ProductRank]
VAR TotalProducts = COUNTA(ALL(Products[ProductID]))
VAR Top20Percent = INT(TotalProducts * 0.2) + 1
VAR Top50Percent = INT(TotalProducts * 0.5) + 1
RETURN
    IF(Rank <= Top20Percent, "A",
    IF(Rank <= Top50Percent, "B", "C"))
```

## 9. Common Anti-Patterns

Mistakes that kill performance or cause bugs.

### Anti-Pattern 1: Overusing ALL()

```dax
// BAD: Removes ALL context, usually not what you want
BadTotal = CALCULATE(SUM(Sales[Amount]), ALL())  // Removes EVERYTHING

// GOOD: Remove only what you need
GoodTotal = CALCULATE(
    SUM(Sales[Amount]),
    ALL(Calendar)  // Remove date filters, keep product filters
)
```

### Anti-Pattern 2: Nested FILTER Calls

```dax
// BAD: O(n^2) complexity, very slow on large tables
BadFiltered = FILTER(
    Products,
    COUNTX(FILTER(Sales, Sales[ProductID] = Products[ProductID]), Sales[Amount]) > 100
)

// GOOD: Use SUMMARIZE or aggregate first
GoodFiltered = 
VAR ProductSalesCount = SUMMARIZE(Sales, Sales[ProductID], "Count", COUNTX(Sales, Sales[Amount]))
RETURN
    FILTER(ProductSalesCount, [Count] > 100)
```

### Anti-Pattern 3: Conflicting CALCULATE Filters

```dax
// BAD: These filters conflict (product can't be A AND B)
Conflicting = CALCULATE(
    SUM(Sales[Amount]),
    Products[Category] = "Electronics",
    Products[Category] = "Clothing"
)
// Result: Always 0

// GOOD: Use OR logic with FILTER
Correct = CALCULATE(
    SUM(Sales[Amount]),
    FILTER(Products, Products[Category] = "Electronics" || Products[Category] = "Clothing")
)
```

### Anti-Pattern 4: RELATED Instead of RELATEDTABLE

```dax
// In Sales table (fact), calculating related dimension value
// GOOD: Get single product name
ProductName = RELATED(Products[ProductName])

// But in Products table, getting related sales
// BAD: This won't work - RELATED only returns one value
TotalSales = RELATED(SUM(Sales[Amount]))  // FAILS

// GOOD: Use SUMX with calculated column, or measure
// (Measures are better for fact tables)
// In a measure:
TotalSalesForProduct = CALCULATE(SUM(Sales[Amount]), ALLEXCEPT(Products, Products[ProductID]))
```

## 10. Debugging DAX

Systematic approach to finding issues.

### DAX Studio Evaluation

```
// Use EVALUATE to test table expressions
EVALUATE
FILTER(Sales, Sales[Amount] > 1000)

// Returns sample of 1000 rows matching filter
// Great for testing FILTER, SUMMARIZE, CALCULATE logic
```

### Step-by-Step Context Diagnosis

```dax
// Create diagnostic measures to understand context at each step

// Step 1: What filters are active?
ActiveFilters = CONCATENATEX(VALUES(Calendar[Year]), Calendar[Year], ", ")

// Step 2: What table rows match the filter?
RowsInContext = COUNTROWS(Sales)

// Step 3: What is the raw aggregation?
RawSum = SUM(Sales[Amount])

// Step 4: After CALCULATE, what changed?
AdjustedSum = CALCULATE(SUM(Sales[Amount]), Calendar[Year] = 2024)

// Step 5: Is context transition happening?
ContextTransitionTest = CALCULATE(
    SUM(Sales[Amount]),
    ALL(Sales)  // This reveals if row context was converted
)
```

### Performance Analyzer

```
Power BI Desktop > View > Performance Analyzer > Start Recording

Then interact with your report:
- Analyze which visuals are slow
- Identify DAX measures taking excessive time
- Look for unexpected CALCULATE operations

General targets:
- Visual queries: < 1 second
- Measure calculations: < 100ms
- Iterators on 1M+ rows: Probably slow, optimize
```

## 11. TREATAS (Virtual Relationships)

TREATAS applies filter context from one table to another WITHOUT a physical relationship. Useful when you can't or shouldn't create a model relationship.

### Syntax

```dax
TREATAS(
    <table_expression>,
    <column1>,
    <column2>,
    ...
)
```

### Common Use Cases

**Filtering across unrelated tables:**
```dax
Budget vs Actual =
VAR ActualSales = SUM(Sales[Amount])
VAR BudgetAmount =
    CALCULATE(
        SUM(Budget[Amount]),
        TREATAS(VALUES(Calendar[Date]), Budget[BudgetDate])
    )
RETURN
    ActualSales - BudgetAmount
```

**Role-playing dimensions without inactive relationships:**
```dax
Ship Date Sales =
CALCULATE(
    SUM(Sales[Amount]),
    TREATAS(VALUES(Calendar[Date]), Sales[ShipDate])
)
```

**When to use TREATAS vs. physical relationships:**
- Use physical relationships for permanent, well-defined connections
- Use TREATAS for ad-hoc analysis, budget vs. actual scenarios, or when adding a relationship would create ambiguity
- TREATAS is slower than physical relationships for large tables -- use it for targeted measures, not as a model design shortcut

---

## 12. Calculation Groups

Calculation groups let you define reusable calculation logic (like time intelligence) that can be applied to ANY measure dynamically. They replace the need to create dozens of "Sales YTD", "Cost YTD", "Revenue YTD" measures.

### Concept

A calculation group is a special table with calculation items. Each item modifies whatever measure the user selects.

**Example calculation group: "Time Intelligence"**

| Calculation Item | Expression |
|---|---|
| Current | SELECTEDMEASURE() |
| YTD | CALCULATE(SELECTEDMEASURE(), DATESYTD(Calendar[Date])) |
| PY | CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR(Calendar[Date])) |
| YoY % | VAR Current = SELECTEDMEASURE() VAR Prior = CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR(Calendar[Date])) RETURN DIVIDE(Current - Prior, Prior) |

**How it works:** The user places "Total Sales" on a visual and adds the Time Intelligence column to rows/columns. Each row shows Total Sales modified by the calculation item (Current, YTD, PY, YoY %).

### Creating Calculation Groups

Calculation groups cannot be created in Power BI Desktop UI. Use **Tabular Editor** (free or paid):

1. Open Tabular Editor, connect to your model
2. Right-click Tables > Create New > Calculation Group
3. Name the group (e.g., "Time Intelligence")
4. Add calculation items with SELECTEDMEASURE() expressions
5. Save and refresh in Power BI Desktop

### Key Rules
- SELECTEDMEASURE() returns whatever measure is in the current context
- Calculation groups apply to ALL measures unless you use ISSELECTEDMEASURE() to target specific ones
- Precedence matters when multiple calculation groups interact -- set the Precedence property to control evaluation order
- Calculation groups require a Tabular model compatibility level of 1500+ (Power BI default)

---

## 13. Disconnected Tables and What-If Parameters

Disconnected tables have no relationship to any other table. They serve as parameter selectors.

### What-If Parameter (Built-in)

Power BI Desktop > Modeling > New Parameter > What-If

This creates:
1. A disconnected table with values (e.g., 0% to 50% in 5% steps)
2. A slicer for the user to pick a value
3. A measure that returns the selected value

```dax
// Auto-generated measure
Growth Rate Value = SELECTEDVALUE('Growth Rate'[Growth Rate], 0.10)

// Use it in your measures
Projected Sales = SUM(Sales[Amount]) * (1 + [Growth Rate Value])
```

### Custom Disconnected Table

For more control, create manually in Power Query or DAX:

```dax
// DAX calculated table
Metric Selector =
DATATABLE(
    "Metric", STRING,
    {
        {"Revenue"},
        {"Profit"},
        {"Units Sold"},
        {"Avg Order Value"}
    }
)
```

Then use SWITCH to branch logic:

```dax
Selected Metric Value =
SWITCH(
    SELECTEDVALUE('Metric Selector'[Metric]),
    "Revenue", SUM(Sales[Amount]),
    "Profit", SUM(Sales[Profit]),
    "Units Sold", SUM(Sales[Quantity]),
    "Avg Order Value", DIVIDE(SUM(Sales[Amount]), DISTINCTCOUNT(Sales[OrderID])),
    BLANK()
)
```

### Field Parameters (Modern Alternative)

Field parameters (preview feature, now GA) let users dynamically swap measures or dimensions in a visual without DAX SWITCH logic:

1. Modeling > New Parameter > Fields
2. Select the measures or columns to include
3. A slicer appears letting the user toggle between them
4. The visual axis/legend/values update dynamically

Field parameters are cleaner than disconnected tables for measure-switching scenarios.

---

## 14. DISTINCTCOUNT Optimization with CallbackDataID

DISTINCTCOUNT is one of the most expensive aggregation functions because VertiPaq must track unique values across filter intersections.

### The Problem

```dax
// This is expensive on high-cardinality columns
Unique Customers = DISTINCTCOUNT(Sales[CustomerID])
```

When CustomerID has millions of unique values, every filter combination requires a full distinct count scan.

### CallbackDataID Reduction Pattern

Reduce the column cardinality that DISTINCTCOUNT operates on:

```dax
// Instead of DISTINCTCOUNT on a high-cardinality column...
// Create a calculated column that maps to a lower-cardinality integer
// (Do this in Power Query, not as a DAX calculated column)

// In Power Query: add an index or hash column
// Then in DAX:
Unique Customers = DISTINCTCOUNT(Sales[CustomerIndex])
```

### Alternative: Use SUMX with DISTINCT

```dax
// Sometimes faster than DISTINCTCOUNT for specific patterns
Unique Customers =
COUNTROWS(
    DISTINCT(Sales[CustomerID])
)
```

### Best Practices for DISTINCTCOUNT
- Avoid DISTINCTCOUNT on text columns -- use integer keys instead
- If you need distinct count across a relationship, use CALCULATE + DISTINCTCOUNT rather than nested iterators
- For approximate distinct counts on very large datasets, consider using DAX APPROXIMATEDISTINCTCOUNT (available in DirectQuery mode)

---

**Golden Rules:**
1. Filter and row context control everything
2. CALCULATE is the most powerful tool; master it first
3. Variables improve readability and performance
4. Measures on fact tables, calculated columns on dimensions
5. Iterators are powerful but slow on large tables
6. Test assumptions in DAX Studio before deploying
7. Use TREATAS for virtual relationships; use calculation groups to avoid measure proliferation
8. Prefer integer keys for DISTINCTCOUNT -- text keys kill performance
