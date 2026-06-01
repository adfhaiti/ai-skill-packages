# Technical Narrative

## Voice Rules

All technical writing follows ADF's B2B peer voice:

- Confident and declarative: "ADF will deploy..." not "It is proposed that..."
- Specific and evidence-based: cite equipment models, team sizes, daily productivity rates
- Active voice throughout; passive voice only when the actor is irrelevant
- No charity framing, no savior narratives, no poverty imagery
- No em dashes; use parentheses, colons, or semicolons
- Bullets sparingly (6-17% of paragraphs); default to prose
- Technical but accessible; avoid jargon without explanation
- Present tense for capabilities ("ADF maintains..."), future tense for proposed actions ("ADF will conduct...")

## Methodology Pattern Templates

Select and adapt the pattern that matches the RFP's core service requirement.
Combine patterns for multi-service proposals.

### Pattern A: Data Collection / Survey

Derived from HFSA, ACCESO, FECCANO, and Bezwen Lekol proposals.

**Structure**:
1. Survey Design and Instrument Development
   - Questionnaire design in Fulcrum (fulcrumapp.com) with built-in validation
   - Skip logic, GPS capture, photo documentation, barcode/QR scanning
   - Bilingual instruments (Haitian Creole primary, French secondary)
   - Pilot testing with minimum 20-30 respondents; revision cycle

2. Enumerator Recruitment, Training, and Certification
   - Recruit from Fond-des-Blancs and surrounding communities
   - 3-5 day training covering: survey ethics, informed consent, device operation,
     data quality protocols, safety procedures
   - Certification test; minimum 80% score to deploy
   - Team structure: 1 supervisor per 4-5 enumerators

3. Field Data Collection
   - Daily productivity: 15-20 household surveys per enumerator per day
   - Real-time data sync via Fulcrum cloud; supervisor dashboard monitoring
   - Daily quality checks: completeness, GPS validity, response consistency
   - Weekly field reports to client

4. Quality Assurance and Data Cleaning
   - Automated validation rules in Fulcrum (range checks, logic checks, required fields)
   - 10% back-check rate (supervisor re-visits)
   - Post-collection cleaning: duplicate removal, outlier flagging, consistency checks
   - Data dictionary and codebook delivery

5. Analysis and Reporting
   - Descriptive statistics, cross-tabulations, geographic analysis
   - Visualization in Power BI or ArcGIS dashboards
   - Draft report, client review, final report with annexes

### Pattern B: Organizational Capacity Strengthening

Derived from Papyrus/USAID CSSP OCA proposal.

**Structure**:
1. Baseline Assessment
   - Organizational Capacity Assessment (OCA) using 7-domain framework:
     Governance, Administration, Human Resources, Financial Management,
     Organizational Management, Program Management, Project Performance Management
   - Facilitated self-assessment workshops with organizational leadership
   - Scoring: 1 (nascent) to 4 (strong) per subdomain

2. Capacity Strengthening Plan Development
   - Gap analysis from OCA scores
   - Prioritized action plan with milestones and responsibilities
   - Resource requirements identification

3. Technical Assistance Delivery
   - Targeted training and mentoring aligned to priority gaps
   - On-site coaching and remote support
   - Tool and template development

4. Progress Monitoring
   - Quarterly progress reviews against capacity strengthening plan
   - Midpoint OCA re-assessment to measure change
   - Adaptive management based on progress

5. Endline Assessment and Reporting
   - Final OCA re-assessment
   - Score comparison (baseline vs. endline) with domain-level analysis
   - Lessons learned and sustainability recommendations

### Pattern C: GIS / Drone / Mapping Services

Derived from FECCANO georeferencing, ACCESO parcel mapping, and HFSA proposals.

**Structure**:
1. Planning and Preparation
   - Area of interest delineation; coordinate reference system selection
   - Flight planning (for drone): altitude, overlap, GSD calculation
   - Ground control point (GCP) placement strategy
   - Equipment preparation: Arrow Gold RTK GNSS (sub-5cm horizontal accuracy),
     DJI Phantom 4 RTK (2-4cm GSD), mobile devices with Fulcrum

2. Field Data Collection
   - Parcel surveys: 8-15 parcels per team per day (RTK GNSS)
   - Drone mapping: 50-200 hectares per day depending on terrain and GSD
   - Attribute data collection concurrent with spatial data (owner, land use, structures)
   - Team structure: 2-person binomes (1 GNSS operator + 1 data recorder)

3. Data Processing
   - Drone imagery: photogrammetric processing (orthomosaic, DSM/DTM, point cloud)
   - GNSS data: post-processing, projection, topology validation
   - QA: positional accuracy check against GCPs, completeness review

4. GIS Database Development
   - Feature class creation in ArcGIS with standardized schema
   - Attribute linking (spatial + survey data)
   - Topology rules and validation
   - Metadata documentation (ISO 19115)

5. Deliverables and Visualization
   - Geodatabase, shapefiles, or GeoJSON per client specification
   - Web maps via ArcGIS Online
   - Print maps at client-specified scale
   - Dashboard integration if requested

### Pattern D: Training and Capacity Building

Derived from Welthungerhilfe drone training proposal.

**Structure**:
1. Needs Assessment and Curriculum Design
   - Pre-training assessment of participant skill levels
   - Curriculum development aligned to learning objectives
   - Training materials in Haitian Creole and French

2. Classroom Instruction
   - Theory modules: concepts, regulations, safety, ethics
   - Interactive exercises and group discussions
   - Duration varies by complexity (typically 2-5 days classroom)

3. Hands-On Practical Training
   - Supervised field exercises with ADF equipment
   - Progressive skill building: basic to advanced operations
   - Individual competency assessment during practicals

4. Certification and Assessment
   - Written examination (minimum 80% pass rate)
   - Practical skills demonstration
   - Certificate of completion for qualifying participants

5. Post-Training Support
   - Reference materials and job aids
   - Remote technical support period (typically 30-90 days)
   - Refresher training option

6. Training Report
   - Participant roster with assessment results
   - Curriculum documentation
   - Recommendations for ongoing skill development

## Evaluation Criteria Alignment

For each evaluation criterion in the RFP, ensure the technical narrative:
1. Uses the evaluator's language (mirror key terms from the evaluation criteria)
2. Addresses every subfactor explicitly
3. Provides specific, verifiable evidence (not generic claims)
4. Connects ADF's approach to the client's stated objectives
5. Quantifies wherever possible (team size, daily output, accuracy specs, timeline)

## Common Technical Sections

### Management Plan

Include: organizational chart, communication protocol, reporting schedule, QA/QC
procedures, risk management approach, issue escalation process. Reference the
project-management skill for detailed structure.

### Staffing Plan

Include: key personnel bios (relevant experience, qualifications), roles and
responsibilities, LOE allocation per team member, supervision structure,
surge capacity, local hiring plan.

Productivity benchmarks for LOE estimation:
- Household surveys: 15-20 per enumerator per day
- Parcel mapping (RTK): 8-15 parcels per team per day
- Drone mapping: 50-200 hectares per day
- OCA facilitation: 2-3 days per organization
- Training delivery: 5-10 days per cohort (depending on curriculum)

### Work Plan

Delegate detailed structure to the project-management skill. Include at minimum:
phased timeline, key milestones, deliverable due dates, dependencies, level of
effort per phase. Present as Gantt chart or phased table.
