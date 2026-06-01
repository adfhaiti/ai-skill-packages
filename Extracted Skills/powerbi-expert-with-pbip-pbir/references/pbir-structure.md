# PBIR File Structure Reference

Complete specifications for every file in a PBIR project. Use this reference when creating or modifying PBIR files.

## Table of Contents

1. [Project File (.pbip)](#1-project-file-pbip)
2. [Report Definition (definition.pbir)](#2-report-definition)
3. [Version Metadata (version.json)](#3-version-metadata)
4. [Report Configuration (report.json)](#4-report-configuration)
5. [Pages Metadata (pages.json)](#5-pages-metadata)
6. [Page Configuration (page.json)](#6-page-configuration)
7. [Visual Configuration (visual.json)](#7-visual-configuration)
8. [Semantic Model Definition (definition.pbism)](#8-semantic-model-definition)
9. [Theme Files](#9-theme-files)
10. [Report Extensions](#10-report-extensions)
11. [Bookmarks](#11-bookmarks)

---

## 1. Project File (.pbip)

The `.pbip` file is the entry point. It tells Power BI Desktop where to find the report and semantic model folders.

```json
{
  "version": "1.0",
  "artifacts": [
    {
      "report": {
        "path": "MyProject.Report"
      }
    }
  ],
  "settings": {
    "enableAutoRecovery": true
  }
}
```

## 2. Report Definition (definition.pbir)

Located at `MyProject.Report/definition.pbir`. Links the report to its semantic model.

**Local semantic model (most common):**
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
  "version": "4.0",
  "datasetReference": {
    "byPath": {
      "path": "../MyProject.SemanticModel"
    }
  }
}
```

**Remote semantic model (Fabric workspace):**
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
  "version": "4.0",
  "datasetReference": {
    "byConnection": {
      "connectionString": "Data Source=\"powerbi://api.powerbi.com/v1.0/myorg/WorkspaceName\";initial catalog=ModelName;semanticmodelid=GUID"
    }
  }
}
```

- `version`: Use "4.0" for PBIR format support
- `byPath`: Relative path to local semantic model folder
- `byConnection`: Connection string for remote models

## 3. Version Metadata (version.json)

Located at `MyProject.Report/definition/version.json`.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
  "version": "1.0.0"
}
```

This file rarely changes. Just include it as-is.

## 4. Report Configuration (report.json)

Located at `MyProject.Report/definition/report.json`. Controls report-level settings.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/1.0.0/schema.json",
  "themeCollection": {
    "baseTheme": {
      "name": "CY24SU06",
      "reportVersionAtImport": "5.55",
      "type": "SharedResources"
    }
  },
  "dataColors": [
    "#118DFF", "#12239E", "#E66C37", "#6B007B",
    "#E044A7", "#744EC2", "#D9B300", "#D64550"
  ],
  "filters": [],
  "annotations": []
}
```

**Key properties:**
- `themeCollection.baseTheme.name`: Built-in theme name (e.g., "CY24SU06" for the default theme)
- `themeCollection.baseTheme.type`: "SharedResources" for built-in, "RegisteredResources" for custom
- `dataColors`: Array of hex color codes used for data series
- `filters`: Report-level filters applied to all pages
- `annotations`: Metadata for external tools

**Common built-in theme names:**
- `CY24SU06` -- Default (modern blue)
- `Accessible Default` -- High contrast accessible
- `City Park` -- Green/earth tones
- `Executive` -- Dark/professional
- `Innovation` -- Bold/colorful

## 5. Pages Metadata (pages.json)

Located at `MyProject.Report/definition/pages/pages.json`. Lists all pages and their display order.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
  "pages": [
    {
      "name": "page_overview_001",
      "displayName": "Sales Overview"
    },
    {
      "name": "page_details_002",
      "displayName": "Product Details"
    }
  ],
  "activePageName": "page_overview_001"
}
```

- `name`: Must match the folder name under `pages/`
- `displayName`: What the user sees in the page tab
- `activePageName`: Page shown when the report opens
- Array order determines tab order in Power BI

## 6. Page Configuration (page.json)

Located at `MyProject.Report/definition/pages/<pageName>/page.json`.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/1.0.0/schema.json",
  "name": "page_overview_001",
  "displayName": "Sales Overview",
  "displayOption": 1,
  "height": 750,
  "width": 1280,
  "ordinal": 0,
  "filters": [],
  "background": {
    "color": "#FFFFFF",
    "transparency": 0
  },
  "wallpaper": {
    "color": "#FFFFFF",
    "transparency": 0
  }
}
```

**Key properties:**
- `displayOption`: 1 = Normal, 2 = Fit to Width, 3 = Fit to Page
- `height`/`width`: Page dimensions in pixels (use 1280x750)
- `ordinal`: Display order (0-based). Must be consistent with pages.json array order
- `filters`: Page-level filters
- `background`: Page canvas background color
- `wallpaper`: Area outside the canvas

## 7. Visual Configuration (visual.json)

Located at `MyProject.Report/definition/pages/<pageName>/visuals/<visualId>/visual.json`.

This is the most complex file. Each visual needs: type, position, data query, and formatting.

### 7.1 Basic Structure

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "visual_revenue_card_001",
  "position": {
    "x": 20,
    "y": 55,
    "z": 1000,
    "width": 195,
    "height": 95,
    "tabOrder": 0
  },
  "visual": {
    "visualType": "card",
    "query": { ... },
    "objects": { ... },
    "visualContainerObjects": { ... },
    "drillFilterOtherVisuals": true
  },
  "filters": [],
  "parentGroupName": null
}
```

### 7.2 Position Properties

```json
"position": {
  "x": 20,       // Left edge (pixels from left of page)
  "y": 55,       // Top edge (pixels from top of page)
  "z": 1000,     // Layer order (higher = on top)
  "width": 195,  // Visual width in pixels
  "height": 95,  // Visual height in pixels
  "tabOrder": 0  // Keyboard tab navigation order
}
```

Page size is 1280x750, so keep x + width <= 1280 and y + height <= 750.

### 7.3 Query Structure (Semantic Query)

The query section defines what data the visual pulls. This is the most important and complex part.

**Single column + single measure example (for a bar chart):**

```json
"query": {
  "queryState": {
    "Category": {
      "projections": [
        {
          "field": {
            "Column": {
              "Expression": {
                "SourceRef": { "Entity": "Sales" }
              },
              "Property": "ProductCategory"
            }
          },
          "queryRef": "Sales.ProductCategory",
          "active": true
        }
      ]
    },
    "Y": {
      "projections": [
        {
          "field": {
            "Measure": {
              "Expression": {
                "SourceRef": { "Entity": "Sales" }
              },
              "Property": "Total Revenue"
            }
          },
          "queryRef": "Sales.Total Revenue",
          "active": true
        }
      ]
    }
  }
}
```

**Single measure example (for a card/KPI):**

```json
"query": {
  "queryState": {
    "Values": {
      "projections": [
        {
          "field": {
            "Measure": {
              "Expression": {
                "SourceRef": { "Entity": "Sales" }
              },
              "Property": "Total Revenue"
            }
          },
          "queryRef": "Sales.Total Revenue",
          "active": true
        }
      ]
    }
  }
}
```

**Data role names by visual type:**

| Visual Type | Data Roles |
|---|---|
| `card` | Values |
| `multiRowCard` | Values |
| `clusteredColumnChart` | Category, Y, Series (optional) |
| `clusteredBarChart` | Category, Y, Series (optional) |
| `stackedColumnChart` | Category, Y, Series |
| `lineChart` | Category, Y, Series (optional) |
| `lineClusteredColumnComboChart` | Category, Y (columns), Y2 (lines) |
| `pieChart` | Category, Y |
| `donutChart` | Category, Y |
| `table` | Values (one projection per column) |
| `pivotTable` | Rows, Columns, Values |
| `slicer` | Values |
| `map` | Category (location), Size, Color (optional) |
| `treemap` | Group, Values, Details (optional) |
| `gauge` | Y (value), TargetValue, MinValue, MaxValue |
| `waterfallChart` | Category, Y, Breakdown (optional) |

**Field reference patterns:**

For a column:
```json
{
  "field": {
    "Column": {
      "Expression": {
        "SourceRef": { "Entity": "TableName" }
      },
      "Property": "ColumnName"
    }
  },
  "queryRef": "TableName.ColumnName",
  "active": true
}
```

For a measure:
```json
{
  "field": {
    "Measure": {
      "Expression": {
        "SourceRef": { "Entity": "TableName" }
      },
      "Property": "MeasureName"
    }
  },
  "queryRef": "TableName.MeasureName",
  "active": true
}
```

### 7.4 Visual Objects (Formatting)

The `objects` section controls visual formatting. Structure varies by visual type but follows a common pattern:

```json
"objects": {
  "general": [
    {
      "properties": {
        "responsive": { "expr": { "Literal": { "Value": "true" } } }
      }
    }
  ],
  "title": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "text": { "expr": { "Literal": { "Value": "'Total Revenue'" } } },
        "fontSize": { "expr": { "Literal": { "Value": "12D" } } },
        "fontColor": { "expr": { "Literal": { "Value": "'#333333'" } } },
        "alignment": { "expr": { "Literal": { "Value": "'center'" } } }
      }
    }
  ],
  "dataLabels": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "fontSize": { "expr": { "Literal": { "Value": "10D" } } }
      }
    }
  ],
  "categoryAxis": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "fontSize": { "expr": { "Literal": { "Value": "11D" } } }
      }
    }
  ],
  "valueAxis": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } }
      }
    }
  ],
  "legend": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "position": { "expr": { "Literal": { "Value": "'Top'" } } }
      }
    }
  ]
}
```

**Value type suffixes in Literal.Value:**
- Strings: `"'mystring'"` (single quotes inside double quotes)
- Numbers (double): `"12D"` (D suffix for decimal/double)
- Numbers (int): `"4L"` (L suffix for long/integer)
- Booleans: `"true"` or `"false"` (no quotes inside)

**Common object categories:**
- `general` -- Responsive behavior, orientation
- `title` -- Visual title text, font, color, alignment
- `subTitle` -- Subtitle configuration
- `dataLabels` -- Show/hide data labels, formatting
- `categoryAxis` -- X-axis configuration
- `valueAxis` -- Y-axis configuration
- `legend` -- Legend position, visibility
- `dataPoint` -- Individual data point colors
- `background` -- Visual background fill
- `border` -- Visual border
- `padding` -- Internal padding
- `labels` -- Slicer/card label formatting
- `values` -- Card/KPI value formatting

### 7.5 visualContainerObjects (Visual Container Objects)

The `visualContainerObjects` section controls the visual container (the box around the visual), separate from the data visual itself. Note: the property name in the actual files is `visualContainerObjects`, not `vcObjects` (both appear in some docs, but files use the longer form).

Every visual should include drop shadows (Center position, #D2D2D2 color) and rounded borders with the theme primary color:

```json
"visualContainerObjects": {
  "title": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "text": { "expr": { "Literal": { "Value": "'Sales by Region'" } } }
      }
    }
  ],
  "border": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "color": {
          "solid": {
            "color": {
              "expr": {
                "ThemeDataColor": { "ColorId": 0, "Percent": 0 }
              }
            }
          }
        },
        "radius": { "expr": { "Literal": { "Value": "10D" } } }
      }
    }
  ],
  "dropShadow": [
    {
      "properties": {
        "show": { "expr": { "Literal": { "Value": "true" } } },
        "position": { "expr": { "Literal": { "Value": "'Center'" } } },
        "color": {
          "solid": {
            "color": { "expr": { "Literal": { "Value": "'#D2D2D2'" } } }
          }
        }
      }
    }
  ]
}
```

## 8. Semantic Model Definition (definition.pbism)

Located at `MyProject.SemanticModel/definition.pbism`.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
  "version": "4.0"
}
```

