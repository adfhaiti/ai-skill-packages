---
name: excel-style
description: "ADF’s Excel formatting, structure, and operational standards for workbooks. Use these for any .xlsx file, spreadsheet, budget, data table, model, or tabular output (financial models, survey datasets, M&E analyses). This skill overrides the public xlsx skill’s visual defaults (fonts, colors, styles, zero/negative formatting) with ADF’s conventions, and adds layout/spacing rules, a revision protocol, chart restrictions, and operating behavior rules. Apply this skill to any request involving Excel or spreadsheet files. Trigger on: Excel, spreadsheet, .xlsx, workbook, data table, budget, model, pivot, chart, tabular data, xls, openpyxl, pandas to_excel, Office Scripts, or any spreadsheet file request. Also trigger on revision verbs: improve, fix, clean up, repair, review, audit, standardize. If the user says 'put this in a spreadsheet' or 'make me a table', use this skill. Use alongside the public xlsx skill for code; this skill covers visual, structure, layout, and behavior."
---

# Josiah's Excel Style + Operating Standards

These standards override the public xlsx skill's defaults where they conflict. The public xlsx skill still governs code mechanics (openpyxl patterns, pandas, LibreOffice recalc, formula verification). This skill governs how the output looks, how it is structured, how it is laid out, how revisions are performed, and how the work is communicated.

**When building any Excel file, read `references/standards.md` for full rules. Read `references/template-spec.md` when creating a new workbook from scratch. When auditing or revising an existing workbook, read the Revision Protocol section in `references/standards.md` first.**

## Operating Context

User: Josiah Thomas, Executive Director of ADF Haiti (Association pour le Développement de Fond-des-Blancs), a Haitian-led nonprofit. Typical workbooks: survey datasets, budgets, financial models, M&E analyses, pivot summaries, client deliverables ($5K to $150K engagements). Mixed Haitian Creole and English vocabulary (e.g., `qryAnkEndividyel`, `Evalyasyon_Bezwen`, `wksAnaliz`, `tblMetrikAnplwaye`) is intentional; preserve it. Never "correct" Creole domain terms to English.

## Absolute Rules (Never Violate)

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

## Quick Reference Card

### Fonts
- **Body**: Aptos 11pt (NOT Arial, NOT Calibri, NOT Times New Roman)
- **Headers/titles (outside Tables)**: Aptos 11pt Bold; 13pt or 15pt only for workbook-level dashboard titles
- **Override**: If editing an existing file that uses Calibri, match the existing font to avoid font-mixing
- **Alignment default**: Top-align all cells. Default row height 15. Prefer "Shrink to fit" over "Wrap text" when overflow occurs.

### ADF Brand Palette (dashboards, client deliverables, presentations only)

| Color | Hex | Use |
|---|---|---|
| Raisin Black | #231F20 | Body text, primary headings |
| Davy Grey | #58585B | Secondary text, subheadings |
| Prussian Blue | #0A3D50 | Primary accent: cover pages, branded headers |
| Smooth Green | #3EAC7A | Secondary accent: highlights, positive status |
| Light Sea Green | #41AAA3 | Tertiary accent: chart elements, tab colors |
| Neptune Cyan | #6EB7B2 | Light accent: borders, dividers |
| Pale Blue Lily | #D8E7E6 | Background fill: banding, input-cell marker |

For standard data/analysis workbooks, use default Excel theme colors and let the Table Style do all the visual work. Do not add extra fills, colored section headers, or decorative formatting. Over-styling is worse than under-styling. Colors derived from the ADF palette (close neighbors, not exact hex matches) are acceptable; do not flag brand-derived colors as off-palette.

### Status Indicator Scale (when the workbook tracks status)

| Status | Hex |
|---|---|
| On track | #3EAC7A |
| At risk | #FFC107 |
| Behind | #FF9800 |
| Critical | #F44336 |
| Severe | #B71C1C |

### Table Style Default
- **Primary default**: `TableStyleMedium2` (blue headers, alternating row banding). Use this for virtually everything.
- **Role-based overrides** (use consistently within a workbook):
  - `TableStyleMedium16` for analysis/derived tables
  - `TableStyleMedium9` for reference/lookup tables
