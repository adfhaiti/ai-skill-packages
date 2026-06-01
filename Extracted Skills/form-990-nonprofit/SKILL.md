---
name: form-990-nonprofit
description: >
  This skill should be used when the user asks to "prepare our 990", "review this 990",
  "complete the Form 990", "help with our annual return", "990 data package", "check our
  990 for errors", "functional expense allocation", "Schedule A public support test", or
  mentions IRS Form 990, nonprofit tax filing, 990 schedules, Part IX expenses, Part VIII
  revenue, governance disclosure, or public charity status. Also trigger on uploads of a
  prior year 990 PDF or QuickBooks trial balance for 990 preparation. Not for 990-EZ,
  990-N, 990-PF, 990-T, or state charitable registrations. Not for general accounting
  (use QuickBooks tools).
---

# Form 990 Nonprofit

Prepare, draft, and review IRS Form 990 (Return of Organization Exempt From Income Tax) for 501(c)(3) public charities. Covers the 12-part core form and all 16 schedules (A through R). Operates in three modes: data gathering for CPA handoff, line-by-line drafting assistance, and compliance review of completed returns.

## Critical Compliance Guardrails

NEVER fabricate financial figures, EIN numbers, or IRS determination letter details. If source data is missing or ambiguous, flag the gap explicitly rather than estimating. Form 990 is a public document; errors have reputational, legal, and tax-exemption consequences.

NEVER provide legal or tax advice. Frame all guidance as "compliance best practices" or "IRS instructions state..." and recommend consultation with a qualified CPA or tax attorney for judgment calls (e.g., unrelated business income classification, lobbying expenditure thresholds, executive compensation reasonableness).

ALWAYS cite the specific IRS instruction reference (e.g., "Per 2025 Form 990 Instructions, Part VIII, Line 2") when explaining line-item requirements.

ALWAYS flag the three automatic revocation triggers:
1. Failure to file for three consecutive years (IRC 6033(j))
2. Material misstatement of revenues or assets
3. Private benefit or inurement issues

## Decision Routing

Parse user intent and branch accordingly:

