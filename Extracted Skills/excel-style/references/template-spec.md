# Excel Template Specification

Use this reference when creating a new workbook from scratch with openpyxl. This provides the exact code patterns to match Josiah's standards, including buffer spacing, top-alignment, Excel-safe Total Rows, structured references, PivotTable injection, data validation, and conditional formatting.

## Master Template: New Workbook Setup

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, NamedStyle
from openpyxl.worksheet.table import Table, TableStyleInfo, TableColumn
from openpyxl.utils import get_column_letter

wb = Workbook()

# 1. Set default font to Aptos 11pt via the Normal named style
#    (This sets the font for ALL cells without requiring per-cell application)
default_font = Font(name='Aptos', size=11)
wb._named_styles['Normal'].font = default_font

# 2. Set default alignment to top-aligned
#    openpyxl does not support changing default alignment via the Normal style directly;
#    apply Alignment per-cell for populated cells, or iterate after data is written.
top_align = Alignment(vertical='top')

# 3. Rename the default sheet using the appropriate prefix
ws = wb.active
ws.title = "wksMainData"  # Use wks/wksPvt/wksQry/wksTOC/wksReadMe prefix
```

## Buffer Spacing Setup (Row 1, Column A, Inter-Table Columns)

```python
# Column A reserved as buffer at width 2.5
ws.column_dimensions['A'].width = 2.5

# Row 1 left empty (no data written to row 1)

# Place the first Table starting at row 2, column B
# Headers at row 2, data from row 3 onward
header_row = 2
data_start_row = 3

# If placing a second Table to the right of the first:
# Leave 2 columns of buffer between them at width 2.5
# Example: first table ends at column H, second starts at column L
ws.column_dimensions['I'].width = 2.5
ws.column_dimensions['J'].width = 2.5
ws.column_dimensions['K'].width = 2.5
# Second table starts at column L
```

## Creating a Table (Standard Pattern)

```python
# After populating headers in row 2 and data in rows 3 through N:
table_style = TableStyleInfo(
    name="TableStyleMedium2",  # Default; use Medium16 for analysis, Medium9 for reference
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False
)

# Define the table range (starting at column B to respect the Column A buffer)
num_cols = 5
num_data_rows = 100
start_col = 'B'
end_col = get_column_letter(1 + num_cols)  # B..F for 5 cols
header_row = 2
last_row = header_row + num_data_rows  # e.g., row 102

table_ref = f"{start_col}{header_row}:{end_col}{last_row}"

table = Table(
    displayName="tblMyTableName",  # PascalCase with tbl prefix
    ref=table_ref,
    tableStyleInfo=table_style
)

ws.add_table(table)

# DO NOT apply Font/Fill/Alignment to header cells; the Table Style handles them
```

## Enabling Total Row (Excel-Safe Pattern)

```python
# CRITICAL: You must BOTH define the table with totalsRowCount AND write
# SUBTOTAL formulas and the "Total" label into the actual total row cells.
# Leaving them blank causes Excel to show a "Repaired Records: Table" error on open.

# Assume headers in row 2, data in rows 3..data_end, total row = data_end + 1
data_end_row = 102
total_row_num = data_end_row + 1  # e.g., row 103
start_col = 'B'
end_col = 'F'

# Build columns list with total row functions
columns = []
for i, header in enumerate(headers):
    col = TableColumn(id=i+1, name=header)
    if header in numeric_columns:
        col.totalsRowFunction = 'sum'
    elif i == 0:
        col.totalsRowFunction = 'none'  # Label cell gets "Total"
    columns.append(col)

table = Table(
    displayName="tblMyTable",
    ref=f"{start_col}2:{end_col}{total_row_num}",  # ref INCLUDES the total row
    tableStyleInfo=table_style,
    tableColumns=columns,
    totalsRowCount=1
)
ws.add_table(table)

# NOW write actual values into the total row cells (this prevents repair errors)
label_col_idx = 2  # column B (first column of the table, since A is buffer)
ws.cell(row=total_row_num, column=label_col_idx, value="Total")

for i, header in enumerate(headers):
    if header in numeric_columns:
        col_num = label_col_idx + i
        col_letter = get_column_letter(col_num)
        ws.cell(row=total_row_num, column=col_num).value = f"=SUBTOTAL(109,tblMyTable[{header}])"
```

**CRITICAL openpyxl note:** Leaving total row cells empty will trigger a "Repaired Records: Table" error in Excel on open. Always write the SUBTOTAL formulas and the "Total" label.

## Date Handling (CRITICAL)

```python
from datetime import datetime, date

