# .fulcrumapp Schema Rules

This is the authoritative reference for building .fulcrumapp JSON files that import successfully into Fulcrum. These property lists were reverse-engineered from working exported files and verified through multiple import cycles.

**The golden rule: every field type MUST include ALL properties listed below, even when the value is null or false. Missing properties cause silent 500 errors on import.**

## Table of Contents

1. [Form-Level Structure](#form-level-structure)
2. [StatusField](#statusfield)
3. [Section](#section)
4. [TextField](#textfield)
5. [ChoiceField](#choicefield)
6. [YesNoField](#yesnofield)
7. [DateTimeField](#datetimefield)
8. [Label](#label)
9. [PhotoField](#photofield)
10. [SignatureField](#signaturefield)
11. [AddressField](#addressfield)
12. [CalculatedField](#calculatedfield)
13. [ClassificationField](#classificationfield)
14. [RecordLinkField](#recordlinkfield)
15. [Repeatable](#repeatable)
16. [visible_conditions Format](#visible_conditions-format)
17. [Builder Function Pattern](#builder-function-pattern)

---

## Form-Level Structure

The .fulcrumapp file is a JSON object with a `form` key:

```json
{
  "form": {
    "name": "Survey Name",
    "description": "Survey description",
    "record_title_key": "a001",
    "title_field_keys": ["a001"],
    "auto_assign": false,
    "hidden_on_dashboard": false,
    "geometry_types": ["Point", "MultiPoint"],
    "geometry_required": false,
    "script": null,
    "status_field": { ... },
    "elements": [ ... ]
  }
}
```

**Required form properties:**
- `name` (string)
- `description` (string, can be empty)
- `record_title_key` (string) -- key of the field used as record title
- `title_field_keys` (array of strings) -- keys composing the title
- `auto_assign` (boolean)
- `hidden_on_dashboard` (boolean)
- `geometry_types` (array) -- typically `["Point"]`
- `geometry_required` (boolean)
- `script` (string or null) -- data events JavaScript
- `status_field` (object) -- StatusField definition
- `elements` (array) -- array of Section objects

---

## StatusField

13 properties. Always present at form level.

```json
{
  "type": "StatusField",
  "key": "@status",
  "label": "Status",
  "data_name": "status",
  "default_value": "in_progress",
  "enabled": true,
  "read_only": false,
  "hidden": false,
  "description": "",
  "choices": [
    {"label": "In Progress", "value": "in_progress", "color": "#CB0D0C"},
    {"label": "Complete", "value": "complete", "color": "#87D30F"}
  ],
  "required": false,
  "disabled": false,
  "default_previous_value": false
}
```

**Fixed values:** `key` must be `"@status"`, `data_name` must be `"status"`, `type` must be `"StatusField"`.

---

## Section

16 properties. Top-level container for fields.

```json
{
  "type": "Section",
  "key": "s001",
  "label": "Section Title",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "section_name",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "display": "inline",
  "elements": []
}
```

**Key properties:**
- `display`: always `"inline"` (or `"drilldown"` for collapsible sections)
- `elements`: array of field objects nested inside this section
- `required`, `disabled`, `hidden`: must be present even as false

---

## TextField

21+ properties depending on numeric mode.

```json
{
  "type": "TextField",
  "key": "a001",
  "label": "Field Label",
  "description": null,
  "required": true,
  "disabled": false,
  "hidden": false,
  "data_name": "field_name",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "ai_prompt": null,
  "numeric": false,
  "pattern": null,
  "pattern_description": null,
  "min_length": null,
  "max_length": null,
  "default_previous_value": false,
  "min": null,
  "max": null,
  "format": null
}
```

**For numeric text fields:**
- Set `numeric: true`
- Set `format: "integer"` or `"decimal"`
- Use `min` and `max` for value constraints

---

## ChoiceField

17 properties (inline choices) or 17 properties (shared choice_list_schema).

```json
{
  "type": "ChoiceField",
  "key": "c001",
  "label": "Choose one",
  "description": null,
  "required": true,
  "disabled": false,
  "hidden": false,
  "data_name": "choice_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "ai_prompt": null,
  "multiple": false,
  "allow_other": false,
  "choices": [
    {"label": "Option A", "value": "Option A"},
    {"label": "Option B", "value": "Option B"},
    {"label": "Lòt", "value": "Lot"}
  ],
  "default_previous_value": false
}
```

**With shared choice list (alternative to inline choices):**
```json
{
  "type": "ChoiceField",
  "key": "c001",
  "label": "Ki sous revni prensipal ou",
  "data_name": "income_source",
  "ai_prompt": null,
  "multiple": false,
  "allow_other": false,
  "default_previous_value": false,
  "choice_list_schema": {
    "name": "Aktivite Ekonomik",
    "description": "",
    "version": 1,
    "choices": [
      {"label": "Agrikiltè", "value": "agrikilte"},
      {"label": "Machann - Komèsan", "value": "machann_komesan"}
    ]
  }
}
```

**Critical:** `multiple` MUST be present even when `false`. `allow_other` should always be `false` -- use the "Lot" pattern instead (add `"Lòt"` as a choice and create a conditional TextField). ADF convention: choice labels use proper Creole with accent marks (è, ò, à), but choice values are always accent-stripped, lowercase ASCII (e.g., label `"Agrikiltè"` → value `"agrikilte"`).

---

## YesNoField

20 properties.

```json
{
  "type": "YesNoField",
  "key": "y001",
  "label": "Èske ou dakò",
  "description": null,
  "required": true,
  "disabled": false,
  "hidden": false,
  "data_name": "yes_no_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "ai_prompt": null,
  "positive": {"label": "Wi", "value": "wi"},
  "negative": {"label": "Non", "value": "non"},
  "neutral": {"label": "Pa Aplikab", "value": "pa_aplikab"},
  "neutral_enabled": true,
  "default_previous_value": false
}
```

**Critical:** `neutral` and `neutral_enabled` MUST be present. For ADF Haitian Creole surveys, always set `neutral_enabled: true` with `"Pa Aplikab"/"pa_aplikab"` as the neutral option. Use `"Wi"/"wi"` and `"Non"/"non"` for positive/negative. The `ai_prompt` property must be included.

---

## DateTimeField

15 properties.

```json
{
  "type": "DateTimeField",
  "key": "d001",
  "label": "Date",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "date_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "default_previous_value": false
}
```

---

## Label

14 properties. Display-only text with no data storage.

```json
{
  "type": "Label",
  "key": "l001",
  "label": "Instructional text here...",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "label_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null
}
```

**Note:** Label does NOT have `default_previous_value`.

---

## PhotoField

Standard common properties plus:

```json
{
  "type": "PhotoField",
  "key": "p001",
  "label": "Take Photo",
  "description": "Take at least 2 photos",
  "required": true,
  "disabled": false,
  "hidden": false,
  "data_name": "photo_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "min_length": 2,
  "max_length": null,
  "default_previous_value": false
}
```

---

## SignatureField

Standard common properties plus:

```json
{
  "type": "SignatureField",
  "key": "sig001",
  "label": "Signature",
  "description": null,
  "required": true,
  "disabled": false,
  "hidden": false,
  "data_name": "signature_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "agreement_text": "I confirm the information is accurate.",
  "default_previous_value": false
}
```

---

## AddressField

Standard common properties plus:

```json
{
  "type": "AddressField",
  "key": "addr001",
  "label": "Address",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "address_field",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "auto_populate": false,
  "default_previous_value": false
}
```

---

## CalculatedField

Standard common properties plus `expression`:

```json
{
  "type": "CalculatedField",
  "key": "calc001",
  "label": "Total Score",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "total_score",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "expression": "NUM($score_a) + NUM($score_b)",
  "default_previous_value": false
}
```

---

## ClassificationField

Standard common properties plus `classification_set_schema`:

```json
{
  "type": "ClassificationField",
  "key": "cls001",
  "label": "Category",
  "description": null,
  "required": true,
  "disabled": false,
  "hidden": false,
  "data_name": "category",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "allow_other": false,
  "classification_set_schema": {
    "name": "Categories",
    "description": "",
    "version": 1,
    "items": [
      {
        "label": "Category A",
        "value": "category_a",
        "child_classifications": [
          {"label": "Sub A1", "value": "sub_a1", "child_classifications": []}
        ]
      }
    ]
  },
  "default_previous_value": false
}
```

---

## RecordLinkField

Standard common properties plus linking configuration:

```json
{
  "type": "RecordLinkField",
  "key": "rl001",
  "label": "Linked Record",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "linked_record",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "allow_creating_records": false,
  "allow_existing_records": true,
  "allow_updating_records": false,
  "allow_multiple_records": false,
  "record_conditions_type": null,
  "record_conditions": null,
  "record_defaults": null,
  "default_previous_value": false
}
```

---

## Repeatable

Container for child records (household members, inventory items, etc.). Repeatable is a TOP-LEVEL element in the form's `elements` array -- it is a sibling to Section, NOT nested inside one.

15 properties.

```json
{
  "type": "Repeatable",
  "key": "60a0",
  "label": "Enfòmasyon Endividyèl",
  "description": null,
  "required": false,
  "disabled": false,
  "hidden": false,
  "data_name": "household_members",
  "default_value": null,
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null,
  "required_conditions_type": null,
  "required_conditions": null,
  "elements": [
    {
      "type": "TextField",
      "key": "4800",
      "label": "Prenon",
      "data_name": "first_name",
      "...": "... (all standard TextField properties)"
    },
    {
      "type": "ChoiceField",
      "key": "266c",
      "label": "Relasyon ak chèf kay la",
      "data_name": "relationship",
      "...": "... (all standard ChoiceField properties)"
    }
  ]
}
```

**Key rules:**
- Repeatable is placed at the TOP LEVEL of form.elements, same level as Section objects
- Fields inside `elements` follow the same property rules as any other field
- Visible_conditions can be applied to the Repeatable itself (e.g., only show household roster if consent is given)
- Max practical nesting: 2 levels (parent > child > grandchild). Deeper nesting causes import/export failures.
- Max ~60 child records per parent for mobile performance
- Max ~35 fields per repeatable row for usability

### Household Survey Repeatable Pattern

A typical census household roster repeatable contains these fields:
1. Label with instructions
2. TextField: First name (prenon)
3. TextField: Last name (siyati)
4. ChoiceField: Relationship to head (chèf kay, madanm/mari, pitit, lòt fanmi...)
5. ChoiceField: Sex (Fi, Gason)
6. TextField (numeric): Year of birth or age
7. ChoiceField: Marital status
8. ChoiceField: Education level
9. ChoiceField: Employment with "Lòt" pattern
10. Additional context-specific questions with skip logic

---

## visible_conditions Format

When using skip logic, include ALL THREE sibling properties:

**Active (field has conditions):**
```json
{
  "visible_conditions_type": "all",
  "visible_conditions_behavior": "clear",
  "visible_conditions": [
    {"field_key": "c004", "operator": "equal_to", "value": "wi"}
  ]
}
```

**Inactive (no conditions):**
```json
{
  "visible_conditions_type": null,
  "visible_conditions_behavior": "clear",
  "visible_conditions": null
}
```

`visible_conditions_type`: `"all"` (AND logic) or `"any"` (OR logic)
`visible_conditions_behavior`: always `"clear"` (clears hidden field values)

**Operators:** `equal_to`, `not_equal_to`, `is_not_empty`, `is_empty`, `contains`, `greater_than`, `less_than`

---

## Builder Function Pattern

Always use Python builder functions to generate .fulcrumapp files. Here is a complete set:

```python
import json, uuid, unicodedata, re

def hk():
    """Generate a random 4-character hex key matching Fulcrum's format."""
    return uuid.uuid4().hex[:4]

def strip_creole_accents(text):
    """Convert accented Creole text to ASCII-safe data name or choice value.
    Strips accents (è→e, ò→o, à→a), lowercases, replaces spaces/hyphens
    with underscores, and removes non-alphanumeric characters.
    Example: 'Èske moun nan toujou al lekòl' → 'eske_moun_nan_toujou_al_lekol'
    Example: 'Selibatè (poko janm marye)' → 'selibate_poko_janm_marye'"""
    nfkd = unicodedata.normalize('NFKD', text)
    ascii_text = ''.join(c for c in nfkd if not unicodedata.combining(c))
    ascii_text = ascii_text.lower().strip()
    ascii_text = re.sub(r'[\s\-]+', '_', ascii_text)
    ascii_text = re.sub(r'[^a-z0-9_]', '', ascii_text)
    ascii_text = re.sub(r'_+', '_', ascii_text).strip('_')
    return ascii_text

def _vc(visible_conditions):
    """Helper: return visible_conditions_type based on whether conditions exist."""
    return "all" if visible_conditions else None

def make_section(key, label, data_name, elements, description=None, 
                 visible_conditions=None, display="inline"):
    return {
        "type": "Section", "key": key, "label": label,
        "description": description, "required": False,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "display": display, "elements": elements
    }

def make_text(key, label, data_name, description, required=True,
              numeric=False, format_type=None, pattern=None,
              pattern_description=None, min_val=None, max_val=None,
              visible_conditions=None):
    return {
        "type": "TextField", "key": key, "label": label,
        "description": description, "required": required,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "ai_prompt": None,
        "numeric": numeric, "pattern": pattern,
        "pattern_description": pattern_description,
        "min_length": None, "max_length": None,
        "default_previous_value": False,
        "min": min_val, "max": max_val, "format": format_type
    }

def make_choice(key, label, data_name, choices, description, required=True,
                multiple=False, visible_conditions=None,
                include_lot=False):
    """Build a ChoiceField. Set include_lot=True to append 'Lòt' as last option.
    choices: list of (label, value) tuples. Always use tuples for Creole forms
    so labels keep accents while values are accent-stripped ASCII.
    Example: [("Agrikiltè", "agrikilte"), ("Machann", "machann")]"""
    choice_list = []
    for c in choices:
        if isinstance(c, tuple):
            choice_list.append({"label": c[0], "value": c[1]})
        else:
            choice_list.append({"label": c, "value": c})
    if include_lot:
        choice_list.append({"label": "Lòt", "value": "Lot"})
        choice_list.append({"label": "Pa Aplikab", "value": "pa_aplikab"})
    return {
        "type": "ChoiceField", "key": key, "label": label,
        "description": description, "required": required,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "ai_prompt": None,
        "multiple": multiple, "allow_other": False,
        "choices": choice_list,
        "default_previous_value": False
    }

def make_lot_text(key, parent_key, parent_label, parent_data_name,
                  visible_conditions=None):
    """Build the conditional 'Lot' TextField that pairs with a ChoiceField.
    Automatically sets visible_conditions to show when parent = 'Lot'."""
    lot_vc = [{"field_key": parent_key, "operator": "equal_to", "value": "Lot"}]
    if visible_conditions:
        lot_vc = visible_conditions + lot_vc
    return make_text(
        key=key, label=parent_label + " - Lot",
        data_name=parent_data_name + "_lot",
        description="Si ou te chwazi 'Lòt' nan kesyon anvan an, ekri repons la isit.",
        required=False, visible_conditions=lot_vc
    )

def make_yesno(key, label, data_name, description, required=True,
               visible_conditions=None, positive_label="Wi",
               positive_value="wi", negative_label="Non",
               negative_value="non", neutral_label="Pa Aplikab",
               neutral_value="pa_aplikab", neutral_enabled=True):
    return {
        "type": "YesNoField", "key": key, "label": label,
        "description": description, "required": required,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "ai_prompt": None,
        "positive": {"label": positive_label, "value": positive_value},
        "negative": {"label": negative_label, "value": negative_value},
        "neutral": {"label": neutral_label, "value": neutral_value},
        "neutral_enabled": neutral_enabled, "default_previous_value": False
    }

def make_datetime(key, label, data_name, description=None, required=False,
                  visible_conditions=None):
    return {
        "type": "DateTimeField", "key": key, "label": label,
        "description": description, "required": required,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "ai_prompt": None,
        "default_previous_value": False
    }

def make_label(key, label, data_name, description=None,
               visible_conditions=None):
    """Labels do NOT have ai_prompt or default_previous_value."""
    return {
        "type": "Label", "key": key, "label": label,
        "description": description, "required": False,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None
    }

def make_photo(key, label, data_name, description=None, required=False,
               min_photos=None, visible_conditions=None):
    return {
        "type": "PhotoField", "key": key, "label": label,
        "description": description, "required": required,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "ai_prompt": None,
        "min_length": min_photos, "max_length": None,
        "default_previous_value": False
    }

def make_repeatable(key, label, data_name, elements, description=None,
                    visible_conditions=None):
    """Build a Repeatable section (top-level, NOT inside a Section).
    Used for household rosters, inventories, etc."""
    return {
        "type": "Repeatable", "key": key, "label": label,
        "description": description, "required": False,
        "disabled": False, "hidden": False, "data_name": data_name,
        "default_value": None, "visible_conditions_type": _vc(visible_conditions),
        "visible_conditions_behavior": "clear",
        "visible_conditions": visible_conditions,
        "required_conditions_type": None, "required_conditions": None,
        "elements": elements
    }

def make_section_notes(key, section_label, section_data_name):
    """Add to the end of every section. Provides a free-text field for
    extra info, respondent commentary, or enumerator observations."""
    return make_text(
        key, "Lòt enfòmasyon / Komantè",
        section_data_name + "_notes",
        description="Espas pou anrejistre nenpòt lòt enfòmasyon, komantè, "
                    "oswa obsèvasyon ki gen rapò ak seksyon sa a. "
                    "Sa ka soti nan moun k ap reponn lan oswa nan obsèvasyon anketè a.",
        required=False
    )

def make_closing_question(key, topic=None):
    """Add as the last field in the final section of interview-style forms.
    Pass topic (in Creole) to customize, or leave None for generic version."""
    if topic:
        label = f"Èske gen lòt bagay ou ta renmen pataje sou {topic}?"
        data_name = "lot_bagay_sou_" + strip_creole_accents(topic)
    else:
        label = "Èske gen lòt bagay ou ta renmen ajoute?"
        data_name = "lot_bagay_ajoute"
    return make_text(
        key, label, data_name,
        description="Kesyon ouvè pou bay moun k ap reponn lan yon dènye chans "
                    "pou pataje nenpòt bagay ki pa t kouvri nan sondaj la. "
                    "Ekri repons lan mo pou mo si posib.",
        required=False
    )

def make_status_field(choices, default_value, enabled=True, label="Estati"):
    return {
        "type": "StatusField", "key": "@status", "label": label,
        "data_name": "status", "default_value": default_value,
        "enabled": enabled, "read_only": False, "hidden": False,
        "description": "",
        "choices": [{"label": c[0], "value": c[1], "color": c[2]} 
                    for c in choices],
        "required": False, "disabled": False,
        "default_previous_value": False
    }

def make_form(name, description, elements, status_field,
              record_title_key, title_field_keys, script=None):
    return {
        "form": {
            "name": name, "description": description,
            "record_title_key": record_title_key,
            "title_field_keys": title_field_keys,
            "auto_assign": False, "hidden_on_dashboard": False,
            "geometry_types": ["Point", "MultiPoint"], "geometry_required": False,
            "script": script, "status_field": status_field,
            "elements": elements
        }
    }
```

### Usage

```python
# Creole status field
status = make_status_field(
    [("Annatant", "annatant", "#FF8819"),
     ("Fini", "fini", "#87D30F"),
     ("Pa Konple", "pa_konple", "#CB0D0C")],
    "annatant"
)

# Generate random hex keys
k1, k2, k3, k4, k5, k6 = [hk() for _ in range(6)]

elements = [
    # Sections contain fields, with section_notes at the end
    make_section("s001", "Demografik", "section_demographics", [
        make_text(k1, "Non", "respondent_name",
                  description="Non konplè moun k ap reponn lan. Mande pou non fanmi tou."),
        make_text(k2, "Ki laj ou", "age",
                  description="Laj an ane konplè. Si moun nan pa konnen, estime ak lane nesans.",
                  numeric=True, format_type="integer", min_val=0, max_val=120),
        # Choice with Lot + Pa Aplikab pattern
        make_choice(k3, "Ki sous revni prensipal ou", "sous_revni_prensipal",
                    [("Agrikiltè", "agrikilte"), ("Machann", "machann"), ("Pwofesè", "pwofese")],
                    description="Sous revni ki pi enpòtan pou fanmi an. Chwazi yon sèl.",
                    include_lot=True),
        make_lot_text(k4, k3, "Ki sous revni prensipal ou", "sous_revni_prensipal"),
        # Section commentary field at the end of every section
        make_section_notes(hk(), "Demografik", "section_demographics"),
    ]),
    # Repeatable at top level (NOT inside Section)
    make_repeatable(hk(), "Manm Kay la", "household_members", [
        make_text(k5, "Prenon", "member_name",
                  description="Prenon ak non fanmi manm kay la."),
        make_choice(k6, "Sèks", "member_sex", [("Fi", "fi"), ("Gason", "gason")],
                    description="Sèks biyolojik manm nan."),
    ]),
    # Closing section for interview-style surveys
    make_section(hk(), "Pou Fini", "section_pou_fini", [
        make_closing_question(hk()),
        make_section_notes(hk(), "Pou Fini", "section_pou_fini"),
    ]),
]

form = make_form(
    "Sondaj Ménaj", "Sondaj nan Fondèblan",
    elements, status, k1, [k1]
)

with open("my_survey.fulcrumapp", "w") as f:
    json.dump(form, f, indent=2, ensure_ascii=False)
```
