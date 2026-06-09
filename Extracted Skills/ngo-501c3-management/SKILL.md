---
name: ngo-501c3-management
description: >
  This skill should be used when the user asks to "start a nonprofit", "form a 501c3",
  "file Form 990", "manage a nonprofit organization", "create a nonprofit board",
  "develop a fundraising strategy", "write a grant proposal", "evaluate nonprofit programs",
  "maintain tax-exempt status", "do nonprofit strategic planning", "manage nonprofit finances",
  "set up nonprofit governance", "manage volunteers", "create a nonprofit budget",
  "navigate 501c3 compliance", or mentions NGO management, nonprofit leadership,
  charitable organization administration, or social enterprise operations.
  Not for for-profit business management, government agency administration,
  or individual tax filing. Make sure to use this skill whenever the user mentions
  nonprofits, NGOs, 501c3, charitable organizations, tax-exempt status, or
  social sector management — even if they don't explicitly say "nonprofit management."
---

# NGO & 501(c)(3) Nonprofit Management

Comprehensive guidance for forming, managing, and sustaining 501(c)(3) nonprofit
organizations. Covers the full lifecycle: legal formation, governance, strategic
leadership, financial management, fundraising, human resources, program evaluation,
risk management, collaboration, and advocacy.

## Core Competency Areas

### 1. Legal Formation & IRS Compliance

Load `references/legal-compliance.md` for detailed procedures on:

- Articles of incorporation and state-level nonprofit formation
- IRS Form 1023 / 1023-EZ for 501(c)(3) determination
- Public charity vs. private foundation classification and the public support test
- IRS Form 990 (990-N, 990-EZ, 990 full) — who files what, schedules, and deadlines
- Maintaining tax-exempt status: UBIT, excess benefit transactions, private inurement
- State charitable solicitation registration requirements
- Expenditure responsibility and equivalency determinations for international grantmaking

**Key thresholds:** File Form 990-N if gross receipts ≤ $50,000; Form 990-EZ if gross
receipts < $200,000 and total assets < $500,000; full Form 990 otherwise. Automatic
revocation occurs after three consecutive years of non-filing.

### 2. Board Governance & Fiduciary Duties

Load `references/governance-board.md` for complete guidance on:

- Board composition, recruitment, and nomination processes
- Fiduciary duties: duty of care, duty of loyalty, duty of obedience
- Board-executive director relationship and role delineation
- Committee structures (executive, finance, audit, governance, development)
- Board self-assessment and governance maturity models
- Bylaws drafting and amendment procedures
- Conflict of interest policies and enforcement

**Core principle:** The board governs; the executive director manages. Confusion between
these roles is the most common governance failure.

### 3. Strategic Leadership & Organizational Effectiveness

Load `references/strategic-leadership.md` for:

- Executive leadership competencies: antigravitational thinking, long-view orientation,
  leveraging serendipity (Dann, 2022 framework)
- Strategic planning cycles and the Strategy Change Cycle (Bryson & George)
- Organizational effectiveness frameworks: multidimensional integrated model (Sowa et al.,
  2004), multiple constituencies approach (Herman & Renz, 1997, 1999)
- Mission drift prevention and theory of change development
- Hybrid organizing and social enterprise models
- Succession planning and leadership pipelines
- Organizational culture development for high performance

**Effectiveness is multidimensional and socially constructed.** No single metric captures
nonprofit effectiveness. Assess across: management effectiveness, program effectiveness,
fundraising efficiency, and legitimacy/reputation.

### 4. Financial Management & Sustainability

Load `references/financial-management.md` for:

- Nonprofit accounting principles (FASB standards, fund accounting)
- Budget development: line-item, program, and flexible budgets
- Financial statements: Statement of Financial Position, Statement of Activities,
  Statement of Cash Flows, Statement of Functional Expenses
- Internal controls, segregation of duties, and audit preparation
- Revenue diversification strategies and earned income models
- Financial ratio analysis: liquidity, leverage, efficiency, sustainability
- Cash flow management and reserves policies
- The Dual Bottom Line Matrix (Zimmerman): balancing mission impact and financial viability

