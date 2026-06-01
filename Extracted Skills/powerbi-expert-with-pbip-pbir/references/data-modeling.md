# Data Modeling Reference for Power BI

## Table of Contents
1. Star Schema Design
2. Relationships and Cardinality
3. Cross-Filtering Direction
4. Storage Modes
5. Model Metadata
6. Date Tables
7. Survey Data Modeling
8. Common Modeling Anti-Patterns
9. Slowly Changing Dimensions
10. Composite Model Patterns

---

## 1. Star Schema Design

Star schema is the foundation of effective Power BI models. Period.

**Why Star Schema?**
- Simplifies relationships (fact tables connect to dimensions, not to each other)
- Improves query performance (fewer joins, clearer optimization paths)
- Makes DAX formulas intuitive
- Scales better as complexity grows

**Structure:**

```
                    Date
                     |
                     |
    Product ----  Fact_Sales  ---- Customer
      |              |              |
      |              |              |
    Store --------- | ---------- Territory
                     |
                  Region
```

**Fact Tables:**
- Contain foreign keys and measures
- Row grain: one row per event/transaction
- Example: Fact_Sales (SalesID, ProductID, CustomerID, DateID, Amount, Quantity)
- Grain must be defined and documented (e.g., "one row per order line")

**Dimension Tables:**
- Contain descriptive attributes
- Slowly changing reference data
- Example: Dim_Product (ProductID, ProductName, Category, SubCategory, Color, Price)
- Primary key: typically integer (surrogate key)

**Snowflake vs. Flat Dimensions:**

Snowflake (normalized):
```
Dim_Product -> Dim_Category -> Dim_Subcategory
```

Power BI prefers flat dimensions. Flatten during load (Power Query) unless:
- Dimension has hundreds of millions of rows (rare)
- Need independent queries on normalized tables (not Power BI use case)

For 99% of models, flatten in Power Query. One dimension table = one query, faster load, simpler relationships.

---

## 2. Relationships and Cardinality

**One-to-Many (1:M)** - The standard
- One product has many sales
- Direction: Dimension -> Fact
- Most common relationship type
- Filters flow naturally from dimension to fact

**One-to-One (1:1)** - Red flag
- Usually means tables should merge
- Example: Employee -> EmployeePhoto by EmployeeID
- Solution: Add photo URL to Employee table instead
- If 1:1 exists, question whether it should

**Many-to-Many (N:M)** - Requires bridge table**
- Example: Students take many Courses, Courses have many Students
- Solution: Create enrollment bridge table
```
Dim_Student -> Bridge_Enrollment -> Dim_Course
               (StudentID, CourseID)
```
- Set 1:M from Dim_Student -> Bridge
- Set 1:M from Dim_Course -> Bridge
- Use bidirectional filtering on Bridge (see Cross-Filtering Direction)

**Active vs. Inactive Relationships**
- Active: Only one active relationship per column pair
- Inactive: Deactivate alternate relationships
- Example: OrderDate and ShipDate both to Calendar
  - OrderDate relationship: ACTIVE
  - ShipDate relationship: INACTIVE
  - Use USERELATIONSHIP() to activate ShipDate in specific measures

```DAX
ShipDateRevenue := SUMX(
  VALUES(Fact_Sales[ShipDate]),
  CALCULATE([Total Revenue], USERELATIONSHIP(Fact_Sales[ShipDate], Dim_Date[Date]))
)
```

---

## 3. Cross-Filtering Direction

**Single Direction (Default, Preferred)**
- Filters flow from dimension to fact only
- Cleaner, less ambiguous
- Better performance
- 95% of models use single direction

Example: Filter by Region -> affects Sales, not vice versa.

**Bidirectional**
- Filters flow both ways
- Required for bridge tables (many-to-many)
- Use sparingly elsewhere

```
Dim_Student <==> Bridge_Enrollment <==> Dim_Course
(bidirectional on both sides for proper filtering)
```

**Risks of Bidirectional:**
- Ambiguity: Which table is the "source of truth" for filters?
- Performance: More joins, slower query optimization
- Filter propagation surprises: Filtering Sales by OrderDate might unexpectedly filter Customer attributes

**Rule:** Use single direction by default. Use bidirectional only for:
- Bridge tables (many-to-many)
- Rare cases of true symmetrical relationships

---

## 4. Storage Modes

**Import (VertiPaq)**
- Data loaded into Power BI engine (in-memory compressed)
- Fastest queries
- Limited by available RAM
- Best for: < 2GB uncompressed, fast query response required
- Refresh required for real-time data

