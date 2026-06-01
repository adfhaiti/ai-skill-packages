# TMDL (Tabular Model Definition Language) Guide

TMDL is the text-based format used for Power BI semantic models. It defines tables, columns, measures, relationships, and data sources in a human-readable, indentation-sensitive syntax.

## Table of Contents

1. [Syntax Basics](#1-syntax-basics)
2. [Database and Model Files](#2-database-and-model-files)
3. [Table Definitions](#3-table-definitions)
4. [Column Definitions](#4-column-definitions)
5. [Measure Definitions](#5-measure-definitions)
6. [Partition / Data Source Definitions](#6-partitions)
7. [Relationships](#7-relationships)
8. [Expressions (Power Query M)](#8-expressions)
9. [Calculated Tables](#9-calculated-tables)
10. [Roles and RLS](#10-roles)

---

## 1. Syntax Basics

TMDL uses indentation (tabs, not spaces) to define hierarchy. Key rules:

- **Comments**: Use `///` for documentation comments (included in metadata), `//` for regular comments
- **Indentation**: One tab per nesting level. Spaces will cause errors.
- **Strings**: Use single quotes for string values in properties
- **Multi-line expressions**: The expression starts on the next line after `=`, indented one level deeper
- **Properties**: Written as `propertyName: value` or `propertyName = expression`

## 2. Database and Model Files

**database.tmdl** -- Database-level metadata:
```tmdl
database MyDatabase
	compatibilityLevel: 1604
```

**model.tmdl** -- Model-level configuration:
```tmdl
model Model
	culture: en-US
	defaultPowerBIDataSourceVersion: powerBI_V3
	discourageImplicitMeasures: true
	sourceQueryCulture: en-US
```

## 3. Table Definitions

Each table gets its own `.tmdl` file in the `tables/` folder.

```tmdl
/// Sales transactions fact table
table Sales
	lineageTag: a1b2c3d4-e5f6-7890-abcd-ef1234567890

	/// Primary key for the sales table
	column SalesID
		dataType: int64
		isKey: true
		formatString: 0
		sourceColumn: SalesID
		summarizeBy: none
		lineageTag: 11111111-2222-3333-4444-555555555555

	column OrderDate
		dataType: dateTime
		formatString: Short Date
		sourceColumn: OrderDate
		summarizeBy: none
		lineageTag: 22222222-3333-4444-5555-666666666666

	column ProductKey
		dataType: int64
		formatString: 0
		sourceColumn: ProductKey
		summarizeBy: none
		lineageTag: 33333333-4444-5555-6666-777777777777

	column CustomerKey
		dataType: int64
		formatString: 0
		sourceColumn: CustomerKey
		summarizeBy: none
		lineageTag: 44444444-5555-6666-7777-888888888888

	column Quantity
		dataType: int64
		formatString: #,##0
		sourceColumn: Quantity
		summarizeBy: sum
		lineageTag: 55555555-6666-7777-8888-999999999999

	column UnitPrice
		dataType: decimal
		formatString: $ #,##0.00
		sourceColumn: UnitPrice
		summarizeBy: none
		lineageTag: 66666666-7777-8888-9999-aaaaaaaaaaaa

	column Region
		dataType: string
		sourceColumn: Region
		summarizeBy: none
		lineageTag: 77777777-8888-9999-aaaa-bbbbbbbbbbbb
```

## 4. Column Definitions

**Data types:**
- `string` -- Text values
- `int64` -- Whole numbers
- `decimal` -- Fixed-point decimal numbers
- `double` -- Floating-point numbers
- `dateTime` -- Date and time values
- `boolean` -- True/false
- `binary` -- Binary data

**Common properties:**
- `dataType`: Required. One of the types above
- `sourceColumn`: Name of the column in the source data
- `formatString`: Display format (e.g., `$ #,##0`, `0.00%`, `Short Date`)
- `summarizeBy`: Default aggregation (`none`, `sum`, `count`, `min`, `max`, `average`)
- `isKey`: Mark as primary key (true/false)
- `isHidden`: Hide from report view (true/false)
- `displayFolder`: Group columns in a folder
- `sortByColumn`: Sort this column by another column's values
- `lineageTag`: Unique GUID identifier

**Calculated columns:**
```tmdl
	column 'Profit Margin' = DIVIDE([Revenue] - [Cost], [Revenue], 0)
		dataType: double
		formatString: 0.00%
		summarizeBy: none
		lineageTag: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
```

## 5. Measure Definitions

Measures are DAX expressions that calculate aggregated values at query time.

**Single-line measure:**
```tmdl
	measure 'Total Revenue' = SUMX(Sales, Sales[Quantity] * Sales[UnitPrice])
		formatString: $ #,##0
		displayFolder: Revenue
		lineageTag: bbbbbbbb-cccc-dddd-eeee-ffffffffffff
```

**Multi-line measure:**
```tmdl
	measure 'Revenue YoY %' =
		VAR CurrentYear = [Total Revenue]
		VAR PriorYear =
			CALCULATE(
				[Total Revenue],
				SAMEPERIODLASTYEAR('Calendar'[Date])
			)
		RETURN
			DIVIDE(CurrentYear - PriorYear, PriorYear, BLANK())
		formatString: 0.0%;-0.0%;0.0%
		displayFolder: Revenue
		lineageTag: cccccccc-dddd-eeee-ffff-111111111111
```

**Format string patterns:**
- Currency: `$ #,##0` or `$ #,##0.00`
- Percentage: `0.0%` or `0.00%`
- Whole number: `#,##0`
- Decimal: `#,##0.00`
- Date: `Short Date` or `Long Date`
- General: `General`

## 6. Partitions

Partitions define where data comes from. The most common type is a Power Query M expression.

**Import mode with M query:**
```tmdl
	partition 'Sales-Partition' = m
		mode: import
		source =
			let
				Source = Csv.Document(File.Contents("C:\Data\sales.csv"), [Delimiter=",", Columns=7, Encoding=65001, QuoteStyle=QuoteStyle.None]),
				#"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
				#"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers", {
					{"SalesID", Int64.Type},
					{"OrderDate", type datetime},
					{"ProductKey", Int64.Type},
					{"CustomerKey", Int64.Type},
					{"Quantity", Int64.Type},
					{"UnitPrice", Currency.Type},
					{"Region", type text}
				})
			in
				#"Changed Type"
```

**Import from SQL:**
```tmdl
	partition 'Sales-SQL' = m
		mode: import
		source =
			let
				Source = Sql.Database("server.database.windows.net", "SalesDB"),
				dbo_Sales = Source{[Schema="dbo", Item="Sales"]}[Data]
			in
				dbo_Sales
```

**Calculated partition (DAX):**
```tmdl
	partition 'DateTable' = calculated
		mode: import
		source = CALENDAR(DATE(2020, 1, 1), DATE(2026, 12, 31))
```

## 7. Relationships

Defined in `relationships.tmdl`.

```tmdl
relationship sales_to_product
	fromColumn: Sales.ProductKey
	toColumn: Product.ProductKey

relationship sales_to_customer
	fromColumn: Sales.CustomerKey
	toColumn: Customer.CustomerKey

relationship sales_to_calendar
	fromColumn: Sales.OrderDate
	toColumn: Calendar.Date
```

**Properties:**
- `fromColumn`: The "many" side (fact table)
- `toColumn`: The "one" side (dimension table)
- `crossFilteringBehavior`: `oneDirection` (default) or `bothDirections`
- `isActive`: `true` (default) or `false` for inactive relationships
- `securityFilteringBehavior`: `oneDirection` or `bothDirections`

**Inactive relationship (for role-playing dimensions):**
```tmdl
relationship sales_shipdate_to_calendar
	fromColumn: Sales.ShipDate
	toColumn: Calendar.Date
	isActive: false
```

## 8. Expressions (Power Query M)

Shared expressions go in `expressions.tmdl`. These are typically used for parameterized data sources.

```tmdl
expression DataSourcePath =
	"C:\Data\" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
	lineageTag: dddddddd-eeee-ffff-1111-222222222222

expression ServerName =
	"myserver.database.windows.net" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
	lineageTag: eeeeeeee-ffff-1111-2222-333333333333
```

## 9. Calculated Tables

Tables derived entirely from DAX expressions.

```tmdl
/// Date dimension table generated via DAX
table Calendar
	lineageTag: ffffffff-1111-2222-3333-444444444444

	column Date
		dataType: dateTime
		formatString: Short Date
		isKey: true
		summarizeBy: none
		lineageTag: 11112222-3333-4444-5555-666677778888

	column Year
		dataType: int64
		formatString: 0
		summarizeBy: none
		lineageTag: 22223333-4444-5555-6666-777788889999

	column Month
		dataType: string
		summarizeBy: none
		sortByColumn: MonthNumber
		lineageTag: 33334444-5555-6666-7777-88889999aaaa

	column MonthNumber
		dataType: int64
		formatString: 0
		isHidden: true
		summarizeBy: none
		lineageTag: 44445555-6666-7777-8888-9999aaaabbbb

	column Quarter
		dataType: string
		summarizeBy: none
		lineageTag: 55556666-7777-8888-9999-aaaabbbbcccc

	partition 'Calendar' = calculated
		mode: import
		source =
			VAR BaseTable = CALENDAR(DATE(2020, 1, 1), DATE(2026, 12, 31))
			RETURN
				ADDCOLUMNS(
					BaseTable,
					"Year", YEAR([Date]),
					"Month", FORMAT([Date], "MMMM"),
					"MonthNumber", MONTH([Date]),
					"Quarter", "Q" & FORMAT(QUARTER([Date]), "0")
				)
```

## 10. Roles (Row-Level Security)

Defined in `roles/` folder.

```tmdl
role 'Regional Sales Manager'
	modelPermission: read

	tablePermission Sales = [Region] = USERPRINCIPALNAME()
```

## Common Patterns for Creating a Semantic Model from CSV

When building a model from CSV data, here's the typical approach:

1. Create one TMDL file per table in `tables/`
2. Each table needs: column definitions + a partition with an M query pointing to the CSV
3. Create `relationships.tmdl` to link tables
4. Add measures to the fact table (or whichever table makes logical sense)
5. Create a Calendar table as a calculated table if date analysis is needed

**Generating lineageTags**: Use any UUID/GUID generator. Each column, measure, table, and relationship should have a unique lineageTag. Format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.
