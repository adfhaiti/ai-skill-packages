# Fulcrum Data Events Reference

Data events are JavaScript functions that run inside Fulcrum forms to add dynamic behavior: auto-populating fields, cascading visibility, validation, HTTP requests, and more. The script goes in the form-level `script` property of the .fulcrumapp JSON.

## Table of Contents

1. [Event Handlers](#event-handlers)
2. [Event Types](#event-types)
3. [Field Modification Functions](#field-modification-functions)
4. [User Interface Functions](#user-interface-functions)
5. [Status and Project Functions](#status-and-project-functions)
6. [Utility Functions](#utility-functions)
7. [Integration Functions](#integration-functions)
8. [Common Patterns](#common-patterns)

---

## Event Handlers

### ON(event, [field_data_name], callback)
Attach a callback to a form or field event.

```javascript
// Form-level event
ON('load-record', function(event) { ... });

// Field-level event (use data_name, not key)
ON('change', 'field_data_name', function(event) { ... });
```

### OFF(event, [field_data_name], callback)
Detach a previously attached callback.

---

## Event Types

### Record-Level Events
| Event | Fires When |
|-------|-----------|
| `load-record` | Record loads for viewing/editin || Record editor displayed (both new and existing) |
| `new-record` | Creating a new record |
| `edit-record` | Editing an existing record |
| `save-record` | Before record saved (after validation passes) |
| `validate-record` | During record validation (use INVALID() to prevent save) |
| `cancel-record` | Editing cancelled by user |
| `unload-record` | Record editor closed || Record is unloaded |
| `change-geometry` | Record GPS/location changes |
| `change-project` | Record's project assignment changes |
| `change-status` | Record's status changes |

### Field-Level Events
| Event | Fires When |
|-------|-----------|
| `change` | Field value changes (requires field_data_name) |
| `focus` | Text/numeric input gains focus |
| `blur` | Text/numeric input loses focus |
| `click` | Hyperlink field is tapped |
| `add-photo` | Photo is added to a photo field |
| `change-audio` | Audio is captured |
| `change-video` | Video is captured |

### Repeatable Events
| Event | Fires When | Signature |
|-------|-----------|-----------|
| `load-repeatable` | Repeatable editor displayed | `ON('load-repeatable', 'data_name', callback)` |
| `new-repeatable` | New repeatable row created | `ON('new-repeatable', 'data_name', callback)` |
| `edit-repeatable` | Existing repeatable row opened | `ON('edit-repeatable', 'data_name', callback)` |
| `save-repeatable` | Before repeatable row saved | `ON('save-repeatable', 'data_name', callback)` |
| `validate-repeatable` | Before save, for validations | `ON('validate-repeatable', 'data_name', callback)` |
| `add-repeatable` | Repeatable row added | `ON('add-repeatable', 'data_name', callback)` |
| `remove-repeatable` | Repeatable row removed | `ON('remove-repeatable', 'data_name', callback)` |

**Important:** Repeatable events always require the repeatable's `data_name` as the second parameter.

---

## Field Modification Functions

### SETVALUE(field_data_name, value)
Set a field's value programmatically.

```javascript
SETVALUE('respondent_name', 'John Doe');
SETVALUE('score', 85);
SETVALUE('consent', 'yes');
SETVALUE('survey_date', new Date().toISOString().split('T')[0]);
```

### SETHIDDEN(field_data_name, boolean)
Show or hide a field dynamically.

```javascript
SETHIDDEN('electricity_source', true);   // hide
SETHIDDEN('electricity_source', false);  // show
```

### SETREQUIRED(field_data_name, boolean)
Make a field required or optional dynamically.

```javascript
SETREQUIRED('phone_number', $has_phone === 'yes');
```

### SETREADONLY(field_data_name, boolean)
Make a field read-only or editable.

### SETLABEL(field_data_name, string_or_null)
Override a field's label text. Pass null to reset to original.

```javascript
SETLABEL('weather_summary', 'Current Weather Conditions');
SETLABEL('weather_summary', null);  // reset
```

### SETDESCRIPTION(field_data_name, string_or_null)
Set or clear a field's help/description text.

### SETCHOICES(field_data_name, choices_array)
Dynamically set choice field options.

```javascript
SETCHOICES('status_field', [
  { label: 'Active', value: 'active' },
  { label: 'Inactive', value: 'inactive' }
]);
```

### SETCHOICEFILTER(field_data_name, values_array)
Filter which choices are visible. Values are partial matches.

```javascript
SETCHOICEFILTER('weather_summary', ['sunny', 'cloudy']);
```

### SETMINLENGTH(field_data_name, number_or_null)
Set minimum length/count for a field.

### SETMAXLENGTH(field_data_name, number_or_null)
Set maximum length/count for a field.

### SETGEOMETRY(geometry_object)
Set a field's geometry (for location fields).

```javascript
SETGEOMETRY({ type: 'Point', coordinates: [-73.9857, 40.7484] });
```

### SETLOCATION(latitude, longitude)
Set the record's location.

```javascript
SETLOCATION(18.2208, -73.7539);  // Fond-des-Blancs
```

---

## User Interface Functions

### ALERT(title, message)
Display a message alert.

```javascript
ALERT('Warning', 'Please verify the GPS coordinates.');
```

### CONFIRM(title, message, callback)
Display a confirmation dialog. Callback receives `{value: 'Okay'}` or `{value: 'Cancel'}`.

```javascript
CONFIRM('Confirm', 'Are you sure?', function(result) {
  if (result.value === 'Okay') {
    // user confirmed
  }
});
```

### PROMPT(title, message, callback)
Display a text input prompt. Callback receives `{input: 'user text'}`.

```javascript
PROMPT('Year', 'Enter the current year', function(result) {
  SETVALUE('year_entered', result.input);
});
```

### MESSAGEBOX(options, callback)
Display a message box with custom buttons.

```javascript
MESSAGEBOX({
  title: 'Choose Action',
  message: 'What would you like to do?',
  buttons: ['Save', 'Discard', 'Cancel']
}, function(result) {
  // result.value is the button label clicked
});
```

### PROGRESS(title, message)
Display a progress indicator. Call with no arguments to dismiss.

```javascript
PROGRESS('Loading', 'Fetching data...');
// ... do work ...
PROGRESS();  // dismiss
```

---

## Status and Project Functions

### SETSTATUS(value)
Set the record's status value.

### SETSTATUSFILTER(values_array)
Filter which status options are available.

### SETSTATUSHIDDEN(boolean)
Show/hide the status field.

### SETSTATUSREADONLY(boolean)
Make status field read-only.

### SETPROJECT(project_id)
Set the record's project.

### SETPROJECTHIDDEN(boolean)
Show/hide the project field.

### SETPROJECTREADONLY(boolean)
Make project field read-only.

---

## Utility Functions

### INVALID(message)
Mark a field as invalid with an error message. Use inside `validate-record` to prevent saving.

```javascript
ON('validate-record', function() {
  if (!$consent_given || $consent_given !== 'wi') {
    INVALID('Consent must be given before saving.');
  }
  if (NUM($age) < 18) {
    INVALID('Respondent must be 18 or older.');
  }
});
```

### CURRENTLOCATION()
Get the device's current GPS location. Returns null if unavailable.

```javascript
var loc = CURRENTLOCATION();
if (loc) {
  var lat = loc.latitude;
  var lng = loc.longitude;
  var alt = loc.altitude;
  var acc = loc.accuracy;    // meters
  var spd = loc.speed;       // m/s
}
```

### STORAGE()
Access local key-value storage (persists across records).

```javascript
var storage = STORAGE();
storage.setItem('last_enumerator', 'Jean');        // must be string
var name = storage.getItem('last_enumerator');      // returns null if missing
storage.removeItem('last_enumerator');
storage.clear();                                     // remove all

// For objects, use JSON
storage.setItem('config', JSON.stringify({mode: 'fast'}));
var config = JSON.parse(storage.getItem('config'));
```

### SETINTERVAL(callback, milliseconds)
Execute a function repeatedly at a time interval. Returns an interval ID.

```javascript
var timerId = SETINTERVAL(function() {
  SETVALUE('elapsed', NUM($elapsed) + 1);
}, 1000);
```

### CLEARINTERVAL(intervalId)
Stop a repeating interval.

```javascript
CLEARINTERVAL(timerId);
```

### SETTIMEOUT(callback, milliseconds)
Execute a function after a delay.

### CLEARTIMEOUT(timeoutId)
Cancel a pending timeout.

### ISLANDSCAPE() / ISPORTRAIT()
Check device orientation.

---

## Integration Functions

### REQUEST(options, callback)
Make an HTTP request. Supports GET, POST, PUT, DELETE.

```javascript
REQUEST({
  url: 'https://api.example.com/data',
  method: 'GET',
  headers: {'Authorization': 'Bearer token123'},
  followRedirect: true
}, function(response) {
  if (response.statusCode === 200) {
    var data = JSON.parse(response.body);
    SETVALUE('result', data.value);
  }
});

// POST with body
REQUEST({
  url: 'https://api.example.com/submit',
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({record_id: RECORDID()})
}, function(response) {
  ALERT('Done', 'Data submitted: ' + response.statusCode);
});
```

### OPENURL(url)
Open a URL in the device browser.

```javascript
OPENURL('https://maps.google.com/?q=' + LATITUDE() + ',' + LONGITUDE());
```

### RECOGNIZETEXT(photo_access_key, callback)
OCR text recognition from a photo field value.

### INFERENCE(options, callback)
AI/ML inference capabilities (advanced).

---

## Common Patterns

### Auto-populate on new record
```javascript
ON('new-record', function(event) {
  SETVALUE('survey_date', new Date().toISOString().split('T')[0]);
  SETVALUE('enumerator_name', USERFULLNAME());
  SETVALUE('enumerator_email', USEREMAIL());
});
```

### Cascading visibility (show fields based on answers)
```javascript
ON('change', 'has_electricity', function(event) {
  var show = ($has_electricity === 'wi');
  SETHIDDEN('electricity_source', !show);
  SETHIDDEN('electricity_hours', !show);
  SETREQUIRED('electricity_source', show);
});
```

### Dependent dropdowns (filter choices based on parent)
```javascript
ON('change', 'department', function(event) {
  var communes = {
    'sud': ['Les Cayes', 'Aquin', 'Camp-Perrin'],
    'grand_anse': ['Jeremie', 'Dame Marie', 'Anse-d-Hainault']
  };
  if ($department && communes[$department]) {
    SETCHOICES('commune', communes[$department].map(function(c) {
      return {label: c, value: c.toLowerCase().replace(/ /g, '_')};
    }));
  }
});
```

### Validation with multiple rules
```javascript
ON('validate-record', function(event) {
  if (!$consent_given || $consent_given !== 'wi') {
    INVALID('Consent must be given before saving the record.');
  }
  if ($respondent_age && NUM($respondent_age) < 18) {
    INVALID('Respondent must be at least 18 years old.');
  }
  if (!LATITUDE() || !LONGITUDE()) {
    INVALID('GPS location is required. Please enable location services.');
  }
});
```

### Calculated running total in repeatable
```javascript
ON('change', 'item_cost', function(event) {
  var total = 0;
  var costs = REPEATABLEVALUES($items, 'item_cost');
  for (var i = 0; i < costs.length; i++) {
    total += NUM(costs[i]) || 0;
  }
  SETVALUE('total_cost', total);
});
```

### Fetch external data on field change
```javascript
ON('change', 'school_code', function(event) {
  if ($school_code) {
    PROGRESS('Loading', 'Fetching school data...');
    REQUEST({
      url: 'https://api.example.com/schools/' + $school_code,
      method: 'GET'
    }, function(response) {
      PROGRESS();  // dismiss
      if (response.statusCode === 200) {
        var school = JSON.parse(response.body);
        SETVALUE('school_name', school.name);
        SETVALUE('school_district', school.district);
        SETVALUE('school_enrollment', school.enrollment);
      } else {
        ALERT('Error', 'School not found for code: ' + $school_code);
      }
    });
  }
});
```

### Confirmation before critical actions
```javascript
ON('change', 'delete_flag', function(event) {
  if ($delete_flag === 'wi') {
    CONFIRM('Warning', 'Are you sure you want to mark this for deletion?',
      function(result) {
        if (result.value === 'Cancel') {
          SETVALUE('delete_flag', null);
        }
      }
    );
  }
});
```

## ADF Production Patterns

These patterns are battle-tested in ADF Haiti production apps. Use them as starting points.

### Conditional Visibility with Clear-on-Hide

When hiding a field, always clear its value to prevent stale data. Always restore visibility on `load-record` for existing records:

```javascript
ON('change', 'trigger_field', function(event) {
  var val = CHOICEVALUE($trigger_field);
  var show = (val === 'target_value');
  SETHIDDEN('dependent_field', !show);
  if (!show) {
    SETVALUE('dependent_field', null); // Clear when hiding
  }
});

// Restore visibility when editing existing records
ON('load-record', function(event) {
  var val = CHOICEVALUE($trigger_field);
  SETHIDDEN('dependent_field', val !== 'target_value');
});
```

### Minimum Photos Validation

```javascript
ON('validate-record', function(event) {
  var photos = $equipment_photos ? $equipment_photos.length : 0;
  if (photos < 2) {
    INVALID('Bezwen omwen 2 foto ekipman.');
  }
});
```

### Field Sum Must Match Total

```javascript
ON('validate-record', function(event) {
  var sum = NUM($teachers_trained) + NUM($teachers_untrained);
  if (sum !== NUM($total_teachers)) {
    INVALID('Total pwofese (' + $total_teachers + ') pa matche ak detay (' + sum + ').');
  }
});
```

### Auto-Set Value Based on Age Threshold

```javascript
function setMaritalStatusForMinors(event) {
  var age = NUM($respondent_age);
  if (age !== null && age < 18) {
    SETVALUE('marital_status', 'non_aplikab');
    SETREADONLY('marital_status', true);
  } else {
    SETREADONLY('marital_status', false);
  }
}

ON('change', 'respondent_age', setMaritalStatusForMinors);
ON('load-record', setMaritalStatusForMinors);
```

### CONFIRM Dialog for Critical Selections

```javascript
ON('change', 'critical_field', function(event) {
  if (CHOICEVALUE($critical_field) === 'critical_violation') {
    CONFIRM('Konfime', 'Ou chwazi yon vyolasyon kritik. Eske ou si?', function(result) {
      if (result.value === 'Cancel') {
        SETVALUE('critical_field', null);
      }
    });
  }
});
```

### Student-Teacher Ratio (CalculatedField)

```javascript
var students = NUM($total_students);
var teachers = NUM($total_teachers);
if (teachers > 0) {
  SETRESULT(ROUND(students / teachers, 1));
} else {
  SETRESULT('N/A');
}
```

### Percentage of Trained Teachers (CalculatedField)

```javascript
var trained = NUM($teachers_trained);
var total = NUM($total_teachers);
if (total > 0) {
  SETRESULT(ROUND((trained / total) * 100, 0) + '%');
} else {
  SETRESULT('N/A');
}
```

## Global Variables Available in Data Events

- `$field_data_name` -- current value of any field (use data_name with $ prefix)
- `LATITUDE()` / `LONGITUDE()` -- record location
- `ALTITUDE()` -- altitude if available
- `USERFULLNAME()` -- current user's full name
- `USEREMAIL()` -- current user's email
- `RECORDID()` -- current record's ID
- `STATUS()` -- current record status value
- `PROJECTNAME()` -- current project name
- `DEVICEMODEL()` -- device model info
- `DEVICEMANUFACTURER()` -- device manufacturer
- `PLATFORM()` -- "iOS" or "Android"
- `PLATFORMVERSION()` -- OS version
