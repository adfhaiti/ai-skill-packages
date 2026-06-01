# Core Form Guide: Parts I through XII

Line-by-line guidance for the 12 parts of IRS Form 990. Each section identifies the data source, common errors, and cross-references to other parts.

## Table of Contents

- [Part I: Summary](#part-i)
- [Part II: Signature Block](#part-ii)
- [Part III: Statement of Program Service Accomplishments](#part-iii)
- [Part IV: Checklist of Required Schedules](#part-iv)
- [Part V: Statements Regarding Other IRS Filings and Tax Compliance](#part-v)
- [Part VI: Governance, Management, and Disclosure](#part-vi)
- [Part VII: Compensation](#part-vii)
- [Part VIII: Statement of Revenue](#part-viii)
- [Part IX: Statement of Functional Expenses](#part-ix)
- [Part X: Balance Sheet](#part-x)
- [Part XI: Reconciliation of Net Assets](#part-xi)
- [Part XII: Financial Statements and Reporting](#part-xii)

---

<a id="part-i"></a>
## Part I: Summary (Page 1)

This is the "face" of the return. All figures here are pulled from later parts; never enter Part I figures independently.

### Header Information

| Field | Source | Notes |
|---|---|---|
| Organization name | IRS determination letter / state registration | Must match EIN records exactly |
| Doing business as | State DBA filing | Only if different from legal name |
| Address | Current principal office | PO Box acceptable; use street address if available |
| EIN | IRS determination letter | 9-digit format: XX-XXXXXXX |
| Telephone | Organization main line | |
| Gross receipts (Line 6) | Calculated | Sum of Part VIII columns (A) lines 1-11 |
| Group return (Line H) | IRS group exemption letter | Most standalone orgs: No |
| Tax-exempt status (Line I) | Determination letter | Check 501(c)(3) box |
| Website (Line J) | Current URL | |
| Form of organization (Line K) | Articles of incorporation | Corporation, Trust, Association, or Other |
| Year of formation (Line L) | Articles of incorporation | |
| State of legal domicile (Line M) | State of incorporation | |

### Summary Financial Lines

| Line | Description | Source | Cross-Reference |
|---|---|---|---|
| 1 | Mission or significant activities | Part III | Brief version; full detail in Part III |
| 2 | Check if Schedule O has supplemental info | | Always Yes for full 990 filers |
| 3 | Number of voting board members | Part VI Line 1a | |
| 4 | Number of independent voting members | Part VI Line 1b | |
| 5 | Total employees | Part V Line 2a | W-3 total |
| 6 | Total volunteers (estimate) | Organization records | Reasonable estimate acceptable |
| 7a | Unrelated business gross income | Form 990-T | $0 if no UBI |
| 7b | Net unrelated business taxable income | Form 990-T | |
| 8 | Contributions and grants | Part VIII Line 1h | |
| 9 | Program service revenue | Part VIII Line 2g | |
| 10 | Investment income | Part VIII Line 3+4+5+6+7 | |
| 11 | Other revenue | Part VIII Lines 8-11 | |
| 12 | Total revenue | Part VIII Line 12 Col(A) | Lines 8+9+10+11 |
| 13 | Grants and similar amounts paid | Part IX Line 1-3 Col(A) | |
| 14 | Benefits paid to members | Part IX Line 4 Col(A) | Usually $0 for 501(c)(3) |
| 15 | Salaries/compensation | Part IX Lines 5-10 Col(A) | |
| 16 | Professional fundraising fees | Part IX Line 11e Col(A) | |
| 17 | Other expenses | Part IX Line 24e minus (13+14+15+16) | Calculated |
| 18 | Total expenses | Part IX Line 25 Col(A) | Lines 13-17 |
| 19 | Revenue less expenses | | Line 12 minus Line 18 |
| 20 | Total assets (EOY) | Part X Line 16 Col(B) | |
| 21 | Total liabilities (EOY) | Part X Line 26 Col(B) | |
| 22 | Net assets (EOY) | Part X Line 32 Col(B) | Line 20 minus Line 21 |

**Common errors:**
- Part I totals do not match detail parts (most frequent 990 error)
- Gross receipts (Line 6) includes items not in total revenue (e.g., gross investment gains before netting)
- Mission statement on Line 1 differs from Part III mission

---

<a id="part-ii"></a>
## Part II: Signature Block

Signed by officer authorized by the governing body. Paid preparer must also sign with PTIN. Electronic filing requires the officer's PIN or e-signature.

Note: Form 990 must be filed electronically for tax years beginning after July 1, 2019 (all current filers).

---

<a id="part-iii"></a>
## Part III: Statement of Program Service Accomplishments (Page 2)

### Line 1: Mission Statement

State the organization's mission as described in the articles of incorporation or bylaws. This should match the exempt purpose in the IRS determination letter. Keep to 2-3 sentences.

### Line 2: New Programs

Answer Yes if any new significant programs were started during the tax year. Describe on Schedule O.

### Line 3: Ceased Programs

Answer Yes if any significant programs ceased during the tax year. Describe on Schedule O.

### Line 4a-4d: Program Service Accomplishments

Report the three largest programs by expense. For each:

| Field | Guidance |
|---|---|
| Code | NTEE code if applicable |
| Expenses | Total direct + allocated expenses for this program |
| Grants included | Dollar amount of grants made as part of this program |
| Revenue | Program service revenue directly attributable to this program |
| Description | 150-250 word factual description with quantitative outcomes |

**Narrative quality standards:**
- Lead with outcomes: "Provided clean water access to 3,200 households" not "Operated a water program"
- Include: number of beneficiaries, geographic scope, measurable results
- Avoid: promotional language, future plans (report what happened this year)
- If program crosses fiscal years, report only the current year's activity and expense

Use Schedule O (Line 4e) for additional programs beyond the top three.

---

<a id="part-iv"></a>
## Part IV: Checklist of Required Schedules (Pages 3-4)

38 yes/no questions determine which schedules must be attached. Answer each question based on the organization's activities during the tax year.

### High-Frequency Triggers for Small 501(c)(3) Public Charities

| Question | Schedule Triggered | Typical Answer for Small Org |
|---|---|---|
| 1: Described in 501(c)(3) or 4947(a)(1)? | Schedule A | Yes (always) |
| 2: Required to complete Schedule B? | Schedule B | Yes if any contributor > $5K |
| 3: Political campaign activities? | Schedule C | Usually No |
| 4: Lobbying activities? | Schedule C | Usually No (unless > $0 lobbying) |
| 6: Maintained donor-advised funds? | Schedule D Part I | Usually No |
| 11: Report on Part X amounts held in escrow? | Schedule D Part IV | Depends |
| 12: Report on Part X endowment funds? | Schedule D Part V | If endowment exists |
| 14a: Provided grants > $5K to organizations? | Schedule I | If applicable |
| 14b: Provided grants > $5K to individuals? | Schedule I | If applicable |
| 15: Professional fundraising services? | Schedule G Part I | If used professional fundraisers |
| 16: Activities outside the US? | Schedule F | Yes for international orgs |
| 17: Report on Schedule F aggregate amounts > $15K? | Schedule F | Yes if foreign grants/activities |
| 25: Excess benefit transaction? | Schedule L | Should be No |
| 26: Loan to/from officer/director? | Schedule L | Should be No |
| 28a-c: Officers/directors with business relationships? | Schedule L | Disclose if applicable |
| 33: Operated a hospital? | Schedule H | No (most orgs) |
| 34: Related organizations? | Schedule R | If applicable |

**Common error:** answering "No" to a question that should be "Yes." The IRS cross-checks Part IV answers against the financial data in Parts VIII-X. Inconsistencies trigger examination.

---

<a id="part-v"></a>
## Part V: Statements Regarding Other IRS Filings and Tax Compliance (Pages 4-5)

### Key Lines

| Line | What It Asks | Data Source |
|---|---|---|
| 1a | Number of W-2s filed | Payroll records / W-3 |
| 1b | Number of 1099-MISCs/1099-NECs filed | AP records; any independent contractor paid >= $600 |
| 2a | Total employees from W-3 | W-3 transmittal |
| 2b | Employment tax returns filed? | Must be Yes if Line 2a > 0 |
| 3a-b | Unrelated business gross income > $1,000? | Form 990-T |
| 4a | Tax on prohibited political expenditures? | Usually No |
| 5a-c | Taxes on excess benefit transactions? | Usually No; Yes is a serious flag |
| 7a-h | Various state/federal filing compliance | Varies by org |
| 13 | Section 4947(a)(1) charitable trust? | Usually No for incorporated nonprofits |

**Common errors:**
- 1099 count is wrong (forgot contractors, or filed 1099-MISC when 1099-NEC was required)
- Line 2a employee count does not match W-3
- Line 2b answered "No" when employees exist

---

<a id="part-vi"></a>
## Part VI: Governance, Management, and Disclosure (Pages 5-6)

### Section A: Governing Body and Management

| Line | Question | Best Practice Answer |
|---|---|---|
| 1a | Number of voting board members | Report actual number at end of year |
| 1b | Number of independent voting members | Per IRC: not compensated, no family/business relationship with officers |
| 2 | Officer/director with family/business relationship? | Disclose on Schedule O if Yes |
| 3 | Management delegation to outside entity? | No (if Yes, explain on Schedule O) |
| 4 | Material changes to governing documents? | If Yes, describe on Schedule O |
| 5 | Material diversion of assets? | MUST be No; Yes triggers serious compliance review |
| 6 | Members or stockholders? | Depends on articles of incorporation |
| 7a-b | Decisions reserved to members? | If membership org |

### Section B: Policies

| Line | Policy | Best Practice |
|---|---|---|
| 10a | Local chapters/affiliates? | |
| 11a | Provided Form 990 to board before filing? | Yes (governance best practice) |
| 12a | Conflict of interest policy? | Yes |
| 12b | Officers/directors required to disclose conflicts? | Yes |
| 12c | Monitored and enforced COI policy? | Yes (explain process on Schedule O) |
| 13 | Whistleblower policy? | Yes (recommended) |
| 14 | Document retention/destruction policy? | Yes (recommended) |
| 15a | Compensation review process for CEO/top officer? | Yes (describe on Schedule O) |
| 15b | Compensation review process for other officers? | Yes |

**Every "No" in Section B that should be "Yes" represents a governance gap.** For any "No" answer to 11a, 12a, 13, or 14, strongly recommend the organization adopt the policy before next filing.

### Section C: Disclosure

| Line | Requirement |
|---|---|
| 18 | Provide Schedule B, Schedule R, and other docs for public inspection |
| 19 | Where is Form 990 available? (Own website, another website, upon request, other) |
| 20 | State(s) where copy of return is filed | List all states where registered |

---

<a id="part-vii"></a>
## Part VII: Compensation (Pages 7-8)

### Section A: Officers, Directors, Trustees, Key Employees, Highest Compensated Employees

Report all individuals who are:
- Current officers, directors, trustees, key employees (regardless of compensation)
- Former officers, directors, trustees, key employees who received > $100K in reportable compensation
- Highest compensated employees (non-officer/director) who received > $100K
- Former highest compensated employees who received > $100K

### Columns

| Column | Source | Notes |
|---|---|---|
| (A) Name and title | Board records, payroll | |
| (B) Average hours/week | Time records or allocation | Include hours for related orgs |
| (C) Position checkboxes | Org chart | Individual trustee, institutional trustee, officer, key employee, highest compensated, former |
| (D) Reportable compensation from org | W-2 Box 1 or 1099-NEC Box 1 | |
| (E) Reportable compensation from related orgs | Related org payroll | |
| (F) Estimated amount of other compensation | Benefits: health, retirement, housing, etc. | Excludes benefits available to all employees |

### Section B: Independent Contractors

Report the 5 highest compensated independent contractors who received > $100K. Include name, business address, description of services, and compensation.

**Common errors:**
- Omitting board members who receive $0 compensation (all must be listed)
- Hours reported as 0 for board members (report actual hours, including preparation time)
- Reportable compensation does not match W-2s
- Key employee threshold: anyone with significant influence over the org, regardless of title

---

<a id="part-viii"></a>
## Part VIII: Statement of Revenue (Page 9)

Revenue is classified into four columns:

| Column | Description |
|---|---|
| (A) Total revenue | All revenue regardless of source |
| (B) Related or exempt function revenue | Revenue from activities related to exempt purpose |
| (C) Unrelated business revenue | Revenue from unrelated trade or business |
| (D) Revenue excluded by 512, 513, 514 | Tax-excluded revenue (e.g., interest on state bonds) |

### Key Lines

| Line | Category | Data Source | Notes |
|---|---|---|---|
| 1a-f | Federated campaigns, membership dues, fundraising events, related orgs, government grants, all other contributions | Donor records, grant agreements | Contributions go in Col(A) only |
| 1g | Noncash contributions | Donation records | Also reported on Schedule M if > $25K total |
| 1h | Total contributions | Sum of 1a-1f | |
| 2a-f | Program service revenue | Revenue by program line | Classify each line into Col(B), (C), or (D) |
| 2g | Total program service revenue | | |
| 3 | Investment income (interest, dividends) | Bank/brokerage statements | Usually Col(A) and (D) |
| 4 | Income from investment of tax-exempt bond proceeds | | Usually $0 for small orgs |
| 5 | Royalties | Licensing agreements | |
| 6a-d | Rental income | Lease agreements | Gross rents, less expenses |
| 7a-d | Net gain/loss on sale of assets | Brokerage statements | Also Schedule D Part VII/VIII |
| 8a-c | Fundraising events | Event records | Gross income, direct expenses, net |
| 9a-b | Gaming | | Usually $0 |
| 10a-b | Gross sales of inventory | | |
| 11a-e | Other revenue | Miscellaneous | |
| 12 | Total revenue | Sum of all lines | Col(A) must = sum of (B)+(C)+(D) + contributions |

**Common errors:**
- Government grants classified as program service revenue instead of contributions (Line 1e vs 2)
- Contract revenue from fee-for-service work not properly classified in Column B vs C
- Noncash contributions on Line 1g not reconciled with Schedule M
- Fundraising event gross/net confusion

**Revenue classification for earned-income nonprofits:** Fee-for-service revenue that is substantially related to the exempt purpose belongs in Column (B). Revenue from activities not substantially related to the exempt purpose belongs in Column (C) and may require Form 990-T. The "substantially related" test asks whether the activity contributes importantly to the organization's exempt purpose, considering the relationship between the business activity and the exempt purpose, not just the use of the income.

**Government grants vs. contracts distinction:** This classification directly affects the public support test on Schedule A. A government grant (contribution, Line 1e) provides funds to support the mission with discretion over use; a government contract (program service revenue, Line 2) purchases specific deliverables. Characteristics of a contract: fixed deliverable requirements, specific performance standards, government retains ownership of work product, payment contingent on delivery. Characteristics of a grant: broad purpose, organizational discretion, reporting requirements but not performance-based payments. See `references/gaap-vs-irs-differences.md` for detailed classification rules.

**Donated services vs. in-kind property:** Donated services (volunteer labor, even specialized) may NOT be reported as revenue on Part VIII. In-kind donations of tangible property (supplies, equipment, food) ARE reported on Line 1g at fair market value. This is one of the most significant differences between GAAP financial statements and the 990. See `references/gaap-vs-irs-differences.md` for the full GAAP reconciliation framework.

**Membership dues split:** When membership includes both a contribution element and a purchased-benefit element (magazine subscription, event admission, merchandise), the exchange portion goes on Line 2 and only the excess (contribution portion) goes on Line 1.

---

<a id="part-ix"></a>
## Part IX: Statement of Functional Expenses (Page 10)

The most complex part. All expenses must be allocated across three functions and reported by 24 natural categories. See `references/functional-expense-guide.md` for detailed allocation methodology.

### Columns

| Column | Function | Definition |
|---|---|---|
| (A) Total | All expenses | Must equal P&L total expenses |
| (B) Program services | Exempt purpose activities | Direct program costs + allocated overhead |
| (C) Management and general | Administrative overhead | Finance, HR, governance, compliance |
| (D) Fundraising | Resource development | Direct fundraising costs + allocated overhead |

Column (A) must equal (B) + (C) + (D) for every line.

### Natural Expense Categories (Lines 1-24)

| Line | Category | Typical Source |
|---|---|---|
| 1 | Grants to domestic organizations | Grant records |
| 2 | Grants to domestic individuals | Grant records |
| 3 | Grants to foreign organizations/individuals | Grant records |
| 4 | Benefits paid to members | Usually $0 for 501(c)(3) |
| 5 | Compensation of current officers/directors/trustees/key employees | Payroll (must match Part VII) |
| 6 | Compensation not included in Line 5 | Payroll for other employees |
| 7 | Other salaries and wages | Additional compensation |
| 8 | Pension plan accruals and contributions | 401k/pension records |
| 9 | Other employee benefits | Health insurance, etc. |
| 10 | Payroll taxes | 941 filings |
| 11a-g | Fees for services (accounting, legal, lobbying, professional fundraising, investment management, other) | AP records |
| 12 | Advertising and promotion | AP records |
| 13 | Office expenses | AP records |
| 14 | Information technology | AP records |
| 15 | Royalties | AP records |
| 16 | Occupancy | Rent, utilities, property tax |
| 17 | Travel | AP records |
| 18 | Payments to affiliates | Affiliate agreements |
| 19 | Conferences/conventions/meetings | AP records |
| 20 | Interest | Loan statements |
| 21 | Payments to affiliates | |
| 22 | Depreciation, depletion, amortization | Depreciation schedule |
| 23 | Insurance | Insurance policies |
| 24a-e | Other expenses | Remaining categories |
| 25 | Total functional expenses | Sum Lines 1-24 |
| 26 | Joint costs (ASC 958-720) | Only if joint cost allocation applies |

**Cross-reference checks:**
- Line 5 Col(A) must be consistent with Part VII Section A total compensation
- Line 25 Col(A) must equal Part I Line 18
- Lines 11a (management fees) and 11e (professional fundraising fees) trigger Schedule G Part I if amounts are significant
- Line 3 (foreign grants) must be consistent with Schedule F amounts

---

<a id="part-x"></a>
## Part X: Balance Sheet (Page 11)

Two columns: beginning of year (BOY) and end of year (EOY). BOY must match prior year EOY exactly.

### Key Lines

| Line | Category | Data Source |
|---|---|---|
| 1 | Cash (non-interest-bearing) | Bank statements |
| 2 | Savings and temporary cash investments | Bank/investment statements |
| 3 | Pledges and grants receivable | AR aging |
| 4 | Accounts receivable | AR aging |
| 5 | Loans to officers/directors/trustees | Should be $0 (red flag if not) |
| 6 | Loans to other disqualified persons | Should be $0 |
| 7 | Notes and loans receivable | Loan documentation |
| 8 | Inventories | Inventory records |
| 9 | Prepaid expenses and deferred charges | GL |
| 10a-c | Land, buildings, equipment (net) | Fixed asset schedule + depreciation |
| 11 | Investments (publicly traded securities) | Brokerage statements |
| 12 | Investments (other securities) | Valuation records |
| 13 | Investments (program-related) | PRI documentation |
| 14 | Intangible assets | GL |
| 15 | Other assets | GL + Schedule D Part IX |
| 16 | Total assets | Sum Lines 1-15 |
| 17 | Accounts payable and accrued expenses | AP aging |
| 18 | Grants payable | Grant agreements |
| 19 | Deferred revenue | Advance payment records |
| 20 | Tax-exempt bond liabilities | Bond documents |
| 21 | Escrow or custodial account liability | Schedule D Part IV |
| 22 | Loans from officers/directors | Should be $0 (red flag) |
| 23 | Secured mortgages/notes payable | Loan documentation |
| 24 | Unsecured notes/loans payable | Loan documentation |
| 25 | Other liabilities | GL + Schedule D Part X |
| 26 | Total liabilities | Sum Lines 17-25 |
| 27 | Net assets without donor restrictions | GL |
| 28 | Net assets with donor restrictions | GL |
| 29 | Retained earnings (only for certain orgs) | Usually $0 for 501(c)(3) |
| 32 | Total net assets or fund balances | Line 27 + 28 (+ 29 if applicable) |
| 33 | Total liabilities and net assets | Line 26 + 32; MUST equal Line 16 |

**Common errors:**
- BOY does not match prior year EOY (data entry error or restatement without explanation)
- Lines 5-6 (loans to officers/disqualified persons) show a balance without Schedule L
- Land/buildings on Line 10 not reported net of accumulated depreciation
- Total assets (Line 16) does not equal total liabilities + net assets (Line 33)
- Net assets with/without donor restrictions split does not match audited financials

---

<a id="part-xi"></a>
## Part XI: Reconciliation of Net Assets (Page 12)

This part reconciles beginning and ending net assets. It must work as a mathematical identity.

| Line | Description | Source |
|---|---|---|
| 1 | Total revenue | Part I Line 12 |
| 2 | Total expenses | Part I Line 18 |
| 3 | Revenue less expenses | Line 1 minus Line 2 |
| 4 | Net assets BOY | Part X Line 32 Col(A) |
| 5 | Net unrealized gains/losses on investments | Investment statements |
| 6 | Donated services and use of facilities | Only if recorded per ASC 958 |
| 7 | Investment expenses | |
| 8 | Prior period adjustments | Should be rare |
| 9 | Other changes in net assets | Explain on Schedule O |
| 10 | Net assets EOY | Must equal Part X Line 32 Col(B) |

**Identity check:** Line 10 = Line 3 + Line 4 + Lines 5 through 9

If this does not balance, there is an error somewhere in the return.

---

<a id="part-xii"></a>
## Part XII: Financial Statements and Reporting (Page 12)

| Line | Question | Notes |
|---|---|---|
| 1 | Accounting method | Cash, accrual, or other |
| 2a | Were financial statements compiled, reviewed, or audited? | Depends on state/funder requirements |
| 2b | If yes, by independent accountant? | Should be Yes |
| 2c | Audit committee or oversight? | Best practice: Yes |
| 3a | Federal audit required? (Single Audit per 2 CFR 200) | Yes if >= $750K in federal expenditures |
| 3b | If yes, was audit performed? | Must be Yes if 3a is Yes |
| 4a | Change in accounting method? | |

**Single Audit threshold:** organizations expending $750,000 or more of federal awards in a fiscal year must have a Single Audit performed per 2 CFR 200 (Uniform Guidance). This is separate from the financial statement audit.