# ALWAYS write Python datetime objects, NEVER text strings
ws.cell(row=3, column=5, value=datetime(2026, 4, 15))
ws.cell(row=3, column=5).number_format = 'yyyy-mm-dd'

# For a column of dates:
for row_idx, d in enumerate(dates, start=data_start_row):
    cell = ws.cell(row=row_idx, column=date_col)
    cell.value = d  # d must be a datetime or date object
    cell.number_format = 'yyyy-mm-dd'

# For datetime fields:
cell.number_format = 'yyyy-mm-dd h:mm'

# NEVER DO THIS:
# ws.cell(row=3, column=5, value="04-15-26")       # Text! Excel flags as error
# ws.cell(row=3, column=5, value="2026-04-15")     # Still text! Won't sort/calculate
```

## Top-Alignment Across All Cells

```python
# Apply top-alignment to all populated cells after data is written
# (openpyxl's Normal style alignment property is unreliable; apply per-cell)
for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
    for cell in row:
        cell.alignment = Alignment(vertical='top')

# Or use shrink_to_fit for cells that might overflow:
cell.alignment = Alignment(vertical='top', shrink_to_fit=True)
```

## Default Row Height

```python
ws.sheet_format.defaultRowHeight = 15
```

## No Manual Header Formatting (DO NOT)

```python
# WRONG: Manually formatting Table header cells
for col_idx in range(2, 2 + num_cols):
    cell = ws.cell(row=header_row, column=col_idx)
    cell.font = Font(name='Aptos', size=11, bold=True)  # DO NOT DO THIS
    cell.fill = PatternFill(...)                         # DO NOT DO THIS

# RIGHT: Let the Table Style handle everything
for col_idx, header in enumerate(headers):
    ws.cell(row=header_row, column=2 + col_idx, value=header)

table = Table(displayName="tblMyTable", ref=ref, tableStyleInfo=style)
ws.add_table(table)
# TableStyleMedium2 automatically applies bold white text on blue header
```

**Rule:** Never apply Font, Fill, or Alignment to cells inside an Excel Table's header row. The Table Style handles header appearance. Manual formatting overrides the style and produces inconsistent results.

## Structured References in Formulas

```python
# Same-row reference within the table (preferred modern syntax):
ws.cell(row=r, column=c).value = "=tblSales[@[Revenue]]-tblSales[@[Cost]]"

# Alternative same-row syntax:
ws.cell(row=r, column=c).value = "=tblSales[[#This Row],[Revenue]]-tblSales[[#This Row],[Cost]]"

# Whole-column aggregation:
ws.cell(row=r, column=c).value = "=SUMIFS(tblSales[Revenue],tblSales[Region],AnalizRegion[@[Region]])"

# Total row reference:
ws.cell(row=r, column=c).value = "=tblSales[[#Totals],[Revenue]]"

# Cross-table INDEX/MATCH lookup (preferred over VLOOKUP):
ws.cell(row=r, column=c).value = (
    '=IFERROR(INDEX(tblLookup[Value],MATCH(tblMain[@[Key]],tblLookup[Key],0)),"NA")'
)

# Safe division:
ws.cell(row=r, column=c).value = "=IFERROR(tblMain[@[Numerator]]/tblMain[@[Denominator]],0)"
```

## Input Cell Marker (Pale Blue Lily Fill)

```python
# Apply Pale Blue Lily fill to input cells in template workbooks
input_fill = PatternFill(start_color="D8E7E6", end_color="D8E7E6", fill_type="solid")

# Apply to a specific range of input cells (outside any Table)
for row_idx in range(5, 25):
    ws.cell(row=row_idx, column=3).fill = input_fill  # Column C, rows 5-24
```

Never apply this fill to cells inside a Table body. Exception: the rule explicitly allows Pale Blue Lily on input cells; that exception is for standalone input cells in templates, not inside a formal Table range.

## Data Validation (Dropdowns, Numeric Ranges, Dates)

```python
from openpyxl.worksheet.datavalidation import DataValidation

# Dropdown list
dv = DataValidation(
    type="list",
    formula1='"Option1,Option2,Option3"',
    allow_blank=True
)
dv.error = "Please select from the list"
dv.errorTitle = "Invalid Entry"
ws.add_data_validation(dv)
dv.add(ws['C5:C100'])  # Apply to input range

