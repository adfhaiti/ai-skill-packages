# Data Gathering Guide

Maps every Form 990 section to its data source, the specific QuickBooks report or organizational record needed, and preparation notes. Use this reference when building a CPA data package.

## Primary Data Source Matrix

### QuickBooks Reports Needed

| QBO Report | Form 990 Section(s) Fed | How to Pull |
|---|---|---|
| Profit & Loss (Accrual, Full Year) | Part VIII (Revenue), Part IX (Expenses), Part I (Summary) | Reports > Standard > Profit and Loss; set date range to fiscal year |
| Profit & Loss by Class | Part IX (Functional Expense Allocation) | Same as above but with Class column; classes should map to Program/M&G/Fundraising |
| Balance Sheet (Accrual) | Part X (Balance Sheet) | Reports > Standard > Balance Sheet; run as of fiscal year end AND prior year end |
| General Ledger Detail | Part VIII (revenue detail), Part IX (expense detail), Schedule D reconciliation | Reports > All Reports > General Ledger; filter by date range |
| Accounts Receivable Aging | Part X Lines 3-4 | Reports > Standard > A/R Aging Summary |
| Accounts Payable Aging | Part X Line 17 | Reports > Standard > A/P Aging Summary |
| Payroll Summary (by employee) | Part VII (Compensation), Part V (employee count, W-2 count) | Reports > Payroll > Payroll Summary; also need W-2s and W-3 |
| 1099 Vendor Report | Part V Line 1b, Part VII Section B | Reports > Vendors & Payables > 1099 Detail (or 1099 Contractor Report) |
| Fixed Asset Listing | Part X Lines 10a-c, Part IX Line 22 | Chart of Accounts > Fixed Asset accounts; need original cost and accumulated depreciation |
| Trial Balance | Reconciliation and verification | Reports > All Reports > Trial Balance |

### Board and Governance Documents Needed

| Document | Form 990 Section(s) Fed | Preparation Notes |
|---|---|---|
| Board meeting minutes (all meetings during fiscal year) | Part VI (governance), Part III (new/ceased programs) | Extract: board size at each meeting, votes taken, compensation approvals, COI disclosures |
| Current board roster with terms | Part VII Section A | Need: legal name, title, average hours/week, start/end dates |
| Conflict of interest policy | Part VI Line 12a | Confirm policy exists; note date of last update |
| Annual COI disclosure forms | Part VI Line 12b | Confirm all board members completed for the year |
| Whistleblower policy | Part VI Line 13 | Confirm policy exists |
| Document retention/destruction policy | Part VI Line 14 | Confirm policy exists |
| Compensation committee minutes or comparability study | Part VI Lines 15a-b, Schedule J | Need: process description, data sources used, board approval documentation |
| Articles of incorporation (current) | Header (formation year, state of domicile, form of organization) | Need certified copy if any amendments during year |
| Bylaws (current) | Part VI governance questions | Need current version |
| IRS determination letter | Header (EIN, exempt status), Schedule A (public charity classification) | Keep on file; rarely changes |

### Operational Records Needed

| Record | Form 990 Section(s) Fed | Preparation Notes |
|---|---|---|
| Grant agreements (received) | Part VIII Line 1 (contributions), Schedule B (contributors) | Need: grantor name, amount, purpose, any restrictions |
| Grant agreements (made) | Part IX Lines 1-3, Schedule I, Schedule F | Need: grantee name, amount, purpose, country |
| Program descriptions and outcome data | Part III (program accomplishments) | Need: narrative descriptions, beneficiary counts, geographic scope, expenses by program |
| Contractor agreements/invoices > $100K | Part VII Section B | Need: contractor name, service description, total paid |
| Fundraising event records | Part VIII Line 8, Schedule G Part II | Need: event name, gross receipts, direct expenses |
| Investment statements | Part VIII Lines 3-7, Part X Lines 11-13, Schedule D | Need: year-end balances, income earned, gains/losses |
| Loan documents | Part X Lines 20-24, Schedule L (if officer/director loans) | Need: lender, balance, terms, interest rate |
| Insurance policies | Part IX Line 23 | Need: type, premium, coverage period |
| Lease agreements | Part IX Line 16, Part VIII Line 6 (if rental income) | Need: property, annual cost, term |
| Depreciation schedule | Part IX Line 22, Part X Line 10 | Need: asset, original cost, method, useful life, current year depreciation, accumulated depreciation |
| Foreign bank account information | Schedule F Part IV | Need: country, account type, maximum balance |
| State charitable registration filings | Part VI Line 20 | List all states where registered |

