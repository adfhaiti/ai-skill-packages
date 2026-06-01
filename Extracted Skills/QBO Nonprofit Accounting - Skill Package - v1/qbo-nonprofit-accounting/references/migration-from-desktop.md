# Migration from QuickBooks Desktop to QBO

Guide for migrating nonprofit accounting from QuickBooks Desktop to QBO. Grounded in London (2019), Ivens (2005), Shelton (2024).

## 1. Pre-Migration Assessment

### File Health
- [ ] Run Verify and Rebuild in Desktop (File > Utilities)
- [ ] Resolve data integrity errors
- [ ] Confirm file opens cleanly

### List Cleanup
- [ ] Inactivate unused COA accounts (QBO Plus limit: 250)
- [ ] Merge duplicate customers, vendors, accounts
- [ ] Standardize naming (remove special characters, apostrophes)
- [ ] Clean class list (QBO Plus: 40 combined classes+locations)

### Reconciliation
- [ ] All bank/credit card accounts reconciled through most recent statement
- [ ] Undeposited Funds verified (should be zero)
- [ ] A/R and A/P aging reviewed

### Financial Snapshot
- [ ] Export Trial Balance, Balance Sheet, P&L, P&L by Class as PDF and Excel

## 2. What the Migration Tool Transfers

| Data | Transfers | Notes |
|---|---|---|
| Chart of accounts | Yes | Numbers, names, types, balances |
| Customers | Yes | Name, contact, open balances |
| Vendors | Yes | Name, contact, open balances |
| Employees | Yes | Names, basic info |
| Items/products | Yes | Name, rate, income account |
| Classes | Yes | May flatten subclass hierarchy |
| Open invoices/bills | Yes | Unpaid with line items |
| Journal entries | Partial | Recent; historical may summarize |
| Bank transactions | Partial | Older may become opening balances |

## 3. Manual Migration Required

| Data | Workaround |
|---|---|
| Memorized transactions | Recreate as Recurring Transactions |
| Custom reports | Recreate and save as Custom Reports |
| Budgets | Re-enter via Settings > Budgeting |
| Attachments | Re-upload to transactions |
| Audit trail | Archived in Desktop only |
| Bank feed rules | Recreate in Transactions > Rules |
| Closing date password | Reset in QBO Advanced settings |
| Multi-currency | Re-enable separately in QBO |

## 4. COA Restructuring (UCOA v3.0)

Migration is the ideal time to implement UCOA v3.0:
1. Export Desktop COA to Excel
2. Map each account to UCOA structure (see ucoa-chart-of-accounts.md)
3. Merge redundant accounts, standardize to 4-digit numbering
4. Import clean UCOA into QBO instead of migrating Desktop COA
5. Post opening balance journal entries

Net asset migration: consolidate three-tier (Unrestricted/Temporarily Restricted/Permanently Restricted) to ASC 958 two-tier (Without/With Donor Restrictions).

## 5. Class and Location Mapping

Map Desktop functional classes to QBO classes. If Desktop uses fund classes, consider Tags. Class hierarchy may flatten; verify and fix manually post-migration. Delete unused classes before migration to save toward 40 limit.

## 6. Customer/Job to Customer/Project

Desktop Jobs do NOT become QBO Projects. After migration: enable Projects, manually create per grant under Customer, re-assign transactions.

## 7. Historical Data Decisions

| Scenario | Recommendation |
|---|---|
| Active fiscal year | Migrate |
| 1-2 years comparative | Migrate opening balances; keep Desktop for detail |
| Closed grants | Archive in Desktop |
| Inactive donors | Migrate as inactive customers |
| Audit trail | Keep in Desktop |

Clean start recommended for UCOA restructuring: import lists + opening balances only.

## 8. Multi-Currency Timing

CRITICAL: Enable multicurrency in QBO BEFORE importing foreign currency transactions.

Sequence: basic setup > enable multicurrency > add HTG > create HTG entities > import/migrate.

If Desktop had multicurrency: disable before migration; re-enable in QBO and re-enter foreign currency opening balances manually.

## 9. Parallel Running (1-3 Months)

1. Enter transactions in both systems
2. Reconcile bank accounts in both monthly
3. Compare Trial Balance, Balance Sheet, P&L, A/R, A/P at month-end
4. Cutover when two consecutive months match (within $10 / 0.1%)

Prefer year-end or quarter-end boundary. Keep Desktop installed for historical reference.

## 10. Post-Migration Validation

### Day 1
- [ ] All COA accounts present with correct numbers/names/types
- [ ] Balances match Desktop Trial Balance
- [ ] Customer/vendor lists complete; open A/R and A/P match

### Week 1
- [ ] Sample transaction posts correctly
- [ ] P&L by Class matches Desktop
- [ ] One bank reconciliation verified

### Month 1
- [ ] Complete month-end close in QBO
- [ ] All reports match Desktop
- [ ] Budget vs. Actual correct

## 11. Common Failures

| Issue | Fix |
|---|---|
| COA exceeds 250 | Inactivate in Desktop or upgrade to Advanced |
| Subclass hierarchy flattens | Manually re-establish parent-child in QBO |
| Multicurrency errors | Disable in Desktop before migration; re-enable in QBO |
| Memorized transactions missing | Recreate from Desktop listing |
| Opening Balance Equity nonzero | Post correcting JEs to net asset accounts; target $0 |
| Bank feeds missing | Reconnect; set start date to avoid duplicates |

## Sources

- London (2019) "QuickBooks for Nonprofits & Churches"
- Ivens (2005) "Running QuickBooks in Nonprofits"
- Shelton (2024) "Mastering QuickBooks 2025", Chapters 2-3