# Numeric range (whole number between 0 and 1,000,000)
dv_num = DataValidation(
    type="whole",
    operator="between",
    formula1=0,
    formula2=1000000
)
ws.add_data_validation(dv_num)
dv_num.add(ws['D5:D100'])

# Date range
dv_date = DataValidation(
    type="date",
    operator="between",
    formula1=datetime(2024, 1, 1),
    formula2=datetime(2030, 12, 31)
)
ws.add_data_validation(dv_date)
dv_date.add(ws['E5:E100'])

# Dropdown sourced from another Table column
dv_list = DataValidation(
    type="list",
    formula1="=tblOptions[OptionName]",
    allow_blank=True
)
ws.add_data_validation(dv_list)
dv_list.add(ws['F5:F100'])
```

## Conditional Formatting: DataBars (Preferred)

```python
from openpyxl.formatting.rule import DataBarRule

# Standard blue dataBar
rule = DataBarRule(
    start_type='min',
    end_type='max',
    color="638EC6",  # Default Excel blue
)
ws.conditional_formatting.add(f"C3:C{max_row}", rule)

# Branded dataBar using Light Sea Green
rule_branded = DataBarRule(
    start_type='min',
    end_type='max',
    color="41AAA3",  # ADF Light Sea Green
)
ws.conditional_formatting.add(f"D3:D{max_row}", rule_branded)
```

## Column Width Auto-Sizing Pattern

```python
def autofit_columns(ws, min_width=8, max_width=50, padding=2, buffer_cols=None):
    """
    Approximate auto-fit based on content length.
    buffer_cols: list of column letters to keep at width 2.5 (e.g., ['A', 'I', 'J'])
    """
    buffer_cols = buffer_cols or ['A']

    for col_idx in range(1, ws.max_column + 1):
        col_letter = get_column_letter(col_idx)
        if col_letter in buffer_cols:
            ws.column_dimensions[col_letter].width = 2.5
            continue

        max_len = 0
        for row_idx in range(1, min(ws.max_row + 1, 200)):
            cell = ws.cell(row=row_idx, column=col_idx)
            if cell.value is not None:
                cell_len = len(str(cell.value))
                if cell_len > max_len:
                    max_len = cell_len
        width = min(max(max_len + padding, min_width), max_width)
        ws.column_dimensions[col_letter].width = width
```

## TOC Sheet (5+ data sheets only)

```python
# Add ONLY when the workbook has 5 or more data sheets (not counting the TOC itself)
def add_toc(wb, data_sheet_names):
    if len(data_sheet_names) < 5:
        return  # Skip TOC for 2-4 sheet workbooks
    ws_toc = wb.create_sheet("wksTOC", 0)
    ws_toc.column_dimensions['A'].width = 2.5  # Column A buffer
    ws_toc['B2'] = "Table of Contents"
    ws_toc['B2'].font = Font(name='Aptos', size=15, bold=True)

    for i, sheet_name in enumerate(data_sheet_names, start=4):
        cell = ws_toc.cell(row=i, column=2)
        cell.value = f"=HYPERLINK(\"#'{sheet_name}'!A1\",\"{sheet_name}\")"
        cell.font = Font(name='Aptos', size=11, color='0563C1')
        cell.alignment = Alignment(vertical='top')
```

## ADF Brand Palette Constants

```python
# Brand colors
ADF_RAISIN_BLACK   = "231F20"
ADF_DAVY_GREY      = "58585B"
ADF_PRUSSIAN_BLUE  = "0A3D50"
ADF_SMOOTH_GREEN   = "3EAC7A"
ADF_LIGHT_SEA_GREEN = "41AAA3"
ADF_NEPTUNE_CYAN   = "6EB7B2"
ADF_PALE_BLUE_LILY = "D8E7E6"

# Status colors
ADF_STATUS_ON_TRACK = "3EAC7A"
ADF_STATUS_AT_RISK  = "FFC107"
ADF_STATUS_BEHIND   = "FF9800"
ADF_STATUS_CRITICAL = "F44336"
ADF_STATUS_SEVERE   = "B71C1C"

# Branded header (for dashboard title rows, NOT for Table headers)
branded_header_font = Font(name='Aptos', size=15, bold=True, color="FFFFFF")
branded_header_fill = PatternFill(
    start_color=ADF_PRUSSIAN_BLUE,
    end_color=ADF_PRUSSIAN_BLUE,
    fill_type="solid"
)
```

## PivotTable Creation (XML Injection Pattern)

openpyxl does NOT have a reliable high-level API for creating PivotTables. Use this XML injection pattern. It creates a real Excel PivotTable that refreshes on open.

```python
import zipfile, shutil, os
from lxml import etree

