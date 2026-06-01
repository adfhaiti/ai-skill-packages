# Common DAX Measure Patterns

Ready-to-use DAX patterns for building dashboards. Adapt table and column names to match the user's data.

## Table of Contents

1. [Basic Aggregations](#1-basic-aggregations)
2. [Time Intelligence](#2-time-intelligence)
3. [Rankings and Top N](#3-rankings-and-top-n)
4. [Ratios and Percentages](#4-ratios-and-percentages)
5. [Running Totals](#5-running-totals)
6. [Conditional / Filtered Measures](#6-conditional-measures)
7. [Statistical Measures](#7-statistical-measures)
8. [Calendar Table (Calculated)](#8-calendar-table)

---

## 1. Basic Aggregations

```dax
// Total Revenue
Total Revenue = SUMX(Sales, Sales[Quantity] * Sales[UnitPrice])

// Total Orders
Total Orders = COUNTROWS(Sales)

// Total Quantity
Total Quantity = SUM(Sales[Quantity])

// Average Order Value
Avg Order Value = DIVIDE([Total Revenue], [Total Orders], 0)

// Distinct Customer Count
Customer Count = DISTINCTCOUNT(Sales[CustomerKey])

// Distinct Product Count
Product Count = DISTINCTCOUNT(Sales[ProductKey])
```

## 2. Time Intelligence

These require a proper date table with a continuous date column marked as the date table in the model.

```dax
// Year-to-Date
Revenue YTD = TOTALYTD([Total Revenue], 'Calendar'[Date])

// Quarter-to-Date
Revenue QTD = TOTALQTD([Total Revenue], 'Calendar'[Date])

// Month-to-Date
Revenue MTD = TOTALMTD([Total Revenue], 'Calendar'[Date])

// Previous Year (Same Period)
Revenue PY =
    CALCULATE(
        [Total Revenue],
        SAMEPERIODLASTYEAR('Calendar'[Date])
    )

// Year-over-Year Change
Revenue YoY Change = [Total Revenue] - [Revenue PY]

// Year-over-Year Percentage
Revenue YoY % =
    VAR CurrentYear = [Total Revenue]
    VAR PriorYear = [Revenue PY]
    RETURN
        DIVIDE(CurrentYear - PriorYear, PriorYear, BLANK())

// Previous Month
Revenue PM =
    CALCULATE(
        [Total Revenue],
        DATEADD('Calendar'[Date], -1, MONTH)
    )

// Month-over-Month Change %
Revenue MoM % =
    VAR Current = [Total Revenue]
    VAR Prior = [Revenue PM]
    RETURN
        DIVIDE(Current - Prior, Prior, BLANK())

// Same Period Last Year YTD
Revenue PY YTD =
    CALCULATE(
        [Revenue YTD],
        SAMEPERIODLASTYEAR('Calendar'[Date])
    )

// Rolling 12 Months
Revenue R12M =
    CALCULATE(
        [Total Revenue],
        DATESINPERIOD('Calendar'[Date], MAX('Calendar'[Date]), -12, MONTH)
    )

// Rolling 3 Months Average
Revenue 3M Avg =
    DIVIDE(
        CALCULATE(
            [Total Revenue],
            DATESINPERIOD('Calendar'[Date], MAX('Calendar'[Date]), -3, MONTH)
        ),
        3
    )
```

## 3. Rankings and Top N

```dax
// Product Rank by Revenue
Product Revenue Rank =
    RANKX(
        ALL(Product[ProductName]),
        [Total Revenue],
        ,
        DESC,
        Dense
    )

// Category Rank
Category Rank =
    RANKX(
        ALL(Product[Category]),
        [Total Revenue],
        ,
        DESC,
        Dense
    )

// Top 10 Flag (for filtering)
Is Top 10 Product =
    IF([Product Revenue Rank] <= 10, 1, 0)
```

## 4. Ratios and Percentages

```dax
// Profit Margin
Profit Margin =
    DIVIDE(
        [Total Revenue] - [Total Cost],
        [Total Revenue],
        0
    )

// Percentage of Grand Total
Revenue % of Total =
    DIVIDE(
        [Total Revenue],
        CALCULATE([Total Revenue], ALL(Sales)),
        0
    )

// Percentage of Parent (e.g., category share within region)
Revenue % of Parent =
    DIVIDE(
        [Total Revenue],
        CALCULATE(
            [Total Revenue],
            ALLEXCEPT(Sales, Sales[Region])
        ),
        0
    )

// Contribution Margin
Contribution % =
    DIVIDE(
        [Total Revenue],
        CALCULATE([Total Revenue], REMOVEFILTERS()),
        0
    )
```

## 5. Running Totals

```dax
// Cumulative Revenue (within year)
Cumulative Revenue =
    CALCULATE(
        [Total Revenue],
        FILTER(
            ALL('Calendar'[Date]),
            'Calendar'[Date] <= MAX('Calendar'[Date])
                && YEAR('Calendar'[Date]) = YEAR(MAX('Calendar'[Date]))
        )
    )

// Running Total across all time
Running Total Revenue =
    CALCULATE(
        [Total Revenue],
        FILTER(
            ALL('Calendar'[Date]),
            'Calendar'[Date] <= MAX('Calendar'[Date])
        )
    )
```

## 6. Conditional / Filtered Measures

```dax
// Revenue for a specific category
Revenue Computers =
    CALCULATE(
        [Total Revenue],
        Product[Category] = "Computers"
    )

// Revenue excluding a category
Revenue Excl Returns =
    CALCULATE(
        [Total Revenue],
        Sales[OrderType] <> "Return"
    )

// New Customer Revenue (first purchase in current period)
New Customer Revenue =
    CALCULATE(
        [Total Revenue],
        FILTER(
            Sales,
            Sales[OrderDate] = CALCULATE(
                MIN(Sales[OrderDate]),
                ALLEXCEPT(Sales, Sales[CustomerKey])
            )
        )
    )

// Revenue with dynamic threshold
Revenue Above Target =
    IF([Total Revenue] >= [Revenue Target], [Total Revenue], BLANK())
```

## 7. Statistical Measures

```dax
// Average
Avg Revenue Per Customer =
    AVERAGEX(
        VALUES(Sales[CustomerKey]),
        [Total Revenue]
    )

// Median
Median Order Value =
    MEDIANX(
        Sales,
        Sales[Quantity] * Sales[UnitPrice]
    )

// Standard Deviation
Revenue StdDev =
    VAR AvgRev = AVERAGEX(VALUES('Calendar'[Date].[Month]), [Total Revenue])
    RETURN
        SQRT(
            AVERAGEX(
                VALUES('Calendar'[Date].[Month]),
                ([Total Revenue] - AvgRev) ^ 2
            )
        )

// Min / Max
Max Daily Revenue =
    MAXX(VALUES('Calendar'[Date]), [Total Revenue])

Min Daily Revenue =
    MINX(VALUES('Calendar'[Date]), [Total Revenue])
```

## 8. Calendar Table (Calculated)

A standard date dimension table created via DAX. Include this whenever the data has date fields.

```dax
// Calculated table DAX (used in the partition source)
VAR BaseTable = CALENDAR(DATE(2020, 1, 1), DATE(2026, 12, 31))
RETURN
    ADDCOLUMNS(
        BaseTable,
        "Year", YEAR([Date]),
        "Month", FORMAT([Date], "MMMM"),
        "MonthNumber", MONTH([Date]),
        "MonthYear", FORMAT([Date], "MMM YYYY"),
        "Quarter", "Q" & FORMAT(QUARTER([Date]), "0"),
        "QuarterNumber", QUARTER([Date]),
        "DayOfWeek", FORMAT([Date], "dddd"),
        "DayOfWeekNumber", WEEKDAY([Date], 2),
        "WeekNumber", WEEKNUM([Date], 2),
        "YearMonth", FORMAT([Date], "YYYY-MM"),
        "IsCurrentMonth", IF(MONTH([Date]) = MONTH(TODAY()) && YEAR([Date]) = YEAR(TODAY()), TRUE(), FALSE()),
        "IsCurrentYear", IF(YEAR([Date]) = YEAR(TODAY()), TRUE(), FALSE())
    )
```

The corresponding TMDL for the Calendar table needs columns for each of these calculated fields, plus the partition definition using this DAX.

## DAX Best Practices

1. **Use variables (VAR/RETURN)** for readability and performance. Calculate intermediate results once instead of repeating expressions.

2. **DIVIDE over division operator** -- `DIVIDE(a, b, 0)` handles division by zero gracefully. The `/` operator returns an error.

3. **CALCULATE for context changes** -- When you need to change the filter context, use CALCULATE. This is the most powerful and most misunderstood DAX function.

4. **Iterators vs. Aggregators** -- `SUMX`, `AVERAGEX`, `COUNTX` iterate row by row. `SUM`, `AVERAGE`, `COUNT` are simple aggregations on a single column. Use iterators when you need row-level calculations (e.g., Quantity * Price).

5. **ALL, ALLEXCEPT, REMOVEFILTERS** -- Use these to clear filter context. `ALL(Table)` removes all filters on a table. `ALLEXCEPT(Table, Column)` removes all filters except the specified column. `REMOVEFILTERS()` is equivalent to `ALL()`.

6. **RELATED for dimension lookups** -- When you need a value from a related dimension table inside a fact table calculation, use `RELATED(DimTable[Column])`. This only works when there's an active relationship from the fact to the dimension.