Use version "4.0" to enable TMDL format support.

## 9. Theme Files

Custom themes go in `MyProject.Report/StaticResources/RegisteredResources/`.

The theme file is a JSON file (e.g., `theme.json`) that follows the Power BI theme schema:

```json
{
  "name": "Custom Corporate Theme",
  "dataColors": [
    "#118DFF", "#12239E", "#E66C37", "#6B007B",
    "#E044A7", "#744EC2", "#D9B300", "#D64550"
  ],
  "background": "#FFFFFF",
  "foreground": "#252423",
  "tableAccent": "#118DFF",
  "textClasses": {
    "callout": {
      "fontSize": 45,
      "fontFace": "Segoe UI",
      "color": "#252423"
    },
    "title": {
      "fontSize": 12,
      "fontFace": "Segoe UI",
      "color": "#252423"
    },
    "header": {
      "fontSize": 12,
      "fontFace": "Segoe UI Semibold",
      "color": "#252423"
    },
    "label": {
      "fontSize": 10,
      "fontFace": "Segoe UI",
      "color": "#666666"
    }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background": [
          {
            "show": true,
            "color": { "solid": { "color": "#FFFFFF" } },
            "transparency": 0
          }
        ],
        "border": [
          {
            "show": false
          }
        ]
      }
    }
  }
}
```

