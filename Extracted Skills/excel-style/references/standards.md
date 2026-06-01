# Excel Style Standards: Full Reference

This document contains the complete, detailed standards derived from analysis of 18 of Josiah's working Excel files, combined with the Claude-for-Excel operating rules for ADF Haiti. Each rule includes the standard, rationale, evidence, and exceptions.

## Table of Contents

1. [Operating Context](#1-operating-context)
2. [Absolute Rules](#2-absolute-rules)
3. [Visual Design](#3-visual-design)
4. [Structure and Layout](#4-structure-and-layout)
5. [Data Formatting](#5-data-formatting)
6. [Formulas and Calculations](#6-formulas-and-calculations)
7. [Charts and Visualizations](#7-charts-and-visualizations)
8. [Conditional Formatting](#8-conditional-formatting)
9. [Workflow and Usability](#9-workflow-and-usability)
10. [Table Styles](#10-table-styles)
11. [Branding](#11-branding)
12. [Scripting](#12-scripting)
13. [Revision Protocol](#13-revision-protocol)
14. [Operating Behavior and Communication](#14-operating-behavior-and-communication)

---

## 1. Operating Context

User: Josiah Thomas, Executive Director of ADF Haiti (Association pour le Développement de Fond-des-Blancs), a Haitian-led nonprofit. Typical workbooks:

- Survey datasets and M&E analyses (Fulcrum exports, household/community surveys, parcel surveys)
- Budgets and financial models for consulting engagements ($5K to $150K)
- Client deliverables: pivot summaries, GIS mapping tables, needs assessments, evaluations
- Internal operations: staff rosters, performance tracking, cash flow models

Mixed Haitian Creole and English vocabulary (e.g., `qryAnkEndividyel`, `Evalyasyon_Bezwen`, `wksAnaliz`, `tblMetrikAnplwaye`, `AnalizVant`) is intentional. Preserve it. Never "correct" Creole domain terms to English.

---

## 2. Absolute Rules

These rules are non-negotiable. Violating any one of them produces a workbook that fails on open or misrepresents data.

1. NEVER fabricate numbers, formulas, findings, or sources. If a value is not in the workbook and cannot be derived, say so.
2. Every data range MUST be a proper Excel Table (including single-column lookup lists).
3. Summary, analysis, and dashboard sheets MUST use formulas (SUMIFS, COUNTIFS, AVERAGEIFS with structured references) or live PivotTables. Hardcoded numbers on derived sheets are forbidden.
4. Dates MUST be real Excel date serials, never text. Default display: `yyyy-mm-dd`.
5. Formulas inside a Table context MUST use structured references. A1 or R1C1 references inside a Table are forbidden.
6. NEVER manually format Table header rows (bold, fill, font color, size). The Table Style governs header appearance.
7. NEVER apply custom fills to Table body cells. Exception: Pale Blue Lily `#D8E7E6` for input cells in templates.
8. NEVER add macros, ActiveX, VBA, sheet/workbook protection, or passwords unless explicitly requested. Output `.xlsx` only.
9. NEVER use pie, doughnut, 3D, or area charts.
10. NEVER use the em dash character in commentary, cell content, documentation, or chat responses. Use parentheses, colons, or semicolons for parenthetical offsets.
11. Before declaring a task done, verify the workbook opens cleanly (no repair dialog, no error-check flags).

---

## 3. Visual Design

### 3.1 Typography

**Rule:** Use Aptos 11pt as the default font for all cell content.

- **Standard:** Aptos 11pt regular for body text; Aptos 11pt Bold for table headers and section titles OUTSIDE of Tables. Larger sizes (13pt, 15pt) only for workbook-level titles on dashboard or summary sheets.
- **Set via the `Normal` named style**, not by applying Font to individual cells. This ensures consistency and lets the Table Style govern header appearance.
- **Rationale:** Aptos is the stated brand font for ADF. The file corpus shows a transition from Calibri (legacy, 16/18 files) to Aptos (3/18 recent files). New files follow the Aptos direction.
- **Exception:** When editing an existing file that uses Calibri, match Calibri to avoid font-mixing. Aptos Narrow is acceptable for data-dense sheets where column width is constrained.

### 3.2 Bold, Italic, and Manual Header Formatting

**Rule:** Bold is reserved for headers and titles OUTSIDE of Tables. Italic is effectively unused. NEVER manually format Table header rows.

- **Standard:** Apply bold only to: sheet-level titles and section labels outside of Tables. Table header rows are styled automatically by the Table Style; do NOT manually apply Font (bold, color, size) or Fill to Table header cells. Any manual formatting on header cells will conflict with the Table Style and produce inconsistent results when the style changes.
- **Rationale:** The corpus consistently uses bold only for structural emphasis, never for data highlighting. Manual header formatting overrides Table Style appearance and causes visual inconsistency.
- **Evidence:** Bold cells are <2% of total cells across all 18 files. Italic appears in only 2-3 files for minor annotations.

### 3.3 Alignment and Row Height

**Rule:** Top-align all cells. Default row height 15.

- **Standard:** Set vertical alignment to top for all cells. Default row height: 15 points. When text overflows a cell, prefer the "Shrink to fit" cell format property over "Wrap text" to keep rows uniform and dense.
- **Rationale:** Top-alignment reads cleanly when rows contain mixed content lengths. Shrink-to-fit avoids the row-height inflation that Wrap-text causes.
- **Exception:** Use Wrap text when a column is intentionally wide for long-form notes (e.g., a `Notes` or `Description` column).

### 3.4 Merged Cells

**Rule:** Avoid merged cells.

- **Standard:** Do not merge cells. The only acceptable use is a single merged title row spanning the full visual width of a dashboard or summary sheet. When a merge is genuinely required, use "Merge Across" (horizontal only, per row) rather than "Merge & Center."
- **Rationale:** Merged cells break Table functionality, pivot table source ranges, and programmatic data access.
- **Evidence:** Only 2/18 files have any merged cells (Performance Workbook: dashboard titles; IPUMS: header rows).

### 3.5 Borders

**Rule:** Do not manually apply borders. Let Table Styles handle visual structure.

- **Standard:** No explicit border formatting on data cells. Tables provide row banding and header separation automatically.
- **Rationale:** Manual borders conflict with Table Styles, create maintenance burden, and look inconsistent when rows are added/removed.
- **Evidence:** Only 3/18 files use explicit borders; the rest rely entirely on Table formatting.
- **Exception:** Thick borders used sparingly in the Performance Workbook for dashboard section separation (1 file, branded deliverable).

### 3.6 Fill Colors and Theming

**Rule:** Default Excel theme colors for data workbooks. ADF brand palette only for dashboards and client deliverables.

- **Standard:** For standard data/analysis work, rely on Table Style built-in fills. Do not add extra fills, colored section headers, or decorative formatting. The Table Style provides all visual structure. Over-styling is worse than under-styling. For dashboards and client deliverables, apply the ADF brand palette (see Section 11). Never apply fill colors to individual cells within a Table.
- **Evidence:** 17/18 files use only theme-based fills. Only the Performance Workbook uses custom ADF hex colors.
- **Exception:** Pale Blue Lily `#D8E7E6` fill is acceptable on input cells in templates. Conditional formatting fills (dataBar, highlight cells) are applied programmatically and do not conflict with this rule.
- **Brand-derived colors:** Colors close to the ADF palette (not exact hex matches) are acceptable when they read as ADF. Do not flag brand-derived colors as off-palette.

---

## 4. Structure and Layout

### 4.1 Layout Buffers (Row 1 and Column A)

**Rule:** Reserve Row 1 and Column A as spacing buffers. Place content starting at row 2, column B.

- **Standard:** Row 1 stays empty. Column A stays empty with width `2.5`. This creates visual breathing room and makes workbooks feel professionally laid out rather than cramped against the edge.
- **Inter-Table buffers:** Leave 2 to 3 empty buffer columns between Tables and surrounding elements. Buffer column width: `2.5`. Example: if a second table starts at column N, columns L and M stay blank at width 2.5.
- **Auto-fit** all data column widths. Manually set `2.5` on buffer columns.
- **Rationale:** Buffer columns and rows make layouts breathable and clearly delineate sections without requiring borders or fills.

### 4.2 Sheet Naming

**Rule:** Use PascalCase prefixed names with no spaces.

- **Standard:** Every sheet name MUST start with a prefix indicating its purpose:
  - `wks` : General worksheet (default)
  - `wksPvt` : Contains a pivot table
  - `wksQry` : Contains query/extracted data
  - `wksTOC` : Table of contents with `HYPERLINK` navigation
  - `wksReadMe` : Documentation/instructions
  - `wksBkp` + YYYYMMDD : Backup snapshot of another sheet
  - Standalone `qry`, `pvt`, `tbl` prefixes: Acceptable in heavily structured workbooks
- **Rationale:** Prefixes enable instant identification of sheet purpose in the sheet tab bar. PascalCase without spaces avoids quoting issues in formulas and structured references.
- **Evidence:** 75/137 sheets (55%) use `wks` prefix across 15/18 files. `qry` prefix on 14 sheets. PascalCase is near-universal.
- **Exception:** Client-facing BHI-style reports may use numbered names ("1. Table Of Contents", "2. Household Demographics") where tab names serve as a visible table of contents.

### 4.3 Excel Tables (Mandatory)

**Rule:** Every data range MUST be formatted as a proper Excel Table.

- **Standard:** Use openpyxl's `Table` object with `TableStyleInfo`. Never leave data as a plain range. Tables enable structured references, auto-filtering, total rows, and consistent formatting.
- **Config:** `showRowStripes=True`, `showColumnStripes=False`, `showFirstColumn=False`, `showLastColumn=False`.
- **Rationale:** Tables are the foundation of the entire workbook structure. They enable structured references (Section 6.1), SUBTOTAL total rows (Section 6.2), and prevent formula errors from range drift.
- **Evidence:** 17/18 files contain formal Excel Tables. 102 total tables across the corpus.
- **Exception:** None. Even single-column reference lists should be Tables.

### 4.4 Table Naming

**Rule:** Use PascalCase prefixed names matching the table's role.

- **Standard:**
  - `tbl` prefix: Primary data tables (63% of observed tables). Example: `tblMainDonorList`, `tblEmployees`, `tblBSC`
  - `qry` prefix: Query/derived/calculated tables (16% of observed tables). Example: `qryDjobKopiEnpresyon`, `qryAnkEndividyel`
  - Avoid generic auto-names like `Table1`, `Table6`
- **Evidence:** 64/102 tables use `tbl` prefix; 16/102 use `qry`. PascalCase is universal for intentionally named tables.

### 4.5 Table Total Row

**Rule:** Enable the Excel Table Total Row feature on tables with numeric columns. Implementation MUST be Excel-safe.

- **Standard:** Use the built-in Table Total Row (Table Tools > Design > Total Row checkbox). Configure SUBTOTAL formulas on numeric columns: `SUBTOTAL(109, tblName[Column])` for sums, `SUBTOTAL(103, ...)` for COUNTA (non-empty counts). Do NOT add a manual sum row below the table.
- **openpyxl implementation:** Set `totalsRowCount=1` on the Table AND write actual values into the total row cells. Write `"Total"` into column A of the total row. Write `=SUBTOTAL(109,tblName[Column])` into each numeric total cell. The table `ref` must include the total row. Leaving total row cells blank causes Excel to show "Repaired Records: Table" error on open.
- **Rationale:** The Table Total Row automatically adjusts when rows are added/filtered. Manual sum rows break when the table expands. SUBTOTAL respects active filters.
- **Evidence:** SUBTOTAL(109,...) appears in 3/18 files (Fluxx Budget, Slack WKKF, Analiz_Biznis).
- **Exception:** Tables with no numeric columns (e.g., a pure text lookup table) do not need a Total Row.

### 4.6 Frozen Panes

**Rule:** Avoid frozen panes by default.

- **Standard:** Do not freeze panes unless the user explicitly requests it or the dataset exceeds 50 columns. Tables already provide header row visibility via the "Header Row" option.
- **Evidence:** Only 3/18 files use frozen panes. Two freeze column A only; one freezes 3 columns.

### 4.7 TOC Navigation

**Rule:** Add a `wksTOC` sheet with `HYPERLINK` navigation for workbooks with 5 or more data sheets only.

- **Standard:** Create `wksTOC` as the first sheet. Each row contains a HYPERLINK formula: `=HYPERLINK("#'sheetName'!A1","sheetName")`.
- **Evidence:** 2/18 files (Slack WKKF, BHI) use this pattern.
- **Exception:** Workbooks with 2, 3, or 4 data sheets do NOT need a TOC. It adds clutter at that scale. Count data sheets only (not the TOC itself).

### 4.8 ReadMe / Reference Sheets

**Rule:** Add documentation sheets for complex workbooks.

- **Standard:** For workbooks with business logic, assumptions, or multi-step workflows, add `wksReadMe` (user instructions) or a `Referans`/`wksReferenceTables` sheet (lookup values, color keys, status definitions).
- **Evidence:** Performance Workbook has `wksReadMe` and `Referans`. Competition Analysis has `wksReferenceTables`.

### 4.9 Pivot-Ready Structure

**Rule:** Structure data tables for aggregation in PivotTables.

- **Standard:** Include a repeating category/identifier column that groups related rows. Example:
  ```
  | Category  | Item                          | Unit Cost |
  |-----------|-------------------------------|-----------|
  | Structure | Portland cement (42.5kg bags) | 850       |
  | Structure | Concrete block 15cm           | 45        |
  | Roofing   | Galvanized sheet 10ft         | 1200      |
  | Roofing   | Ridge cap                     | 350       |
  ```
- **Rationale:** Category column enables PivotTable summarization without restructuring.
- **Evidence:** Confirmed in Analiz_Biznis, BHI, Fulcrum data files.

---

## 5. Data Formatting

### 5.1 Date Format and Storage

**Rule:** Dates MUST be real Excel date serial numbers, not text strings. Default display: `yyyy-mm-dd`.

- **Standard:** In openpyxl, write Python `datetime` objects and apply number format `yyyy-mm-dd`. Never write date strings like "04-01-26" as text; Excel flags these as "Text Date with 2-Digit Year" errors and they cannot sort, filter, or participate in date arithmetic. For datetime fields: `yyyy-mm-dd h:mm`.
- **Exception:** `mm/dd/yyyy` acceptable if user explicitly requests US format.

### 5.2 Percentages

**Rule:** Default to `0.00%` for percentage fields.

- **Standard:** Two decimal places. Use `0%` only for whole-number completion metrics.
- **Evidence:** 4/18 files use `0.00%`; 2 use `0%`; 1 uses `0.0%`.

### 5.3 Currency

**Rule:** Use locale-aware currency formatting and always specify currency in the column header.

- **Standard:**
  - Haitian Gourde: `[$HTG] #,##0.00`
  - US Dollar: `"$"#,##0.00` or `_("$"* #,##0.00_)`
- Include the currency name in the column header (e.g., `Montan (HTG)`, `Amount (USD)`).
- **Exception:** When a workbook deals exclusively in one currency and the header makes it unambiguous.

### 5.4 Thousands and Decimals

**Rule:** `#,##0` for whole numbers; `#,##0.00` for decimals. Apply thousands separators to any numeric column routinely exceeding 999.

- **Exception:** ID numbers, codes, phone numbers remain unformatted text.

### 5.5 Zero Handling

**Rule:** Display actual zeros. Do NOT use dash-for-zero formatting.

- **Standard:** The public xlsx skill mandates `$#,##0;($#,##0);-`. This is NOT used here. Display `0` or `0.00` as appropriate.
- **Evidence:** 0/18 files use dash-for-zero formatting.

---

## 6. Formulas and Calculations

### 6.1 Structured Table References

**Rule:** All formulas inside a Table context MUST use structured references, not cell addresses.

- **Standard:**
  - Same-row: `tblName[@[ColumnName]]` or `tblName[[#This Row],[ColumnName]]`
  - Whole-column: `tblName[ColumnName]`
  - Totals-row: `tblName[[#Totals],[ColumnName]]`
- **Never** use `A1`, `$B$5`, or `R1C1` style references within a Table context.
- **Evidence:** Every formula-bearing file (6/18) uses structured references predominantly:
  - `=tblSlackEngagementSurvey[[#This Row],[Frequency]]/tblUseResponseCount[[#Totals],[Frequency]]`
  - `=SUMIFS(qryDjobKopiEnpresyon[Montant],qryDjobKopiEnpresyon[Mwa],AnalizVant[[#This Row],[Mwa]])`
  - `=COUNTIF(tblDataShareEnfoEndividyel[451_laj_moun_lan],"<18")`
- **Exception:** Cell references acceptable for cross-sheet references outside of Tables, or for HYPERLINK targets.

### 6.2 SUBTOTAL for Totals

**Rule:** Use SUBTOTAL function (109) for filtered-aware sums in Table Total Rows.

- **Standard:** `SUBTOTAL(109, tblName[Column])` for sums. `SUBTOTAL(103, ...)` for COUNTA. Respects active filters.
- **Evidence:** 3/18 files use SUBTOTAL with function 109.

### 6.3 Aggregation Functions

**Rule:** Prefer SUMIFS for conditional aggregation; INDEX/MATCH for lookups.

- **Standard:**
  - `SUMIFS` / `COUNTIFS` / `AVERAGEIFS` for conditional aggregation (not `SUMPRODUCT`, not filtered ranges)
  - `INDEX`/`MATCH` for lookups (not `VLOOKUP`; `XLOOKUP` only if workbook targets Excel 365 only)
  - `COUNTIF`/`COUNTA` for data quality counts
  - `IFERROR` for error handling on lookups and division
- **Evidence:** SUMIFS: 217 uses in Analiz_Biznis. INDEX/MATCH: 17 each. VLOOKUP: 0 uses across all 18 files.

### 6.4 Error Handling

**Rule:** Wrap lookups and divisions in IFERROR.

- **Standard:** `=IFERROR(formula, "NA")` for lookups that may miss a match; `=IFERROR(formula, 0)` for divisions that may hit zero denominators.
- **Evidence:** Competition Analysis wraps age calculations in IFERROR consistently.

### 6.5 No Hardcoded Summary Data

**Rule:** Every summary, analysis, or derived sheet MUST pull values from source tables via formulas or live PivotTables.

- **Standard:** A summary table with static numbers typed into cells is never acceptable. If a value can be calculated from source data, it MUST be a formula or a PivotTable.
- **Rationale:** Static summaries are immediately stale when source data changes and cannot be audited.
- **Evidence:** All analysis files in the corpus (Analiz_Biznis, Competition, Slack WKKF) use formula-driven summaries.

---

## 7. Charts and Visualizations

### 7.1 Chart Type Selection

**Rule:** Default to bar charts for categorical comparisons. Scatter for continuous relationships. BAN pie, doughnut, 3D, and area charts.

- **Standard:**
  - **Bar** (horizontal or vertical) for comparing categories, frequencies, survey responses, demographic breakdowns
  - **Scatter** for plotting two continuous variables against each other
  - **Line** acceptable for time series when explicitly requested
  - **100% stacked bar** instead of pie for parts-of-a-whole comparisons
  - **Histogram** for distributions of a single variable
  - **BANNED:** pie, doughnut, area, 3D (any variant), radar, surface
- **Evidence:** 42 bar charts across 4 files; 20 scatter charts in 2 files. Zero pie, area, or 3D charts in the entire corpus.

### 7.2 Chart Selection by Analytical Question

Match chart to the question being asked:

| Question | Chart |
|---|---|
| How do these categories compare? | Horizontal or vertical bar |
| How does this change over time? | Line (time series) or bar (discrete periods) |
| How are these two variables related? | Scatter |
| How is this single variable distributed? | Histogram |
| What share does each part contribute? | 100% stacked bar (never pie) |
| Where is this located? | Geographic map (outside Excel's native chart types) |
| How do these items rank? | Sorted bar chart |

### 7.3 Chart Formatting (Dataviz Discipline)

**Rule:** Keep charts clean. Declutter aggressively. Use color to highlight.

- **Standard:**
  - Default Excel chart styles; remove excess gridlines, borders, chart-area fills
  - Direct data labels preferred over legends when few series
  - One accent color on the focal series; neutral grey (`#999999` or `#BFBFBF`) on context series
  - Consistent color meaning within a workbook (same category gets same color across charts)
  - No 3D effects, no shadows, no rotating
  - Title explains the insight, not the data source (e.g., "Revenue concentrated in Q4" not "Revenue by quarter")
- **Rationale:** Dataviz principles per IBCS, Knaflic, Evergreen, FT Visual Vocabulary: declutter, focus attention, label directly, use color with intent.
- **Branded deliverables:** Apply ADF palette to chart series. Prussian Blue `#0A3D50` as primary/focal, Light Sea Green `#41AAA3` as secondary, Smooth Green `#3EAC7A` for positive status, Neptune Cyan `#6EB7B2` for tertiary.

### 7.4 Axis and Scale

- Always start numeric axes at zero for bar charts (truncated axes mislead).
- Scatter and line chart axes may start away from zero when the data range justifies it.
- Use thousands/millions scaling when values exceed 10,000 (axis label "Revenue (millions USD)").
- Format axis numbers with thousands separators.

---

## 8. Conditional Formatting

### 8.1 Preferred Types

**Rule:** Use conditional formatting (especially dataBars) for visual data analysis on summary sheets.

- **Standard:**
  - **dataBars** are the primary CF type. Apply to numeric columns on analysis/pivot sheets.
  - **containsText** for flagging specific values
  - **duplicateValues** for data quality checks
  - **top10** for highlighting outliers
- **Evidence:** 10/18 files use CF. dataBar accounts for ~90% of all CF rules. Used heavily in analysis files (BHI: 132 rules, Competition: 26, Fulcrum HDI: 95).
- **Exception:** Never apply CF to raw data entry sheets.

### 8.2 dataBar Color

- Default Excel blue (`#638EC6`) for standard workbooks.
- Light Sea Green (`#41AAA3`) for branded workbooks.
- Status scale colors for status columns (Smooth Green / Yellow / Orange / Red / Dark Red).

---

## 9. Workflow and Usability

### 9.1 Protection

**Rule:** Never protect sheets or workbooks.

- **Standard:** No password protection, no sheet protection, no cell locking. All cells remain editable.
- **Evidence:** 0/18 files use any form of protection.

### 9.2 Comments

**Rule:** Do not use cell comments.

- **Standard:** Document assumptions in a `wksReadMe` sheet or `Referans` sheet. For inline notes, add a dedicated "Notes" column in the Table.
- **Evidence:** 0/18 files contain cell comments.

### 9.3 Data Validation

**Rule:** Add data validation to input cells in templates.

- **Standard:** For workbooks that accept user input (budgets, templates, forms), add dropdown lists, numeric ranges, or date constraints using Excel's Data Validation feature.
- **Evidence:** 1/18 files (Performance Workbook) uses data validation.

### 9.4 Input vs. Output Cell Distinction

**Rule:** Visually distinguish input cells in template workbooks.

- **Standard:** Apply Pale Blue Lily fill `#D8E7E6` to input cells; leave calculated cells unfilled. Do NOT use the public xlsx skill's blue-text convention.
- **Rationale:** Pale Blue Lily reads as a subtle input marker and matches the ADF palette.

---

## 10. Table Styles

### 10.1 Default Style

**Rule:** Use `TableStyleMedium2` as the default.

- **Standard:** Apply `TableStyleMedium2` (blue header row, alternating white/light blue row banding) to all tables unless a contextual override applies.
- **Evidence:** 47/102 tables (46%) across 9/18 files use TableStyleMedium2.

### 10.2 Role-Based Overrides

| Table Role | Style | Evidence |
|---|---|---|
| Primary/default | `TableStyleMedium2` | 47 tables, 9 files |
| Analysis/derived | `TableStyleMedium16` | 25 tables, 1 file (but consistent) |
| Reference/lookup | `TableStyleMedium9` | 5 tables, 1 file |
| ~~Source/raw data~~ | ~~`TableStyleMedium7`~~ | BANNED: use TableStyleMedium2 for raw data |
| ~~Project schedules~~ | ~~`TableStyleDark1`~~ | BANNED: do not use any TableStyleDark* style |

- **Standard:** If using multiple styles in one workbook, each style must map to a consistent role. Do not mix styles arbitrarily.
- **Exception:** When editing an existing workbook, match its existing style rather than forcing a change.

### 10.3 Configuration

**Rule:** Enable row stripes; disable column stripes.

```python
TableStyleInfo(
    name="TableStyleMedium2",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False
)
```

---

## 11. Branding

### 11.1 ADF Brand Palette

**Rule:** Apply the full ADF palette for dashboards and client deliverables. Standard data/analysis workbooks use default theme colors.

| Name | Hex | Use |
|---|---|---|
| Raisin Black | `#231F20` | Body text, primary headings |
| Davy Grey | `#58585B` | Secondary text, subheadings |
| Prussian Blue | `#0A3D50` | Primary accent (cover pages, heading bars, branded headers) |
| Smooth Green | `#3EAC7A` | Secondary accent, positive status |
| Light Sea Green | `#41AAA3` | Tertiary accent, chart elements, tab colors |
| Neptune Cyan | `#6EB7B2` | Light accent (borders, dividers) |
| Pale Blue Lily | `#D8E7E6` | Background fill, branded banding, input-cell marker |

Colors derived from the ADF palette (close neighbors, not exact hex matches) are acceptable. Do not flag brand-derived colors as off-palette.

### 11.2 Status Indicator Colors

| Status | Hex |
|---|---|
| On track | `#3EAC7A` |
| At risk | `#FFC107` |
| Behind | `#FF9800` |
| Critical | `#F44336` |
| Severe | `#B71C1C` |

### 11.3 Mixed Language Convention

**Rule:** Domain terms in Haitian Creole; technical/structural terms in English.

- **Standard:** Sheet names, table names, and column headers commonly mix Creole domain vocabulary (Analiz, Metrik, Done, Mwa, Biznis, Kalite, Vant, Endividyel, Evalyasyon) with English structural terms (Data, Analysis, Main, TOC, ReadMe). This is intentional; preserve it. Never "correct" Creole to English.
- **Evidence:** Observed throughout the corpus (`wksAnaliz`, `tblMetrikAnplwaye`, `AnalizVant`, `qryDjobKopiEnpresyon`, `Evalyasyon_Bezwen_Lekol_FdB`).
- **Exception:** For client deliverables to English-speaking audiences, use English throughout.

---

## 12. Scripting

**Rule:** Prefer Office Scripts (TypeScript) over VBA or legacy macros for automation requests.

- **Standard:** If the user requests automation code, write Office Scripts unless the user explicitly asks for VBA. State assumptions explicitly (target workbook structure, ranges, trigger mode). Output files remain `.xlsx` unless user requests `.xlsm`.
- **Rationale:** Office Scripts are cross-platform (web, desktop), work with modern Excel, and don't carry macro-security baggage. VBA is legacy and triggers security warnings.

---

## 13. Revision Protocol

**Triggered by:** `improve`, `fix`, `clean up`, `repair`, `review`, `audit`, `standardize`.

### 13.1 Style Inheritance

- If the workbook's existing Table styles, PivotTable styles, colors, and themes are ADF brand-derived: **inherit them**. Do not replace with defaults.
- If the existing styling is NOT brand-derived: apply the defaults from this document (`TableStyleMedium2`, role-based overrides, ADF palette where appropriate).
- Role-based Table style overrides and banned-style rules apply to new workbooks, or to revisions where the existing styling is not brand-derived.

### 13.2 PivotTable Caveat (Audit Mode)

**Before** flagging any summary block as hardcoded or a dead copy of a source Table, inspect `worksheet.pivotTables` on that sheet. PivotTable output cells read as raw numeric values through structured cell reads but are live aggregations from their source Table. They are compliant, not violations. Confirm a range is not a PivotTable output before calling it static.

### 13.3 Diagnostic Pass

Run BEFORE making any changes. Report findings as a numbered list. Execute fixes in dependency order (structural first, cosmetic last). For destructive changes (deleting sheets, replacing formulas not authored by Claude, removing data), state the change and wait for confirmation.

**25-point diagnostic checklist:**

1. Data ranges that are not Excel Tables. Convert.
2. Text dates flagged as "Text Date with 2-Digit Year." Convert to real dates, apply `yyyy-mm-dd`.
3. Manual sum rows below data. Remove and enable Total Row with `SUBTOTAL`.
4. A1 or R1C1 references inside Tables. Rewrite as structured references.
5. Generic sheet or table names (`Sheet1`, `Table1`, `Table6`). Rename per convention.
6. Merged cells outside dashboard title rows. Unmerge and restructure.
7. Hardcoded numbers on summary or analysis sheets. Replace with `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` or a live PivotTable.
8. Tables with numeric columns lacking Total Rows. Enable with `SUBTOTAL(109, ...)`.
9. Manually formatted Table headers (bold, fill, font color). Strip so the Table Style governs.
10. Custom fills on Table body cells. Remove, except Pale Blue Lily input-cell markers.
11. Banned styles (`TableStyleDark*`, `TableStyleMedium7`). Switch to `TableStyleMedium2` or role-based override.
12. Inconsistent number formats within a single column. Standardize.
13. Pie, doughnut, 3D, area charts. Propose bar or scatter; rebuild on approval.
14. Cell comments. Migrate to `wksReadMe` or a Notes column.
15. Workbook or sheet protection. Remove unless explicitly requested.
16. Frozen panes without clear justification. Remove.
17. Missing data validation on input-template cells. Add dropdowns, numeric ranges, date constraints.
18. Workbook with 5+ data sheets and no `wksTOC`. Add one with `HYPERLINK` navigation.
19. Spaces or special characters in sheet or table names. Rename PascalCase.
20. `.xlsm` file with no active macros. Recommend Save As `.xlsx`.
21. Duplicate values in ID or key columns. Flag for review.
22. Broken formulas (`#REF!`, `#NAME?`, circular references). Diagnose root cause before patching.
23. Columns with mixed types (numbers as text, dates as strings). Convert.
24. Data entry tables missing a repeating category or grouping column. Propose restructure.
25. Missing buffer spacing (Row 1, Column A at width 2.5, inter-Table columns). Add.

### 13.4 Fix Execution Order

Execute in dependency order:

1. **Structural first:** Convert ranges to Tables; fix text dates; rename sheets/tables; unmerge cells; restructure data
2. **Formulas next:** Replace A1 references with structured references; replace hardcoded summaries with SUMIFS/COUNTIFS or PivotTables; wrap in IFERROR
3. **Total rows:** Enable Total Rows and write SUBTOTAL formulas
4. **Banned styles:** Switch to TableStyleMedium2 or role-based override
5. **Cosmetic last:** Strip manual header formatting; remove custom fills; apply Pale Blue Lily to input cells; apply Aptos 11pt via Normal style; set buffer column widths
6. **Navigation:** Add `wksTOC` if 5+ data sheets
7. **Verification:** Open in Excel (or LibreOffice with recalc) and confirm no repair dialog, no error-check flags, no broken formulas

---

## 14. Operating Behavior and Communication

### 14.1 Operating Behavior

- Read the open workbook's structure (sheets, tables, named ranges, PivotTables) before making substantive changes.
- Execute silently. Do not narrate cell clicks, tool mechanics, or internal file reads. Lead with the result (numbers, before/after, chart).
- For multiple changes: compact numbered summary at the end, one line per change. No play-by-play.
- If the user's request cannot be derived from the workbook, say so explicitly. Do not invent data.
- Before declaring done, verify the file opens in Excel without repair dialogs or error-check flags.

### 14.2 Communication

- Professional casual tone suitable for a 40-year-old executive peer.
- Radically direct. State findings plainly. No hedging, sugarcoating, or over-caveating.
- No unprompted praise ("great question"), no motivational padding, no polite filler.
- No em dashes. Use parentheses, colons, or semicolons for parenthetical offsets.
- Default language English. Switch to Haitian Creole for domain terms when the workbook already uses them. Preserve existing mixed-language vocabulary; never "normalize" Creole to English.

### 14.3 Escape Clause

If any instruction here would require fabricating or distorting facts, break the instruction and explain why. This overrides formatting, brevity, and style rules.
