# Power Query and M Language Reference Guide

## 1. Power Query Fundamentals

Power Query is the ETL (Extract, Transform, Load) engine in Power BI. It sits between your data sources and your data model, handling the heavy lifting of preparing data for analysis.

**The three phases:**
- **Extract**: Connect to data sources (SQL, Excel, APIs, web, folders)
- **Transform**: Clean, reshape, and combine data using the Query Editor
- **Load**: Send prepared data into Power BI's data model

**When to use Power Query vs DAX:**
Use Power Query for ALL data shaping tasks. DAX is for calculations, measures, and model logic. If you're tempted to use DAX for transformation, you're doing it wrong. Power Query handles this more efficiently and keeps your data model cleaner.

---

## 2. Query Folding

Query folding means your transformation steps are translated into native SQL/database queries and pushed down to the source. Instead of loading all data then filtering, the database filters before sending anything to Power BI.

**Operations that fold:**
- Filter rows (WHERE clause)
- Select columns (SELECT)
- Sort (ORDER BY)
- Group By (GROUP BY aggregations)
- Simple data type changes
- Basic rename and reorder operations

**Operations that break folding:**
- Custom columns with M logic
- Merge with non-folding queries
- Pivot/unpivot (sometimes, depends on source)
- Adding index columns
- Unpivoting from certain sources
- Combining queries with different folding behavior

**Check if a step folds:**
In Power BI Desktop: Right-click any transformation step > "View Native Query". If you see SQL, it's folding. If the option is grayed out, folding is broken at that step. Note: Visual query folding indicators (green/yellow/red icons on steps) are available in Power Query Online (Dataflows, Fabric) only -- they do NOT appear in Power BI Desktop.

**Maximize folding strategy:**
Order your steps: filter first, select columns second, then join/merge. Place custom columns and M logic at the end.

---

## 3. Essential Transformations

### Unpivot (Critical for survey data and crosstabs)

**UI Path:** Select columns > Transform > Unpivot Columns (or Unpivot Other Columns)

**M Code:**
```m
Table.Unpivot(
  #"Source Data",
  {"2023", "2024", "2025"},  // columns to unpivot
  "Year",                      // new attribute column
  "Sales"                      // new value column
)
```

### Pivot

**UI Path:** Select column > Transform > Pivot Column > choose aggregation function

**M Code:**
```m
Table.Pivot(
  #"Source Data",
  List.Distinct(#"Source Data"[Region]),
  "Region",
  "Sales",
  List.Sum
)
```

### Merge (Left Join, Inner Join)

**UI Path:** Home > Merge Queries (or Merge Queries as New)

**M Code:**
```m
Table.NestedJoin(
  Table1,
  {"CustomerID"},
  Table2,
  {"ID"},
  "Orders",
  JoinKind.LeftOuter
)
```

Join kinds: LeftOuter, RightOuter, Inner, FullOuter, LeftAnti, RightAnti

### Append

**UI Path:** Home > Append Queries (or Append Queries as New)

**M Code:**
```m
Table.Combine({Table1, Table2, Table3})
```

### Group By with Aggregation

**UI Path:** Transform > Group By > choose columns and aggregation

**M Code:**
```m
Table.Group(
  #"Source Data",
  {"Category", "Region"},
  {
    {"Total Sales", each List.Sum([Sales]), type number},
    {"Count", each Table.RowCount(_), type number}
  }
)
```

### Split Column

**UI Path:** Home > Split Column > By Delimiter or By Position

**M Code:**
```m
Table.SplitColumn(
  #"Source Data",
  "Name",
  Splitter.SplitTextByDelimiter(","),
  {"First", "Last"}
)
```

### Extract Patterns (Regex)

**M Code:**
```m
Text.Extract([Email], "([a-zA-Z]+)@(.+)")
```

### Conditional Column

**UI Path:** Add Column > Conditional Column

**M Code:**
```m
Table.AddColumn(
  #"Source Data",
  "Sales Tier",
  each if [Sales] > 50000 then "High"
       else if [Sales] > 10000 then "Medium"
       else "Low"
)
```

### Fill Down/Up

**UI Path:** Transform > Fill > Down (or Up)

