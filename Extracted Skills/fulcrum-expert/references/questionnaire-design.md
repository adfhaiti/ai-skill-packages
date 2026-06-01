# Questionnaire Design Methodology for Fulcrum

This reference covers research-backed questionnaire design principles applied to Fulcrum mobile data collection. It bridges the gap between statistical rigor and practical form building: every design decision here has a downstream impact on data quality and analytical power.

## Table of Contents

1. [Variable Classification and Field Type Mapping](#1-variable-classification-and-field-type-mapping)
2. [Question Formulation and Wording](#2-question-formulation-and-wording)
3. [Response Scale Design](#3-response-scale-design)
4. [Questionnaire Structure and Sequencing](#4-questionnaire-structure-and-sequencing)
5. [Mobile-Specific UI/UX Optimization](#5-mobile-specific-uiux-optimization)
6. [Validation and Error Prevention](#6-validation-and-error-prevention)
7. [The 6-Phase Mobile Questionnaire Pipeline](#7-the-6-phase-mobile-questionnaire-pipeline)
8. [The 4-Stage Validation Funnel](#8-the-4-stage-validation-funnel)
9. [Pilot Testing and Quality Assurance](#9-pilot-testing-and-quality-assurance)
10. [Sampling Considerations](#10-sampling-considerations)

---

## 1. Variable Classification and Field Type Mapping

Before configuring a single field in Fulcrum, classify each variable by its statistical type. This determines which Fulcrum field to use and, critically, which analyses are valid downstream. Getting this wrong means the dataset may lack the structural integrity needed for valid inference.

### The Two Diagnostic Tests

Apply these sequentially to every variable:

**The Subtraction Test:** If subtracting one record's value from another yields a meaningful quantitative difference, the variable is quantitative. If not (e.g., subtracting "Severe Itch" from "Moderate Itch" is meaningless), it's qualitative.

**The Mid-Way Test:** For variables that pass the Subtraction Test, check whether a value exactly midway between two data points is logically meaningful. Duration of 10 minutes to 13 minutes = 11.5 minutes works (continuous). Number of children 5 to 8 = 6.5 children does not work (discrete).

### Variable Type to Fulcrum Field Mapping

| Variable Type | Properties | Fulcrum Field | Example |
|---------------|-----------|---------------|---------|
| **Quantitative: Continuous** | Can take any value between two points; passes both tests | TextField (numeric=True, format="decimal") | Duration in minutes, weight in kg, distance |
| **Quantitative: Discrete** | Countable whole numbers; passes Subtraction but fails Mid-Way | TextField (numeric=True, format="integer") with min/max | Number of children, number of rooms, livestock count |
| **Qualitative: Nominal** | Unordered categories; no meaningful ranking | ChoiceField (multiple=False) | Gender, water source, religion, crop type |
| **Qualitative: Ordinal** | Ordered categories but intervals are not equal | ChoiceField or ClassificationField | Education level, wealth ranking, condition severity |
| **Qualitative: Binary** | Exactly two options | YesNoField | Has latrine (Wi/Non), consent given |

### Why This Matters for Analysis

The field type you choose dictates the analytical pipeline:

- **Nominal fields** restrict you to frequency analysis and chi-squared tests for independence. You cannot compute a meaningful mean or median.
- **Ordinal fields** allow median, IQR, and non-parametric tests (Mann-Whitney, Kruskal-Wallis) but not arithmetic means.
- **Continuous/discrete numeric fields** support the full range of descriptive and inferential statistics.

Choosing a ChoiceField with ranges ("18-25", "26-35") when you could collect exact age as a numeric TextField throws away analytical power. You can always group continuous data into categories during analysis, but you can never recover precision from pre-categorized data.

### Design Workflow

1. **Define operational variables.** Translate research questions into specific, measurable variables. Use validated scales when available (e.g., PASI for psoriasis severity) rather than inventing ad-hoc measures.
2. **Classify each variable** using the Subtraction and Mid-Way tests.
3. **Identify dependent vs. independent variables.** The outcome variables (dependent) should be the focus; explanatory variables (independent/predictor) support the analysis. This hierarchy informs the logical flow and branching logic within the Fulcrum app.
4. **Identify confounding and control variables.** Design fields to track external factors that might cause spurious associations. These often become required fields that enumerators must complete regardless of skip logic.
5. **Map to Fulcrum field types** using the table above.

### The "Good Variable" Checklist

Every variable in the questionnaire should demonstrate:

- **Reliability:** Consistent results if measured repeatedly under similar conditions
- **Validity:** Actually measures what it claims to measure
- **Objectivity:** Minimizes subjective interpretation by the enumerator
- **Clarity:** Unambiguous to both enumerator and respondent
- **Feasibility:** Can realistically be collected in field conditions
- **Low cost:** Does not require specialized equipment or excessive time

---

## 2. Question Formulation and Wording

Enumerators read these questions aloud. The wording directly determines data quality. Poor phrasing introduces measurement error that no amount of statistical analysis can fix.

### Core Principles

**Use simple, everyday language.** Avoid jargon, acronyms, and complex syntax. Keep questions under 25 words when possible. Write at the literacy level of your respondent population. For ADF Haiti surveys, this means plain Haitian Creole with familiar vocabulary.

**Ask one thing at a time.** Double-barreled questions ("Do you have access to clean water and sanitation?") force the respondent to answer two different questions with one response. Split them.

**Avoid leading questions.** "Don't you agree that the water quality has improved?" pushes toward a particular answer. Neutral phrasing: "How would you describe the water quality compared to last year?"

**Avoid vague qualifiers.** Words like "usually," "often," "regularly," and "recently" mean different things to different people. Replace with specific timeframes or frequencies: "In the last 7 days, how many times did you...?" instead of "How often do you...?"

**Handle sensitive topics carefully.** For income, age in some cultures, health status, or other personal topics:
- Use ranges instead of exact values when respondents are likely to refuse (e.g., income brackets rather than exact amounts)
- Place sensitive questions later in the questionnaire after rapport is established
- Use normalizing introductions: "Many families in this area face challenges with..." before a sensitive question
- Consider self-administration mode for highly sensitive items if literacy permits

**Provide "Pa Konnen" (Don't Know) options judiciously.** For factual questions where a respondent genuinely might not know the answer, include it. But don't add it to every question -- research shows it encourages satisficing (choosing the easy out rather than thinking).

### Distinguishing Instructions from Questions

In enumerator-administered surveys, the text contains two audiences: words the enumerator reads aloud to the respondent, and instructions the enumerator follows silently. In Fulcrum:

- **Field label** = what gets read aloud (or close to it)
- **Field description** = enumerator instructions, edge case handling, observation notes

Use the description field to clearly mark instructions like "LI TOUT CHWA YO" (READ ALL OPTIONS) or "PA SOUFLE REPONS" (DO NOT PROMPT). This distinction prevents enumerators from accidentally reading internal instructions to respondents.

### Question Types and When to Use Them

| Question Type | Fulcrum Field | Best For | Watch Out For |
|---------------|--------------|----------|---------------|
| Closed single-select | ChoiceField (multiple=False) | Categories with 2-7 options | Ensure exhaustive + mutually exclusive options |
| Closed multi-select | ChoiceField (multiple=True) | "Check all that apply" scenarios | Better to use forced-choice (Wi/Non per item) for statistical rigor |
| Open numeric | TextField (numeric=True) | Counts, ages, measurements | Set realistic min/max bounds |
| Open text | TextField | Names, locations, qualitative responses | Hard to analyze at scale; use sparingly |
| Binary | YesNoField | Screening, yes/no facts | Always include N/A for questions that may not apply |
| Date/time | DateTimeField | Event dates, timestamps | Default to survey date for common fields |
| Likert/rating | ChoiceField with ordered options | Attitudes, satisfaction, severity | See Scale Design section below |

### "Check All That Apply" vs. Forced Choice

Research shows that "check all that apply" (ChoiceField with multiple=True) produces lower-quality data than presenting each option as a separate Yes/No question. With checkboxes, respondents tend to select fewer items due to satisficing. With forced choice, the enumerator must ask about each item explicitly.

**When to use forced choice (separate YesNoField per item):**
- The list has 3-8 items and each one matters independently
- You need to distinguish "No" from "not asked" in the data
- Statistical analysis requires each item as a separate binary variable

**When checkboxes are acceptable:**
- The list is very long (10+ items) and you only need to know which apply
- The items are not independently important for analysis
- Speed matters more than completeness

---

## 3. Response Scale Design

### Likert and Rating Scales

When measuring attitudes, satisfaction, severity, or agreement:

- **7-point scales** are optimal for reliability and validity based on research consensus
- **5-point scales** are a good compromise when respondent literacy or cognitive load is a concern (common in rural Haiti field contexts)
- **Even-numbered scales** (4 or 6 point) force respondents to choose a direction, useful when you need to avoid neutral clustering
- Scales with fewer than 5 points lose discriminating power; more than 9 rarely add information

### Midpoint Considerations

A neutral midpoint ("Neither agree nor disagree") can become a "dumping ground" for respondents who find the question confusing or socially undesirable. To minimize misuse:
- Improve item clarity so respondents can actually choose a side
- Offer separate "Pa Aplikab" and "Pa Konnen" options off the scale rather than letting the midpoint absorb these responses
- For enumerator-administered surveys, clear field descriptions help the enumerator probe rather than accept a quick neutral answer

### Scale Direction

Present scales with the negative end first (1 = strongly disagree) and positive end last. Research shows primacy effects (tendency to pick the first option heard) are weaker for attitudinal items but stronger for factual and longer scales. For oral administration, rotate scale direction or read all options to mitigate order bias.

### Implementing Scales in Fulcrum

Use a ChoiceField with ordered choices. Include the numeric value in the choice value for easier analysis:

```python
# 5-point satisfaction scale
make_choice(hk(), "Ki jan ou satisfè ak sèvis la?", "satisfaksyon_sevis",
    [("1 - Pa satisfè ditou", "1"),
     ("2 - Pa twò satisfè", "2"),
     ("3 - Ni youn ni lòt", "3"),
     ("4 - Satisfè", "4"),
     ("5 - Trè satisfè", "5")],
    description="Li tout chwa yo pou moun nan. Pa soufle repons. "
                "Si moun nan ezite, repete chwa yo yon fwa.",
    include_lot=False)
```

---

## 4. Questionnaire Structure and Sequencing

The order of questions affects response quality, completion rates, and respondent cooperation. These are not arbitrary preferences; they're evidence-based patterns.

### The Funnel Approach

Move from general to specific within each topic. Broad questions first, detailed follow-ups after. This prevents early specific questions from biasing how respondents think about later general ones.

**Example flow for a health section:**
1. "How would you describe your general health?" (general)
2. "Have you been sick in the last 30 days?" (more specific)
3. "What was the illness?" (specific follow-up, conditional on #2)
4. "Did you seek treatment?" (even more specific)

### Sequencing Rules

1. **Start simple and build rapport.** Begin with easy, non-threatening questions directly related to the survey's stated purpose. The first question is the most important for determining whether the respondent will cooperate through the rest.

2. **Group by topic.** Keep all questions about the same subject together. Use Fulcrum Sections to create clear topic boundaries. Add transitional text in Section labels or Label fields: "Kounye a, m pral poze ou kèk kesyon sou edikasyon..." (Now I'm going to ask you some questions about education...).

3. **Place demographics and sensitive questions last.** Age, income, marital status, and other personal classification data go at the end. By this point, the respondent has invested time and built trust, making them more likely to answer honestly. The exception: demographic questions needed for skip logic (like age for an adult-only section) should go wherever the logic requires them.

4. **Use screening questions early.** If the survey only applies to certain respondents (e.g., households with children under 5), place the screening question before the irrelevant sections and use skip logic to route past them.

5. **End with the open-ended closing question.** Give respondents a final chance to share anything not covered (the `make_closing_question` builder handles this).

### Section Design in Fulcrum

Each Fulcrum Section should map to one coherent topic. A typical household survey structure:

1. **Konsantman ak Idantifikasyon** (Consent & Identification) -- consent, enumerator ID, date, location
2. **Enfòmasyon sou Kay la** (Household Information) -- household head, household size, housing type
3. **Demografik** (Demographics) -- repeatable for household members
4. **[Thematic sections]** -- water/sanitation, health, education, livelihoods, etc.
5. **Obsèvasyon Anketè** (Enumerator Observations) -- things the enumerator notes visually
6. **Kesyon Final** (Final Questions) -- demographics not yet captured, sensitive questions, closing open-ended question

---

## 5. Mobile-Specific UI/UX Optimization

Fulcrum runs on phones and tablets with limited screen real estate. Design choices that work on paper can fail on mobile.

### Avoid Grids and Matrices

Paper questionnaires often use grid layouts (rows of items, columns of response options). On mobile screens, these require horizontal scrolling, cause misalignment errors, and frustrate enumerators. Convert every grid into an item-by-item format where each row becomes its own ChoiceField or YesNoField.

### Input Field Optimization

- **Radio buttons (ChoiceField, single):** Use for 2-7 options. All options visible at once.
- **Drop-down equivalent:** For long lists (8+ options), Fulcrum displays a scrollable picker. Consider ClassificationField for hierarchical lists.
- **Forced-choice format:** For "check all that apply" with fewer than 8 items, use separate YesNoFields instead of a multi-select ChoiceField (see Question Types section above).

### Minimize Typing

In field conditions (rain, sun glare, dust), typing on a phone is slow and error-prone. Prefer ChoiceFields and YesNoFields over TextFields wherever possible. When a TextField is necessary, use numeric mode with min/max constraints to reduce keystrokes and prevent out-of-range values.

### Leverage Device Sensors

- **GPS:** Auto-capture coordinates on new-record via data events. Use `LATITUDE()` / `LONGITUDE()` rather than asking enumerators to type locations.
- **Camera:** Use PhotoField for visual verification (housing condition, water source, infrastructure).
- **Timestamps:** Auto-populate survey start/end times to monitor interview duration (a key paradata indicator of data quality).

---

## 6. Validation and Error Prevention

Mobile platforms allow real-time validation that paper cannot. Use it aggressively.

### Numeric Bounds

Set `min` and `max` on every numeric TextField. Think about realistic bounds:
- Age: min=0, max=120
- Household size: min=1, max=30
- Number of meals per day: min=0, max=10
- Income (monthly HTG): min=0, max=500000

### Cross-Field Logic Checks

Use `validate-record` data events to catch inconsistencies before the record is saved:

```javascript
// Age of marriage cannot exceed current age
if (NUM($age_marriage) > NUM($age_current)) {
  INVALID('Laj maryaj pa ka pi gran pase laj aktyèl.');
}

// If respondent has children, number must be > 0
if ($has_children === 'wi' && (!$number_children || NUM($number_children) < 1)) {
  INVALID('Si moun nan gen pitit, kantite a dwe pi gran pase 0.');
}
```

### Required Fields Strategy

Make fields required when missing data would compromise the analysis. But don't make everything required; it leads to enumerators entering garbage data just to advance. A good rule: required for primary outcome variables and key demographics; optional for supplementary detail and open-ended responses.

### GPS Validation

For surveys where location matters (household visits, infrastructure inspections), validate that GPS is captured:

```javascript
ON('validate-record', function(event) {
  if (!LATITUDE() || !LONGITUDE()) {
    INVALID('Pozisyon GPS obligatwa. Tann GPS fikse anvan sove.');
  }
});
```

---

## 7. The 6-Phase Mobile Questionnaire Pipeline

Building a field-ready mobile questionnaire is not a single step. It follows a structured pipeline where each phase has distinct goals, outputs, and quality gates.

### Phase 1: Define
**Goal:** Translate research questions into operational variables.

- Identify research objectives and the decisions the data will inform
- List every variable needed, classify each using the Subtraction and Mid-Way tests
- Identify dependent vs. independent variables; note confounders and controls
- Choose validated instruments where available (don't reinvent scales)
- Determine administration mode: enumerator-administered (CAPI) or self-administered
- **Output:** Variable list with classifications and target Fulcrum field types

### Phase 2: Draft
**Goal:** Write questions and response options.

- Apply question wording principles (one concept per question, no leading, no vague qualifiers)
- Design response scales (5-7 points for attitudes, numeric for counts)
- Determine forced-choice vs. check-all-that-apply for each multi-item question
- Write enumerator instructions (field descriptions) for every data-collection field
- **Output:** Draft questionnaire in natural language with field type annotations

### Phase 3: Format
**Goal:** Optimize for mobile delivery.

- Convert grids/matrices to item-by-item format
- Minimize typing (prefer choice fields and yes/no fields)
- Reduce cognitive load: one question per screen, clear visual hierarchy
- Set touch-target-friendly layouts (avoid cramped multi-column designs)
- Add standardized enumerator cues in descriptions: "LI TOUT CHWA YO" (read all options), "PA SOUFLE REPONS" (don't prompt)
- **Output:** Mobile-formatted questionnaire ready for Fulcrum implementation

### Phase 4: Route
**Goal:** Implement skip logic and sequencing.

- Apply the funnel approach within each topic section
- Place screening questions before conditional sections
- Implement skip logic using `visible_conditions` or `SETHIDDEN()` data events
- Ensure interview momentum: respondents should never see obviously irrelevant questions
- Add validation rules (numeric bounds, cross-field consistency checks, GPS requirement)
- **Output:** Fulcrum .fulcrumapp file with complete routing logic

### Phase 5: Test
**Goal:** Validate the instrument before field deployment.

- Run through the 4-Stage Validation Funnel (see below)
- Fix identified issues and re-test if changes are significant
- **Output:** Field-tested, revised questionnaire

### Phase 6: Deploy
**Goal:** Launch data collection with quality monitoring.

- Train enumerators on the app interface and question interpretation
- Deploy to devices and verify sync
- Monitor paradata (duration, GPS, timestamps, enumerator patterns)
- Establish daily supervisor review cycles
- **Output:** Live data collection with active QA

## 8. The 4-Stage Validation Funnel

Each stage catches different types of problems. Skipping stages means shipping bugs.

### Stage 1: Expert Review
**Who:** Subject matter experts, survey methodologists
**What:** Review questionnaire for content validity, variable classification accuracy, question wording, scale design, and logical flow. Check that every research question maps to at least one form field.
**Catches:** Conceptual errors, missing variables, double-barreled questions, inappropriate field types

### Stage 2: Cognitive Interviews
**Who:** 5-10 respondents from the target population
**What:** "Think-aloud" protocol where respondents verbalize their thought process as they answer. The interviewer probes: "What does this question mean to you?" "How did you arrive at that answer?"
**Catches:** Ambiguous wording, cultural misinterpretation, response options that don't match how people actually think about the topic

### Stage 3: Behavior Coding
**Who:** 3-5 trained enumerators conducting real interviews while a coder observes
**What:** Systematic coding of interviewer-respondent interaction. Track: questions read exactly as written vs. modified, requests for clarification, inadequate answers, enumerator probing behavior.
**Catches:** Questions that enumerators consistently rephrase (indicating poor wording), response options that don't match natural answers, skip logic errors

### Stage 4: Live Pilot
**Who:** 15-30 respondents under realistic field conditions
**What:** Full dress rehearsal with the Fulcrum app on target devices. Monitor completion time, "Lot" (Other) selection frequency, skip logic paths, app performance, GPS capture, sync behavior.
**Catches:** Technical bugs, missing response categories (high Lot rates), unrealistic completion time, device/connectivity issues

### Quick Reference: What Each Stage Catches

| Problem Type | Expert Review | Cognitive | Behavior Coding | Live Pilot |
|---|---|---|---|---|
| Missing variables | X | | | |
| Wrong field types | X | | | |
| Ambiguous wording | X | X | X | |
| Cultural issues | | X | | |
| Enumerator errors | | | X | |
| Skip logic bugs | X | | | X |
| Missing categories | | X | | X |
| Timing problems | | | | X |
| Device/tech issues | | | | X |

## 9. Pilot Testing and Quality Assurance

Never field an untested questionnaire. At minimum, complete Stages 1 and 4 of the Validation Funnel above. Ideally complete all four stages.

### Pilot Testing Protocol (Stage 4 Detail)

1. **Sample:** 15-30 respondents from the target population under realistic field conditions
2. **Method:** Full data collection simulation with Fulcrum app on target devices
3. **What to check:**
   - Do respondents understand every question as intended?
   - Are response options exhaustive? (Track how often "Lot" is selected -- high Lot rates indicate missing categories)
   - Does skip logic work correctly in all paths?
   - How long does the full interview take? (Target: under 25 minutes for ADF Haiti household surveys, under 45 minutes for complex assessments)
   - Does the app perform well on target devices? Does GPS lock in reasonable time?
   - Does data sync correctly over available connectivity?
4. **Iterate:** Revise questions, add missing choice options, adjust skip logic, and pilot again if changes are significant.

### Enumerator Training

- Train on the app's interface, not just the questionnaire content
- Practice reading questions uniformly without altering wording
- Teach non-directive probing: "Can you tell me more?" rather than suggesting answers
- Role-play difficult scenarios (refusals, ambiguous answers, edge cases)

### Ongoing Quality Control (Paradata)

Once data collection begins, monitor:

- **GPS coordinates:** Are interviews happening at the correct locations?
- **Interview duration:** Too short (< 15 min for a 45-min survey) suggests skipping or fabrication. Too long may indicate enumerator confusion.
- **Timestamps:** Interviews at unusual hours may be suspect.
- **"Lot" (Other) frequency:** High rates suggest missing response categories that should be added.
- **Back-checks:** Re-contact 10% of respondents (randomly selected) to verify key responses.
- **Enumerator patterns:** Compare response distributions across enumerators to detect systematic bias.

### Supervisor-to-Enumerator Ratio

Maintain 1 supervisor for every 5-10 enumerators. Supervisors review completed records daily, check for patterns (e.g., one enumerator always selecting the same responses), and address issues before they compound.

### Field QA Checklist

Before each data collection session, verify:
- [ ] All devices have the latest form version synced
- [ ] GPS is enabled and acquiring a fix
- [ ] Battery is sufficient for the session (>50%)
- [ ] Offline mode is working (test by toggling airplane mode)
- [ ] Enumerator understands the day's route and target sample

---

## 10. Sampling Considerations

While sampling design is typically decided before the Fulcrum form is built, the form itself needs to support the chosen methodology.

### Sampling Methods

- **Simple Random:** Every unit has equal selection chance. The form needs a unique ID field to link to the sampling frame.
- **Stratified:** Population divided into subgroups (strata); random sampling within each. Include a stratum identifier field in the form.
- **Cluster:** Pre-existing groups selected (e.g., villages), then all or a sample within. Include cluster ID in the form.
- **Systematic:** Every nth unit selected. The form needs a sequence counter or the enumerator follows a predetermined list.

### Sample Size Awareness

The form doesn't calculate sample size, but the designer should know the target. Undersized samples produce underpowered studies; oversized samples waste resources. Key factors:

- **Level of significance (alpha):** Typically 0.05
- **Power (1-beta):** Minimum 0.80 recommended
- **Effect size:** Smaller expected effects require larger samples
- **Variance:** Higher outcome variation requires more data points

**Rule of thumb:** For populations above 20,000, the population size itself doesn't significantly affect the required sample size. If the population is unknown, assume 20,000+.

### Form Fields That Support Sampling

Always include:
- Unique respondent/household ID (links to sampling frame)
- Cluster/stratum identifiers (for complex sampling designs)
- Enumerator ID (for inter-rater reliability analysis)
- GPS coordinates (for spatial sampling verification)
- Interview start/end timestamps (for paradata analysis)
