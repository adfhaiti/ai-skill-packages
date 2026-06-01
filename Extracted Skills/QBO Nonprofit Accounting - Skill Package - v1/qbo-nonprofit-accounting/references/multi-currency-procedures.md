# Multi-Currency Procedures: HTG/USD Operations in QBO

Complete procedures for managing Haitian Gourde (HTG) and US Dollar (USD) operations in QuickBooks Online. Grounded in Shelton (2024), Ringstrom (2024), Biafore (2016), and BRH rate sourcing practices.

## 1. Pre-Enable Checklist

**WARNING: Enabling multicurrency is IRREVERSIBLE.**

- [ ] QBO plan is Essentials, Plus, or Advanced (not Simple Start)
- [ ] Home currency correctly set to USD (cannot change after)
- [ ] Export Trial Balance and Balance Sheet (backup)
- [ ] Review all existing customers/vendors (currency locks after multicurrency enabled)
- [ ] Classes already enabled (enable Classes BEFORE multicurrency)
- [ ] Document current BRH reference rate

## 2. Enabling Multicurrency

Path: **Settings > Account and Settings > Advanced > Currency**

1. Toggle Multicurrency ON
2. QBO warning: "Are you sure? You can't undo this."
3. Confirm. Home currency displays as USD.

## 3. Adding HTG

Path: **Settings > Currencies > Add Currency**

1. Search "Haitian Gourde" or "HTG", select it
2. QBO may auto-populate a rate (unreliable for HTG)
3. Always manually verify against BRH reference rate

QBO downloads rates every 4 hours from Wall Street on Demand (S&P Global). For HTG, these are frequently inaccurate or stale.

## 4. Creating Foreign Currency Entities

### HTG Customers
**Sales > Customers > New Customer**, set Currency to HTG. Currency locks after first transaction. Need both USD and HTG for same client? Create two records.

### HTG Vendors
**Expenses > Vendors > New Vendor**, set Currency to HTG. Same lock rule.

### HTG Bank Accounts
**Settings > Chart of Accounts > New**: Type Bank, Detail Type Checking, Currency HTG. Enter opening balance in HTG.

## 5. Exchange Rate Management

### BRH Reference Rate
Authoritative source: Banque de la Republique d'Haiti (brh.ht), daily taux de reference.

### Viewing/Editing
Path: **Settings > Currencies > select HTG > View Exchange Rates**

### Manual Entry
**Settings > Currencies > select HTG > Edit Rate**. Enter as "1 USD = [X] HTG" with 4 decimal places (e.g., 131.4285).

### Per-Transaction Override
On any HTG transaction, click the exchange rate field to override with the BRH rate for that specific date.

### Update Schedule
- Weekly minimum: Monday, using prior Friday BRH rate
- Per-transaction ideal: BRH rate for transaction date (required for large transactions)
- Month-end required: BRH rate as of last business day (for revaluation)

Maintain a rate log (date, BRH rate, QBO rate entered, source, who updated).

## 6. Recording HTG Transactions

### HTG Expense
**+ New > Expense**: select HTG vendor, HTG payment account, enter amount in HTG, verify exchange rate, assign category/class/project. QBO calculates USD equivalent.

### HTG Invoice
**+ New > Invoice**: select HTG customer, enter amounts in HTG, verify rate, assign class/project.

### HTG Bill
**+ New > Bill**: select HTG vendor, enter in HTG, verify rate, assign category/class/project.

### USD-to-HTG Transfer
**+ New > Transfer**: from USD bank, to HTG bank. Enter USD amount transferred and HTG amount received. QBO calculates effective rate; any difference creates exchange gain/loss.

## 7. HTG Bank Reconciliation

Manual import (Haitian banks lack direct feeds):
1. Download statement as CSV, format: Date (yyyy-mm-dd), Description, Amount
2. Upload to **Transactions > Bank Transactions > HTG account**
3. Review on For Review tab

Reconcile: **Settings > Reconcile > select HTG account**. Enter statement ending balance in HTG. QBO tracks HTG natively; Balance Sheet reports USD equivalent.

## 8. Period-End Revaluation

QBO auto-revalues open HTG invoices/bills when rates change. QBO does NOT auto-revalue HTG bank balances.

Manual bank revaluation JE:
1. Determine HTG bank balance at period-end
2. Calculate USD equivalent at period-end BRH rate
3. Compare to current USD equivalent on Balance Sheet
4. Post adjusting JE:

| Date | Account | Debit | Credit | Memo |
|---|---|---|---|---|
| Period-end | Exchange Gain or Loss | [difference] | | [Month] revaluation - HTG bank |
| Period-end | 1020 Operating Checking (HTG) | | [difference] | [Month] revaluation - HTG bank |

(Reverse debit/credit if USD equivalent increased.) Do NOT assign Classes to revaluation entries.

## 9. Realized vs. Unrealized Gain/Loss

**Realized**: when HTG transaction settles at different rate than recorded. QBO auto-posts to Exchange Gain or Loss account.

**Unrealized**: when open HTG balances are revalued at period-end. QBO handles open invoices/bills automatically; bank balances require manual JE (Section 8).

Exchange Gain or Loss account: auto-created by QBO. Maps to 990 Part VIII Line 10 (gain) or Part IX Line 24 (loss).

## 10. Reporting

All standard reports display in USD. Foreign-currency detail available within individual transactions.

Useful reports: Balance Sheet (all accounts in USD at current rate), P&L by Class (USD equivalent), Transaction Detail by Account (HTG account detail), Unrealized Gain/Loss, A/R and A/P Aging (both currencies shown).

Export HTG detail: run Transaction Detail by Account for HTG accounts, export to Excel (includes both HTG and USD amounts).

## 11. Common Issues

| Issue | Fix |
|---|---|
| Wrong currency on customer/vendor | Cannot change; create new record with correct currency |
| Stale HTG rate | Always manually update from BRH before entering transactions |
| Large gain/loss on payment | Expected; review Exchange Gain or Loss register monthly |
| Bank balance USD mismatch | Post manual revaluation JE (Section 8) |
| Cannot disable multicurrency | No fix; start new company file if truly not needed |
| Transfer shows gain/loss | Correct behavior; review at period-end |
| Reports show different USD amounts over time | QBO revalues open items at current rate; P&L retains original rate |
| Need both currencies on one invoice | QBO invoices are single-currency; add note in memo/footer |

## Sources

- Shelton (2024) "Mastering QuickBooks 2025", Chapter 16
- Ringstrom (2024) "QBO For Dummies 2025", Chapter 4
- Biafore (2016) "QuickBooks 2016: The Missing Manual", Appendix H
- BRH: brh.ht (taux de reference)
