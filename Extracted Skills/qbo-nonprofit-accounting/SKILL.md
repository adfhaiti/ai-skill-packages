---
name: qbo-nonprofit-accounting
description: >
  This skill applies when users ask about QuickBooks Online for nonprofits,
  nonprofit accounting in QBO, chart of accounts setup, recording grants or
  contributions, functional expense allocation, multi-currency (USD/HTG),
  migrating from QuickBooks Desktop to QBO, or generating nonprofit financial
  statements. Triggers include "set up QuickBooks for our nonprofit", "how do I
  record a grant in QBO", "migrate from QuickBooks Desktop to Online",
  "QuickBooks multi-currency", "chart of accounts for nonprofit", "record an
  expense in gourdes", "help with our books", "nonprofit accounting", and "QBO
  setup". Not for Form 990 preparation, review, or filing (use
  form-990-nonprofit skill). Not for Excel formatting or spreadsheet creation
  (use excel-style skill). Not for general IT troubleshooting (use it-support
  skill).
---

# QBO Nonprofit Accounting

Provide step-by-step QuickBooks Online guidance for 501(c)(3) organizations operating in dual-currency environments. Covers initial setup through year-end close, grounded in GAAP/ASC 958, UCOA v3.0 chart of accounts, and IRS Form 990 functional expense categories.

Primary audience: nonprofit executive director or bookkeeper with moderate accounting knowledge but limited QBO experience. Provide exact QBO menu paths, account numbers, and compliance context at every step.

## Decision Routing

Parse user intent, then branch:

| User Intent | Branch | Reference to Load |
|---|---|---|
| Set up QBO for a nonprofit from scratch or restructure existing setup | Setup & Configuration | `references/qbo-setup-guide.md` |
| Record transactions, manage day-to-day bookkeeping | Daily Operations | `references/daily-operations-guide.md` |
| Move data from QuickBooks Desktop to QBO | Migration | `references/migration-from-desktop.md` |
| Connect QBO with other systems (banks, Fulcrum, payroll, donors) | Integration & Sync | `references/integration-patterns.md` |
| Handle foreign currency transactions, exchange rates, revaluation | Multi-Currency | `references/multi-currency-procedures.md` |
| Generate reports, prepare for audit, support Form 990 prep | Reporting & Compliance | `references/reporting-guide.md` |

If intent spans multiple branches, load the primary branch reference first, then load secondary references as needed. If intent is ambiguous, ask the user to clarify before loading references.

## Reference Loading Table

Load references on-demand, not upfront. Each branch specifies which file to load.

| File | Content | Load When |
|---|---|---|
| `references/ucoa-chart-of-accounts.md` | Full UCOA v3.0 chart with account numbers, types, detail types, Form 990 line mappings | Setup; any question about account numbers or COA structure |
| `references/qbo-setup-guide.md` | Step-by-step QBO configuration: company setup, multicurrency, classes, products, connected accounts | Setup & Configuration branch |
| `references/daily-operations-guide.md` | Transaction recording: contributions, invoicing, expenses, payroll, bank rec, petty cash, month-end | Daily Operations branch |
| `references/migration-from-desktop.md` | QB Desktop to QBO migration: assessment, tool transfers, manual steps, parallel running, validation | Migration branch |
| `references/integration-patterns.md` | Bank feeds, CSV import, Fulcrum workflow, donor platforms, payroll sync, API, automation | Integration & Sync branch |
| `references/multi-currency-procedures.md` | HTG/USD procedures: enabling, exchange rates, BRH sourcing, revaluation, gain/loss, reconciliation | Multi-Currency branch |
| `references/reporting-guide.md` | ASC 958 financial statements, grant reports, CPA data package, year-end close, 990 handoff | Reporting & Compliance branch |

## QBO Edition Constraints

Procedures vary by QBO edition. Always specify when a feature requires a higher tier.

| Feature | Simple Start | Essentials | Plus | Advanced |
|---|---|---|---|---|
| Classes | No | No | 40 (combined with Locations) | Unlimited |
| Locations | No | No | 40 (combined with Classes) | Unlimited |
| Chart of Accounts limit | 250 | 250 | 250 | Unlimited |
| Users | 1 | 3 | 5 | 25 |
| Projects | No | No | Yes | Yes |
| Budgets | No | No | Yes | Yes |
| Custom roles | No | No | No | Yes |
| Batch transactions | No | No | No | Yes |
| Invoice import | No | No | Yes | Yes |
| Multicurrency | No | Yes | Yes | Yes |

Source: Shelton (2024) Table 2.1.

## Compliance Guardrails

- NEVER fabricate account numbers, exchange rates, or financial figures.
- NEVER provide tax advice. Frame as "IRS instructions state..." or "GAAP requires..."
- ALWAYS warn before irreversible QBO actions: enabling multicurrency, deleting transactions, closing books.
- ALWAYS specify the QBO edition when procedures differ across plans.
- ALWAYS note when a procedure requires QBO Advanced.
- ALWAYS recommend accrual basis for GAAP-compliant nonprofit reporting.
- ALWAYS assign functional classes (Program Services, Management and General, Fundraising) to expense transactions.

## Output Standards

- Step-by-step procedures: numbered steps with exact QBO menu paths in bold
- Account references: include account number, name, and type
- Financial figures: whole dollars, comma-separated thousands
- Exchange rates: 4 decimal places
- Journal entries: standard debit/credit table format with Date, Account, Debit, Credit, Class, Memo
- All Excel output: proper Excel Tables with TableStyleInfo, Aptos 11pt, built-in Table Styles
- All Word output: ADF brand standards per adf-docx-style skill

## Cross-Skill Handoffs

| When | Hand Off To |
|---|---|
| Form 990 preparation or specific 990 schedules | `form-990-nonprofit` skill |
| Excel workbook formatting or data table creation | `excel-style` + `xlsx` skills |
| Word document formatting for reports or proposals | `adf-docx-style` + `docx` skills |
| Fulcrum form design for field data collection | `fulcrum-expert` skill |
| Haitian Creole translation for bilingual documents | `haitian-creole` skill |

## Sources

- Shelton (2024) "Mastering QuickBooks 2025"
- Ringstrom (2024) "QuickBooks Online For Dummies, 2025 Edition"
- Katz Pollock (2024) "QBO: From Setup to Tax Time"
- London (2019) "QuickBooks for Nonprofits & Churches"
- Ivens (2005) "Running QuickBooks in Nonprofits"
- Mainini (2009) "Non-Profit Accounting: Functional Expense Allocation"
- FASB ASC 958: Not-for-Profit Entities
- IRS Form 990 Instructions (current revision)
