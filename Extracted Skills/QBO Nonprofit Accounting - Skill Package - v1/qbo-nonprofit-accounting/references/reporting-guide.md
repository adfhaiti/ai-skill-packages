# Reporting Guide: Nonprofit Financial Statements in QBO

Procedures for ASC 958 statements, grant reports, CPA exports, and year-end close. Grounded in London (2019), Ivens (2005), Mainini (2009).

## 1. ASC 958 Overview

| Statement | QBO Report | Post-Processing |
|---|---|---|
| Statement of Financial Position | Balance Sheet | Group by net asset class; rename headers |
| Statement of Activities | P&L by Class | Add net asset columns; reclassify Retained Earnings |
| Statement of Functional Expenses | P&L by Class (expenses) | Matrix: natural expense rows x functional columns |
| Statement of Cash Flows | Statement of Cash Flows | Verify operating/investing/financing categories |

QBO cannot natively produce GAAP-compliant nonprofit statements. All require Excel post-processing.

Path: **Reports** (left menu). Common controls: date range, accounting method (use Accrual for GAAP), rows/columns grouping, export to Excel/PDF.

## 2. Statement of Financial Position

Path: **Reports > Balance Sheet**

1. Set date to fiscal year-end, Accrual basis
2. Export to Excel
3. Replace Equity section with: Net Assets Without Donor Restrictions (3100), Net Assets With Donor Restrictions (3200)
4. Remove Opening Balance Equity and Retained Earnings lines (should be zero after year-end JE)
5. Rename "Equity" to "Net Assets"
6. Add comparative prior-year column

Verify: Total Assets = Total Liabilities + Total Net Assets.

## 3. Statement of Activities

Path: **Reports > Profit and Loss by Class**

1. Set fiscal year, Accrual basis
2. Export to Excel
3. Restructure columns: Without Donor Restrictions, With Donor Restrictions, Total
4. Add "Net Assets Released from Restrictions" line
5. Add opening/closing net asset balances

## 4. Statement of Functional Expenses

Path: **Reports > Profit and Loss by Class** (expenses section)

1. Export to Excel, delete Revenue section
2. Verify columns: Program Services, M&G, Fundraising, Total
3. Map each expense row to Form 990 Part IX line (see ucoa-chart-of-accounts.md)
4. Verify: column sums = Total; total expenses match P&L

Allocation verification (Mainini 2009): ED salary splits all three functions; occupancy by square footage; program staff 100% Program; fundraising staff 100% Fundraising.

## 5. Statement of Cash Flows

Path: **Reports > Statement of Cash Flows**

Indirect method. Verify: operating (net income + non-cash adjustments + working capital changes), investing (fixed assets), financing (loans, restricted long-term contributions). Net change + beginning cash = ending cash = Balance Sheet cash.

## 6. Grant Compliance Reports

### Budget vs. Actual
Path: **Reports > Budget vs. Actuals** (requires budget setup on Plus/Advanced). Or export P&L filtered by Customer + Project, compare to grant budget in Excel.

### Grant Expenditure Detail
Path: **Reports > P&L > Customize > Filter by Customer + Project**

### Burn Rate
Run monthly P&L by Customer/Project. Calculate: (total spent / budget) vs. (months elapsed / grant period).

## 7. Custom Report Configurations

Save frequently used reports: **run report > customize > Save Customization**

Recommended saved reports: Monthly P&L by Function, YTD P&L by Function, YTD P&L by Grant, Balance Sheet, A/R Aging, A/P Aging, Trial Balance, General Ledger, Donor Summary.

## 8. CPA Data Package

Export checklist (all Accrual basis, fiscal year):
1. Trial Balance (year-end)
2. Balance Sheet (year-end + prior year-end)
3. P&L by Class (full year)
4. P&L by Customer (grant detail)
5. General Ledger (full year)
6. A/R and A/P Aging Detail (year-end)
7. Bank Reconciliation Reports (all accounts, all months)
8. 1099 Detail Report
9. Payroll Summary

Supplementary (not in QBO): board minutes, conflict of interest disclosures, grant agreements, lease/insurance, bank statements, payroll tax filings.

Hand off to `form-990-nonprofit` skill for 990 preparation.

## 9. Year-End Close

### Pre-Close
- [ ] All transactions entered for final month
- [ ] All bank/credit card accounts reconciled through year-end
- [ ] Adjusting JEs posted (accruals, prepaid amortization, depreciation)
- [ ] Foreign currency revalued at year-end BRH rate
- [ ] Undeposited Funds = zero
- [ ] A/R and A/P aging reviewed
- [ ] Payroll finalized

### Net Asset Reclassification
QBO accumulates net income in Retained Earnings. Post year-end JE:
- Debit: Retained Earnings (current-year net income)
- Credit: 3100 Without Donor Restrictions (unrestricted portion)
- Credit: 3200 With Donor Restrictions (restricted portion)
- Do NOT assign Classes (balance sheet reclassification)
- Memo: "FY20XX year-end net asset reclassification"

### Set Closing Date
Path: **Settings > Account and Settings > Advanced > Accounting > Close the books**
Set date to last day of fiscal year. Set password (share only with ED and CPA).

### Post-Close
- [ ] Balance Sheet shows correct net asset balances
- [ ] P&L matches board-approved financials
- [ ] Trial Balance debits = credits
- [ ] Closing date set and password-protected

## 10. Form 990 Handoff

| 990 Section | QBO Source |
|---|---|
| Part I (Summary) | P&L total revenue/expenses, net assets |
| Part VIII (Revenue) | P&L revenue detail |
| Part IX (Expenses) | P&L by Class (functional matrix) |
| Part X (Balance Sheet) | Balance Sheet BOY and EOY |
| Schedule A (Public Support) | Contribution detail by donor (5+ years) |
| Schedule F (Foreign Activities) | Haiti-tagged transactions |

Invoke `form-990-nonprofit` skill with exported data package.

## Sources

- London (2019) "QuickBooks for Nonprofits & Churches"
- Ivens (2005) "Running QuickBooks in Nonprofits"
- Mainini (2009) "Non-Profit Accounting: Functional Expense Allocation"
- FASB ASC 958