| User Intent | Branch | Primary Output |
|---|---|---|
| Gather data, organize for CPA, build data package | [Prepare](#prepare) | XLSX workbook + data checklist |
| Complete specific parts/lines, draft narrative sections | [Draft](#draft) | Form content (text + figures) |
| Review uploaded 990 for errors, inconsistencies, risks | [Review](#review) | Review report with findings |
| Answer a specific 990 question (line guidance, deadline, etc.) | [Quick Reference](#quick-reference) | Direct answer with IRS citation |

If intent is ambiguous, ask which mode before proceeding.

## Reference Loading Table

Load on-demand based on the active branch. Never load all references upfront.

| File | Content | Load When |
|---|---|---|
| `references/core-form-guide.md` | Parts I-XII line-by-line guidance, data sources, common errors | Draft, Review, Quick Reference |
| `references/schedules-guide.md` | All 16 schedules: trigger conditions, key fields, 501(c)(3) focus | Draft, Review (when schedules involved) |
| `references/compliance-review-checklist.md` | Systematic review organized by risk area, cross-reference checks | Review |
| `references/data-gathering-guide.md` | Data collection mapped to form sections, QBO report names, board doc requirements | Prepare |
| `references/functional-expense-guide.md` | Part IX allocation methodology, reasonable allocation bases, common pitfalls | Draft (Part IX), Review (expense review) |
| `references/gaap-vs-irs-differences.md` | GAAP vs 990 reporting differences, contribution classification, pledge recognition, reconciliation mechanics | Prepare (from audited financials), Draft (Schedule D Parts XI-XII), Review (reconciliation checks) |
| `examples/data-package-template.md` | Template structure for CPA data package workbook | Prepare |
| `examples/review-report-template.md` | Template for 990 review findings report | Review |

---

<a id="prepare"></a>
## Branch: Prepare

Load `references/data-gathering-guide.md` and `examples/data-package-template.md`.

Goal: produce a structured data package (XLSX workbook with multiple tabs) containing all information a CPA needs to complete the Form 990, plus a checklist of outstanding items.

### Step 1: Determine Filing Profile

Collect or confirm these parameters before gathering data:

- Organization legal name, EIN, fiscal year end
- Filing threshold confirmation (gross receipts >= $200K OR total assets >= $500K requires full 990)
- Tax-exempt status: 501(c)(3) public charity vs. other
- Public charity classification (Schedule A line: 170(b)(1)(A)(vi) most common for small orgs)
- Prior year 990 available? (If uploaded, extract prior year figures for comparison)
- Accounting method (accrual vs. cash; most nonprofits use accrual)
- State filing requirements (some states require 990 copy)

### Step 2: Map Data Sources to Form Sections

Use the mapping table in `references/data-gathering-guide.md` to identify which QuickBooks reports, board documents, and operational records feed each Part and Schedule.

Primary data sources:
- QuickBooks: Trial Balance, Profit & Loss by Class, Balance Sheet, General Ledger detail
- Board records: meeting minutes, conflict of interest disclosures, compensation approvals
- Operational records: grant agreements, program descriptions, contractor payments (1099 threshold)
- Prior year 990: comparison figures, carryforward items, public support test history

### Step 3: Build the Data Package Workbook

Generate an XLSX workbook following the template in `examples/data-package-template.md`. Tabs include:

1. **Filing Profile**: organization info, fiscal year, accounting method, officer/director roster
2. **Revenue (Part VIII)**: contributions, program service revenue, investment income, other revenue; classified by column (related, unrelated, excluded)
3. **Expenses (Part IX)**: functional expense allocation across program, management/general, fundraising; all 24 natural expense categories
4. **Balance Sheet (Part X)**: beginning and end of year assets, liabilities, net assets
5. **Officers & Compensation (Part VII)**: name, title, hours, reportable compensation, other compensation, estimated benefits
6. **Program Accomplishments (Part III)**: mission statement, top 3 programs with descriptions, expenses, revenue, grants
7. **Governance (Part VI)**: board size, independence, policies in place, process descriptions
8. **Schedule Triggers (Part IV)**: answers to all 38 checklist questions determining required schedules
9. **Outstanding Items**: checklist of missing data with responsible party and deadline

### Step 4: Cross-Check and Validate

Before delivering the data package:
- Verify total revenue in Part VIII ties to the P&L
- Verify total expenses in Part IX tie to the P&L
- Verify balance sheet (Part X) beginning-of-year matches prior year end-of-year
- Verify net assets reconciliation (Part XI) works: BOY net assets + revenue - expenses = EOY net assets
- Flag any officer/director compensation that exceeds $150K (triggers Schedule J)
- Flag any single contributor exceeding $5K (triggers Schedule B)
- Flag foreign activities, grants, or accounts (triggers Schedule F)

---

<a id="draft"></a>
## Branch: Draft

Load `references/core-form-guide.md`. Load `references/schedules-guide.md` when working on schedules. Load `references/functional-expense-guide.md` when working on Part IX.

Goal: generate draft content for specific Form 990 parts or schedules, given source financial data and organizational information.

### Drafting Protocol

1. Identify which Part(s) or Schedule(s) the request targets
2. Load the relevant reference for line-by-line guidance
3. Request or locate source data needed for those sections
4. Generate draft content with:
   - Numerical figures formatted per IRS conventions (whole dollars, no cents)
   - Narrative descriptions written in clear, factual prose (Part III program accomplishments, Schedule O explanations)
   - Cross-references validated (e.g., Part I summary figures must match Parts VIII, IX, X)
5. Flag any line where source data is insufficient or a judgment call is required

### Narrative Drafting Standards

Part III (Program Accomplishments) and Schedule O narratives require specific qualities:

- Lead with measurable outcomes, not activities: "Trained 839 teachers across 50 schools" not "Conducted teacher training programs"
- Include quantitative metrics: beneficiaries served, units delivered, geographic scope
- Connect program activities to the exempt purpose stated in the determination letter
- Keep each program description to 150-250 words (Part III allows limited space; overflow to Schedule O)
- Avoid fundraising language or promotional tone; this is an informational return, not a donor appeal

### Functional Expense Allocation (Part IX)

This is the most complex and error-prone section. Load `references/functional-expense-guide.md` before drafting Part IX.

Core principles:
- Direct costs: assign to the function (program, management, fundraising) that directly benefits
- Shared costs: allocate using a reasonable, consistent, documented basis (time studies, square footage, headcount)
- Compensation: allocate based on documented time allocation across functions
- Joint costs (activities combining program + fundraising): follow ASC 958-720 criteria; allocate only if purpose, audience, and content tests are all met

### Schedule Trigger Logic

Part IV contains 38 yes/no questions. Each "yes" triggers a corresponding schedule. When drafting, systematically evaluate each question against the organization's activities. Common triggers for small 501(c)(3) public charities:

- Schedule A: ALWAYS required (public charity status and public support test)
- Schedule B: required if any contributor gave > $5,000 (or > 2% of total contributions if greater)
- Schedule D: required if the organization reported donor-advised funds, endowments, escrow accounts, or certain asset categories
- Schedule F: required if the organization conducted activities or had grants/employees outside the US
- Schedule O: ALWAYS required (supplemental information)

---

<a id="review"></a>
## Branch: Review

Load `references/compliance-review-checklist.md` and `examples/review-report-template.md`. Load `references/core-form-guide.md` if specific part guidance is needed.

Goal: systematically review a completed Form 990 (PDF or data) for errors, inconsistencies, compliance risks, and best practice gaps. Produce a structured findings report.

### Review Protocol

1. **Intake**: read the uploaded 990 PDF; extract key figures and narrative content
2. **Mathematical verification**: check all arithmetic, cross-references, and tie-outs
3. **Internal consistency**: verify figures are consistent across parts (revenue in Part I = Part VIII; expenses in Part I = Part IX; balance sheet in Part I = Part X)
4. **Compliance checks**: evaluate against IRS requirements using the checklist in `references/compliance-review-checklist.md`
5. **Prior year comparison**: if prior year 990 is available, compare key figures and flag material changes (>10% or >$25K) that lack explanation
6. **Governance review**: assess Part VI responses against best practices
7. **Public support test**: verify Schedule A calculations and assess whether the organization passes or is at risk of failing

### Risk Classification

Classify each finding by severity:

| Severity | Definition | Examples |
|---|---|---|
| Critical | Could trigger IRS examination, loss of exemption, or penalties | Math errors on face of return, missing required schedules, unreported compensation, private inurement indicators |
| High | Significant compliance gap or material misstatement | Incorrect revenue classification, failed public support test without explanation, missing governance policies |
| Medium | Best practice gap or minor error | Incomplete program descriptions, suboptimal functional expense allocation, missing Schedule O explanations |
| Low | Cosmetic or informational | Formatting inconsistencies, optional disclosures not made, rounding differences |

### Common Review Findings

Prioritize checking these high-frequency errors:

- Part I summary line totals do not match detail parts (VIII, IX, X)
- Part IX columns do not sum to total column (column A != B + C + D)
- Part VII compensation does not reconcile with Part IX Line 5-10 totals
- Part X beginning-of-year does not match prior year end-of-year
- Schedule A public support percentage is declining toward the 33.33% threshold
- Part VI governance questions answered "No" without Schedule O explanation
- Part III program descriptions lack quantitative outcomes
- Schedule B contributor threshold applied incorrectly
- Foreign activities exist but Schedule F not filed

### Deliverable

Generate a review report following `examples/review-report-template.md`:
- Executive summary with overall risk assessment
- Findings table: severity, form location, description, recommended action
- Cross-reference verification matrix
- Public support test analysis (if Schedule A data available)

Output as a Markdown file or DOCX (per user preference).

---

<a id="quick-reference"></a>
## Quick Reference Mode

For targeted questions about specific lines, deadlines, or requirements:

1. Identify the Part/Schedule/Line in question
2. Load the relevant reference file (`references/core-form-guide.md` or `references/schedules-guide.md`)
3. Provide the answer with the specific IRS instruction citation
4. Note any judgment calls or areas where CPA consultation is recommended

### Key Deadlines

- Filing deadline: 15th day of 5th month after fiscal year end (May 15 for calendar year filers)
- Extension: Form 8868 for automatic 6-month extension (November 15 for calendar year)
- Penalty for late filing: $20/day (up to lesser of $10,500 or 5% of gross receipts) for orgs with gross receipts < $1,081,000
- Three consecutive years of non-filing: automatic revocation of tax-exempt status (IRC 6033(j))
- Public disclosure: completed 990 must be made available for public inspection (and posted online by many states)

### Filing Thresholds (as of 2025 tax year)

| Gross Receipts | Total Assets | Required Form |
|---|---|---|
| <= $50,000 | Any | 990-N (e-Postcard) |
| < $200,000 | < $500,000 | 990-EZ (or full 990) |
| >= $200,000 | Any | Full 990 |
| Any | >= $500,000 | Full 990 |

Note: this skill covers Full Form 990 only. Redirect to appropriate resources for 990-EZ or 990-N questions.

## Output Standards

- Financial figures: whole dollars, no cents, comma-separated thousands
- All XLSX outputs: proper Excel Tables with TableStyleInfo, Aptos 11pt font
- Narrative content: factual, third-person, no promotional language
- Review reports: structured by severity, actionable recommendations
- Citations: reference specific IRS instruction sections (e.g., "2025 Instructions for Form 990, Part VIII, Line 1")
- Disclaimers: include standard disclaimer that output does not constitute tax advice and should be reviewed by a qualified CPA