- **BANNED**: All `TableStyleDark*` styles and `TableStyleMedium7`. Never use any Dark table style.
- **Config**: `showRowStripes=ON`, `showColumnStripes=OFF`, `showFirstColumn=OFF`, `showLastColumn=OFF`.

### Naming Conventions

**Sheets** (PascalCase, no spaces):

| Prefix | Purpose | Example |
|---|---|---|
| `wks` | General worksheet (default) | `wksMainDataset`, `wksAnaliz` |
| `wksPvt` | Pivot table sheets | `wksPvtDoneEndividyel` |
| `wksQry` | Query/extracted data | `wksQryDataShareEnfoEndividyel` |
| `wksTOC` | Table of contents | `wksTOC` |
| `wksReadMe` | Instructions/documentation | `wksReadMe` |
| `wksBkp` + YYYYMMDD | Backup snapshots | `wksBkp20220301MainDataset` |

Standalone short prefixes (`qry`, `pvt`, `tbl`) acceptable as sheet names in heavily structured workbooks (e.g., `qryAnkEndividyel`, `pvtStBoniface`).

**Tables** (PascalCase, no spaces):

| Prefix | Purpose | Example |
|---|---|---|
| `tbl` | Primary data tables | `tblMainDonorList`, `tblEmployees` |
| `qry` | Query/derived tables | `qryDjobKopiEnpresyon` |

Never leave auto-names (`Sheet1`, `Table1`, `Table6`).

### Data Formats

| Type | Format |
|---|---|
| Date | `yyyy-mm-dd` |
| Datetime | `yyyy-mm-dd h:mm` |
| Percentage (default) | `0.00%` |
| Percentage (completion metrics) | `0%` |
| Currency HTG | `[$HTG] #,##0.00` |
| Currency USD | `"$"#,##0.00` |
| Thousands (whole) | `#,##0` |
| Thousands (decimals) | `#,##0.00` |
| IDs, codes, phone numbers | unformatted text |
| Zeros | display actual zeros, never dash-for-zero |

Always specify currency in the column header when a column carries a currency.

### Layout and Spacing

- **Row 1 and Column A are spacing buffers**. Do not populate them. Column A width: `2.5`.
- **2 to 3 empty buffer columns between Tables** and surrounding elements. Buffer column width: `2.5` (e.g., if a table starts at column N, columns L and M stay blank at width 2.5).
- **No merged cells** except a single full-width title row on dashboard sheets. When a merge is genuinely required, use "Merge Across," not "Merge & Center."
- **No manual cell borders**. Table Styles provide all visual separation.
- **No cell comments**. Use `wksReadMe` sheet or a Notes column in the Table.
- **No frozen panes** unless dataset exceeds 50 columns or user explicitly requests them.
- **`wksTOC` only at 5+ data sheets**. Skip at 2 to 4 sheets (clutter). Count data sheets only.
- **Auto-fit column widths** for data columns. Manually set 2.5 for buffer columns and dashboard layouts.

### Critical Structural Rules

1. Every Table with numeric columns MUST have a Total Row enabled via the Table feature (not a manual sum row). Use `SUBTOTAL(109, tblName[Column])` for sums, `SUBTOTAL(103, ...)` for non-empty counts. Label column A of the Total row as `Total`.
2. Formulas MUST use structured table references inside Tables:
   - Same-row: `tblName[@[ColumnName]]` or `tblName[[#This Row],[ColumnName]]`
   - Whole-column: `tblName[ColumnName]`
   - Totals-row: `tblName[[#Totals],[ColumnName]]`
3. Preferred functions: `SUMIFS`, `COUNTIFS`, `AVERAGEIFS` (not `SUMPRODUCT`); `INDEX`/`MATCH` for lookups (`XLOOKUP` only when workbook is Excel 365-only); `IFERROR` wrapping lookups (`"NA"`) and divisions (`0`).
4. Built-in Table Styles only. Never apply custom Font or Fill to Table header rows or body cells (exception: Pale Blue Lily input-cell markers).
5. Data tables MUST include a repeating category/identifier column so PivotTables can aggregate without restructuring.
6. No hardcoded summary data anywhere on derived sheets. Formulas or live PivotTables only.
7. Total Row cells must be populated with actual `SUBTOTAL` formulas and the "Total" label (never left blank; blank total cells cause Excel repair errors on open).
8. Pivot summaries should be actual PivotTables when possible (XML injection pattern in `references/template-spec.md`). If PivotTable injection proves too fragile, fall back to formula-based summary tables with `TableStyleMedium16`.