### 5. Fundraising & Philanthropy

Load `references/fundraising-philanthropy.md` for:

- Development planning: annual fund, major gifts, planned giving, capital campaigns
- Donor cultivation cycle: identification, qualification, cultivation, solicitation, stewardship
- Grant writing: foundation research, proposal development, logic models, reporting
- Corporate partnerships and sponsorships
- Online and digital fundraising strategies
- Servant-leadership approach to fundraising (Wildstein, 2023)
- Donor-advised funds, endowments, and complex gifts
- Fundraising ethics (AFP Code of Ethical Standards)

### 6. Human Resources & Volunteer Management

Load `references/hr-volunteer-management.md` for:

- Hiring practices: job descriptions, equitable recruitment, selection, onboarding
- Performance management: SMART goals, weekly one-on-ones, evaluations, progressive discipline
- Compensation strategy: IRS rebuttable presumption of reasonableness, total rewards
- Total inclusion management: leveraging diversity for mission and equity
- Volunteer program design: recruitment, training, retention, recognition
- Employment law compliance: exempt/non-exempt classification, independent contractors
- Staff development and retention of high performers

### 7. Program Evaluation & Impact Measurement

Load `references/program-evaluation.md` for:

- Logic models and theories of change
- Outcome measurement frameworks and indicator development
- Formative vs. summative evaluation design
- Data collection methods: quantitative, qualitative, mixed methods
- Utilization-focused evaluation (Patton)
- Effect size and meaningful significance vs. statistical significance
- Reporting to stakeholders: funders, board, community
- Building a culture of learning and continuous improvement

### 8. Risk Management & Compliance

Load `references/risk-compliance.md` for:

- Enterprise risk management for nonprofits
- Risk identification, assessment, prioritization, and mitigation planning
- Insurance: D&O, general liability, workers' compensation, cyber liability
- Internal controls and fraud prevention
- Whistleblower policies and document retention
- Crisis management and business continuity planning
- Legal compliance calendar and regulatory scanning
- Ethical decision-making frameworks (Jeavons core values framework)

### 9. Interorganizational Collaboration

Load `references/collaboration-partnerships.md` for:

- Collaboration continuum: networking, coordination, cooperation, collaboration, integration
- Partnership life cycle: formation, implementation, evaluation, adaptation
- Trust-building in interorganizational relationships (Vangen & Huxham, 2003)
- Collective impact models and backbone organizations
- Meta-organizations and network governance
- Cross-sector partnerships with government and business
- Measuring collaboration effectiveness

### 10. Advocacy & Lobbying

Load `references/advocacy-lobbying.md` for:

- Distinction between advocacy (unlimited) and lobbying (limited for 501c3)
- 501(h) election: expenditure test vs. insubstantial part test
- Direct vs. grassroots lobbying definitions and reporting
- Permissible legislative activities and prohibitions on political campaign intervention
- Advocacy strategy development: power mapping, coalition building, media advocacy
- Measuring advocacy impact beyond policy wins
- Voter engagement and nonpartisan election activities

## Operational Workflow

When responding to a nonprofit management query:

1. **Identify the domain:** Determine which competency area(s) the query addresses.
2. **Load relevant references:** Use `readReference` with skill name `ngo-501c3-management`
   and the appropriate file path from the competency table above.
3. **Assess context:** Determine the organization's stage (startup, growth, mature,
   turnaround) and size; calibrate guidance accordingly.
4. **Provide actionable guidance:** Offer procedural steps, templates, or frameworks
   appropriate to the user's specific situation.
5. **Identify compliance triggers:** Flag IRS deadlines, filing requirements, or legal
   risks relevant to the query.
6. **Recommend further resources:** Suggest applicable tools, checklists, or references
   from the NGO document library at `C:\Users\josiah.local\Desktop\NGO Docs`.

## United States 501(c)(3) Quick Reference