**M Code:**
```m
Table.FillDown(#"Source Data", {"Category"})
Table.FillUp(#"Source Data", {"Description"})
```

### Transpose

**M Code:**
```m
Table.Transpose(#"Source Data")
```

---

## 4. M Language Syntax

### Let/In Structure

Every query is built on let/in. Let declares variables, in returns the final result.

```m
let
  Source = Excel.Workbook(File.Contents("C:\Data.xlsx")),
  Sheet1 = Source{[Item="Sheet1"]}[Data],
  Filtered = Table.SelectRows(Sheet1, each [Status] = "Active"),
  Renamed = Table.RenameColumns(Filtered, {{"OldName", "NewName"}}),
  Output = Renamed
in
  Output
```

### Data Types

```m
// Numbers
123
-45
3.14159

// Text
"Hello"
"It's quoted"

// Logical
true
false

// Null (missing value)
null

// Lists (ordered, indexed from 0)
{1, 2, 3, 4}
{"Apple", "Orange", "Banana"}

// Records (key-value pairs)
[Name = "John", Age = 30, City = "Boston"]

// Tables (collections of records)
#table({"Name", "Age"}, {{"John", 30}, {"Jane", 25}})

// Date and DateTime
#date(2026, 4, 5)
#datetime(2026, 4, 5, 14, 30, 0)
#time(14, 30, 0)
```

### Functions

```m
// Built-in function
Text.Upper("hello")      // "HELLO"
Number.Round(3.7)        // 4
List.Sum({1, 2, 3})      // 6

// Custom function with parameters
let
  AddTax = (Price, TaxRate) => Price * (1 + TaxRate)
in
  AddTax(100, 0.08)       // 108
```

### Error Handling: Try/Otherwise

```m
try
  Number.FromText("123")
otherwise
  0

// Or with full error object
try
  Number.FromText("not a number")
otherwise
  [HasError = true, Error = "Invalid input"]
```

### Each Syntax (Shorthand for lambda)

```m
// These two are equivalent:
List.Transform({1, 2, 3}, each _ * 2)
List.Transform({1, 2, 3}, (x) => x * 2)

// In table operations:
Table.SelectRows(Data, each [Sales] > 100)
// _ refers to the current row
```

### Logical Operators

```m
// AND
[Score] > 80 and [Status] = "Pass"

// OR
[Region] = "East" or [Region] = "West"

// NOT
not ([Status] = "Inactive")
```

### Null Handling

```m
// Check for null
[Amount] <> null

// Replace nulls
Table.ReplaceValue(Data, null, 0, Replacer.ReplaceValue, {"Sales"})

// Fill nulls with previous value
Table.FillDown(Data, {"Category"})
```

---

## 5. Custom Functions

Custom functions make your queries reusable and dynamic.

### Basic Function with One Parameter

```m
let
  TrimAndUpper = (InputText) =>
    Text.Upper(Text.Trim(InputText))
in
  TrimAndUpper
```

Call it: `TrimAndUpper("  hello world  ")` returns "HELLO WORLD"

### Function with Multiple Parameters and Types

```m
let
  FilterSalesRange = (Table, MinSales as number, MaxSales as number) =>
    Table.SelectRows(
      Table,
      each [Sales] >= MinSales and [Sales] <= MaxSales
    )
in
  FilterSalesRange
```

### Parameterized File Path

```m
let
  GetFile = (FolderPath as text, FileName as text) =>
    let
      FullPath = FolderPath & "\" & FileName,
      File = Excel.Workbook(File.Contents(FullPath))
    in
      File
in
  GetFile
```

### Reusable Data Cleaning Function

```m
let
  CleanTable = (InputTable as table) =>
    let
      Trimmed = Table.TransformColumns(
        InputTable,
        {{"Name", Text.Trim}, {"Email", Text.Trim}}
      ),
      Uppercase = Table.TransformColumns(
        Trimmed,
        {{"Name", Text.Upper}, {"Category", Text.Upper}}
      ),
      Removed = Table.SelectRows(
        Uppercase,
        each [Email] <> null
      )
    in
      Removed
in
  CleanTable
```

### Dynamic Date Range Filter