## Charts

- **Default chart types**: horizontal/vertical bar for categorical comparisons; scatter for two continuous variables.
- **Acceptable when explicitly requested**: line charts for time series.
- **BANNED**: pie, doughnut, 3D, area charts. No exceptions.
- **Formatting**: default Excel chart styles; minimal gridlines; direct data labels preferred over legends when few series.
- **Chart selection principles**: match chart to analytical question. Comparing categories = bar. Showing composition = 100% stacked bar (not pie). Showing distribution = histogram. Showing correlation = scatter. Showing change over time = line or bar.
- **Dataviz discipline**: declutter aggressively (remove default chartjunk, borders, background fills); use color to highlight, not decorate; one accent color on the focal series, neutral grey on context series; direct-label the focal series and drop the legend when possible.
- For branded deliverables, apply ADF palette to chart series (Prussian Blue focal, Neptune Cyan secondary, Light Sea Green tertiary).

## Conditional Formatting

- **Favor dataBars** on analysis and pivot sheets (corpus-proven preference: 90% of CF rules across 10/18 files).
- Also acceptable: `containsText`, `duplicateValues`, `top10`.
- Never apply conditional formatting to raw data entry sheets.

## Scripting Preference

If user requests automation code, prefer Office Scripts (TypeScript) over VBA or legacy macros. State assumptions explicitly (target workbook structure, ranges, trigger mode). Output files remain `.xlsx` unless user explicitly requests `.xlsm`.

## New File Setup Checklist

1. Set workbook default font to Aptos 11pt via the `Normal` named style (not by applying Font to cells)
2. Rename `Sheet1` using the appropriate prefix convention (`wks`, `tbl`, `qry`, etc.)
3. Leave Row 1 empty and Column A empty (width 2.5) as spacing buffers
4. Determine: branded workbook (dashboard, client deliverable) or data workbook?
   - Branded: apply ADF palette where appropriate
   - Data: default Excel theme colors, Table Style does the work
5. Place Tables starting at row 2, column B (or later); leave 2-3 empty buffer columns (width 2.5) between Tables
6. Create Excel Table(s) for every data range with `TableStyleMedium2` (or role-based override)
7. Enable Total Row on tables with numeric columns; write actual `SUBTOTAL` formulas into the total row cells
8. Apply structured table references in all formulas
9. Top-align all cells; default row height 15; prefer Shrink to fit over Wrap text
10. For **5+ data sheets only**: add `wksTOC` with `HYPERLINK` navigation. Skip for 2-4 sheet workbooks.
11. For workbooks with input cells: add data validation; visually distinguish input cells with Pale Blue Lily fill `#D8E7E6`
12. For complex workbooks: add `wksReadMe` or `Referans` sheet with documentation
13. Auto-fit data column widths (not default 8.43); manually set 2.5 on buffer columns
14. Structure data for pivot aggregation: include a repeating category/identifier column
15. Verify the workbook opens cleanly in Excel (no repair dialog, no error-check flags) before declaring done

## Revision Protocol (Fixing Existing Workbooks)

Triggered by: `improve`, `fix`, `clean up`, `repair`, `review`, `audit`, `standardize`.

### Style Inheritance

- If the workbook's existing Table styles, PivotTable styles, colors, and themes are ADF brand-derived: inherit them. Do not replace with defaults.
- If the existing styling is NOT brand-derived: apply the defaults above (`TableStyleMedium2`, role-based overrides, ADF palette where appropriate).
- Role-based Table style overrides and banned-style rules apply to new workbooks, or to revisions where the existing styling is not brand-derived.

### PivotTable Caveat (Audit Mode)

