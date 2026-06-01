# UCOA v3.0 Chart of Accounts for Nonprofit QBO

Standard Unified Chart of Accounts (UCOA v3.0) adapted for a small Haitian-American 501(c)(3) operating in dual-currency (USD home, HTG foreign). Every expense account includes its Form 990 Part IX functional expense line mapping. Grounded in London (2019), Ivens (2005), Mainini (2009), and IRS Form 990 Instructions.

## Account Numbering Convention

| Range | Category |
|---|---|
| 1000-1999 | Assets |
| 2000-2999 | Liabilities |
| 3000-3999 | Net Assets (Equity) |
| 4000-4999 | Revenue |
| 5000-5999 | Cost of Services Sold (COSS) |
| 6000-6999 | Operating Expenses |
| 7000-7999 | Fundraising Expenses |
| 8000-8999 | Other Income / Expense |

## QBO Type and Detail Type Reference

When creating accounts in QBO, each account requires both a Type and a Detail Type. The Detail Type determines reporting behavior.

---

## 1000-1999: Assets

### 1000 Cash and Cash Equivalents

| Acct # | Account Name | QBO Type | QBO Detail Type | Currency | Notes |
|---|---|---|---|---|---|
| 1010 | Operating Checking (USD) | Bank | Checking | USD | Primary US operating account |
| 1020 | Operating Checking (HTG) | Bank | Checking | HTG | Primary Haiti operating account (BUH/Sogebank) |
| 1030 | Savings (USD) | Bank | Savings | USD | Reserve / restricted cash |
| 1040 | Petty Cash (USD) | Bank | Cash on Hand | USD | US petty cash |
| 1050 | Petty Cash (HTG) | Bank | Cash on Hand | HTG | Haiti petty cash |
| 1060 | MonCash Mobile Money (HTG) | Bank | Cash on Hand | HTG | Digicel MonCash account |
| 1070 | PayPal | Bank | Checking | USD | If applicable |
| 1080 | Undeposited Funds | Other Current Assets | Undeposited Funds | USD | QBO system account; clear regularly |

### 1100 Accounts Receivable

| Acct # | Account Name | QBO Type | QBO Detail Type | Currency | Notes |
|---|---|---|---|---|---|
| 1100 | Accounts Receivable (USD) | Accounts Receivable | Accounts Receivable | USD | Auto-created by QBO |
| 1110 | Accounts Receivable (HTG) | Accounts Receivable | Accounts Receivable | HTG | Created when multicurrency enabled |
| 1150 | Grants Receivable | Other Current Assets | Other Current Assets | USD | Pledged but not yet received grant funds |
| 1160 | Pledges Receivable | Other Current Assets | Other Current Assets | USD | Individual donor pledges |

### 1200 Prepaid and Other Current Assets

| Acct # | Account Name | QBO Type | QBO Detail Type | Notes |
|---|---|---|---|---|
| 1200 | Prepaid Expenses | Other Current Assets | Prepaid Expenses | Insurance, rent, subscriptions paid in advance |
| 1210 | Employee Advances | Other Current Assets | Employee Cash Advances | Field per diem advances; reconcile monthly |
| 1220 | Security Deposits | Other Current Assets | Other Current Assets | Office rent deposit, utility deposits |
| 1230 | Inventory - Exam Vouchers | Other Current Assets | Inventory | EkiTek Academy certification exam vouchers |

### 1300 Fixed Assets

| Acct # | Account Name | QBO Type | QBO Detail Type | Notes |
|---|---|---|---|---|
| 1300 | Vehicles | Fixed Assets | Vehicles | Organizational vehicles |
| 1310 | Accumulated Depreciation - Vehicles | Fixed Assets | Accumulated Depreciation | Contra asset |
| 1320 | Computer Equipment | Fixed Assets | Machinery & Equipment | Laptops, servers, tablets |
| 1330 | Accumulated Depreciation - Computer Equipment | Fixed Assets | Accumulated Depreciation | Contra asset |
| 1340 | Drone Equipment | Fixed Assets | Machinery & Equipment | DJI drones, sensors, accessories |
| 1350 | Accumulated Depreciation - Drone Equipment | Fixed Assets | Accumulated Depreciation | Contra asset |
| 1360 | GPS/Survey Equipment | Fixed Assets | Machinery & Equipment | GNSS receivers, total stations |
| 1370 | Accumulated Depreciation - GPS/Survey Equipment | Fixed Assets | Accumulated Depreciation | Contra asset |
| 1380 | Office Furniture and Fixtures | Fixed Assets | Furniture & Fixtures | Desks, chairs, shelving |
| 1390 | Accumulated Depreciation - Furniture | Fixed Assets | Accumulated Depreciation | Contra asset |
| 1395 | Leasehold Improvements | Fixed Assets | Leasehold Improvements | Office build-out costs |
| 1396 | Accumulated Amortization - Leasehold | Fixed Assets | Accumulated Depreciation | Contra asset |