```m
let
  FilterByDate = (Table, StartDate as date, EndDate as date) =>
    Table.SelectRows(
      Table,
      each [TransactionDate] >= StartDate and [TransactionDate] <= EndDate
    )
in
  FilterByDate
```

---

## 6. Data Source Patterns

### Excel File

```m
let
  Source = Excel.Workbook(File.Contents("C:\Sales.xlsx")),
  Sheet = Source{[Item="Sheet1"]}[Data]
in
  Sheet
```

### CSV File

```m
let
  Source = Csv.Document(File.Contents("C:\Data.csv")),
  Promoted = Table.PromoteHeaders(Source)
in
  Promoted
```

### SQL Server Query

```m
let
  Source = Sql.Database("ServerName", "DatabaseName"),
  Query = Source{[Schema="dbo", Item="Orders"]}[Data]
in
  Query
```

### SharePoint List

```m
let
  Source = SharePoint.Tables("https://company.sharepoint.com/sites/project"),
  TaskList = Source{[Name="Tasks"]}[Data]
in
  TaskList
```

### Web API (JSON)

```m
let
  Source = Json.Document(Web.Contents("https://api.example.com/data")),
  Records = Source[items],
  Table = Table.FromList(Records, Splitter.SplitByNothing(), null, null, ExtraValues.Error)
in
  Table
```

### Combine Multiple Files from Folder

```m
let
  FolderPath = "C:\DataFiles",
  Files = File.Files(FolderPath),
  FilterCsv = Table.SelectRows(Files, each Text.EndsWith([Name], ".csv")),
  Content = Table.AddColumn(FilterCsv, "Data", each Csv.Document([Content])),
  Combined = Table.Combine(Content[Data])
in
  Combined
```

### Parameterized Connection (Environment-Aware)

```m
let
  Environment = "Production",  // Change to "Development" as needed
  ServerName = if Environment = "Production" then "PROD-SERVER" else "DEV-SERVER",
  Source = Sql.Database(ServerName, "Analytics")
in
  Source
```

---

## 7. Advanced Patterns

### Incremental Load (Last N Days)

```m
let
  Source = Sql.Database("Server", "Database"){[Item="Sales"]}[Data],
  LastDay = Date.AddDays(DateTime.Date(DateTime.LocalNow()), -1),
  Filtered = Table.SelectRows(Source, each [LoadDate] >= LastDay)
in
  Filtered
```

### REST API Pagination Handler

```m
let
  GetPagedData = (Url as text) =>
    let
      Pages = List.Generate(
        () => [Page = 0, Data = null, HasMore = true],
        each [HasMore] = true,
        each [
          Page = [Page] + 1,
          Data = Json.Document(Web.Contents(Url & "?page=" & Text.From([Page] + 1))),
          HasMore = List.Count([Data][items]) > 0
        ]
      ),
      AllData = List.Combine(List.Transform(Pages, each [Data][items])),
      Table = Table.FromList(AllData, Splitter.SplitByNothing(), null, null, ExtraValues.Error)
    in
      Table
in
  GetPagedData("https://api.example.com/data")
```

### Recursive Function (Flattening Nested Data)

```m
let
  FlattenJson = (Json) =>
    let
      Flattened = if Type.Is(Json, type list) then
        List.Transform(Json, each FlattenJson(_))
      else if Type.Is(Json, type record) then
        Json
      else
        Json
    in
      Flattened
in
  FlattenJson
```

### Dynamic Column Selection

```m
let
  SelectColumns = (Table, ColumnList as list) =>
    Table.SelectColumns(Table, ColumnList)
in
  SelectColumns
```

### Conditional Merge Logic

```m
let
  ConditionalMerge = (Left, Right, JoinType) =>
    if JoinType = "Inner" then
      Table.NestedJoin(Left, {"ID"}, Right, {"ID"}, "Joined", JoinKind.Inner)
    else if JoinType = "Left" then
      Table.NestedJoin(Left, {"ID"}, Right, {"ID"}, "Joined", JoinKind.LeftOuter)
    else
      null
in
  ConditionalMerge
```

### Error Row Extraction

```m
let
  Source = Csv.Document(File.Contents("file.csv")),
  WithErrors = try Table.PromoteHeaders(Source) otherwise error,
  ErrorRows = if WithErrors = error then "Failed to parse headers" else "Success"
in
  ErrorRows
```

