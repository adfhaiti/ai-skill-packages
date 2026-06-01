# Compliance Matrix

## Excel Table Schema

Create as a proper Excel Table (openpyxl: Table + TableStyleInfo) with these 10 columns:

| Column | Type | Description |
|---|---|---|
| Req_ID | Text | Unique identifier: R-[RFP Section]-[Seq]. Example: R-C3.1-001 |
| RFP_Section | Text | Section/page reference in the original RFP |
| Requirement | Text | Verbatim or close-paraphrase of the requirement |
| Category | Text | One of 6 categories (see below) |
| Proposal_Section | Text | Target section in the proposal that addresses this |
| Compliance_Status | Text | One of 4 statuses (see below) |
| Response_Summary | Text | Brief description of how the proposal addresses the requirement |
| Evidence | Text | Specific evidence: past project, staff qualification, equipment, methodology |
| Page_Ref | Text | Page number(s) in the final proposal. Populated in Step 6 (Verify). |
| Notes | Text | Internal notes: risks, assumptions, items needing user input |

## Requirement Extraction Rules

1. Extract every requirement, not just the obvious ones. Check: scope of work, evaluation
   criteria, instructions to offerors, terms and conditions, attachments, and amendment documents.
2. One row per discrete requirement. If a paragraph contains multiple requirements, split them.
3. Use the RFP's own numbering where it exists. Add sequence numbers for unnumbered requirements.
4. Preserve the RFP's language closely; do not over-interpret.

## Numbering Convention

Format: R-[Section]-[Sequence]

- Section = RFP section reference (e.g., C3.1, L.4, M.2, Annex-B)
- Sequence = three-digit counter within that section (001, 002, 003)
- Example: R-C3.1-001 = first requirement extracted from RFP Section C.3.1

## Category Classification

| Category | Covers |
|---|---|
| Technical | Methodology, approach, tools, data collection methods, analysis, deliverables |
| Management | Management plan, communication, reporting, QA/QC, risk mitigation |
| Staffing | Key personnel, qualifications, LOE, org chart, CVs |
| Cost | Budget, rates, cost breakdown, indirect costs, payment terms |
| Administrative | Registration, certifications, insurance, forms, representations |
| Past Performance | References, similar contracts, performance history |

## Compliance Status Definitions

| Status | Definition | Conditional Format Color |
|---|---|---|
| Compliant | ADF fully meets the requirement with existing capabilities and evidence | Smooth Green (#3eac7a) |
| Partially Compliant | ADF meets the core requirement but with gaps or qualifications | Light Sea Green (#41aaa3) |
| Non-Compliant | ADF cannot meet the requirement as stated | Red (#c0392b) |
| Needs Clarification | Requirement is ambiguous or requires user input to assess | Davy Grey (#58585b) |

## Gap Analysis Workflow

After populating all rows:

1. Filter for Non-Compliant and Needs Clarification rows.
2. For each Non-Compliant row, assess: can the gap be closed through teaming, subcontracting,
   or a credible mitigation plan? If yes, note the mitigation in Response_Summary and change
   status to Partially Compliant. If no, flag for go/no-go discussion.
3. For Needs Clarification rows, prepare questions for Step 3 (Clarify Gaps).
4. Count: total requirements, compliant, partially compliant, non-compliant, needs clarification.

## Go/No-Go Recommendation Matrix

| Condition | Recommendation |
|---|---|
| All mandatory requirements Compliant or Partially Compliant | Proceed |
| 1-2 mandatory requirements Non-Compliant with viable mitigation | Proceed with caveats |
| 3+ mandatory requirements Non-Compliant | Recommend no-bid |
| Any pass/fail requirement Non-Compliant | Recommend no-bid |
| Compliance rate below 70% | Recommend no-bid |

Present the matrix summary and recommendation to the user before drafting.
