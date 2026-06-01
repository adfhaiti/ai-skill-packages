---
name: rfp-response-engine
description: >
  This skill applies when the user asks to respond to an RFP, RFQ, EOI, or
  solicitation; draft a technical or cost proposal; build a capability
  statement; create a compliance matrix; write a bid response; or prepare a
  proposal package. Triggers include "respond to an RFP," "write a proposal
  for this RFP," "draft an RFQ response," "prepare an EOI," "build a
  capability statement," "create a technical proposal," "write a bid,"
  "put together a proposal package," "respond to this solicitation,"
  "compliance matrix for this RFP," and "past performance writeup."
  Not for grant applications or fundraising appeals (use adf-content-writer).
  Not for post-award project management documents (use project-management).
  Not for unsolicited proposals or concept notes.
---

# RFP Response Engine

Produce ready-to-submit proposal response packages for ADF Haiti's for-profit
data collection, GIS/drone mapping, and program evaluation services. Accept an
RFP, RFQ, EOI, or capability-statement request as input; deliver a complete,
compliant proposal package as output.

## Reference Loading Table

Load references on-demand as each workflow step requires them.

| File | Content | Load When |
|---|---|---|
| `references/rfp-parsing-guide.md` | Extraction categories, RFP type patterns, red flags, go/no-go criteria | Step 1: Parse |
| `references/compliance-matrix.md` | Excel Table schema, requirement numbering, status definitions, gap analysis | Step 2: Compliance Matrix |
| `references/technical-narrative.md` | Voice rules, methodology patterns by service line, evaluation alignment | Step 4: Draft (technical sections) |
| `references/budget-construction.md` | LOE calculations, rate card logic, cost templates, reasonableness checks | Step 4: Draft (cost sections) |
| `references/adf-differentiators.md` | Win themes, past performance summaries, differentiator matrix by RFP type | Step 4: Draft (all sections) |
| `references/capability-statement.md` | Document structure, org data block, formatting rules, tailoring guidance | When capability statement requested |

## Sibling Skill Delegation

| Skill | Delegate When |
|---|---|
| adf-docx-style | Formatting any .docx deliverable (cover pages, headers, table styles) |
| adf-content-writer | Organizational knowledge, mission/vision language, boilerplate |
| project-management | WBS, schedule, risk register, SOW structure, PM methodology |
| adf-haiti-design | Brand assets, color palette, logo placement, design guidelines |

## Modular Outputs

Each proposal package assembles from these modules. Not every RFP requires all modules.

1. **Compliance Matrix** (XLSX): Maps every RFP requirement to a proposal section with status, evidence, and page references.
2. **Technical Narrative** (DOCX): Methodology, approach, management plan tailored to the solicitation.
3. **Workplan and Schedule** (DOCX or XLSX): Phased timeline with milestones, deliverables, and dependencies. Delegate structure to project-management skill.
4. **Staffing Plan** (DOCX): Key personnel, roles, qualifications, LOE allocation.
5. **Cost Proposal** (XLSX): Line-item budget with LOE calculations, unit costs, and budget narrative.
6. **Executive Summary** (DOCX): 1-2 page overview synthesized after all other sections are drafted.
7. **Capability Statement** (DOCX or PDF): Standalone 1-2 page organizational profile for EOIs and pre-qualification.
8. **Past Performance** (DOCX): Project summaries with client, value, period, scope, and outcomes.

## Workflow

### Step 1: Parse the RFP

Load `references/rfp-parsing-guide.md`. Extract requirements across 7 categories:
submission logistics, formatting, evaluation criteria, mandatory sections, technical
requirements, eligibility/qualifications, budget format. Identify RFP type (USAID,
World Bank/IDB, large INGO, Haitian government, other). Flag red flags for go/no-go.

Present a structured brief to the user before proceeding.

### Step 2: Build the Compliance Matrix

Load `references/compliance-matrix.md`. Create an Excel Table with 10 columns mapping
every extracted requirement. Number requirements using the convention R-[Section]-[Seq].
Classify each as Technical, Management, Staffing, Cost, Administrative, or Past Performance.
Run gap analysis; present go/no-go recommendation if critical gaps exist.

### Step 3: Clarify Gaps

Use AskUserQuestion to resolve: missing information the RFP requires but ADF references
do not cover; ambiguous requirements needing interpretation; strategic choices (teaming,
subcontracting, pricing strategy). Cap at 5 questions per round.

### Step 4: Draft Proposal Sections

Load `references/technical-narrative.md`, `references/budget-construction.md`, and
`references/adf-differentiators.md` as each section requires.

Draft in this order:
1. Technical narrative (methodology, approach, management plan)
2. Staffing plan
3. Workplan/schedule (delegate structure to project-management skill)
4. Cost proposal (LOE x rates = line totals; verify arithmetic)
5. Past performance
6. Executive summary (last; synthesizes all other sections)

Apply ADF voice throughout: confident, declarative, B2B peer tone. "ADF will conduct..."
not "It is proposed that..." No charity framing. No savior narratives.

### Step 5: Format Deliverables

Delegate to adf-docx-style for all Word documents. Apply ADF brand standards:
Aptos 11pt body, Prussian Blue (#0a3d50) headers, Pale Blue Lily (#d8e7e6) table banding.
Verify formatting requirements from compliance matrix (page limits, font, margins, spacing).

### Step 6: Verify Compliance

Cross-check every compliance matrix row against the final deliverables. Confirm:
- Every "Compliant" row has corresponding content at the referenced page/section
- Page limits respected
- All mandatory sections present
- Budget arithmetic verified (LOE x rate = line total; line totals sum to category totals)
- No em dashes anywhere in any deliverable

Update compliance matrix Page_Ref column with final page numbers.

## Scope Boundaries

**In scope**: Competitive proposal responses to formal solicitations where ADF is bidding
for-profit services (data collection, GIS/drone mapping, program evaluation, training,
capacity assessment).

**Out of scope**: Grant applications to foundations or donors (use adf-content-writer);
post-award project management documents like inception reports, progress reports, final
reports (use project-management); unsolicited concept notes; proposals for services ADF
does not offer.

## Quality Standards

1. **Compliance**: Every RFP requirement mapped and addressed. Zero unaddressed mandatory requirements.
2. **Traceability**: Every budget line item traceable to LOE and rate inputs. Arithmetic verifiable.
3. **Voice**: Confident, specific, evidence-based. No filler, no hedging, no charity language.
4. **Brand**: All documents follow ADF brand standards via adf-docx-style delegation.
5. **Completeness**: Proposal package includes all modules the RFP requires; nothing extra, nothing missing.