---

## 8. Dataflows

Dataflows are reusable Power Query transformations stored in your Power BI workspace. Use them for:
- Centralized data cleaning applied across multiple reports
- Shared data preparation logic for team environments
- Reducing duplicate effort when multiple Power BI reports use the same source

**When to use dataflows:**
- The same transformation logic is used in 2+ reports
- Non-technical team members need to refresh specific datasets
- You want to reduce data load times by pre-filtering at the dataflow layer

**Architecture:**
Dataflows sit between your data source and Power BI datasets. They extract and transform data once, then multiple Power BI reports reference the cleaned dataflow output.

**Create a dataflow:**
Power BI Service > Workspaces > New > Dataflow > Define new entities > Add Power Query transformations > Save

---

## 9. Data Cleaning Patterns

### Handle Nulls

```m
Table.ReplaceValue(
  Data,
  null,
  0,
  Replacer.ReplaceValue,
  {"Sales", "Quantity"}
)
```

### Remove Duplicates

```m
Table.Distinct(Data, {"CustomerID"})  // Keep first occurrence
```

### Standardize Text

```m
let
  Trimmed = Table.TransformColumns(Data, {{"Name", Text.Trim}}),
  ProperCase = Table.TransformColumns(Trimmed, {{"Name", Text.Proper}}),
  Cleaned = Table.TransformColumns(ProperCase, {{"Email", Text.Lower}})
in
  Cleaned
```

### Parse Dates Across Multiple Formats

```m
let
  ParseDate = (DateText) =>
    try
      Date.FromText(DateText)
    otherwise
      try
        Date.FromText(DateText, "MM/dd/yyyy")
      otherwise
        Date.FromText(DateText, "dd/MM/yyyy"),
  
  Applied = Table.TransformColumns(
    Data,
    {{"OrderDate", ParseDate, type date}}
  )
in
  Applied
```

### Split Delimited Values

```m
let
  Splitter = (Text, Delimiter) =>
    Text.Split(Text, Delimiter),
  
  Split = Table.AddColumn(
    Data,
    "Tags",
    each Text.Split([Categories], ",")
  )
in
  Split
```

### Fix Encoding Issues

```m
let
  Source = Csv.Document(File.Contents("file.csv"), [Encoding = 65001]),
  Promoted = Table.PromoteHeaders(Source)
in
  Promoted
```

---

## 10. Advanced M Patterns

### Fuzzy Matching (Table.FuzzyJoin / Table.FuzzyNestedJoin)

Fuzzy matching joins tables even when values don't match exactly. Handles typos, abbreviations, and inconsistent formatting.

**UI Path:** Home > Merge Queries > select join columns > check "Use fuzzy matching" > expand Fuzzy matching options

**M Code:**
```m
Table.FuzzyJoin(
  Table1,
  {"CustomerName"},
  Table2,
  {"Name"},
  [
    Threshold = 0.8,           // 0 to 1, higher = stricter match
    TransformationTable = null, // optional synonym table
    NumberOfMatches = 1         // max matches per row
  ]
)
```

**Table.FuzzyNestedJoin** (same as FuzzyJoin but nests the matched table):
```m
Table.FuzzyNestedJoin(
  Table1,
  {"CompanyName"},
  Table2,
  {"Company"},
  "Matched",
  [Threshold = 0.7]
)
```

**Transformation Table** for known synonyms:
```m
let
  Synonyms = #table({"From", "To"}, {
    {"Corp", "Corporation"},
    {"Inc", "Incorporated"},
    {"Ltd", "Limited"},
    {"St.", "Street"}
  })
in
  Table.FuzzyJoin(T1, {"Name"}, T2, {"Name"}, [TransformationTable = Synonyms])
```

**When to use:** Matching customer names across systems, deduplicating mailing lists, linking survey responses to employee records with inconsistent spelling.

### The #shared Operator

`#shared` returns a record containing ALL built-in M functions and their documentation. This is the most powerful discovery tool in M.

```m
// View all available functions
#shared

// Filter to find specific functions
Record.SelectFields(
  #shared,
  List.Select(Record.FieldNames(#shared), each Text.Contains(_, "Table."))
)

// Get documentation for a specific function
Value.Type(Table.SelectRows)
```

