# Daily Operations Guide: Nonprofit Bookkeeping in QBO

Procedures for recording transactions, managing day-to-day bookkeeping, and executing month-end close in QuickBooks Online for a 501(c)(3). Grounded in London (2019), Ivens (2005), Ringstrom (2024), Katz Pollock (2024), and Mainini (2009).

## 1. Recording Contributions

### Unrestricted Contributions

Path: **+ New > Sales Receipt** (payment received) or **+ New > Invoice** (pledged)

Sales Receipt: select Customer (donor), date, payment method, deposit to bank account, line item mapped to 4100 Contributions - Unrestricted, amount, memo (check number, acknowledgment status). Save.

Invoice (pledge): select Customer, invoice date, due date, line item 4100, save. When payment received: **+ New > Receive Payment**, select invoice.

### Restricted Contributions

Same procedure; line item maps to **4110 Contributions - Restricted**. Add detailed memo describing restriction. Track using Customer/Project if grant-specific.

### In-Kind Contributions

Path: **+ New > Journal Entry**

| Date | Account | Debit | Credit | Memo |
|---|---|---|---|---|
| [date] | [Asset or Expense account] | [FMV] | | In-kind: [description] |
| [date] | 4120 In-Kind Contributions | | [FMV] | In-kind: [description] |

### Release from Restriction

| Date | Account | Debit | Credit | Memo |
|---|---|---|---|---|
| [date] | 4900 Net Assets Released from Restriction | [amount] | | Release: [grant/purpose] |
| [date] | 4100 Contributions - Unrestricted | | [amount] | Release: [grant/purpose] |

## 2. Contract Invoicing (USD and HTG)

Path: **+ New > Invoice**

Select Customer, product/service (service line), description matching SOW deliverable, quantity/rate per contract, Class (Program Services or subclass), Project (grant/contract), memo with contract reference. Save and Send.

HTG invoices: customer must be HTG-currency. Verify exchange rate (click rate field to override with BRH rate).

Progress invoicing (Plus/Advanced): create Estimate for full contract, then **+ New > Invoice > Create from Estimate** for each milestone.

## 3. Functional Expense Allocation

Three categories (Mainini 2009): Program Services (990 Col B), Management and General (Col C), Fundraising (Col D).

**Approach 1 (Recommended): Transaction-Level.** Assign Class on every line. For shared costs, split into multiple lines (e.g., internet: 60% Program / 25% M&G / 15% Fundraising).

**Approach 2: Period-End JE.** Record shared expenses to default class, redistribute via month-end journal entry.

Allocation bases: personnel (time study), occupancy (square footage), office/IT (headcount), vehicles (trip logs), software (direct assignment).

Common misclassifications: grant writing is Fundraising (not Program); ED salary splits all three functions; board meeting costs are M&G.

## 4. Recording Expenses

**Direct payment:** **+ New > Expense**. Select payee, payment account, date, line items with Category, Amount, Class, Customer/Project. Attach receipt.

**Credit card:** Same as above; payment account = credit card account.

**Bill (A/P):** **+ New > Bill**. Enter vendor, dates, line items. Pay later via **+ New > Pay Bills**.

## 5. Payroll Journal Entries

### US Payroll (QBO Payroll Add-On)
Auto-posts. No manual entry needed.

### Haiti Payroll (External)
Calculate externally. Monthly JE with: gross wages by employee (Debit 6000/6010 by Class per time study), withholdings (Credit 2300-series liabilities: ONA, OFATMA, IRI, CAS), employer contributions (Debit 6040-6060), net pay (Credit HTG bank).

Allocation: enumerators/field staff 100% Program; ED split per time study; finance 90% M&G; fundraising coordinator 100% Fundraising.

## 6. Petty Cash and MonCash

Accounts: 1040 (USD), 1050 (HTG), 1060 MonCash (HTG).

Replenish: **+ New > Expense** from bank to petty cash account. Record expenditures: **+ New > Expense** with payment account = petty cash, proper expense category and class. Reconcile MonCash monthly against Digicel statement.

## 7. Bank Reconciliation

Path: **Settings > Reconcile**

1. Select account, enter statement ending date and balance (in account currency)
2. Check off matching transactions
3. Difference must reach $0.00 / 0.00 HTG
4. Investigate discrepancies: missing transactions, duplicates, bank fees (6330), interest (8000)
5. Click **Finish Now**

Reconcile every account monthly within 10 days of statement close.

## 8. Accounts Payable Workflow

Enter bills: **+ New > Bill** with category, class, project. Review: **Reports > A/P Aging Summary**. Pay: **+ New > Pay Bills**, select bills, payment account. Vendor credits: **+ New > Vendor Credit**, apply to next bill payment.

## 9. Common Journal Entries

**Depreciation (monthly):** Debit 66XX depreciation expense (by class allocation) / Credit 13XX accumulated depreciation.

**Prepaid amortization:** Debit expense account (by allocation) / Credit 1200 Prepaid Expenses.

**Deferred revenue recognition:** Debit 2100 Deferred Revenue / Credit 4200 Contract Revenue (Class: Program Services).

**Write-off uncollectible:** Debit 6930 Bad Debt (M&G) / Credit 1100 A/R.

## 10. Month-End Close Checklist

### Week 1
- [ ] All transactions entered for closed month
- [ ] HTG bank transactions imported (CSV)
- [ ] Bank feed For Review tab cleared
- [ ] Undeposited Funds = zero

### Week 2
- [ ] All bank/credit card accounts reconciled
- [ ] Depreciation, prepaid amortization, payroll JEs posted
- [ ] Functional allocation adjustments posted
- [ ] HTG exchange rate updated to month-end BRH rate
- [ ] HTG bank revaluation JE posted

### Review
- [ ] P&L by Class: all expenses have class
- [ ] Balance Sheet cash matches reconciled balances
- [ ] A/R and A/P aging reviewed
- [ ] 6990 Miscellaneous reclassified
- [ ] Month-end reports exported and filed

## 11. Internal Controls

Segregation (London 2019): bookkeeper enters, ED reviews weekly. Payments over $500: ED approval. Bank rec: bookkeeper prepares, ED signs off. New vendors: ED approves.

QBO Audit Log: **Reports > Audit Log** (automatic, cannot be edited). Receipt policy: all expenses over $25 require receipt, uploaded within 7 days. Check signing: under $500 one signature, $500-$5,000 two signatures, over $5,000 board approval.

Monthly board package: P&L by Class (month + YTD), Balance Sheet, Budget vs. Actual, cash flow summary, A/R Aging.

## Sources

- London (2019) "QuickBooks for Nonprofits & Churches", Chapters 4-8
- Ivens (2005) "Running QuickBooks in Nonprofits", Chapters 5-10
- Ringstrom (2024) "QBO For Dummies 2025", Chapters 5-7
- Katz Pollock (2024) "QBO: From Setup to Tax Time", Chapters 4-8
- Mainini (2009) "Non-Profit Accounting: Functional Expense Allocation"
