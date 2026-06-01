# Compliance Review Checklist

Systematic review checklist for evaluating a completed Form 990 for errors, inconsistencies, and compliance risks. Organized by risk area, from highest to lowest priority.

## How to Use This Checklist

1. Work through each section in order (highest risk first)
2. For each check, record: Pass / Fail / N/A
3. For each Fail, classify severity (Critical / High / Medium / Low)
4. Document the specific finding and recommended corrective action
5. Compile findings into the review report template

---

## Section 1: Mathematical Verification (Critical Priority)

These are objective, binary checks. Any failure here indicates a definitive error.

### Cross-Reference Tie-Outs

| Check ID | Description | How to Verify |
|---|---|---|
| M-01 | Part I Line 8 = Part VIII Line 1h Col(A) | Compare directly |
| M-02 | Part I Line 9 = Part VIII Line 2g Col(A) | Compare directly |
| M-03 | Part I Line 12 = Part VIII Line 12 Col(A) | Compare directly |
| M-04 | Part I Line 18 = Part IX Line 25 Col(A) | Compare directly |
| M-05 | Part I Line 19 = Part I (Line 12 minus Line 18) | Calculate |
| M-06 | Part I Line 20 = Part X Line 16 Col(B) | Compare directly |
| M-07 | Part I Line 21 = Part X Line 26 Col(B) | Compare directly |
| M-08 | Part I Line 22 = Part X Line 32 Col(B) | Compare directly |
| M-09 | Part VIII Col(A) = Col(B) + Col(C) + Col(D) for each line | Verify all lines |
| M-10 | Part IX Col(A) = Col(B) + Col(C) + Col(D) for each line | Verify all lines |
| M-11 | Part X Line 16 = Sum of Lines 1-15 (both columns) | Calculate |
| M-12 | Part X Line 26 = Sum of Lines 17-25 (both columns) | Calculate |
| M-13 | Part X Line 33 = Line 26 + Line 32 (both columns) | Calculate |
| M-14 | Part X Line 33 = Line 16 (both columns) | Assets = Liabilities + Net Assets |
| M-15 | Part XI reconciliation: Line 10 = Line 3 + Line 4 + Lines 5-9 | Calculate |
| M-16 | Part XI Line 10 = Part X Line 32 Col(B) | Compare directly |
| M-17 | Part XI Line 4 = Part X Line 32 Col(A) | Compare directly |

### Internal Arithmetic

| Check ID | Description |
|---|---|
| M-18 | Part VIII Line 1h = sum of Lines 1a through 1f |
| M-19 | Part VIII Line 12 = sum of all revenue lines |
| M-20 | Part IX Line 25 = sum of Lines 1-24 (all columns) |
| M-21 | Part VII Section A total compensation reconciles with Part IX Lines 5-10 |

---

## Section 2: Prior Year Consistency (High Priority)

### Year-Over-Year Checks

| Check ID | Description | Threshold for Flagging |
|---|---|---|
| Y-01 | Part X Col(A) BOY = prior year Part X Col(B) EOY | Must match exactly |
| Y-02 | Total revenue change from prior year | Flag if change > 25% without explanation |
| Y-03 | Total expense change from prior year | Flag if change > 25% without explanation |
| Y-04 | Net assets change from prior year | Flag if change > 25% without explanation |
| Y-05 | Number of board members changed | Flag if material change |
| Y-06 | Number of employees changed | Flag if material change |
| Y-07 | Functional expense ratios changed significantly | Flag if program % changed > 5 points |
| Y-08 | Public support percentage (Schedule A) trending | Flag if declining toward 33.33% threshold |
| Y-09 | New schedules filed vs. prior year | Verify new schedule triggers are real |
| Y-10 | Programs listed in Part III match prior year | Flag any unexplained additions/removals |

---

## Section 3: Revenue Classification (High Priority)

| Check ID | Description | Risk if Wrong |
|---|---|---|
| R-01 | Government grants on Line 1e vs. program service revenue on Line 2 | Misclassification affects public support test |
| R-02 | Fee-for-service revenue properly classified as related (Col B) vs. unrelated (Col C) | UBI exposure if Col C understated |
| R-03 | Investment income in correct column (usually D) | |
| R-04 | Noncash contributions (Line 1g) consistent with Schedule M totals | Math error |
| R-05 | Fundraising event net income correctly calculated (Line 8c = 8a - 8b) | |
| R-06 | Gross receipts on Page 1 include all revenue items per instructions | Gross receipts != total revenue |
| R-07 | Any unrelated business income > $1,000 reported; Form 990-T filed | Penalty exposure |
| R-08 | Membership dues properly split between contributions and program revenue | Affects public support test |

---

## Section 4: Expense Allocation (High Priority)

| Check ID | Description | Risk if Wrong |
|---|---|---|
| E-01 | Functional expense ratios are reasonable for org type | Program typically 65-85% for service orgs |
| E-02 | Management/general allocation basis is documented and reasonable | IRS scrutiny if M&G > 25% |
| E-03 | Fundraising allocation basis is documented and reasonable | Must include ALL fundraising costs |
| E-04 | Officer compensation (Line 5) allocated across functions | Cannot be 100% to one function |
| E-05 | Depreciation (Line 22) allocated consistently with asset use | |
| E-06 | Joint cost allocation (Line 26) meets ASC 958-720 three-test criteria | Purpose, audience, content tests |
| E-07 | Rent/occupancy (Line 16) allocated by space usage | |
| E-08 | Travel (Line 17) allocated by purpose of trip | |
| E-09 | No expense categories appear in wrong natural category | Common: IT in office expenses, insurance in other |
| E-10 | Total expenses reconcile to audited financial statements | If audit available |