---

## 2000-2999: Liabilities

### 2000 Current Liabilities

| Acct # | Account Name | QBO Type | QBO Detail Type | Notes |
|---|---|---|---|---|
| 2000 | Accounts Payable (USD) | Accounts Payable | Accounts Payable | QBO auto-created |
| 2010 | Accounts Payable (HTG) | Accounts Payable | Accounts Payable | Created with multicurrency |
| 2050 | Accrued Expenses | Other Current Liabilities | Other Current Liabilities | Month-end accruals |
| 2100 | Deferred Revenue | Other Current Liabilities | Other Current Liabilities | Contract advances received but not yet earned |
| 2110 | Refundable Advances | Other Current Liabilities | Other Current Liabilities | Grant advances subject to return if unspent |

### 2200 Payroll Liabilities

| Acct # | Account Name | QBO Type | QBO Detail Type | Notes |
|---|---|---|---|---|
| 2200 | Federal Income Tax Withheld | Other Current Liabilities | Federal Income Tax Payable | US employees |
| 2210 | State Income Tax Withheld | Other Current Liabilities | State/Local Income Tax Payable | US employees |
| 2220 | Social Security/Medicare Withheld | Other Current Liabilities | Other Current Liabilities | US employees |
| 2230 | Social Security/Medicare (Employer) | Other Current Liabilities | Other Current Liabilities | US employer match |
| 2300 | ONA Contributions Payable | Other Current Liabilities | Other Current Liabilities | Haiti: Office National d'Assurance (pension) |
| 2310 | OFATMA Contributions Payable | Other Current Liabilities | Other Current Liabilities | Haiti: workplace injury insurance |
| 2320 | IRI Withholding Payable | Other Current Liabilities | Other Current Liabilities | Haiti: Impot sur le Revenu (income tax) |
| 2330 | CAS Contributions Payable | Other Current Liabilities | Other Current Liabilities | Haiti: Contribution au Fonds d'Assurance Sociale |

### 2400 Other Liabilities

| Acct # | Account Name | QBO Type | QBO Detail Type | Notes |
|---|---|---|---|---|
| 2400 | Credit Card Payable | Credit Card | | If organizational credit card is used |
| 2500 | Notes Payable - Current | Other Current Liabilities | Current Portion of Long-Term Debt | Loans due within 12 months |
| 2600 | Notes Payable - Long Term | Long Term Liabilities | Notes Payable | Loans due beyond 12 months |

---

## 3000-3999: Net Assets (Equity)

| Acct # | Account Name | QBO Type | QBO Detail Type | Notes |
|---|---|---|---|---|
| 3000 | Opening Balance Equity | Equity | Opening Balance Equity | QBO auto-created; target balance: $0 after setup |
| 3050 | Retained Earnings | Equity | Retained Earnings | QBO auto-created; reclassify to 3100/3200 at year-end |
| 3100 | Net Assets Without Donor Restrictions | Equity | Opening Balance Equity | Unrestricted net assets (ASC 958) |
| 3200 | Net Assets With Donor Restrictions | Equity | Opening Balance Equity | Time- or purpose-restricted (ASC 958) |

### Year-End Procedure

QBO accumulates current-year net income in Retained Earnings. At year-end, post a journal entry:
- Debit: 3050 Retained Earnings
- Credit: 3100 Without Donor Restrictions (unrestricted portion)
- Credit: 3200 With Donor Restrictions (restricted portion, if applicable)

Do NOT assign Classes to this entry (balance sheet reclassification, not a functional expense).

---