---

## Data Package Workbook Tab Structure

### Tab 1: Filing Profile

| Field | Value | Source |
|---|---|---|
| Legal Name | | Determination letter |
| DBA | | State filing |
| EIN | | Determination letter |
| Address | | Current records |
| Website | | |
| Phone | | |
| Fiscal Year End | | (MM/DD) |
| Accounting Method | | (Accrual / Cash) |
| Year of Formation | | Articles |
| State of Legal Domicile | | Articles |
| Tax-Exempt Status | 501(c)(3) | Determination letter |
| Public Charity Classification | | Determination letter (line number on Schedule A) |
| Gross Receipts (current year) | | QBO P&L + investment gains |
| Total Assets (EOY) | | QBO Balance Sheet |
| Form Required | 990 / 990-EZ | Based on thresholds |
| Filing Deadline | | 5th month + 15th day after FYE |
| Extension Filed? | | Form 8868 |
| Prior Year 990 Available? | | (attach if yes) |
| Financial Statements Audited? | | If yes, attach audit report |
| Single Audit Required? | | (>= $750K federal expenditures) |

### Tab 2: Officer/Director/Key Employee Roster

| Name | Title | Avg Hours/Week | Reportable Comp (W-2 Box 1) | Other Comp from Org | Estimated Benefits | Comp from Related Orgs | Independent? | Voting Member? |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Include ALL current officers, directors, trustees, key employees regardless of compensation level.

### Tab 3: Revenue Detail

Map to Part VIII lines:

| Revenue Category | Part VIII Line | Amount | Column (A/B/C/D) | Source Document |
|---|---|---|---|---|
| Individual donations | 1a or 1f | | A only | Donor records |
| Foundation grants | 1f | | A only | Grant agreements |
| Government grants | 1e | | A only | Grant agreements |
| Corporate donations | 1f | | A only | Donor records |
| Noncash contributions | 1g | | A only | Donation records |
| Program service: [line 1] | 2a | | B or C | QBO by class |
| Program service: [line 2] | 2b | | B or C | QBO by class |
| Interest income | 3 | | A and D | Bank statements |
| Dividends | 3 | | A and D | Investment statements |
| Rental income (gross) | 6a | | | Lease agreements |
| Rental expenses | 6b | | | |
| Fundraising events (gross) | 8a | | | Event records |
| Fundraising direct expenses | 8b | | | |
| Other revenue: [describe] | 11a-e | | | |

### Tab 4: Expense Detail by Function

Map to Part IX lines. For each natural expense category, provide total and functional allocation:

| Expense Category | Part IX Line | Total Col(A) | Program Col(B) | M&G Col(C) | Fundraising Col(D) | Allocation Basis |
|---|---|---|---|---|---|---|
| Grants to domestic orgs | 1 | | | | | Direct |
| Grants to foreign orgs | 3 | | | | | Direct |
| Officer/director comp | 5 | | | | | Time allocation |
| Other salaries | 6-7 | | | | | Time/function |
| Pension contributions | 8 | | | | | Follow salary allocation |
| Other benefits | 9 | | | | | Follow salary allocation |
| Payroll taxes | 10 | | | | | Follow salary allocation |
| Accounting fees | 11a | | | | | Usually M&G |
| Legal fees | 11b | | | | | By purpose |
| Professional fundraising | 11e | | | | | All fundraising |
| Other professional fees | 11g | | | | | By purpose |
| Advertising | 12 | | | | | By purpose |
| Office expenses | 13 | | | | | Headcount or direct |
| IT | 14 | | | | | Headcount or direct |
| Occupancy | 16 | | | | | Square footage |
| Travel | 17 | | | | | By trip purpose |
| Conferences | 19 | | | | | By purpose |
| Interest | 20 | | | | | By asset use |
| Depreciation | 22 | | | | | By asset use |
| Insurance | 23 | | | | | By type/coverage |
| Other: [describe] | 24a-e | | | | | Varies |

