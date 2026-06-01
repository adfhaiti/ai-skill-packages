# Schedules Guide: Schedules A through R

Reference for all 16 Form 990 schedules. Each entry covers: trigger conditions, key fields, 501(c)(3)-specific guidance, and common errors. Schedules are listed in filing frequency order for small public charities.

## Table of Contents

- [Always Required](#always-required): Schedule A, Schedule O
- [Frequently Required](#frequently-required): Schedule B, Schedule D, Schedule F
- [Conditionally Required](#conditionally-required): Schedule C, Schedule G, Schedule I, Schedule J, Schedule K, Schedule L, Schedule M, Schedule N, Schedule R
- [Rarely Required for Small 501(c)(3)s](#rarely-required): Schedule E, Schedule H

---

<a id="always-required"></a>
## Always Required

### Schedule A: Public Charity Status and Public Support

**Trigger:** Part IV Line 1 (always Yes for 501(c)(3) organizations)

**Purpose:** demonstrate the organization qualifies as a public charity (not a private foundation) by meeting one of the public support tests.

**Part I: Reason for Public Charity Status**

Check ONE box (lines 1-12) matching the determination letter classification. Most common for small orgs:

| Line | Classification | Typical Org |
|---|---|---|
| 7 | 509(a)(1) and 170(b)(1)(A)(vi) | Publicly supported: receives substantial public support from general public/government |
| 9 | 509(a)(2) | Receives support from exempt activities, member dues, and public support |
| 10 | 509(a)(4) testing new org | Public charity in first 5 years (testing postponed until end of 6th year) |

**First 5 Years:** Organizations in their first five tax years of 501(c)(3) exemption are automatically accorded public charity status and are not tested on the support schedule until the end of their sixth year.

**Part II: Support Schedule for 509(a)(1)/170(b)(1)(A)(vi) Organizations**

5-year support schedule comparing public support to total support.

Key line-by-line:
- Line 1: gifts, grants, contributions, membership fees (from all sources)
- Line 2: tax revenues levied for the organization's benefit (include even if not reported as revenue on Part VIII)
- Line 3: value of services/facilities furnished by government units without charge
- Line 5: **2% limitation** (the critical calculation): for each non-government, non-publicly-supported-org contributor, the amount exceeding 2% of 5-year total support (Line 13) is subtracted from public support. This caps the influence of any single large donor.
- Line 6: public support = Lines 1+2+3+4 minus Line 5
- Lines 7-10: non-public-support items (investment income, UBI net income, other income)
- Line 13: total support (denominator)
- Line 14: public support percentage (Line 6 / Line 13)

**Critical note on capital gains:** capital gains are EXCLUDED from both public support tests entirely. They do not appear on any support schedule line.

**2% Limitation Mechanics (Line 5):**
- Applies to contributions from individuals, trusts, and corporations (NOT from governmental units or other publicly supported organizations)
- Related donors must be aggregated per Section 4946(a)(1)(C)-(G): family members (spouse, ancestors, children through great-grandchildren and their spouses), >20% owners of corporations/partnerships/trusts, and >35% controlled entities of any such persons
- Each aggregated donor group's contributions exceeding 2% of 5-year total support are subtracted

**Unusual Grants Exclusion:** Large one-time grants can be excluded from both the numerator and denominator if all of the following factors are present:
1. The grant was attracted by the organization's publicly supported nature
2. The grant is unusual or unexpected in amount
3. The grant is in cash, marketable securities, or exempt-purpose assets
4. No material restrictions imposed by the grantor
5. If for operating expenses, expressly limited to one year
6. The donor has a history (or the organization can demonstrate it will continue to attract broad support)

Apply for an IRS ruling before excluding if the grant is borderline.

**Testing Results (Part II, Section C):**
- >= 33.33% on Line 14: automatic pass; qualifies for current year AND next year
- >= 10% but < 33.33%: may qualify under facts-and-circumstances test (Line 17a/b)
- < 10%: fails; must complete Part III or file as private foundation (Form 990-PF)
- A pass on the prior year's Schedule A covers the current year (Line 16b)

**Facts-and-Circumstances Test (10% minimum):**
If the percentage is at least 10% but below 33.33%, the organization must demonstrate on Schedule A Part VI:
- It maintains a continuous, bona fide program for solicitation from the general public
- The scope of fundraising is reasonable in light of charitable activities
- It is organized and operated to attract new and additional public or governmental support on a continuous basis
- Simply checking the box on Line 17a is NOT sufficient; specific evidence must be provided in Part VI

**Part III: Support Schedule for 509(a)(2) Organizations**

Dual test (BOTH must be met):
1. Public support percentage >= 33.33% (no facts-and-circumstances alternative)
2. Investment + UBI income percentage <= 33.33%

Key differences from Part II:
- Program service revenue IS included in public support (Line 2)
- Revenue from activities excepted from UBI under Section 513 is included (Line 3)
- Disqualified persons (per Section 4946, the private foundation definition) have their contributions/receipts excluded from public support (Line 7a)
- Per-source limitation: for non-disqualified-person payers, amounts from Lines 2-3 exceeding the greater of $5K or 1% of total support are excluded (Line 7b)
- Net losses from UBI must be reported as $0 (cannot offset support)

**Fluidity Between Tests:** An organization that fails Part II may attempt Part III, and vice versa. The regulations permit switching between the two tests each year. Failing both tests requires filing Form 990-PF as a private foundation.

**Common errors:**
- Wrong public charity classification checked (does not match determination letter)
- Support test uses wrong years (should be current + 4 prior years)
- 2% limitation not applied or applied incorrectly (Part II)
- Related donors not aggregated per Section 4946(a)(1)(C)-(G) linking rules
- Capital gains included in support (they should be excluded entirely)
- Net UBI losses entered as negative (must be $0)
- Agency funds excluded from Schedule A Line 1 even though they are excluded from Part VIII revenue (agency funds received from other public charities should be included on Schedule A)
- Organization fails the test but does not disclose or take remedial action
- Government grants classified inconsistently between Part VIII and Schedule A

---

### Schedule O: Supplemental Information to Form 990

**Trigger:** ALWAYS required for full Form 990 filers

**Purpose:** provide supplemental narrative explanations for items referenced throughout the core form.

**Required disclosures (minimum):**

- Part III Line 4 additional program descriptions (if > 3 programs)
- Part VI Line 2 (family/business relationships among officers/directors)
- Part VI Line 6 (members or stockholders)
- Part VI Line 11a (process for reviewing 990 before filing)
- Part VI Line 12c (conflict of interest policy monitoring process)
- Part VI Line 15a-b (compensation setting process)
- Part VI Line 19 (documents available to public)
- Any "Yes" answer in Part IV that requires narrative explanation

**Writing standards:**
- Factual, specific, and concise
- Reference the specific Part/Line being explained
- Include dates, amounts, and names where relevant
- Describe processes, not intentions ("The board reviews compensation annually using comparable data" not "The organization intends to review compensation")

---

<a id="frequently-required"></a>
## Frequently Required

### Schedule B: Schedule of Contributors

**Trigger:** Part IV Line 2 (organization received contributions from any single contributor exceeding the greater of $5,000 or 2% of total contributions on Part VIII Line 1h)

**Important:** Schedule B is NOT required to be made publicly available. Contributor names and addresses are redacted from the public inspection copy.

**Part I: Contributors**

For each contributor meeting the threshold:
- Name, address
- Total contributions during the year
- Type of contribution (person, payroll, noncash)
- Noncash description and FMV if applicable

**Common errors:**
- Forgetting government grant agencies as "contributors" (they count)
- Not aggregating multiple contributions from the same donor
- Treating the $5,000 threshold as per-gift instead of per-donor annual total

---

### Schedule D: Supplemental Financial Statements

**Trigger:** multiple Part IV questions (6, 7, 8, 9, 10, 11, 12)

**Parts most relevant to small 501(c)(3)s:**

| Part | Content | Trigger |
|---|---|---|
| Part V | Endowment Funds | If org has endowment (Part IV Line 10) |
| Part VII | Investments: Other Securities | If Part X Line 12 Col(B) > 0 |
| Part VIII | Investments: Program Related | If Part X Line 13 Col(B) > 0 |
| Part IX | Other Assets | If Part X Line 15 Col(B) > 0 |
| Part X | Other Liabilities | If Part X Line 25 Col(B) > 0 |
| Part XI | Reconciliation of Revenue | |
| Part XII | Reconciliation of Expenses | |
| Part XIII | Supplemental Info on Endowments | If endowment narrative needed |

**Parts XI and XII** reconcile the Form 990 revenue and expense figures to the audited financial statements. Required if the organization's financial statements use a different accounting method or classifications than the 990.

**Common errors:**
- Schedule D Part XI/XII reconciliation does not actually reconcile (math error)
- Endowment fund reported without spending policy description
- Other assets/liabilities listed without adequate description

---

### Schedule F: Statement of Activities Outside the United States

**Trigger:** Part IV Lines 14b, 15, 16, or 17 (foreign activities, employees, grants, accounts)

**Especially relevant for organizations operating in Haiti or other countries.**

**Part I: General Information on Activities Outside the United States**

For each region/country:
- Number of offices
- Number of employees/agents
- Activities conducted (describe using IRS activity codes: program services, grantmaking, fundraising, investments)
- Total expenditures for the region

**Part II: Grants and Other Assistance to Organizations or Entities Outside the United States**

For each foreign grantee:
- Name, IRS/EIN (if any), region
- Purpose of grant
- Amount of cash grant
- Manner of cash disbursement
- Amount of noncash assistance
- Method of valuation
- Description of noncash assistance

**Part III: Grants and Other Assistance to Individuals Outside the United States**

Aggregated by type of assistance and region.

**Part IV: Foreign Forms**

Report if the organization filed Forms 3520, 3520-A, 926, or had foreign financial accounts (FBAR).

**Common errors:**
- Not filing Schedule F when the organization has employees or operations abroad
- Listing grants by individual name when only aggregate reporting is required for individuals (Part III)
- Not reporting foreign bank accounts on Part IV even though FBAR was filed separately

---

<a id="conditionally-required"></a>
## Conditionally Required

### Schedule C: Political Campaign and Lobbying Activities

**Trigger:** Part IV Lines 3 (political campaign) or 4-5 (lobbying)

501(c)(3) organizations are PROHIBITED from engaging in political campaign intervention. Any political activity is a serious compliance issue.

Lobbying is permitted within limits:
- Organizations that filed Form 5768 (501(h) election): use Part II-A expenditure test
- Organizations without 501(h) election: use Part II-B substantial part test

**For most small 501(c)(3)s:** if no lobbying or political activity, Schedule C is not required.

---

### Schedule G: Fundraising and Gaming

**Trigger:** Part IV Lines 17-19

| Part | Trigger | Content |
|---|---|---|
| Part I | Professional fundraising services (Part IV Line 17) | List professional fundraisers, amounts paid, amounts raised |
| Part II | Fundraising events (Part VIII Line 8a gross > $15K) | Report up to 2 largest events: gross receipts, direct expenses, net |
| Part III | Gaming activities | Usually not applicable |

---

### Schedule I: Grants and Other Assistance

**Trigger:** Part IV Lines 21-22 (grants > $5K to domestic organizations or individuals)

**Part II:** each domestic grantee organization receiving > $5K:
- Name, EIN, IRC section
- Amount of cash grant
- Purpose of grant
- Whether grant is part of an ongoing relationship

**Part III:** each type of assistance to domestic individuals:
- Type of grant, number of recipients
- Amount, method of determining recipients
- Description of noncash assistance

---

### Schedule J: Compensation Information

**Trigger:** Part IV Line 23 (any Part VII Section A individual received > $150K from org + related orgs)

Reports detailed breakdown of compensation for highly compensated individuals:
- Base compensation, bonus/incentive, other reportable, retirement/deferred, nontaxable benefits, total
- First-class travel, travel for companions, tax indemnification, discretionary spending, housing allowance, health/social club dues, personal services

**This schedule invites IRS scrutiny on executive compensation reasonableness.** Ensure compensation comparability data and board approval are documented.

---

### Schedule K: Supplemental Information on Tax-Exempt Bonds

**Trigger:** Part IV Line 24a (outstanding tax-exempt bond issues)

Rarely applies to small nonprofits unless the organization has financed a building or facility with tax-exempt bonds.

---

### Schedule L: Transactions with Interested Persons

**Trigger:** Part IV Lines 25-28

Reports four categories of interested person transactions:

**Part I: Excess Benefit Transactions (IRC 4958)**

CRITICAL compliance area. An excess benefit transaction (EBT) occurs when a 501(c)(3) public charity, 501(c)(4), or 501(c)(29) organization provides an economic benefit to a disqualified person that exceeds the value of consideration received.

Disqualified persons (DPs) under Section 4958 include:
- 1st degree: any person in a position of substantial influence over the organization at any time during the 5-year period ending on the transaction date. Automatically includes: voting board members, Presidents/CEOs/COOs, Treasurers/CFOs
- 2nd degree: family members of 1st-degree DPs (spouse, ancestors, children through great-grandchildren and their spouses)
- 3rd degree: 35%-controlled entities (corporations, partnerships, trusts) of any DP

Excise tax consequences (imposed on the DP, not the organization):
- 25% tax on the excess benefit amount (initial tax)
- 200% tax if the excess benefit is not corrected by a specified date
- 10% tax on organization managers who approved the EBT knowingly (capped at $20,000 per transaction per manager)

The "rebuttable presumption of reasonableness" protects compensation arrangements when: (a) approved by an independent board/committee, (b) based on comparable data, and (c) documented contemporaneously.

**Any "Yes" on Part IV Line 25 (excess benefit) is a serious red flag requiring immediate legal counsel.**

**Part II: Loans to/from officers, directors, trustees, key employees, highest compensated employees, and disqualified persons**
- Report all outstanding loans regardless of amount
- Include: borrower/lender name, purpose, original amount, balance due, terms, interest rate, whether in default, whether board-approved, whether written agreement exists
- Loans to insiders are a significant compliance risk and may constitute excess benefit transactions

**Part III: Grants or assistance benefiting interested persons**
- Report grants/assistance to TDOKEs, creators/founders, substantial contributors, their family members, or 35%-controlled entities
- Exceptions: charitable class distributions on equal terms, and employee scholarship programs meeting Section 4945(d)(3) criteria with objective/nondiscriminatory selection

**Part IV: Business transactions with interested persons**
- Report transactions exceeding $100K (or exceeding the lesser of $10K or 1% of the organization's total revenue) between the organization and: current/former officers, directors, trustees, key employees, or their family members or 35%-controlled entities
- Include: nature of relationship, transaction description, amount, terms

**Common errors:**
- Not recognizing that excessive compensation IS an excess benefit transaction
- Failing to apply the 5-year lookback for DP status
- Not aggregating family member transactions
- Omitting loans to officers/directors that appear as receivables on Part X Lines 5-6 without filing Schedule L
- Reporting only the organization's side of the transaction without the DP's benefit

---

### Schedule M: Noncash Contributions

**Trigger:** Part IV Line 29 (aggregate noncash contributions > $25K reported on Part VIII Line 1g)

Report by type of property:
- Art, collectibles, clothing, food, household items, cars/vehicles, boats, securities, real estate, equipment, drugs/medical supplies, etc.
- Number of items, FMV, method of valuation, whether sold/held

---

### Schedule N: Liquidation, Termination, Dissolution, or Significant Disposition of Net Assets

**Trigger:** Part IV Lines 31-32

Rarely applicable unless the organization is ceasing operations or transferring substantial assets.

---

### Schedule R: Related Organizations and Unrelated Partnerships

**Trigger:** Part IV Lines 33-38

Report:
- Disregarded entities (Part I)
- Related tax-exempt organizations (Part II)
- Related organizations taxable as partnership (Part III)
- Related organizations taxable as corporation or trust (Part IV)
- Transactions between the filing org and related orgs (Part V)

---

<a id="rarely-required"></a>
## Rarely Required for Small 501(c)(3)s

### Schedule E: Schools

**Trigger:** Part IV Line 13 (organization operates a private school)

Reports nondiscrimination policy, racially nondiscriminatory policies, and related compliance. Only for organizations operating a school as defined by the IRS (not merely providing educational programs).

### Schedule H: Hospitals

**Trigger:** Part IV Line 20 (organization operates a hospital)

Not applicable to most small nonprofits.

---

## Schedule Selection Quick Reference

For a small 501(c)(3) public charity with international operations (e.g., ADF Haiti profile):

| Schedule | Likely Required? | Reason |
|---|---|---|
| A | Yes (always) | Public charity status |
| B | Likely yes | If any donor gave > $5K |
| C | Usually no | Unless lobbying expenditures |
| D | Depends | If endowment, other assets/liabilities, or reconciliation needed |
| E | No | Not a school |
| F | Yes | International operations/grants |
| G | Depends | If professional fundraiser or events > $15K |
| H | No | Not a hospital |
| I | Depends | If domestic grants > $5K |
| J | Depends | If any individual received > $150K total comp |
| K | Usually no | Unless tax-exempt bond financing |
| L | Hopefully no | Interested person transactions (compliance issue) |
| M | Depends | If noncash contributions > $25K |
| N | No | Unless liquidating/dissolving |
| O | Yes (always) | Supplemental information |
| R | Depends | If related organizations exist |