| Topic | Key Reference |
|-------|--------------|
| Formation | Articles of incorporation → EIN → Form 1023/1023-EZ → State registrations |
| Annual filing | Form 990 series due 15th day of 5th month after fiscal year end |
| Public support test | 33⅓% minimum public support (facts and circumstances test available) |
| Lobbying limits (501h) | 20% of first $500k exempt purpose expenditures for total lobbying |
| Private benefit prohibition | No more than incidental private benefit; no inurement to insiders |
| UBIT | Tax on income from regularly carried-on trade or business unrelated to exempt purpose |
| Board minimum | IRS recommends at least 3 independent directors (state law may require more) |

## IRS Timeline Compliance

| Deadline | Action |
|----------|--------|
| Within 27 months of incorporation | File Form 1023/1023-EZ for retroactive tax-exempt status |
| 15th day of 5th month after FY close | File annual Form 990 series |
| By fiscal year end | Distribute charitable contribution acknowledgments for gifts ≥ $250 |
| January 31 | Issue W-2s to employees; file W-3 with SSA |
| January 31 | Issue 1099-NEC to independent contractors paid ≥ $600 |
| Quarterly | File Form 941 (employer's quarterly federal tax return) if applicable |
| Ongoing | File state charitable solicitation renewals (varies by state) |

## References

All reference files are located in the `references/` directory. Each covers a single
competency domain in depth. Load only the files needed for the current query:

| File | Domain | Size |
|------|--------|------|
| `references/legal-compliance.md` | Legal formation, IRS Form 990, tax-exempt compliance | ~3,000 words |
| `references/governance-board.md` | Board governance, fiduciary duties, board-staff relations | ~2,500 words |
| `references/strategic-leadership.md` | Executive leadership, strategic planning, effectiveness | ~3,000 words |
| `references/financial-management.md` | Nonprofit accounting, budgeting, sustainability | ~3,000 words |
| `references/fundraising-philanthropy.md` | Fundraising, grant writing, donor relations | ~3,000 words |
| `references/hr-volunteer-management.md` | Hiring, performance, compensation, volunteers | ~2,500 words |
| `references/program-evaluation.md` | Logic models, outcomes measurement, evaluation design | ~2,500 words |
| `references/risk-compliance.md` | Risk management, insurance, ethics, crisis planning | ~2,500 words |
| `references/collaboration-partnerships.md` | Interorganizational collaboration, collective impact | ~2,500 words |
| `references/advocacy-lobbying.md` | Advocacy, lobbying rules (501h, political prohibition) | ~2,500 words |

## NGO Document Library

The user maintains an extensive library of nonprofit management literature at
`C:\Users\josiah.local\Desktop\NGO Docs` containing over 160 PDFs including:

- **Core reference works:** Jossey-Bass Handbook of Nonprofit Leadership and Management
  (Renz, Brown, Andersson, 2024), Managing and Leading Nonprofit Organizations (Dann, 2022),
  Managing to Change the World (Green & Hauser, 2012)
- **IRS/legal:** Starting and Managing a Nonprofit Organization (Hopkins, 2017), How to
  Form a Nonprofit Corporation (Mancuso, 2021), IRS Form 990 preparation guides
- **Leadership:** Executive Director's Guide to Thriving (Carlson & Donohoe, 2010),
  Joan Garry's Guide to Nonprofit Leadership (2020), Finding Your Way in the Nonprofit
  Sector (Bruton, 2023)
- **Effectiveness research:** Herman & Renz, Sowa et al. (2004), Liket & Maas (2015)
- **Collaboration:** Wood & Gray, Huxham, Gazley, Guo & Acar, Foster-Fishman et al.
- **Fundraising:** Wildstein (2023), Shaker, Wiepking & Nathan
- **Program evaluation:** Patton, Campbell-Patton

Search this library using keywords when domain-specific evidence is needed to support
guidance. The `IRS 501c3 - 990 Related` subfolder contains specialized tax compliance
references.
