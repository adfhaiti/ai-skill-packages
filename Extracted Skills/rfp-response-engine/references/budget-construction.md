# Budget Construction

## LOE Calculation Method

Every budget starts with Level of Effort (LOE) estimation, not with dollar amounts.

1. Decompose the scope into discrete tasks from the workplan.
2. For each task, estimate person-days using ADF productivity benchmarks.
3. Assign personnel categories to each task.
4. Multiply person-days by daily rates to calculate personnel costs.
5. Add non-personnel costs tied to specific tasks.
6. Apply indirect rates if applicable.

### ADF Productivity Benchmarks

| Activity | Unit | Daily Rate | Notes |
|---|---|---|---|
| Household surveys | Surveys per enumerator per day | 15-20 | Depends on questionnaire length and travel distance |
| Parcel mapping (RTK GNSS) | Parcels per team per day | 8-15 | 2-person team; depends on parcel size and terrain |
| Drone mapping | Hectares per day | 50-200 | Depends on GSD, terrain, and weather |
| Data entry/cleaning | Records per person per day | 80-120 | If manual digitization required |
| OCA facilitation | Organizations per facilitator | 0.3-0.5 (2-3 days per org) | Includes preparation and scoring |
| Training delivery | N/A | 1 day per training day | Plus 2-3 days preparation per training week |
| GIS processing | Parcels per analyst per day | 30-50 | Post-field processing and QA |
| Report writing | Pages per analyst per day | 3-5 | Technical reports with data analysis |

### Personnel Categories

| Category | Typical Roles | Rate Basis |
|---|---|---|
| Senior Technical | Project Director, Senior GIS Analyst, Lead Evaluator | Daily rate |
| Mid-Level Technical | GIS Analyst, Data Analyst, M&E Officer, Trainer | Daily rate |
| Field Staff | Enumerators, Survey Supervisors, GNSS Operators | Daily rate |
| Administrative | Finance, Logistics, Driver | Daily rate |

## Rate Card Logic

ADF does not publish a fixed rate card. Rates are built per-proposal based on:

1. **Market benchmarks**: Rates comparable to Haitian NGO and consulting sector norms
2. **Project complexity**: Technical specialization commands higher rates
3. **Client type**: USAID-funded projects may require NICRA-based rates; INGO projects
   use simplified rates; government contracts often have rate ceilings
4. **Duration**: Longer engagements may use slightly lower daily rates
5. **Competition**: Adjust within a defensible range based on competitive landscape

Build rates bottom-up from actual staff costs plus reasonable margin, not top-down
from what the market will bear.

## Non-Personnel Costs

| Category | Typical Items | Estimation Method |
|---|---|---|
| Travel and Transport | Vehicle rental, fuel, motorcycle rental, per diem | Per-trip or per-day; specify routes |
| Equipment | Device rental/depreciation, GNSS, drones, tablets | Per-day or lump sum amortization |
| Communications | Airtime, internet, data plans | Per-month or per-device |
| Supplies | Printing, field supplies, batteries, safety gear | Lump sum per activity |
| Software | Fulcrum licenses, ArcGIS Online, Power BI | Per-month or per-seat |
| Venue/Facilities | Training venue rental, refreshments | Per-day or per-event |
| Subcontracts | Specialized services ADF subcontracts | Per deliverable or LOE-based |

## Indirect Cost Treatment

### USAID-Funded Projects

If ADF has a Negotiated Indirect Cost Rate Agreement (NICRA), apply the negotiated rate.
If not, use the 10% de minimis rate per 2 CFR 200.414(f) or propose a rate with
supporting documentation.

Indirect costs typically applied to: Modified Total Direct Costs (MTDC), which excludes
equipment over $5,000, subawards over $25,000, and participant support costs.

### INGO and Other Clients

Most INGOs accept a simplified overhead/administrative cost line (typically 7-15% of
direct costs). Some require overhead included in line-item rates (fully loaded rates).

Clarify with the user which approach the RFP requires.

### Haitian Government

Government contracts often have specific rules on overhead and profit margins. Check
the specific solicitation and CNMP regulations.

## Budget Format Templates

### Template 1: LOE-Based (Most Common)

| Line | Personnel Category | Role | Unit (Days) | Rate (USD/Day) | Quantity | Total |
|---|---|---|---|---|---|---|
| 1.1 | Senior Technical | Project Director | Day | [rate] | [days] | [calc] |
| 1.2 | Mid-Level Technical | GIS Analyst | Day | [rate] | [days] | [calc] |
| ... | | | | | | |
| **Subtotal Personnel** | | | | | | **[sum]** |
| 2.1 | Travel | Vehicle rental | Day | [rate] | [days] | [calc] |
| ... | | | | | | |
| **Subtotal Non-Personnel** | | | | | | **[sum]** |
| **Total Direct Costs** | | | | | | **[sum]** |
| Indirect Costs | [rate]% of MTDC | | | | | **[calc]** |
| **Total Project Cost** | | | | | | **[sum]** |

### Template 2: Phased Budget

Break Template 1 into phases matching the workplan. Each phase has its own personnel
and non-personnel subtotals. Useful for milestone-based payments.

### Template 3: Milestone-Based

| Milestone | Description | Deliverable | Payment (USD) | % of Total |
|---|---|---|---|---|
| M1 | Inception | Inception report, tools | [amount] | [%] |
| M2 | Data collection complete | Raw dataset | [amount] | [%] |
| M3 | Final deliverables | Final report, clean data | [amount] | [%] |
| **Total** | | | **[sum]** | **100%** |

## Budget Narrative Structure

For each cost category, provide a brief justification:

1. **Personnel**: Roles, qualifications justifying rates, LOE calculation logic
2. **Travel**: Routes, frequency, vehicle type, per diem basis
3. **Equipment**: Why needed, rental vs. purchase rationale, depreciation method
4. **Other Direct Costs**: Itemized justification for each line
5. **Indirect Costs**: Rate basis and what it covers

## Cost Reasonableness Checklist

Before finalizing any budget:

- [ ] Every line item traces to a specific workplan task
- [ ] LOE calculations use documented productivity benchmarks
- [ ] Rates are within market range for Haiti consulting sector
- [ ] Non-personnel costs are itemized (no unexplained lump sums over $500)
- [ ] Arithmetic verified: unit x quantity = line total; line totals sum correctly
- [ ] Indirect rate applied correctly to the right cost base
- [ ] Total within RFP budget ceiling (if stated)
- [ ] Payment schedule aligns with deliverable timeline
- [ ] Currency consistent throughout (USD unless RFP specifies otherwise)
- [ ] Contingency included only if RFP allows; clearly labeled