### Tab 5: Balance Sheet

Map to Part X:

| Account | Part X Line | BOY Amount | EOY Amount | Source |
|---|---|---|---|---|
| Cash (checking) | 1 | | | QBO |
| Cash (savings) | 2 | | | QBO |
| Grants receivable | 3 | | | QBO AR |
| Accounts receivable | 4 | | | QBO AR |
| Prepaid expenses | 9 | | | QBO |
| Land | 10a | | | Fixed asset schedule |
| Buildings (net) | 10a | | | Fixed asset schedule |
| Equipment (net) | 10a | | | Fixed asset schedule |
| Investments | 11-13 | | | Investment statements |
| Other assets | 15 | | | QBO (describe each) |
| **Total Assets** | **16** | | | **Sum** |
| Accounts payable | 17 | | | QBO AP |
| Grants payable | 18 | | | Grant agreements |
| Deferred revenue | 19 | | | QBO |
| Loans payable | 23-24 | | | Loan docs |
| Other liabilities | 25 | | | QBO (describe each) |
| **Total Liabilities** | **26** | | | **Sum** |
| Net assets without restrictions | 27 | | | QBO |
| Net assets with restrictions | 28 | | | QBO |
| **Total Net Assets** | **32** | | | **Sum** |
| **Total L + NA** | **33** | | | **Must = Total Assets** |

### Tab 6: Program Accomplishments

For each program (at least the top 3 by expense):

| Field | Program 1 | Program 2 | Program 3 |
|---|---|---|---|
| Program name | | | |
| NTEE code | | | |
| Total expenses | | | |
| Grants included in expenses | | | |
| Revenue attributable to program | | | |
| Narrative description (150-250 words) | | | |
| Number of beneficiaries | | | |
| Geographic scope | | | |
| Key outcomes/metrics | | | |

### Tab 7: Schedule Trigger Worksheet

Answer all 38 Part IV questions with source documentation:

| Q# | Question Summary | Answer (Y/N) | Schedule Triggered | Notes/Documentation |
|---|---|---|---|---|
| 1 | 501(c)(3) or 4947(a)(1)? | | A | |
| 2 | Schedule B required? | | B | |
| 3 | Political campaign activities? | | C | |
| ... | ... | ... | ... | ... |

### Tab 8: Outstanding Items Tracker

| Item | Form Section | Responsible Person | Due Date | Status | Notes |
|---|---|---|---|---|---|
| | | | | Not Started / In Progress / Complete | |

---

## Data Quality Checks Before Delivery

Run these verification checks before handing off the data package:

1. QBO Trial Balance total debits = total credits
2. P&L total revenue matches Tab 3 total
3. P&L total expenses matches Tab 4 total Col(A)
4. Balance Sheet ties: Assets = Liabilities + Net Assets (both BOY and EOY)
5. BOY balance sheet matches prior year 990 Part X Col(B) (or prior year EOY if no prior 990 available)
6. Tab 4 functional allocation: Col(A) = Col(B) + Col(C) + Col(D) for every line
7. Tab 2 compensation totals reconcile with Tab 4 Lines 5-10
8. All Tab 7 "Yes" answers have corresponding documentation attached
9. Tab 8 has no "Not Started" items with past-due dates