def add_pivot_table(xlsx_path, source_sheet, source_ref, source_table_name,
                    pivot_sheet_index, pivot_location_ref,
                    row_field_index, row_field_name, row_values,
                    data_field_index, data_field_name,
                    pivot_name="PivotTable1",
                    num_source_cols=None):
    """
    Inject a PivotTable into an existing xlsx file via XML manipulation.

    Args:
        xlsx_path: Path to the xlsx file (modified in-place)
        source_sheet: Name of the sheet containing source data
        source_ref: Cell range of source data (e.g., "B2:F52")
        source_table_name: Name of the source Excel Table (e.g., "tblRawData")
        pivot_sheet_index: 1-based sheet index where pivot will be placed
        pivot_location_ref: Cell range for pivot output (e.g., "H3:I7")
        row_field_index: 0-based index of the row field in source columns
        row_field_name: Name of the row field column
        row_values: List of unique values for the row field (sorted)
        data_field_index: 0-based index of the data/value field
        data_field_name: Name of the data field column
        pivot_name: Display name for the pivot table
        num_source_cols: Number of columns in the source Table
    """
    NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    NS_RELS = "http://schemas.openxmlformats.org/package/2006/relationships"

    num_vals = len(row_values)
    shared_items_xml = "".join(f'<s v="{v}"/>' for v in row_values)

    items_xml = "".join(f'<item x="{i}"/>' for i in range(num_vals))
    items_xml += '<item t="default"/>'

    row_items_xml = '<i><x/></i>'
    for i in range(1, num_vals):
        row_items_xml += f'<i><x v="{i}"/></i>'
    row_items_xml += '<i t="grand"><x/></i>'

    pivot_fields_parts = []
    for i in range(num_source_cols):
        if i == row_field_index:
            pivot_fields_parts.append(
                f'<pivotField axis="axisRow" showAll="0">'
                f'<items count="{num_vals+1}">{items_xml}</items>'
                f'</pivotField>'
            )
        elif i == data_field_index:
            pivot_fields_parts.append('<pivotField dataField="1" showAll="0"/>')
        else:
            pivot_fields_parts.append('<pivotField showAll="0"/>')

    pivot_cache_def = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pivotCacheDefinition xmlns="{NS}" xmlns:r="{NS_R}" refreshOnLoad="1" createdVersion="8" refreshedVersion="8" recordCount="0">
<cacheSource type="worksheet">
<worksheetSource name="{source_table_name}" sheet="{source_sheet}"/>
</cacheSource>
<cacheFields count="{num_source_cols}">
<cacheField name="{row_field_name}" numFmtId="0">
<sharedItems count="{num_vals}">{shared_items_xml}</sharedItems>
</cacheField>
</cacheFields>
</pivotCacheDefinition>'''

    pivot_cache_records = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pivotCacheRecords xmlns="{NS}" count="0"/>'''

    pivot_table = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pivotTableDefinition xmlns="{NS}" name="{pivot_name}" cacheId="0" dataCaption="Values"
 updatedVersion="8" minRefreshableVersion="3" useAutoFormatting="1" itemPrintTitles="1"
 createdVersion="8" indent="0" outline="1" outlineData="1" multipleFieldFilters="0">
<location ref="{pivot_location_ref}" firstHeaderRow="1" firstDataRow="1" firstDataCol="1"/>
<pivotFields count="{num_source_cols}">
{"".join(pivot_fields_parts)}
</pivotFields>
<rowFields count="1"><field x="{row_field_index}"/></rowFields>
<rowItems count="{num_vals+1}">{row_items_xml}</rowItems>
<colItems count="1"><i/></colItems>
<dataFields count="1">
<dataField name="Sum of {data_field_name}" fld="{data_field_index}" baseField="0" baseItem="0"/>
</dataFields>
<pivotTableStyleInfo name="PivotStyleMedium2" showRowHeaders="1" showColHeaders="1"
 showRowStripes="0" showColStripes="0" showLastColumn="1"/>