**DirectQuery**
- Queries sent to source database in real-time
- No data copied to Power BI
- Slower (network + DB query overhead)
- No DAX calculated columns, limited calculated tables
- Best for: Real-time requirements, massive datasets (> 10GB), compliance reasons

**Dual Mode**
- Table can use Import or DirectQuery depending on query context
- Rarely used, complex interaction rules
- Skip unless you have specific requirements

**Composite Models**
- Mix Import and DirectQuery in one model
- Common pattern: DirectQuery fact table, Import dimensions
- Reduces memory while keeping dimensions fast

```
Dim_Product (IMPORT) -> Fact_Sales (DIRECTQUERY) <- Dim_Date (IMPORT)
                             |
                        (Real-time database)
```

**Direct Lake (Fabric)**
- OneLake storage, zero-copy semantics -- reads Parquet/Delta files directly
- Performance close to Import mode without data duplication
- Automatic fallback to DirectQuery if data exceeds memory limits
- Fabric-exclusive: requires Lakehouse or Warehouse in Microsoft Fabric
- Not available in Power BI Desktop standalone; use Fabric workspace
- Ideal for large datasets (10GB+) in Fabric environments
- Supports V-Order optimization for faster column reads

**Trade-offs:**
| Mode | Speed | Memory | Real-time | Refresh | DAX Features |
|------|-------|--------|-----------|---------|--------------|
| Import | Fast | High | No | Required | Full |
| DirectQuery | Slow | Low | Yes | N/A | Limited |
| Composite | Medium | Medium | Mixed | Partial | Mostly |

---

## 5. Model Metadata

**Default Summarization**
- Set on numeric columns
- DO NOT SET on dimension keys
- Examples:
  - ProductID: Don't Summarize (it's a key!)
  - Sales Amount: Sum
  - Unit Price: Average
  - Store Count: Count (Distinct)

**Data Categories**
- Improve visualizations and geographic filtering
- Geography: Set on Address, City, State, Country, PostalCode
- URL: Set on web address columns
- Image URL: Points to image files
- Barcode: For barcode readers

**Display Folders**
```
Measures:
  Sales
    ├─ Total Revenue
    ├─ Revenue YoY Growth
  Costs
    ├─ Total COGS
    ├─ Cost Per Unit
```

Organize in model for cleaner field list.

**Sort By Column**
- Month Name sorts by Month Number (1-12, not alphabetical)
- City sorts by Region (geographic order)
- Example: Month.Name sorted by Month.MonthNumber

**Hidden Columns**
- Hide dimension keys (ProductID, CustomerID, etc.)
- Hide bridge table keys
- Hide any column users shouldn't directly interact with
- Visible in DAX, hidden from UI

---

## 6. Date Tables

Every model needs a proper date table. Build it systematically.

**Required Attributes:**
- Continuous dates with no gaps
- All dates in ISO format (YYYY-MM-DD)
- Primary key: Date (or DateID as integer)
- Year, Quarter, Month, Day, DayOfWeek
- Month Name, Day Name (sorted by number, not alphabetically)
- Fiscal periods if applicable
- Indicators: IsWeekend, IsHoliday, IsLastDayOfMonth

**Create in Power Query:**

```M
let
    StartDate = #date(2020, 1, 1),
    EndDate = #date(2026, 12, 31),
    DateCount = Duration.Days(EndDate - StartDate) + 1,
    Dates = List.Dates(StartDate, DateCount, Duration.From(1)),
    Table = Table.FromList(Dates, Splitter.SplitByNothing()),
    DateColumn = Table.RenameColumns(Table, {{"Column1", "Date"}}),
    AddYear = Table.AddColumn(DateColumn, "Year", each Date.Year([Date])),
    AddQuarter = Table.AddColumn(AddYear, "Quarter", 
      each "Q" & Text.From(Date.QuarterOfYear([Date]))),
    AddMonth = Table.AddColumn(AddQuarter, "Month", each Date.Month([Date])),
    AddMonthName = Table.AddColumn(AddMonth, "MonthName", each Text.Proper(Date.ToText([Date], "MMMM"))),
    AddDay = Table.AddColumn(AddMonthName, "DayOfWeek", each Date.DayOfWeekName([Date])),
    AddWeekend = Table.AddColumn(AddDay, "IsWeekend", 
      each [Date.DayOfWeek([Date]) = Day.Saturday or Date.DayOfWeek([Date]) = Day.Sunday]),
    ChangeTypes = Table.TransformColumnTypes(AddWeekend, {
      {"Date", type date}, {"Year", Int64.Type}, {"Quarter", type text},
      {"Month", Int64.Type}, {"MonthName", type text}, {"DayOfWeek", type text},
      {"IsWeekend", type logical}
    })
in
    ChangeTypes
```

