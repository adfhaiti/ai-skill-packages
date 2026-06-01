# RFP Parsing Guide

## Extraction Categories

Parse every RFP, RFQ, EOI, or solicitation document into these 7 categories before
any drafting begins.

### 1. Submission Logistics

Extract: deadline (date, time, timezone), submission method (email, portal, physical),
recipient name/address, required number of copies (if physical), file format requirements,
file naming conventions, maximum file size, whether technical and cost proposals must be
separate submissions.

### 2. Formatting Requirements

Extract: page limits (total and per-section), font and size requirements, margin
requirements, line spacing, header/footer requirements, page numbering format,
section labeling conventions, appendix rules (count toward page limit or not).

**ADF defaults when RFP is silent**: Aptos 11pt, 1-inch margins, 1.15 line spacing,
single-sided, letter size (8.5x11). Apply ADF brand formatting via adf-docx-style.

### 3. Evaluation Criteria

Extract: scoring methodology (points, percentages, adjectival ratings), weight per
criterion, evaluation factors and subfactors, pass/fail requirements, best-value or
lowest-price-technically-acceptable determination method.

Map each criterion to the proposal section that will address it. Flag any criterion
worth >25% of total score for extra attention in drafting.

### 4. Mandatory Sections

Extract: required proposal outline or table of contents, mandatory section headings,
required forms and attachments, certifications and representations, required annexes.

List every mandatory section. Mark each as: included in ADF standard package, requires
new content, or requires external input (user must provide).

### 5. Technical Requirements

Extract: scope of work or statement of objectives, deliverables list with due dates,
performance standards or acceptance criteria, reporting requirements, geographic scope,
period of performance, option periods, specific methodologies required or preferred.

### 6. Eligibility and Qualifications

Extract: organizational requirements (registration, certifications, insurance),
minimum experience (years, similar contracts, dollar thresholds), key personnel
requirements (qualifications, certifications, minimum experience), past performance
requirements (number of references, recency, relevance, contract size), teaming or
subcontracting requirements, small business or local content requirements.

Cross-check against ADF qualifications:
- US 501(c)(3), Haiti-registered
- EIN 82-2714270, UEI VFB2VGT7N963, CAGE 99MB2
- NAICS: 541990, 541620, 541370, 541690, 611430
- Key equipment: Arrow Gold RTK GNSS (sub-5cm), DJI Phantom 4 drones (2-4cm), Fulcrum, ArcGIS

### 7. Budget Format

Extract: required budget template (if provided), cost categories, allowable costs,
indirect cost treatment (overhead, G&A, fee/profit), currency, payment terms,
cost-realism or cost-reasonableness evaluation approach, required cost breakdowns
(by task, by year, by personnel category).

## RFP Type Patterns

### USAID (Direct or through Primes)

Expect: SF-330 or similar forms, past performance questionnaires, DUNS/UEI requirements,
cost-realism evaluation, detailed evaluation criteria with subfactors, organizational
conflict of interest disclosure, Section 889 compliance. Technical and cost proposals
typically separate volumes. NICRA or proposed indirect rates required.

### World Bank / IDB

Expect: REOI followed by shortlist and full RFP, QCBS or QBS selection, standardized
forms (Technical and Financial Proposal forms), mandatory CVs in prescribed format,
association/consortium requirements, point-based evaluation. Budget typically in
prescribed template with person-months.

### Large INGOs (Mercy Corps, CRS, WHH, WVI, etc.)

Expect: shorter RFQs, often template-based, emphasis on methodology and local presence,
less rigid formatting, budget in Excel with line items, references required but format
flexible. Evaluation often combines technical quality and price.

### Haitian Government

Expect: French-language documents, CNMP (Commission Nationale des Marches Publics)
procedures, specific legal registration requirements, budget in HTG (Haitian Gourdes),
DGI (Direction Generale des Impots) compliance certificates. Formatting requirements
vary by ministry.

## Red Flags Checklist

Flag these for go/no-go discussion with the user:

- [ ] Deadline less than 5 business days away
- [ ] Scope includes services ADF does not offer (construction, medical, legal)
- [ ] Requires certifications ADF does not hold
- [ ] Minimum contract value or past performance threshold ADF cannot meet
- [ ] Requires insurance coverage ADF does not carry
- [ ] Geographic scope outside ADF operational area without clear logistics plan
- [ ] Teaming requirement with no identified partner
- [ ] Budget ceiling below ADF cost of delivery
- [ ] Organizational conflict of interest concerns
- [ ] Scope requires more than 12 staff simultaneously (ADF has 10-12 total)

Present red flags to the user before proceeding to compliance matrix.
