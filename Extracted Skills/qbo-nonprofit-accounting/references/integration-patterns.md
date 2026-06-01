# Integration Patterns Reference

Bank feeds, CSV imports, field data collection sync, donor platform reconciliation,
payroll integration, and API automation patterns for QBO nonprofit operations.

---

## 1. Bank Feeds

### US Bank Accounts (Automatic)

QBO connects directly to most US banks for automatic transaction download.

**Setup:** **Settings > Banking > Connect account** > search institution > authenticate >
select accounts > map to QBO bank accounts.

**Matching rules:** **Banking > Bank rules** > create rules to auto-categorize:
- Recurring vendors (rent, utilities, insurance) > assign expense account + class
- Payroll processor (Gusto, ADP) > assign Payroll Expense accounts
- Known donors (recurring gifts) > assign contribution income account

**Best practice:** Review and approve bank feed transactions weekly. Do not let
unreviewed transactions accumulate beyond 30 days.

### Haiti Bank Accounts (Manual CSV)

Haitian banks (Unibank, Sogebank, BNC, BUH) do not connect to QBO bank feeds.
Download statements manually and import via CSV.

**Monthly procedure:**
1. Download bank statement from online banking portal (CSV or Excel format)
2. Reformat to QBO CSV import template (Date, Description, Amount columns)
3. Convert HTG amounts if needed; QBO records in the account's designated currency
4. **Banking > Upload transactions** > select the HTG bank account > upload CSV
5. Match or add transactions in the Banking register
6. Reconcile at month-end using the bank statement balance

**CSV format requirements:**
- Date format: MM/DD/YYYY
- Amount: single column (positive for deposits, negative for withdrawals) OR separate
  Debit/Credit columns
- Description: vendor/payee name
- No header rows beyond the column names
- UTF-8 encoding (critical for Haitian Creole characters in descriptions)

## 2. Bank Feed Rules for Functional Allocation

Create rules to auto-assign classes (functional categories) to recurring transactions:

| Transaction Pattern | Account | Class |
|---|---|---|
| Office rent payment | 7200 Occupancy | Management and General |
| Field vehicle fuel (Digicel MonCash) | 7400 Transportation | Program Services |
| Internet (Digicel/Natcom) | 7530 IT and Communications | Management and General |
| Donor platform fees (Givebutter) | 8200 Fundraising Expenses | Fundraising |

**Setup:** **Banking > Bank rules** > Add rule > set conditions (payee contains,
amount range) > assign category, class, and optionally location/customer.

For expenses requiring split allocation (e.g., shared office costs), do not use
bank rules. Instead, record as a journal entry with split lines by class.

## 3. Receipt Capture

QBO mobile app captures receipt images and extracts vendor, date, and amount.

**Procedure:** Open QBO mobile > tap camera icon > photograph receipt > review
extracted data > assign account and class > save.

**For Haiti field operations:** Train field staff to photograph receipts immediately.
HTG receipts often fade quickly in tropical humidity. Receipt images attach to the
transaction record for audit trail.

**Limitations:** OCR does not reliably read Haitian Creole or French text. Manual
review of extracted data is required for all non-English receipts.

## 4. CSV/Excel Import for Bulk Transactions

### Transaction Import

**Settings > Import data > select type** (invoices, bills, bank transactions,
journal entries, chart of accounts, customers, vendors, products/services).

**Journal entry bulk import (QBO Advanced only):**
- Prepare CSV with columns: JournalDate, JournalNo, AccountName, Debits, Credits,
  Description, Name (customer/vendor), Class, Location
- **Settings > Import data > Journal entries** > map columns > import
- Verify imported entries in the Journal Entry register

**Standard edition workaround:** QBO Plus does not support journal entry import.
Options: (a) enter manually, (b) use third-party app (Transaction Pro Importer,
SaasAnt), (c) upgrade to Advanced.

### Chart of Accounts Import

Use during initial setup or migration. Prepare CSV with: Account Name, Account Type,
Detail Type, Description, Account Number (if enabled).

**Settings > Import data > Chart of accounts** > upload CSV > map columns > import.

**Critical:** Enable account numbers BEFORE importing: **Settings > Advanced >
Chart of accounts > Enable account numbers**. Account numbers cannot be added via
import if this setting is off.

## 5. Fulcrum-to-QBO Workflow

ADF uses Fulcrum (fulcrumapp.com) for field data collection. Fulcrum data feeds
into QBO for invoicing and expense tracking.

### Contract Invoicing Workflow

1. **Fulcrum:** Complete data collection for a contract deliverable (e.g., 500
   household surveys for Client X)
2. **Fulcrum export:** Export completion summary (record count, dates, quality metrics)
3. **QBO:** Create invoice for Client X referencing the contract deliverable
   - **+ New > Invoice** > select customer > add line items matching contract terms
   - Attach Fulcrum export summary as supporting documentation
   - Assign to Class: Program Services; Location: project location
4. **QBO:** Send invoice; track in A/R aging

### Field Expense Tracking

1. **Fulcrum:** Field supervisors log expenses in a Fulcrum expense tracking app
   (fuel, per diem, materials, transport)
2. **Export:** Weekly CSV export of field expenses
3. **QBO:** Import as bills or expenses
   - Map Fulcrum expense categories to QBO expense accounts
   - Assign Class based on project (Program Services for client contracts,
     Management and General for internal operations)

### Recommended Fulcrum Fields for QBO Mapping