## 4000-4999: Revenue

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part VIII Line | Notes |
|---|---|---|---|---|---|
| 4100 | Contributions - Unrestricted | Income | Non-Profit Income | Line 1h | Donations without donor restrictions |
| 4110 | Contributions - Restricted | Income | Non-Profit Income | Line 1h | Donations with donor restrictions |
| 4120 | In-Kind Contributions | Income | Non-Profit Income | Line 1h | Non-cash gifts (services, goods) |
| 4130 | Contributed Services | Income | Non-Profit Income | Line 1h | Donated professional services meeting ASC 958 criteria |
| 4200 | Contract Revenue | Income | Service/Fee Income | Line 2 | Earned revenue from data collection, GIS, evaluation contracts |
| 4210 | Grant Revenue - Government | Income | Non-Profit Income | Line 1e | Government grants (federal, state, local) |
| 4220 | Grant Revenue - Private | Income | Non-Profit Income | Line 1f | Foundation and corporate grants |
| 4300 | Training Revenue | Income | Service/Fee Income | Line 2 | EkiTek Academy training fees, workshop fees |
| 4400 | Special Event Revenue - Gross | Income | Non-Profit Income | Line 8a | Fundraising events (gross receipts) |
| 4410 | Less: Direct Benefit to Donors | Income | Non-Profit Income | Line 8b | Event costs directly benefiting attendees (contra) |
| 4500 | Membership Dues | Income | Non-Profit Income | Line 3 | If applicable |
| 4900 | Net Assets Released from Restriction | Income | Non-Profit Income | N/A | Release when restriction is met; offset in restricted column |

---

## 5000-5999: Cost of Services Sold (COSS)

Direct costs attributable to contract/grant service delivery. All COSS accounts are 100% Program Services.

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Class |
|---|---|---|---|---|---|
| 5100 | Enumerator Wages | Cost of Goods Sold | Other Costs of Services - COS | Line 7 | Program Services |
| 5110 | Field Supervisor Wages | Cost of Goods Sold | Other Costs of Services - COS | Line 7 | Program Services |
| 5120 | Field Per Diem | Cost of Goods Sold | Other Costs of Services - COS | Line 16 | Program Services |
| 5130 | Field Transportation | Cost of Goods Sold | Other Costs of Services - COS | Line 16 | Program Services |
| 5140 | Data Collection Supplies | Cost of Goods Sold | Other Costs of Services - COS | Line 12 | Program Services |
| 5150 | Subcontractor Costs | Cost of Goods Sold | Other Costs of Services - COS | Line 11g | Program Services |
| 5160 | Drone Flight Costs | Cost of Goods Sold | Other Costs of Services - COS | Line 24e | Program Services |
| 5170 | GIS Software Licenses (Project) | Cost of Goods Sold | Other Costs of Services - COS | Line 24e | Program Services |
| 5180 | Training Materials and Supplies | Cost of Goods Sold | Other Costs of Services - COS | Line 12 | Program Services |
| 5190 | Exam Voucher Costs | Cost of Goods Sold | Other Costs of Services - COS | Line 12 | Program Services |

---

## 6000-6999: Operating Expenses

### 6000 Personnel

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6000 | Salaries - Officers/Directors | Expense | Salaries & Wages | Line 5 | Split per time study |
| 6010 | Salaries - Other Employees | Expense | Salaries & Wages | Line 7 | Split per time study |
| 6020 | Employee Benefits | Expense | Employee Benefits | Line 9 | Follow salary allocation |
| 6030 | Payroll Taxes - US | Expense | Payroll Expenses | Line 10 | Follow salary allocation |
| 6040 | ONA Employer Contributions | Expense | Payroll Expenses | Line 10 | Follow salary allocation |
| 6050 | OFATMA Employer Contributions | Expense | Payroll Expenses | Line 10 | Follow salary allocation |
| 6060 | CAS Employer Contributions | Expense | Payroll Expenses | Line 10 | Follow salary allocation |
| 6070 | Contract Labor / Consultants | Expense | Other Business Expenses | Line 11g | Direct assignment or time study |

### 6100 Professional Services

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6100 | Accounting Fees | Expense | Legal & Professional Fees | Line 11c | 100% M&G |
| 6110 | Legal Fees | Expense | Legal & Professional Fees | Line 11b | Direct assignment |
| 6120 | Other Professional Fees | Expense | Legal & Professional Fees | Line 11g | Direct assignment |
| 6130 | Audit Fees | Expense | Legal & Professional Fees | Line 11c | 100% M&G |

### 6200 Occupancy

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6200 | Rent | Expense | Rent or Lease of Buildings | Line 15 | Square footage allocation |
| 6210 | Utilities - Electric | Expense | Utilities | Line 15 | Square footage allocation |
| 6220 | Utilities - Water | Expense | Utilities | Line 15 | Square footage allocation |
| 6230 | Repairs and Maintenance | Expense | Repair & Maintenance | Line 15 | Square footage allocation |
| 6240 | Security | Expense | Other Business Expenses | Line 24e | Square footage allocation |