**Mark as Date Table:**
- Model tab -> Mark as date table -> Select Date column
- Required for certain DAX functions (TOTALYTD, DATESYTD)

**Template (minimal):**

| Date | Year | Quarter | Month | MonthName | DayOfWeek | IsWeekend |
|------|------|---------|-------|-----------|-----------|-----------|
| 2020-01-01 | 2020 | Q1 | 1 | January | Wednesday | false |
| 2020-01-02 | 2020 | Q1 | 1 | January | Thursday | false |

---

## 7. Survey Data Modeling

Survey data arrives wide (many columns). Transform to star schema.

**Before (Wide Format):**
```
RespondentID, Q1_Answer, Q2_Answer, Q3_Answer, Q1_Timestamp, Q2_Timestamp, ...
123, "Strongly Agree", "Agree", "Neutral", 2026-01-01, 2026-01-01, ...
124, "Neutral", "Strongly Agree", "Disagree", 2026-01-02, 2026-01-02, ...
```

**After (Star Schema):**

Fact_Responses:
```
ResponseID, RespondentID, QuestionID, AnswerID, AnswerValue, ResponseDate
1, 123, 1, 4, 4, 2026-01-01
2, 123, 2, 3, 3, 2026-01-01
3, 123, 3, 2, 2, 2026-01-01
4, 124, 1, 2, 2, 2026-01-02
```

Dim_Question:
```
QuestionID, QuestionText, TopicID, QuestionOrder
1, "Overall satisfaction?", 1, 1
2, "Recommendation likelihood?", 2, 3
3, "Product quality?", 1, 2
```

Dim_Answer:
```
AnswerID, AnswerValue, AnswerText, AnswerOrder
1, 1, "Strongly Disagree", 1
2, 2, "Disagree", 2
3, 3, "Neutral", 3
4, 4, "Agree", 4
5, 5, "Strongly Agree", 5
```

Dim_Respondent:
```
RespondentID, Department, Region, ResponseCompletion
123, Sales, North, 2026-01-01
124, Marketing, South, 2026-01-02
```

**Unpivot in Power Query:**
- Select all answer columns
- Transform -> Unpivot Columns
- Rename "Attribute" column to "QuestionID" (strip "Q" prefix)
- Rename "Value" column to "AnswerText"
- Extract QuestionID using List.Distinct and lookup

**Label Encoding:**
Use numeric AnswerID (1-5) instead of one-hot encoding columns. More compact, easier to aggregate.

---

## 8. Common Modeling Anti-Patterns

**Wide Flat Tables**
- Avoid: One table with 200 columns
- Problem: Redundant data, hard to maintain, poor relationships
- Solution: Decompose into fact + dimensions

**Long Relationship Chains**
- Avoid: Product -> Category -> Group -> Division (4 hops to fact)
- Problem: Ambiguous filtering, slow queries
- Solution: Flatten dimensions; add Division directly to Product

**Bidirectional Everywhere**
- Avoid: Every relationship bidirectional
- Problem: Unpredictable filter behavior, ambiguity
- Solution: Use single direction; bidirectional only for bridges

**Calculated Columns on Fact Tables**
- Avoid: Adding columns in fact table via DAX
- Problem: Uses memory, hard to refresh, slow
- Solution: Add in Power Query before load

**Missing Date Table**
- Avoid: Using date directly from fact table
- Problem: Can't use time intelligence functions (YTD, MTD)
- Solution: Build proper Dim_Date, mark as date table

**Text Keys Instead of Integers**
- Avoid: ProductID = "PROD-00123"
- Problem: Larger memory footprint, slower joins
- Solution: Use integer surrogate keys (1, 2, 3, ...)

---

## 9. Slowly Changing Dimensions

Data changes over time. Plan how to handle it.

**Type 1: Overwrite**
- Update dimension in place, lose history
- Use when: History doesn't matter (e.g., current address)
- Implementation: Simple UPDATE in source

```
Dim_Customer before: CustomerID=5, Name=John, City=Boston
Dim_Customer after: CustomerID=5, Name=John, City=NYC
(History lost)
```

**Type 2: Historical Tracking**
- Keep multiple rows per entity with effective dates
- Use when: Need historical analysis (price changes, territory moves)
- Implementation: Add EffectiveDate, ExpirationDate, IsCurrentFlag