---

## Section 5: Governance and Compliance (Medium Priority)

| Check ID | Description | Best Practice |
|---|---|---|
| G-01 | Part VI Line 3: management not delegated to outside entity | If Yes, requires explanation |
| G-02 | Part VI Line 5: no material diversion of assets | MUST be No |
| G-03 | Part VI Line 11a: Form 990 provided to board before filing | Should be Yes |
| G-04 | Part VI Line 12a: conflict of interest policy exists | Should be Yes |
| G-05 | Part VI Line 12b: annual COI disclosures obtained | Should be Yes |
| G-06 | Part VI Line 12c: COI policy monitored and enforced | Should be Yes; explain on Schedule O |
| G-07 | Part VI Line 13: whistleblower policy | Should be Yes |
| G-08 | Part VI Line 14: document retention policy | Should be Yes |
| G-09 | Part VI Line 15: compensation review process documented | Should be Yes; explain on Schedule O |
| G-10 | Part V Line 2b: employment tax returns filed (if employees exist) | Must be Yes |
| G-11 | Part V Lines 1a-b: W-2 and 1099 counts reasonable for org size | Cross-check with employee/contractor count |
| G-12 | Part VII: all board members listed (even zero compensation) | Must list all |
| G-13 | Part VII: hours reported for all individuals | Cannot be zero for active directors |

---

## Section 6: Schedule-Specific Checks (Medium Priority)

### Schedule A: Public Support Test

| Check ID | Description |
|---|---|
| SA-01 | Correct public charity classification checked (matches determination letter) |
| SA-02 | 5-year support schedule uses correct years |
| SA-03 | Gross receipts cap applied correctly (greater of $5K or 1% per source) |
| SA-04 | Public support percentage calculated correctly |
| SA-05 | Percentage is above 33.33% (or 10% with facts-and-circumstances) |
| SA-06 | If percentage declining, trend analysis performed and documented |

### Schedule B: Contributors

| Check ID | Description |
|---|---|
| SB-01 | All contributors exceeding threshold are listed |
| SB-02 | Contributions from same donor aggregated (not listed separately) |
| SB-03 | Government grants included as contributions (if classified as such on Part VIII) |

### Schedule D: Supplemental Financial Statements

| Check ID | Description |
|---|---|
| SD-01 | Parts XI-XII reconciliation balances |
| SD-02 | Endowment fund (Part V) spending policy described |
| SD-03 | Other assets/liabilities adequately described |

### Schedule F: Foreign Activities

| Check ID | Description |
|---|---|
| SF-01 | All countries of operation listed |
| SF-02 | Foreign grant amounts reconcile with Part IX Line 3 |
| SF-03 | Number of foreign employees/agents consistent with organization records |
| SF-04 | Foreign financial accounts disclosed on Part IV |
| SF-05 | FBAR filing status addressed |

### Schedule O: Supplemental Information

| Check ID | Description |
|---|---|
| SO-01 | All required governance explanations present (Part VI Lines 2, 6, 11a, 12c, 15a-b, 19) |
| SO-02 | Explanations reference specific Part/Line numbers |
| SO-03 | Narratives are factual, specific, and complete |
| SO-04 | Any "Yes" answers in Part IV that require narrative are addressed |

---

## Section 7: Red Flag Indicators (High Priority)

These patterns do not necessarily indicate errors but warrant additional scrutiny:

| Check ID | Pattern | Concern |
|---|---|---|
| RF-01 | Net assets declining for 3+ consecutive years | Financial sustainability |
| RF-02 | Program expense ratio below 65% | IRS benchmark for charitable orgs |
| RF-03 | Fundraising costs exceed fundraising revenue | Fundraising efficiency concern |
| RF-04 | Executive compensation > 15% of total expenses | Reasonableness question |
| RF-05 | Loans to officers/directors (Part X Lines 5-6) | Private benefit/inurement |
| RF-06 | Related party transactions (Part IV Lines 25-28) | Conflict of interest |
| RF-07 | Excess benefit transaction (Part V Line 5a) | IRC 4958 violation |
| RF-08 | Unrelated business income growing year over year | May threaten exempt status if substantial |
| RF-09 | Significant in-kind/noncash contributions without Schedule M | Valuation risk |
| RF-10 | Multiple governance policies missing (Part VI Section B) | Governance weakness |
| RF-11 | Board has < 3 independent members | Governance weakness |
| RF-12 | Single individual controls both program and finances | Lack of segregation of duties |

---

## Review Report Structure

After completing all applicable checks, compile findings using this structure:

1. **Executive Summary**: overall risk level (Low / Moderate / High / Critical), number of findings by severity, top 3 findings requiring immediate attention
2. **Mathematical Verification**: pass/fail status for all M-series checks
3. **Prior Year Comparison**: significant variances with explanations (if available)
4. **Findings Detail**: table with Check ID, Severity, Description, Location (Part/Line), Recommended Action
5. **Public Support Test Analysis**: current percentage, trend, risk of falling below threshold
6. **Governance Assessment**: policy gaps and recommendations
7. **Disclaimer**: standard language that review does not constitute an audit or legal/tax advice