</pivotTableDefinition>'''

    tmp = xlsx_path + ".tmp"
    sheet_xml_name = f"xl/worksheets/sheet{pivot_sheet_index}.xml"

    with zipfile.ZipFile(xlsx_path, 'r') as zin, zipfile.ZipFile(tmp, 'w') as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)

            if item.filename == 'xl/workbook.xml':
                tree = etree.fromstring(data)
                pivot_caches = etree.SubElement(tree, f'{{{NS}}}pivotCaches')
                pc = etree.SubElement(pivot_caches, f'{{{NS}}}pivotCache')
                pc.set('cacheId', '0')
                pc.set(f'{{{NS_R}}}id', 'rId_pvtCache1')
                data = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)

            elif item.filename == 'xl/_rels/workbook.xml.rels':
                tree = etree.fromstring(data)
                rel = etree.SubElement(tree, 'Relationship')
                rel.set('Id', 'rId_pvtCache1')
                rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotCacheDefinition')
                rel.set('Target', 'pivotCache/pivotCacheDefinition1.xml')
                data = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)

            elif item.filename == '[Content_Types].xml':
                tree = etree.fromstring(data)
                ns_ct_tag = tree.tag.split('}')[0] + '}' if '}' in tree.tag else ''
                for pn, ct in [
                    ('/xl/pivotCache/pivotCacheDefinition1.xml', 'application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml'),
                    ('/xl/pivotCache/pivotCacheRecords1.xml', 'application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml'),
                    ('/xl/pivotTables/pivotTable1.xml', 'application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml'),
                ]:
                    ov = etree.SubElement(tree, f'{ns_ct_tag}Override')
                    ov.set('PartName', pn)
                    ov.set('ContentType', ct)
                data = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)

            zout.writestr(item, data)

        zout.writestr('xl/pivotCache/pivotCacheDefinition1.xml', pivot_cache_def)
        zout.writestr('xl/pivotCache/pivotCacheRecords1.xml', pivot_cache_records)
        zout.writestr('xl/pivotCache/_rels/pivotCacheDefinition1.xml.rels',
            f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<Relationships xmlns="{NS_RELS}">'
            f'<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotCacheRecords" Target="pivotCacheRecords1.xml"/>'
            f'</Relationships>')
        zout.writestr('xl/pivotTables/pivotTable1.xml', pivot_table)
        zout.writestr('xl/pivotTables/_rels/pivotTable1.xml.rels',
            f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<Relationships xmlns="{NS_RELS}">'
            f'<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotCacheDefinition" Target="../pivotCache/pivotCacheDefinition1.xml"/>'
            f'</Relationships>')
        zout.writestr(f'xl/worksheets/_rels/sheet{pivot_sheet_index}.xml.rels',
            f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<Relationships xmlns="{NS_RELS}">'
            f'<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotTable" Target="../pivotTables/pivotTable1.xml"/>'
            f'</Relationships>')

    shutil.move(tmp, xlsx_path)
```

**Usage:**

```python
add_pivot_table(
    xlsx_path="output.xlsx",
    source_sheet="wksRawData",
    source_ref="B2:F52",
    source_table_name="tblRawData",
    pivot_sheet_index=2,
    pivot_location_ref="H3:I7",
    row_field_index=0,
    row_field_name="commune",
    row_values=["Anse-a-Veau", "Cavaillon", "Fond-des-Blancs", "Jeremie"],
    data_field_index=5,
    data_field_name="monthly_income_htg",
    pivot_name="PivotTable1",
    num_source_cols=6
)
```

**Key notes:**
- Set `refreshOnLoad="1"` so the pivot auto-refreshes on open
- Use `worksheetSource name="tblRawData"` (Table name) instead of a cell range so the cache stays in sync with Table growth
- Place PivotTables on `wksAnaliz` alongside formula-based query tables, or on a dedicated `wksPvt` sheet
- Use `PivotStyleMedium2` to match the overall workbook aesthetic

## Charts: Bar and Scatter Patterns

```python
from openpyxl.chart import BarChart, ScatterChart, Reference, Series

# Bar chart for categorical comparison
bar = BarChart()
bar.type = "bar"       # horizontal bar; use "col" for vertical
bar.style = 2           # Keep it clean; default styles are fine
bar.title = "Revenue by Region (2026 YTD)"
bar.x_axis.title = None  # Drop redundant axis titles; use chart title
bar.y_axis.title = None

cats = Reference(ws, min_col=2, min_row=3, max_row=12)  # Category labels
data = Reference(ws, min_col=3, min_row=2, max_row=12)  # One data series incl. header
bar.add_data(data, titles_from_data=True)
bar.set_categories(cats)
bar.legend = None  # Drop legend when only one series; direct-label via data labels

ws.add_chart(bar, "F3")

# Scatter for continuous relationships
scatter = ScatterChart()
scatter.style = 2
scatter.title = "Age vs. Income"
xvals = Reference(ws, min_col=3, min_row=3, max_row=102)
yvals = Reference(ws, min_col=4, min_row=3, max_row=102)
series = Series(yvals, xvals, title_from_data=False)
scatter.series.append(series)
ws.add_chart(scatter, "F20")
```

**Banned:** pie (PieChart), doughnut (DoughnutChart), area (AreaChart), 3D variants. Do not instantiate these.

## Complete Example: Analysis Workbook with Buffers

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo, TableColumn
from openpyxl.utils import get_column_letter
from datetime import datetime

wb = Workbook()
wb._named_styles['Normal'].font = Font(name='Aptos', size=11)

# Raw data sheet
ws_data = wb.active
ws_data.title = "wksRawData"
ws_data.column_dimensions['A'].width = 2.5
ws_data.sheet_format.defaultRowHeight = 15

# Analysis sheet (for formula-based summaries)
ws_analiz = wb.create_sheet("wksAnaliz")
ws_analiz.column_dimensions['A'].width = 2.5

# Pivot sheet (for PivotTables)
ws_pvt = wb.create_sheet("wksPvtSummary")
ws_pvt.column_dimensions['A'].width = 2.5

# Populate wksRawData with headers in row 2, data from row 3
headers = ["commune", "household_id", "household_size", "survey_date", "monthly_income_htg"]
for i, h in enumerate(headers):
    ws_data.cell(row=2, column=2 + i, value=h)

# (fill data rows 3..52 here; dates as datetime objects with yyyy-mm-dd format)

# Create the Table (range includes header row 2 through data row 52)
style_default = TableStyleInfo(name="TableStyleMedium2",
                                showFirstColumn=False, showLastColumn=False,
                                showRowStripes=True, showColumnStripes=False)

table = Table(
    displayName="tblRawData",
    ref=f"B2:F52",
    tableStyleInfo=style_default
)
ws_data.add_table(table)

# Top-align all populated cells
for row in ws_data.iter_rows(min_row=2, max_row=52, min_col=2, max_col=6):
    for cell in row:
        cell.alignment = Alignment(vertical='top')

# Set column widths (auto-fit-ish)
for col_letter, width in [('B', 18), ('C', 14), ('D', 16), ('E', 14), ('F', 20)]:
    ws_data.column_dimensions[col_letter].width = width

# Only 3 data sheets; skip wksTOC per the 5+ rule.

wb.save("output.xlsx")
```

## Checklist Before Saving

1. All data ranges are formal Tables (no plain ranges)
2. All Tables have intentional names (`tbl`/`qry` prefix, PascalCase)
3. Tables with numeric columns have Total Row enabled AND SUBTOTAL formulas written into cells
4. All formulas use structured references (not A1/B2 cell references) inside Tables
5. Font is Aptos 11pt throughout (set via Normal style only; no manual application)
6. Sheet names follow prefix conventions (no `Sheet1`, `Sheet2`)
7. Row 1 is empty. Column A is empty with width 2.5.
8. Inter-Table buffer columns are 2.5 wide and empty
9. All cells are top-aligned; default row height is 15; Shrink to fit used for potential overflow
10. No merged cells (except dashboard titles)
11. No cell comments
12. No protection, no macros, no VBA
13. Column widths are reasonable (not default 8.43); buffer cols are 2.5
14. If 5+ data sheets: `wksTOC` exists. Skip TOC for 2-4 sheet workbooks.
15. If client deliverable: ADF brand palette applied on dashboards
16. No `TableStyleDark*` or `TableStyleMedium7` styles anywhere
17. No hardcoded summary data; every aggregation is a formula or PivotTable
18. No extra fills, colored section headers, or decorative formatting on data workbooks
19. No manual Font/Fill formatting on Table header rows (Table Style governs headers)
20. All dates are real `datetime` objects with `yyyy-mm-dd` number format (never text strings)
21. Total row cells are populated with `SUBTOTAL` formulas and "Total" label (not blank)
22. No pie, doughnut, 3D, or area charts; bar and scatter only (line for time series when requested)
23. Input cells (if any) use Pale Blue Lily `#D8E7E6` fill; data validation applied where appropriate
24. File opens in Excel without repair dialog and without error-check flags on any cell
