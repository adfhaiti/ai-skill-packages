# Fulcrum Calculation Fields Reference

Calculation fields use JavaScript expressions to compute values dynamically. They are read-only to users and update automatically when referenced fields change.

## Table of Contents

1. [Math Functions](#math-functions)
2. [String Functions](#string-functions)
3. [Date/Time Functions](#datetime-functions)
4. [Array Functions](#array-functions)
5. [Logic Functions](#logic-functions)
6. [Field Access Functions](#field-access-functions)
7. [Repeatable Functions](#repeatable-functions)
8. [Type Conversion](#type-conversion)
9. [Special Functions](#special-functions)
10. [Expression Examples](#expression-examples)

---

## Math Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| ABS | `ABS(number)` | Absolute value |
| CEIL / CEILING | `CEIL(number)` | Round up to nearest integer |
| FLOOR | `FLOOR(number)` | Round down to nearest integer |
| ROUND | `ROUND(number, decimals)` | Round to specified decimal places |
| SQRT | `SQRT(number)` | Square root |
| POW / POWER | `POW(base, exponent)` | Raise to power |
| MIN | `MIN(a, b, ...)` | Minimum value |
| MAX | `MAX(a, b, ...)` | Maximum value |
| SUM | `SUM(a, b, ...)` | Sum of values |
| AVERAGE | `AVERAGE(a, b, ...)` | Mean of values |
| MEDIAN | `MEDIAN(a, b, ...)` | Median value |
| LOG | `LOG(number)` | Natural logarithm |
| LOG10 | `LOG10(number)` | Base-10 logarithm |
| EXP | `EXP(number)` | e raised to power |
| PI | `PI()` | Pi constant (3.14159...) |
| RAND | `RAND()` | Random number 0-1 |
| MOD | `MOD(number, divisor)` | Modulo/remainder |
| EVEN | `EVEN(number)` | Round up to nearest even integer |
| ODD | `ODD(number)` | Round up to nearest odd integer |
| SIGN | `SIGN(number)` | Returns -1, 0, or 1 |
| PRODUCT | `PRODUCT(a, b, ...)` | Product of values |

### Trigonometric
| Function | Syntax |
|----------|--------|
| SIN | `SIN(radians)` |
| COS | `COS(radians)` |
| TAN | `TAN(radians)` |
| ASIN | `ASIN(value)` |
| ACOS | `ACOS(value)` |
| ATAN | `ATAN(value)` |
| ATAN2 | `ATAN2(y, x)` |
| DEGREES | `DEGREES(radians)` |
| RADIANS | `RADIANS(degrees)` |

---

## String Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| CONCAT | `CONCAT(str1, str2, ...)` | Join strings |
| CONTAINS | `CONTAINS(string, search)` | Check if string contains substring (boolean) |
| FIND | `FIND(search, string)` | Position of substring (1-based, 0 if not found) |
| REPLACE | `REPLACE(string, old, new)` | Replace first occurrence |
| SUBSTITUTE | `SUBSTITUTE(string, old, new)` | Replace all occurrences |
| TRIM | `TRIM(string)` | Remove leading/trailing whitespace |
| LEFT | `LEFT(string, count)` | First N characters |
| RIGHT | `RIGHT(string, count)` | Last N characters |
| MID | `MID(string, start, count)` | Substring from position |
| LEN | `LEN(string)` | String length |
| UPPER | `UPPER(string)` | Uppercase |
| LOWER | `LOWER(string)` | Lowercase |
| PROPER | `PROPER(string)` | Title case |
| REPT | `REPT(string, count)` | Repeat string N times |
| CHAR | `CHAR(code)` | Character from ASCII code |
| CODE | `CODE(character)` | ASCII code from character |
| EXACT | `EXACT(str1, str2)` | Case-sensitive comparison |
| SEARCH | `SEARCH(search, string)` | Case-insensitive FIND |
| CLEAN | `CLEAN(string)` | Remove non-printable characters |
| DOLLAR | `DOLLAR(number, decimals)` | Format as currency string |
| FIXED | `FIXED(number, decimals)` | Format number with fixed decimals |
| TEXT | `TEXT(value, format)` | Format value as text |
| VALUE | `VALUE(string)` | Parse number from string |
| LPAD | `LPAD(string, length, pad_char)` | Left-pad string |
| RPAD | `RPAD(string, length, pad_char)` | Right-pad string |

---

## Date/Time Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| DATE | `DATE(year, month, day)` | Create date |
| DATEVALUE | `DATEVALUE(date_string)` | Parse date from string |
| DATEADD | `DATEADD(date, count, unit)` | Add time to date. Units: 'years', 'months', 'days', 'hours', 'minutes' |
| TIMEDIFF | `TIMEDIFF(date1, date2, unit)` | Difference between dates. Units: 'years', 'months', 'days', 'hours', 'minutes', 'seconds' |
| TIMESTAMP | `TIMESTAMP()` | Current timestamp string |
| NOW | `NOW()` | Current date/time |
| TODAY | `TODAY()` | Current date (no time) |
| YEAR | `YEAR(date)` | Extract year |
| MONTH | `MONTH(date)` | Extract month (1-12) |
| DAY | `DAY(date)` | Extract day of month |
| HOUR | `HOUR(datetime)` | Extract hour |
| MINUTE | `MINUTE(datetime)` | Extract minute |
| SECOND | `SECOND(datetime)` | Extract second |
| WEEKDAY | `WEEKDAY(date)` | Day of week (0=Sunday) |
| FORMATDATE | `FORMATDATE(date, format)` | Format date string |
| TIMEVALUE | `TIMEVALUE(time_string)` | Parse time from string |
| EOMONTH | `EOMONTH(date, months)` | End of month, offset by months |
| NETWORKDAYS | `NETWORKDAYS(start, end)` | Working days between dates |

---

## Array Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| ARRAY | `ARRAY(a, b, c, ...)` | Create array |
| FLATTEN | `FLATTEN(nested_array)` | Flatten nested arrays |
| PLUCK | `PLUCK(array_of_objects, key)` | Extract values by key |
| SORT | `SORT(array)` | Sort ascending |
| UNIQUE | `UNIQUE(array)` | Remove duplicates |
| COMPACT | `COMPACT(array)` | Remove null/undefined |
| FIRST | `FIRST(array)` | First element |
| LAST | `LAST(array)` | Last element |
| NTH | `NTH(array, index)` | Element at index |
| SLICE | `SLICE(array, start, end)` | Sub-array |
| CONTAINS | `CONTAINS(array, value)` | Check if array contains value |
| INTERSECTION | `INTERSECTION(arr1, arr2)` | Common elements |
| DIFFERENCE | `DIFFERENCE(arr1, arr2)` | Elements in arr1 not in arr2 |
| UNION | `UNION(arr1, arr2)` | Combined unique elements |
| WITHOUT | `WITHOUT(array, values...)` | Remove specific values |
| SHUFFLE | `SHUFFLE(array)` | Random order |
| EVERY | `EVERY(array, func)` | Test if all pass |
| SOME | `SOME(array, func)` | Test if any pass |
| MAP | `MAP(array, func)` | Transform each element |
| FILTER | `FILTER(array, func)` | Filter elements |
| REDUCE | `REDUCE(array, func, initial)` | Reduce to single value |
| GROUPBY | `GROUPBY(array, key)` | Group by property |
| COUNTBY | `COUNTBY(array, key)` | Count by property |
| SORTBY | `SORTBY(array, key)` | Sort by property |
| INDEXOF | `INDEXOF(array, value)` | Index of value (-1 if missing) |

---

## Logic Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| IF | `IF(condition, true_val, false_val)` | Conditional |
| AND | `AND(a, b, ...)` | All true |
| OR | `OR(a, b, ...)` | Any true |
| NOT | `NOT(value)` | Negate |
| ISNAN | `ISNAN(value)` | Check if NaN |
| ISNULL | `ISNULL(value)` | Check if null |
| ISBLANK | `ISBLANK(value)` | Check if blank/empty |
| ISNUMBER | `ISNUMBER(value)` | Check if number |
| ISTEXT | `ISTEXT(value)` | Check if text |
| IFS | `IFS(cond1, val1, cond2, val2, ...)` | Multiple conditions |
| SWITCH | `SWITCH(expr, case1, val1, case2, val2, default)` | Switch/case |
| CHOOSE | `CHOOSE(index, val1, val2, ...)` | Choose by index |
| COALESCE | `COALESCE(a, b, c, ...)` | First non-null value |

---

## Field Access Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| FIELD | `FIELD(data_name)` | Get field definition object |
| FIELDNAMES | `FIELDNAMES()` | Array of all data_names |
| FIELDTYPE | `FIELDTYPE(data_name)` | Field type string |
| CHOICEVALUE | `CHOICEVALUE($field)` | Selected value from choice field |
| CHOICEVALUES | `CHOICEVALUES($field)` | Array of selected values (multi-choice) |
| CHOICELABEL | `CHOICELABEL($field)` | Display label of selected choice |
| STATUSVALUE | `STATUSVALUE()` | Current status value |
| STATUSLABEL | `STATUSLABEL()` | Current status label |

---

## Repeatable Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| REPEATABLEVALUES | `REPEATABLEVALUES($repeatable, 'field_data_name')` | Array of values from repeatable field |
| REPEATABLESUM | `REPEATABLESUM($repeatable, 'numeric_field')` | Sum of numeric field across repeatable rows |
| REPEATABLECOUNT | `REPEATABLECOUNT($repeatable)` | Number of rows in repeatable |
| REPEATABLEAVERAGE | `REPEATABLEAVERAGE($repeatable, 'field')` | Average across rows |
| REPEATABLEMIN | `REPEATABLEMIN($repeatable, 'field')` | Minimum across rows |
| REPEATABLEMAX | `REPEATABLEMAX($repeatable, 'field')` | Maximum across rows |
| REPEATABLEMEDIAN | `REPEATABLEMEDIAN($repeatable, 'field')` | Median across rows |

---

## Type Conversion

| Function | Syntax | Description |
|----------|--------|-------------|
| NUM / NUMBER | `NUM(value)` | Convert to number |
| STRING | `STRING(value)` | Convert to string |
| BOOLEAN | `BOOLEAN(value)` | Convert to boolean |
| PARSEINT | `PARSEINT(string)` | Parse integer |
| PARSEFLOAT | `PARSEFLOAT(string)` | Parse float |

---

## Special Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| LATITUDE | `LATITUDE()` | Record latitude |
| LONGITUDE | `LONGITUDE()` | Record longitude |
| ALTITUDE | `ALTITUDE()` | Record altitude |
| STATUS | `STATUS()` | Current record status |
| PROJECTNAME | `PROJECTNAME()` | Current project name |
| RECORDID | `RECORDID()` | Current record ID |
| USERFULLNAME | `USERFULLNAME()` | Current user's name |
| USEREMAIL | `USEREMAIL()` | Current user's email |
| DEVICEMODEL | `DEVICEMODEL()` | Device model |
| DEVICEMANUFACTURER | `DEVICEMANUFACTURER()` | Device maker |
| PLATFORM | `PLATFORM()` | "iOS" or "Android" |
| PLATFORMVERSION | `PLATFORMVERSION()` | OS version |
| APPLICATIONVERSION | `APPLICATIONVERSION()` | Fulcrum app version |
| GEOMETRYTYPE | `GEOMETRYTYPE()` | Geometry type ("Point", etc.) |
| GEOMETRYCOORDINATES | `GEOMETRYCOORDINATES()` | Coordinates array |
| LOCALE | `LOCALE()` | Device locale |

---

## Expression Examples

### Scoring
```javascript
// Sum of Likert scale responses (1-5)
NUM($q1_score) + NUM($q2_score) + NUM($q3_score)

// Percentage
ROUND((NUM($correct) / NUM($total)) * 100, 1)

// Weighted average
(NUM($test1) * 0.3 + NUM($test2) * 0.3 + NUM($final) * 0.4)
```

### Conditional Text
```javascript
// Pass/fail
IF(NUM($score) >= 80, 'Pass', IF(NUM($score) >= 60, 'Marginal', 'Fail'))

// Multi-condition
IF(AND(NUM($age) >= 18, $consent === 'wi'), 'Eligible', 'Not Eligible')

// Nested IFS
IFS(
  NUM($score) >= 90, 'Excellent',
  NUM($score) >= 80, 'Good',
  NUM($score) >= 70, 'Satisfactory',
  NUM($score) >= 60, 'Needs Improvement',
  true, 'Unsatisfactory'
)
```

### Date Calculations
```javascript
// Days between dates
TIMEDIFF($end_date, $start_date, 'days')

// Age from birthdate
FLOOR(TIMEDIFF(TODAY(), $date_of_birth, 'years'))

// Deadline (30 days from survey)
DATEADD($survey_date, 30, 'days')
```

### Repeatable Aggregation
```javascript
// Count items
REPEATABLECOUNT($items)

// Total cost
REPEATABLESUM($line_items, 'item_cost')

// Average score
REPEATABLEAVERAGE($assessments, 'score')

// Comma-separated list
REPEATABLEVALUES($students, 'student_name').join(', ')
```

### String Manipulation
```javascript
// Full name
CONCAT($first_name, ' ', $last_name)

// Record label
CONCAT($school_name, ' - ', FORMATDATE($visit_date, '%Y-%m-%d'))

// Extract domain from email
RIGHT($email, LEN($email) - FIND('@', $email))
```

### Geospatial
```javascript
// GPS coordinates as string
CONCAT(STRING(LATITUDE()), ', ', STRING(LONGITUDE()))

// Distance placeholder (basic Haversine not built in; use data events for complex geo)
CONCAT('Lat: ', FIXED(LATITUDE(), 6), ' Lon: ', FIXED(LONGITUDE(), 6))
```