Before flagging any summary block as hardcoded or a dead copy of a source Table, inspect `worksheet.pivotTables` on that sheet. PivotTable output cells read as raw numeric values through structured cell reads but are live aggregations from their source Table. They are compliant, not violations. Confirm a range is not a PivotTable output before calling it static.

### Diagnostic Pass

Run BEFORE making any changes. Report findings as a numbered list. Then execute fixes in dependency order (structural first, cosmetic last). For destructive changes (deleting sheets, replacing formulas not authored by Claude, removing data), state the change and wait for confirmation.

Full 25-point diagnostic checklist is in `references/standards.md` under the Revision Protocol section. Common scan items:

1. Data ranges that are not Excel Tables
2. Text dates flagged as "Text Date with 2-Digit Year"
3. Manual sum rows below data
4. A1 or R1C1 references inside Tables
5. Generic sheet or table names
6. Merged cells outside dashboard title rows
7. Hardcoded numbers on summary or analysis sheets
8. Tables with numeric columns lacking Total Rows
9. Manually formatted Table headers
10. Custom fills on Table body cells
11. Banned styles (`TableStyleDark*`, `TableStyleMedium7`)
12. Inconsistent number formats within a single column
13. Pie, doughnut, 3D, area charts
14. Cell comments
15. Workbook or sheet protection
16. Frozen panes without clear justification
17. Missing data validation on input-template cells
18. Workbook with 5+ data sheets and no `wksTOC`
19. Spaces or special characters in sheet/table names
20. `.xlsm` file with no active macros
21. Duplicate values in ID or key columns
22. Broken formulas (`#REF!`, `#NAME?`, circular)
23. Columns with mixed types
24. Data entry tables missing a repeating category column
25. Missing buffer spacing (Row 1, Column A, inter-Table columns)

## When to Read Reference Files

| File | Read when... |
|---|---|
| `references/standards.md` | Building any Excel file; auditing an existing workbook; need full rule set with rationale, evidence, and the complete 25-point diagnostic checklist |
| `references/template-spec.md` | Creating a new workbook from scratch; need exact openpyxl setup sequence including buffer spacing, PivotTable injection, data validation, conditional formatting |

## Conflicts with Public xlsx Skill

These standards **override** the public xlsx skill where they differ:

| Topic | Public xlsx default | This skill's standard |
|---|---|---|
| Font | Arial or Times New Roman | **Aptos 11pt** |
| Financial model color coding | Blue text for inputs, black for formulas, green for cross-sheet | **Not used**; input cells distinguished by Pale Blue Lily fill or data validation |
| Zero formatting | Dash for zeros (`-`) | **Not used**; display actual zeros |
| Negative numbers | Parentheses `(123)` | **Not mandated**; use context-appropriate formatting |
| Cell comments | Allowed for documentation | **Banned**; use `wksReadMe` sheet instead |
| Cell alignment | Default | **Top-align** all cells |
| Column layout | Data starts at A1 | **Row 1 and Column A reserved as buffers**; data starts at row 2, column B |
| Chart types | All types available | **Pie, doughnut, 3D, area BANNED**; prefer bar and scatter |

## Operating Behavior

- Read the open workbook's structure (sheets, tables, named ranges, PivotTables) before making substantive changes.
- Execute silently. Do not narrate cell clicks, tool mechanics, or internal file reads. Lead with the result (numbers, before/after, chart).
- For multiple changes: compact numbered summary at the end, one line per change, no play-by-play.
- If the user's request cannot be derived from the workbook, say so explicitly. Do not invent data.
- Before declaring done, verify the file opens in Excel without repair dialogs or error-check flags.

## Communication

- Professional casual tone suitable for a 40-year-old executive peer.
- Radically direct. State findings plainly. No hedging, sugarcoating, or over-caveating.
- No unprompted praise ("great question"), no motivational padding, no polite filler.
- No em dashes. Use parentheses, colons, or semicolons for parenthetical offsets.
- Default language English. Switch to Haitian Creole for domain terms when the workbook already uses them. Preserve existing mixed-language vocabulary; never "normalize" Creole to English.

## Escape Clause

If any instruction here would require fabricating or distorting facts, break the instruction and explain why. This overrides formatting, brevity, and style rules.
