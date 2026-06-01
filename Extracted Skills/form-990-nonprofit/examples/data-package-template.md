# Data Package Template

Template structure for the CPA data package workbook. Use this as the blueprint when generating the XLSX output in the Prepare branch.

## Workbook Specifications

- File format: XLSX with proper Excel Tables (TableStyleInfo)
- Font: Aptos 11pt throughout
- Each tab: one Excel Table with header row and total row where applicable
- Named ranges for key figures that cross-reference between tabs
- Conditional formatting: highlight incomplete cells in yellow

## Tab List and Column Definitions

### Tab 1: Filing_Profile

Single-column layout (Field / Value / Source / Notes). No Table needed; use simple key-value pairs.

Fields: Legal Name, DBA, EIN, Address (Street, City, State, ZIP), Website, Phone, Fiscal Year End, Accounting Method, Year of Formation, State of Legal Domicile, Tax-Exempt Status, Public Charity Classification (Schedule A line), Gross Receipts, Total Assets EOY, Form Required, Filing Deadline, Extension Filed, Prior Year 990 Available, Audit Performed, Single Audit Required.

### Tab 2: Officers_Directors

Table columns:
- Name (text)
- Title (text)
- Average_Hours_Per_Week (number, 1 decimal)
- Hours_Related_Orgs (number, 1 decimal)
- Individual_Trustee (Y/N)
- Institutional_Trustee (Y/N)
- Officer (Y/N)
- Key_Employee (Y/N)
- Highest_Compensated (Y/N)
- Former (Y/N)
- Reportable_Comp_Org (currency)
- Reportable_Comp_Related (currency)
- Estimated_Other_Comp (currency)
- Independent (Y/N)
- Voting_Member (Y/N)

Total row: sum Reportable_Comp_Org, Reportable_Comp_Related, Estimated_Other_Comp.

### Tab 3: Revenue

Table columns:
- Part_VIII_Line (text: "1a", "1b", etc.)
- Revenue_Category (text)
- Amount_Total_ColA (currency)
- Amount_Related_ColB (currency)
- Amount_Unrelated_ColC (currency)
- Amount_Excluded_ColD (currency)
- Source_Document (text)
- Notes (text)

Total row: sum all currency columns.
Validation: Amount_Total_ColA must equal sum of ColB + ColC + ColD (except for contributions which are Col A only).

### Tab 4: Expenses_Functional

Table columns:
- Part_IX_Line (text: "1", "2", "3", etc.)
- Expense_Category (text)
- Total_ColA (currency)
- Program_ColB (currency)
- MandG_ColC (currency)
- Fundraising_ColD (currency)
- Allocation_Basis (text: "Direct", "Time", "Sq Footage", "Headcount", etc.)
- Notes (text)

Total row: sum all currency columns.
Validation: Total_ColA must equal Program_ColB + MandG_ColC + Fundraising_ColD for every row.

### Tab 5: Balance_Sheet

Table columns:
- Part_X_Line (text)
- Account_Description (text)
- BOY_Amount (currency)
- EOY_Amount (currency)
- Source (text)
- Notes (text)

Include subtotal rows for: Total Assets (Line 16), Total Liabilities (Line 26), Total Net Assets (Line 32), Total L+NA (Line 33).
Validation: Line 33 must equal Line 16 for both BOY and EOY.

### Tab 6: Programs

Table columns:
- Program_Name (text)
- Program_Number (integer: 1, 2, 3, etc.)
- NTEE_Code (text)
- Total_Expenses (currency)
- Grants_Included (currency)
- Revenue_Attributable (currency)
- Beneficiaries_Served (integer)
- Geographic_Scope (text)
- Key_Outcomes (text)
- Narrative_Description (long text)

Sort by Total_Expenses descending (largest program first).

### Tab 7: Schedule_Triggers

Table columns:
- Question_Number (integer: 1-38)
- Question_Summary (text)
- Answer (text: "Yes" / "No" / "N/A")
- Schedule_Triggered (text: "A", "B", "C", etc.)
- Documentation_Reference (text)
- Notes (text)

Pre-populate all 38 questions from Part IV.

### Tab 8: Outstanding_Items

Table columns:
- Item_Description (text)
- Form_Section (text)
- Responsible_Person (text)
- Due_Date (date)
- Status (text: "Not Started" / "In Progress" / "Complete")
- Notes (text)

Conditional formatting: "Not Started" with past Due_Date highlighted red.

### Tab 9: Contractor_1099

Table columns (for Part VII Section B):
- Contractor_Name (text)
- Business_Address (text)
- Service_Description (text)
- Total_Compensation (currency)

Include only contractors paid > $100K. Sort by Total_Compensation descending. List top 5.

### Tab 10: Contributors (for Schedule B preparation)

Table columns:
- Contributor_Name (text)
- Contributor_Type (text: "Individual" / "Organization" / "Government")
- Total_Contributions (currency)
- Cash_Amount (currency)
- Noncash_Amount (currency)
- Noncash_Description (text)

Include only contributors exceeding the greater of $5,000 or 2% of Part VIII Line 1h.
Mark this tab CONFIDENTIAL (Schedule B is not publicly disclosed).

---

## Delivery Checklist

Before delivering the data package workbook, verify:

- [ ] All tabs present and populated
- [ ] All Excel Tables formatted with TableStyleInfo
- [ ] Revenue total (Tab 3) ties to QBO P&L total revenue
- [ ] Expense total (Tab 4) ties to QBO P&L total expenses
- [ ] Balance sheet (Tab 5) ties: Assets = Liabilities + Net Assets (both BOY and EOY)
- [ ] BOY figures match prior year EOY
- [ ] Functional allocation validates: Col(A) = Col(B) + Col(C) + Col(D) on every row
- [ ] Officer compensation (Tab 2) reconciles with Tab 4 Lines 5-10
- [ ] All Schedule Triggers (Tab 7) answered
- [ ] Outstanding items (Tab 8) identified with responsible parties
- [ ] Tab 10 (Contributors) marked confidential