```
CustomerID, Name, City, EffectiveDate, ExpirationDate, IsCurrentFlag
5, John, Boston, 2023-01-01, 2025-12-31, false
5, John, NYC, 2026-01-01, 9999-12-31, true
```

Join fact table to dimension using:
```DAX
Fact_Sales.CustomerID = Dim_Customer.CustomerID
AND Fact_Sales.SalesDate BETWEEN Dim_Customer.EffectiveDate 
    AND Dim_Customer.ExpirationDate
```

---

## 10. Composite Model Patterns

Mix Import and DirectQuery for large-scale models.

**Aggregation Table Pattern:**
- DirectQuery fact table (raw, massive)
- Import aggregated fact table (rolled-up monthly/yearly)
- Queries hit aggregated table first, fall back to detail if needed
- Configuration: Enable folding, set aggregation relationships

```
Dim_Date (IMPORT)
    |
    ├-> Fact_Sales_Monthly (IMPORT - aggregation)
    |
    └-> Fact_Sales_Detail (DIRECTQUERY - source)
```

**Dimension Import, Fact DirectQuery:**
- Keep all dimensions in memory (fast joins)
- Stream fact data from database (real-time)
- Common for fast-changing facts with stable dimensions
- Better performance than pure DirectQuery

**When to Use Composite:**
- Fact table > 4GB uncompressed
- Near real-time data required
- Dimensions stable, manageable size
- User base tolerates query latency

**Trade-offs:**
- More complex to maintain
- Partial-cache ambiguity (some data cached, some live)
- Not all DAX features available on DirectQuery tables

---

## 11. Field Parameters

Field parameters let users dynamically switch which measure or dimension appears in a visual axis, legend, or value well. They replaced the old "disconnected slicer + SWITCH" pattern.

### Creating Field Parameters

1. Go to **Modeling > New Parameter > Fields**
2. Select the measures or columns to include
3. Power BI creates a special table and a slicer
4. Users toggle between fields dynamically in the report

### Use Cases

- **Measure switching**: Let users toggle between Revenue, Profit, and Units on the same chart
- **Dimension switching**: Let users switch the X-axis between Region, Product Category, and Sales Rep
- **Dynamic legends**: Change what the color grouping represents

### How It Works Internally

Field parameters create a calculated table with three columns:
- The parameter name (display text)
- The field reference (points to the actual measure/column)
- An ordinal for sort order

```dax
// Auto-generated by Power BI
Metric Selection = {
    ("Revenue", NAMEOF('Sales'[Total Revenue]), 0),
    ("Profit", NAMEOF('Sales'[Total Profit]), 1),
    ("Units", NAMEOF('Sales'[Units Sold]), 2)
}
```

### Best Practices
- Name the parameter clearly (e.g., "Select Metric" not "Parameter 1")
- Limit to 5-7 options per parameter -- too many overwhelms users
- Field parameters work with calculation groups for powerful combinations
- Available in Power BI Desktop (GA since late 2023) and Power BI Service

---

## 12. TREATAS for Virtual Relationships

When you need a relationship-like filter flow but can't (or shouldn't) add a physical relationship, use TREATAS in DAX measures. See `dax-guide.md` section 11 for full syntax and patterns.

**When TREATAS is better than a physical relationship:**
- Budget vs. Actual tables sharing a date column but with different grains
- Multiple fact tables that share a dimension but would create ambiguous paths
- Temporary analysis without modifying the model structure

**When to use a physical relationship instead:**
- Permanent, well-defined connections
- When performance matters on large tables (physical relationships are faster)
- When the relationship needs to support bidirectional filtering or RLS

---

## Quick Reference Checklist

- [ ] Define fact table grain clearly (one row per what?)
- [ ] Use integer surrogate keys for all dimension keys
- [ ] Hide all key columns from users
- [ ] Create proper Dim_Date and mark as date table
- [ ] Set default summarization (especially "Don't Summarize" for keys)
- [ ] Use single-direction relationships (default)
- [ ] Flatten dimensions in Power Query (avoid snowflake)
- [ ] Unpivot survey data into fact/dimension structure
- [ ] Review for bidirectional relationships and justify each
- [ ] Document slowly changing dimension strategy
- [ ] Consider composite models if fact table > 2GB
- [ ] Sort Month/Day names by their numeric equivalents
- [ ] Consider field parameters for user-facing measure/dimension switching
- [ ] Use TREATAS for virtual relationships where physical ones would create ambiguity