| Fulcrum Field | QBO Field | Notes |
|---|---|---|
| project_name | Customer:Project | Maps to QBO project for job costing |
| expense_category | Account | Maps to COA expense account |
| amount_htg | Amount | Foreign currency amount |
| amount_usd | Amount | Home currency amount |
| receipt_photo | Attachment | Attach to QBO transaction |
| date | Transaction Date | Use field collection date |
| approved_by | Memo | Supervisor approval reference |

## 6. Donor Platform Reconciliation

### Givebutter

Givebutter deposits net of processing fees. Monthly reconciliation:

1. **Givebutter dashboard:** Export transaction report (CSV) for the month
2. **Identify:** Gross donations, processing fees, net deposits
3. **QBO entries:**
   - Debit: Bank account (net deposit amount)
   - Debit: 8210 Payment Processing Fees (Fundraising class)
   - Credit: 4100 Individual Contributions (amount per donor, Without Donor
     Restrictions or With Donor Restrictions as applicable)
4. **Reconcile:** Match QBO bank feed entries to Givebutter deposit report

### Donorbox

Same pattern as Givebutter. Export monthly report, record gross contributions
and processing fees separately.

### Zelle / Direct Bank Transfer

No processing fees. Record full amount as contribution income.
Match bank feed entries to donor records manually.

### Reconciliation Frequency

Monthly at minimum. For active fundraising campaigns, reconcile weekly to ensure
donor acknowledgment letters are timely (required for gifts over $250 per
IRS Publication 1771).

## 7. Payroll Integration

### US-Based Staff (if applicable)

If using Gusto, ADP, or QBO Payroll:
- Enable direct integration via **Apps > Find apps** > select payroll provider
- Payroll transactions post automatically to mapped accounts
- Verify class assignments monthly (payroll typically maps to Management and General
  unless staff are 100% program)

### Haiti-Based Staff (Manual Entry)

Haiti payroll is processed outside QBO (typically via manual calculation or local
payroll service). Record via journal entry:

**Monthly payroll JE:**
- Debit: 6100 Salaries and Wages (split by class based on time allocation)
- Debit: 6120 ONA Employer Contribution (class follows salary split)
- Debit: 6130 OFATMA Employer Contribution (class follows salary split)
- Credit: 2100 Accounts Payable or Bank (net pay)
- Credit: 2110 Payroll Tax Payable - ONA (employee + employer portions)
- Credit: 2120 Payroll Tax Payable - OFATMA
- Credit: 2130 Payroll Tax Payable - IRI (employee withholding)
- Credit: 2140 Payroll Tax Payable - CAS (if applicable)

**Functional allocation of payroll:**
Use monthly time studies or annual allocation percentages to split salary costs
across Program Services, Management and General, and Fundraising classes.

## 8. QBO API Overview

QBO provides a REST API for programmatic integration. Relevant for:
- Automated invoice creation from project management systems
- Bulk transaction import beyond CSV capabilities
- Custom reporting and data extraction
- Real-time sync with external databases

**Access:** Requires Intuit Developer account, OAuth 2.0 authentication, and
QBO API subscription. Technical implementation requires a developer.

**Key endpoints for nonprofit operations:**
- `/invoice` - create/read/update invoices
- `/journalentry` - create journal entries programmatically
- `/account` - read chart of accounts
- `/reports` - pull financial reports (P&L, Balance Sheet)
- `/customer` - manage donor/client records

**Rate limits:** 500 requests per minute per realm (company). Batch operations
recommended for bulk imports.

## 9. Zapier/Make Automation Patterns

Low-code automation for recurring workflows:

### Pattern 1: New Fulcrum Record to QBO Invoice Line

**Trigger:** New record in Fulcrum app (completed survey)
**Action:** Update Google Sheet tracking deliverable progress
**Threshold trigger:** When record count reaches contract milestone, create QBO invoice

### Pattern 2: Givebutter Donation to QBO Sales Receipt

**Trigger:** New donation in Givebutter
**Action:** Create QBO sales receipt with donor name, amount, and class assignment
**Benefit:** Eliminates manual donation entry; maintains real-time contribution records

### Pattern 3: Bank Statement Email to QBO Import

**Trigger:** Email from Haiti bank with statement attachment
**Action:** Parse attachment, reformat CSV, upload to QBO via API
**Note:** Requires custom parsing logic; bank statement formats vary

### Automation Cautions

- Always include error handling and notification on failure
- Test with small batches before enabling for all transactions
- Review automated entries weekly; do not rely on unmonitored automation
- Multi-currency transactions require extra validation (exchange rate accuracy)

## 10. Import Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| CSV import fails silently | Special characters (accents, Creole characters) | Save as UTF-8 with BOM |
| Duplicate transactions after import | Bank feed + manual import overlap | Delete duplicates in Banking register; use one method per account |
| Wrong currency on imported transactions | Account currency mismatch | Verify account's designated currency before import |
| Class not assigned on imported transactions | CSV missing Class column | Add Class column to CSV or edit transactions post-import |
| Customer/vendor not found | Name mismatch between CSV and QBO | Create customer/vendor first, or match names exactly |
| Date format errors | Regional date format mismatch | Use MM/DD/YYYY for US locale QBO |
| Amount sign reversed | Debit/credit convention differs | Check if QBO expects positive=deposit or separate columns |
| Import exceeds row limit | QBO limits CSV imports to 1,000 rows | Split file into batches under 1,000 rows each |