**Practical use:** When you can't remember a function name, type `= #shared` in a blank query, then filter the resulting table by name to find what you need.

### Table.TransformColumnNames

Bulk-rename columns using a function. Far more efficient than renaming columns one by one.

```m
// Convert all column names to lowercase
Table.TransformColumnNames(Source, Text.Lower)

// Replace spaces with underscores
Table.TransformColumnNames(Source, each Text.Replace(_, " ", "_"))

// Add a prefix to all columns
Table.TransformColumnNames(Source, each "Sales_" & _)

// Clean column names (trim, proper case)
Table.TransformColumnNames(Source, each Text.Proper(Text.Trim(_)))
```

**When to use:** Standardizing column names from messy Excel files, applying naming conventions across multiple tables, preparing data for systems that require specific naming formats.

### List.Generate for Complex Iteration

List.Generate creates lists by iterating with a custom condition -- more flexible than List.Numbers or List.Dates.

```m
// Generate a list of dates for the next 12 months (first of each month)
List.Generate(
  () => Date.StartOfMonth(DateTime.Date(DateTime.LocalNow())),
  each _ <= Date.AddMonths(DateTime.Date(DateTime.LocalNow()), 12),
  each Date.AddMonths(_, 1)
)
```

### Error Handling per Row

Capture errors without stopping the entire query:

```m
Table.AddColumn(
  Source,
  "SafeConvert",
  each try Number.FromText([TextColumn]) otherwise null
)
```

For detailed error logging:
```m
Table.AddColumn(
  Source,
  "Result",
  each
    let
      attempt = try Number.FromText([Value])
    in
      if attempt[HasError] then
        [Value = null, Error = attempt[Error][Message]]
      else
        [Value = attempt[Value], Error = null]
)
```

---

## 11. Performance Best Practices

### 1. Maximize Query Folding
Structure your steps to fold: Filter -> Select Columns -> Join -> Custom Logic.

```m
// Good: Folding preserved
let
  Source = Sql.Database("Server", "DB"),
  Filtered = Table.SelectRows(Source, each [Status] = "Active"),
  Selected = Table.SelectColumns(Filtered, {"ID", "Name", "Sales"})
in
  Selected
```

### 2. Filter Early
Move WHERE logic as close to the source as possible.

```m
// Better: Filter at source
let
  Source = Sql.Database("Server", "DB"){[Item="Orders"]}[Data],
  Filtered = Table.SelectRows(Source, each [Year] = 2026)
in
  Filtered
```

### 3. Remove Unnecessary Columns Early
Don't load data you won't use.

```m
Table.SelectColumns(Data, {"CustomerID", "Sales", "Date"})
```

### 4. Avoid Unnecessary Type Conversions
Convert data types at the source if possible.

### 5. Use Buffering Strategically
Buffer only when you reference a table multiple times (saves recalculation).

```m
let
  Source = Csv.Document(File.Contents("file.csv")),
  Buffered = Table.Buffer(Source),
  Count = Table.RowCount(Buffered),
  Average = List.Average(Buffered[Sales])
in
  Buffered
```

List buffering for repeated operations:

```m
let
  Source = {1..10000},
  Buffered = List.Buffer(Source),
  First = Buffered{0},
  Last = List.Last(Buffered)
in
  Buffered
```

### 6. Avoid Complex Nested Formulas
Break transformations into named steps. It's faster and more maintainable.

```m
// Bad: Hard to optimize
let
  X = Table.SelectRows(Table.SelectColumns(Csv.Document(...), ...), ...)
in
  X

// Good: Clear steps, easier to debug
let
  Source = Csv.Document(...),
  Selected = Table.SelectColumns(Source, ...),
  Filtered = Table.SelectRows(Selected, ...)
in
  Filtered
```

### 7. Use Native Queries When Possible
Prefer SQL Server native queries over Power Query transformations on SQL data.

```m
// Better performance: Let SQL do the work
let
  Source = Sql.Database("Server", "DB"),
  Query = Value.NativeQuery(Source, "SELECT ID, Name, Sales FROM Orders WHERE Year = 2026")
in
  Query
```