### 6300 Office and Administrative

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6300 | Office Supplies | Expense | Office/General Administrative Expenses | Line 12 | Headcount allocation |
| 6310 | Postage and Shipping | Expense | Office/General Administrative Expenses | Line 12 | Direct assignment |
| 6320 | Printing and Copying | Expense | Office/General Administrative Expenses | Line 12 | Direct assignment |
| 6330 | Bank Fees and Charges | Expense | Bank Charges | Line 24e | 100% M&G |
| 6340 | Licenses and Permits | Expense | Taxes Paid | Line 24e | 100% M&G |

### 6400 Technology

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6400 | Software Subscriptions | Expense | Other Business Expenses | Line 24e | Direct assignment or time study |
| 6410 | Internet / Telecommunications | Expense | Utilities | Line 24e | Time study allocation |
| 6420 | Computer Supplies and Maintenance | Expense | Repair & Maintenance | Line 24e | Headcount allocation |
| 6430 | Cloud Storage / Hosting | Expense | Other Business Expenses | Line 24e | Direct assignment |
| 6440 | Fulcrum Subscription | Expense | Other Business Expenses | Line 24e | 100% Program Services |
| 6450 | GIS Software (Org-wide) | Expense | Other Business Expenses | Line 24e | Direct assignment |

### 6500 Travel

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6500 | Domestic Travel | Expense | Travel | Line 16 | Direct assignment |
| 6510 | International Travel | Expense | Travel | Line 16 | Direct assignment |
| 6520 | Vehicle Fuel | Expense | Auto | Line 16 | Trip log allocation |
| 6530 | Vehicle Maintenance | Expense | Auto | Line 16 | Trip log allocation |
| 6540 | Meals - Travel | Expense | Travel Meals | Line 16 | Direct assignment |
| 6550 | Lodging | Expense | Travel | Line 16 | Direct assignment |

### 6600 Depreciation and Amortization

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6600 | Depreciation - Vehicles | Expense | Depreciation | Line 21 | Trip log allocation |
| 6610 | Depreciation - Computer Equipment | Expense | Depreciation | Line 21 | Headcount allocation |
| 6620 | Depreciation - Drone Equipment | Expense | Depreciation | Line 21 | 100% Program Services |
| 6630 | Depreciation - GPS/Survey Equipment | Expense | Depreciation | Line 21 | 100% Program Services |
| 6640 | Depreciation - Furniture | Expense | Depreciation | Line 21 | Square footage allocation |
| 6650 | Amortization - Leasehold Improvements | Expense | Depreciation | Line 21 | Square footage allocation |

### 6700 Insurance

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6700 | General Liability Insurance | Expense | Insurance | Line 22 | Square footage or headcount |
| 6710 | Directors and Officers Insurance | Expense | Insurance | Line 22 | 100% M&G |
| 6720 | Vehicle Insurance | Expense | Insurance | Line 22 | Trip log allocation |
| 6730 | Workers Compensation | Expense | Insurance | Line 22 | Follow salary allocation |
| 6740 | Property Insurance | Expense | Insurance | Line 22 | Square footage allocation |

### 6800 Programs and Community Development

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6800 | Scholarships and Awards | Expense | Other Business Expenses | Line 1 | 100% Program Services |
| 6810 | Community Grants Made | Expense | Other Business Expenses | Line 1 | 100% Program Services |
| 6820 | Program Supplies | Expense | Other Business Expenses | Line 12 | 100% Program Services |
| 6830 | Participant Support Costs | Expense | Other Business Expenses | Line 24e | 100% Program Services |

### 6900 Miscellaneous

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Allocation Notes |
|---|---|---|---|---|---|
| 6900 | Dues and Memberships | Expense | Other Business Expenses | Line 24e | Direct assignment |
| 6910 | Staff Training and Development | Expense | Other Business Expenses | Line 24e | Follow salary allocation |
| 6920 | Conferences and Meetings | Expense | Other Business Expenses | Line 17 | Direct assignment |
| 6930 | Bad Debt Expense | Expense | Other Business Expenses | Line 24e | 100% M&G |
| 6990 | Miscellaneous Expense | Expense | Other Business Expenses | Line 24e | Review and reclassify monthly |

---

