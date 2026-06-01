# QBO Setup Guide for Nonprofits

Step-by-step QBO configuration for 501(c)(3) organizations. Grounded in Shelton (2024), Ringstrom (2024), Katz Pollock (2024).

## 1. Company Setup

Path: **Settings > Account and Settings > Company**

1. Navigate to quickbooks.intuit.com, start free trial or sign in
2. Company name: legal name from IRS determination letter
3. Industry: Nonprofit Organization
4. Business type: Nonprofit organization
5. Address: US registered agent address
6. Fiscal year start month: per bylaws (most use January or July)
7. EIN: organization's Employer Identification Number

## 2. Plan Selection

QBO Plus ($99/mo) is minimum for nonprofits needing Classes, Projects, and Budgets. QBO Advanced ($235/mo) for 250+ accounts, 5+ users, custom roles, batch entry. Check TechSoup for nonprofit discounts.

| Feature | Simple Start | Essentials | Plus | Advanced |
|---|---|---|---|---|
| Users | 1 | 3 | 5 | 25 |
| Classes | No | No | 40 | Unlimited |
| Projects | No | No | Yes | Yes |
| Multicurrency | No | Yes | Yes | Yes |
| COA limit | 250 | 250 | 250 | Unlimited |

## 3. Account and Settings

Path: **Settings > Account and Settings > Advanced**

1. First month of fiscal year: set correctly
2. Accounting method: **Accrual** (GAAP requirement)
3. Close the books: set after year-end close (see reporting-guide.md)
4. Track classes: ON (Plus/Advanced); assign "One to each row in transaction"
5. Track locations: ON if multi-site (shares 40 limit with classes on Plus)
6. Currency/Multicurrency: enable ONLY if needed; IRREVERSIBLE (see multi-currency-procedures.md)
7. Projects: ON (Plus/Advanced)

Enable features in this order: COA first, then Classes/Locations, then Multicurrency, then Projects, then Bank connections.

## 4. Chart of Accounts Import

Path: **Settings > Import Data > Chart of Accounts**

See `references/ucoa-chart-of-accounts.md` for full UCOA v3.0 structure.

1. Download QBO sample import file for column reference
2. Prepare file: Account Number, Account Name, Type, Detail Type
3. Use `Parent:Subaccount` naming for hierarchy
4. File must be under 1,000 rows, 2 MB, and CLOSED in Excel
5. Upload, map columns, review, import
6. Verify: toggle on account numbers display, check types and hierarchy

Net asset accounts (create manually if not imported):
- 3100 Net Assets Without Donor Restrictions (Equity: Opening Balance Equity)
- 3200 Net Assets With Donor Restrictions (Equity: Opening Balance Equity)

## 5. Multi-Currency (If Needed)

Path: **Settings > Account and Settings > Advanced > Currency**

IRREVERSIBLE. See `references/multi-currency-procedures.md` for full procedures and pre-enable checklist.

1. Toggle Multicurrency ON, confirm warning
2. Add HTG: **Settings > Currencies > Add Currency > Haitian Gourde**
3. Set initial rate manually (use BRH reference rate, not QBO auto-rate)

## 6. Class Tracking

Path: **Settings > All Lists > Classes**

Create functional classes:

| Class | Purpose | 990 Column |
|---|---|---|
| Program Services | Program delivery | B |
| Management and General | Admin/oversight | C |
| Fundraising | Donor acquisition | D |

Optional subclasses under Program Services: Data Collection, GIS and Mapping, Program Evaluation, Digital Training, Capacity Building, Community Development.

## 7. Location Tracking (Optional)

Path: **Settings > All Lists > Locations**

Create if multi-site: Fond-des-Blancs, Port-au-Prince, US Operations.

## 8. Products and Services

Path: **Sales > Products and Services > New**

Create service items for each revenue line:

| Name | Type | Income Account |
|---|---|---|
| Data Collection Services | Service | 4200 Contract Revenue |
| GIS and Mapping Services | Service | 4200 Contract Revenue |
| Program Evaluation Services | Service | 4200 Contract Revenue |
| Digital Training Services | Service | 4200 Contract Revenue |
| Capacity Assessment Services | Service | 4200 Contract Revenue |
| Data Analysis and Visualization | Service | 4200 Contract Revenue |

## 9. Customer Setup (Grantors/Donors)

Path: **Sales > Customers > New Customer**

Grantors/clients: org name, contact email, currency (USD or HTG; locks after first transaction), payment terms per contract.

Donors: "Last, First" format, email for acknowledgments, USD currency.

If both USD and HTG invoicing needed for same client: create two records (e.g., "Client (USD)" and "Client (HTG)").

## 10. Vendor Setup

Path: **Expenses > Vendors > New Vendor**

Set currency before first transaction (permanent). Toggle "Track payments for 1099" ON for US vendors paid $600+ who are not corporations.

## 11. Project Setup (Grants/Contracts)

Path: **Business Overview > Projects > New Project** (Plus/Advanced)

Enable: **Settings > Advanced > Projects > ON**

Create a Project for each active grant/contract under the corresponding Customer. Include: name, customer, status, start/end dates, notes (contract value, deliverables, reporting schedule).

## 12. Bank and Credit Card Connections

US banks: **Transactions > Bank Transactions > Link Account** (automatic feed).

Haitian banks (BUH, Sogebank, BNC, Unibank): manual CSV import. See `references/integration-patterns.md`.

## 13. User Roles

Path: **Settings > Manage Users > Add User**

| Role | Typical User |
|---|---|
| Company Admin | Executive Director |
| Standard (All Access) | Bookkeeper/Finance Manager |
| Standard (Limited) | Program Manager (customized) |
| Reports Only | Board Treasurer |

Plus: max 5 users. Advanced: max 25, custom roles available.

## 14. Recurring Transactions

Path: **Settings > Recurring Transactions > New**

Set up for: monthly rent, internet, software subscriptions, depreciation JE, prepaid amortization JE. Use split lines for functional allocation of shared expenses.

## Post-Setup Verification

- [ ] Company info correct (name, EIN, fiscal year)
- [ ] Plan is Plus or Advanced
- [ ] COA imported with correct numbers, names, types
- [ ] Multicurrency enabled with HTG (if needed)
- [ ] Classes enabled with functional categories
- [ ] Products/services created for all service lines
- [ ] Key customers and vendors created with correct currency
- [ ] Active grants/contracts set up as Projects
- [ ] Bank accounts connected or import workflow established
- [ ] Users created with appropriate roles
- [ ] Recurring transactions configured

## Sources

- Shelton (2024) "Mastering QuickBooks 2025", Chapters 1-4
- Ringstrom (2024) "QBO For Dummies 2025", Chapters 1-3
- Katz Pollock (2024) "QBO: From Setup to Tax Time", Chapters 1-5