To use a custom theme, update `report.json`:
```json
"themeCollection": {
  "baseTheme": {
    "name": "theme",
    "reportVersionAtImport": "5.55",
    "type": "RegisteredResources"
  }
}
```

## 10. Report Extensions

Located at `MyProject.Report/definition/reportExtensions.json`. Used for report-level measures (rare, usually measures go in the semantic model).

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/reportExtension/1.0.0/schema.json",
  "measures": [
    {
      "name": "Selected Year",
      "expression": "SELECTEDVALUE(Calendar[Year])",
      "formatString": "General"
    }
  ]
}
```

## 11. Bookmarks

Located at `MyProject.Report/definition/bookmarks/`.

`bookmarks.json`:
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmarksMetadata/1.0.0/schema.json",
  "bookmarks": [
    {
      "name": "bookmark_overview",
      "displayName": "Overview View"
    },
    {
      "name": "bookmark_detail",
      "displayName": "Detail View"
    }
  ]
}
```

Individual bookmark files (e.g., `bookmark_overview.bookmark.json`):
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
  "name": "bookmark_overview",
  "displayName": "Overview View",
  "explorationState": {
    "version": "1.0",
    "activeSection": "page_overview_001",
    "filters": {
      "byTarget": []
    }
  }
}
```

## Size and Performance Limits

- Max 1,000 pages per report
- Max 1,000 visuals per page (practical limit: 20-30 for performance)
- Max 300 MB for resource files
- Max 300 MB for report definition files
- Recommended: Keep under 500 files total for smooth Desktop authoring

## File Encoding

- All JSON files: UTF-8 without BOM
- All TMDL files: UTF-8 without BOM
- Line endings: CRLF (Power BI Desktop convention, but LF also works)