## 7000-7999: Fundraising Expenses

These accounts are 100% Fundraising class. Separated from operating expenses for clear 990 Part IX Column D reporting.

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part IX Line | Notes |
|---|---|---|---|---|---|
| 7000 | Fundraising Salaries | Expense | Salaries & Wages | Line 7 | Dedicated fundraising staff |
| 7100 | Donor Acknowledgments | Expense | Other Business Expenses | Line 24e | Thank-you letters, receipts |
| 7200 | Fundraising Printing and Design | Expense | Advertising | Line 24e | Appeals, annual report print |
| 7300 | Fundraising Platform Fees | Expense | Other Business Expenses | Line 24e | Givebutter, Donorbox processing fees |
| 7400 | Special Event Costs | Expense | Other Business Expenses | Line 24e | Event expenses (net of direct donor benefit) |
| 7500 | Fundraising Travel | Expense | Travel | Line 16 | Donor visits, fundraising trips |
| 7600 | Digital Marketing - Fundraising | Expense | Advertising | Line 24e | Social media ads, email platforms |
| 7900 | Other Fundraising Costs | Expense | Other Business Expenses | Line 24e | Catch-all; review and reclassify |

---

## 8000-8999: Other Income / Expense

| Acct # | Account Name | QBO Type | QBO Detail Type | 990 Part VIII Line | Notes |
|---|---|---|---|---|---|
| 8000 | Interest Income | Other Income | Interest Earned | Line 4 | Bank interest |
| 8010 | Dividend Income | Other Income | Dividend Income | Line 5 | If invested |
| 8100 | Exchange Gain or Loss | Other Expense | Exchange Gain or Loss | Line 10 / Part IX Line 24 | QBO auto-created with multicurrency |
| 8200 | Gain/Loss on Disposal of Assets | Other Income | Gain/Loss on Sale of Assets | Line 7 | Fixed asset sales |
| 8300 | Interest Expense | Other Expense | Other Miscellaneous Expense | Part IX Line 19 | Loan interest |
| 8900 | Other Income | Other Income | Other Miscellaneous Income | Line 11e | Catch-all; review and reclassify |
| 8910 | Other Expense | Other Expense | Other Miscellaneous Expense | Part IX Line 24 | Catch-all; review and reclassify |

---

## Functional Expense Allocation Summary

| Allocation Basis | When to Use | Documentation Required |
|---|---|---|
| Direct assignment | Expense clearly serves one function only | Invoice/receipt showing program/admin/fundraising purpose |
| Time study | Personnel costs; shared staff | Annual time allocation survey or time logs |
| Square footage | Occupancy costs (rent, utilities, insurance) | Floor plan with labeled areas per function |
| Headcount | Supplies, IT, shared services | Staff list with functional assignment |
| Trip logs | Vehicle costs | Mileage/trip log with purpose per trip |

Revisit allocation bases annually or when staffing/program mix changes materially (Source: Mainini 2009).

---

## Form 990 Part IX Line Quick Reference

| 990 Line | Description | UCOA Account Range |
|---|---|---|
| Line 1 | Grants and similar amounts paid | 6800-6810 |
| Line 5 | Compensation of current officers, directors, key employees | 6000 |
| Line 7 | Other salaries and wages | 5100-5110, 6010, 7000 |
| Line 9 | Employee benefits | 6020 |
| Line 10 | Payroll taxes | 6030-6060 |
| Line 11b | Legal fees | 6110 |
| Line 11c | Accounting fees | 6100, 6130 |
| Line 11g | Other professional fees | 6070, 6120, 5150 |
| Line 12 | Office expenses | 6300-6320, 5140, 5180-5190, 6820 |
| Line 15 | Occupancy | 6200-6240 |
| Line 16 | Travel | 5120-5130, 6500-6550, 7500 |
| Line 17 | Conferences and meetings | 6920 |
| Line 19 | Interest expense | 8300 |
| Line 21 | Depreciation | 6600-6650 |
| Line 22 | Insurance | 6700-6740 |
| Line 24e | Other expenses | All remaining |

## Sources

- London (2019) "QuickBooks for Nonprofits & Churches"
- Ivens (2005) "Running QuickBooks in Nonprofits"
- Mainini (2009) "Non-Profit Accounting: Functional Expense Allocation"
- IRS Form 990 Instructions (current revision)
- FASB ASC 958: Not-for-Profit Entities
- UCOA Nonprofit Chart of Accounts, Version 3.0
