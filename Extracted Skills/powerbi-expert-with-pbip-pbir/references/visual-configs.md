# Visual Configuration Patterns

Complete visual.json examples for each common visual type. Copy and adapt these patterns when building dashboards.

## Table of Contents

1. [Card (Single KPI)](#1-card)
2. [Multi-Row Card](#2-multi-row-card)
3. [Clustered Column Chart](#3-clustered-column-chart)
4. [Stacked Column Chart](#4-stacked-column-chart)
5. [Clustered Bar Chart](#5-clustered-bar-chart)
6. [Line Chart](#6-line-chart)
7. [Combo Chart (Line + Column)](#7-combo-chart)
8. [Pie Chart](#8-pie-chart)
9. [Donut Chart](#9-donut-chart)
10. [Table](#10-table)
11. [Matrix (Pivot Table)](#11-matrix)
12. [Slicer](#12-slicer)
13. [Shape (Text Box)](#13-shape)
14. [Gauge](#14-gauge)
15. [Treemap](#15-treemap)
16. [KPI Visual](#16-kpi)

---

## 1. Card

Single KPI value display. Great for headline numbers at the top of a dashboard. The top title bar should be hidden; only the bottom category label (which shows the measure name) should be visible.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "card_total_revenue",
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
              "nativeQueryRef": "Total Revenue",
              "displayName": "Total Revenue"
            }
          ]
        }
      },
      "sortDefinition": {
        "sort": [
          {
            "field": {
              "Measure": {
                "Expression": {
                  "SourceRef": { "Entity": "Sales" }
                },
                "Property": "Total Revenue"
              }
            },
            "direction": "Descending"
          }
        ],
        "isDefaultSort": true
      }
    },
    "objects": {
      "categoryLabels": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } }
          }
        }
      ],
      "labels": [
        {
          "properties": {
            "labelDisplayUnits": { "expr": { "Literal": { "Value": "1D" } } },
            "fontSize": { "expr": { "Literal": { "Value": "30D" } } },
            "labelPrecision": { "expr": { "Literal": { "Value": "0L" } } }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "false" } } }
          }
        }
      ],
      "border": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "color": { "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 0, "Percent": 0 } } } } },
            "radius": { "expr": { "Literal": { "Value": "10D" } } }
          }
        }
      ],
      "dropShadow": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "position": { "expr": { "Literal": { "Value": "'Center'" } } },
            "color": { "solid": { "color": { "expr": { "Literal": { "Value": "'#D2D2D2'" } } } } }
          }
        }
      ]
    },
    "drillFilterOtherVisuals": true
  },
  "filters": []
}
```

## 2. Multi-Row Card

Multiple KPIs in a grid layout.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "multicard_kpis",
  "position": { "x": 10, "y": 10, "z": 1, "width": 600, "height": 100, "tabOrder": 0 },
  "visual": {
    "visualType": "multiRowCard",
    "query": {
      "queryState": {
        "Values": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            },
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Orders"
                }
              },
              "queryRef": "Sales.Total Orders",
              "active": true
            },
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Avg Order Value"
                }
              },
              "queryRef": "Sales.Avg Order Value",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {},
    "visualContainerObjects": {}
  },
  "filters": []
}
```

## 3. Clustered Column Chart

Best for comparing values across categories.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "chart_revenue_by_category",
  "position": { "x": 10, "y": 100, "z": 2, "width": 400, "height": 300, "tabOrder": 1 },
  "visual": {
    "visualType": "clusteredColumnChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "Category"
                }
              },
              "queryRef": "Product.Category",
              "active": true
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {
      "dataLabels": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } }
          }
        }
      ],
      "categoryAxis": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } }
          }
        }
      ],
      "valueAxis": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "text": { "expr": { "Literal": { "Value": "'Revenue by Category'" } } }
          }
        }
      ]
    }
  },
  "filters": []
}
```

## 4. Stacked Column Chart

Add a `Series` data role for stacking.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "chart_revenue_stacked",
  "position": { "x": 420, "y": 100, "z": 2, "width": 400, "height": 300, "tabOrder": 2 },
  "visual": {
    "visualType": "stackedColumnChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Calendar" } },
                  "Property": "Quarter"
                }
              },
              "queryRef": "Calendar.Quarter",
              "active": true
            }
          ]
        },
        "Series": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "Category"
                }
              },
              "queryRef": "Product.Category",
              "active": true
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {},
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "text": { "expr": { "Literal": { "Value": "'Revenue by Quarter and Category'" } } }
          }
        }
      ]
    }
  },
  "filters": []
}
```

## 5. Clustered Bar Chart

Same as column chart but horizontal. Good for long category labels.

```json
{
  "visual": {
    "visualType": "clusteredBarChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "ProductName"
                }
              },
              "queryRef": "Product.ProductName",
              "active": true
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
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
  }
}
```

## 6. Line Chart

Best for trends over time.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "chart_revenue_trend",
  "position": { "x": 10, "y": 100, "z": 2, "width": 600, "height": 300, "tabOrder": 1 },
  "visual": {
    "visualType": "lineChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Calendar" } },
                  "Property": "Date"
                }
              },
              "queryRef": "Calendar.Date",
              "active": true
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {
      "lineStyles": [
        {
          "properties": {
            "strokeWidth": { "expr": { "Literal": { "Value": "3D" } } }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "text": { "expr": { "Literal": { "Value": "'Revenue Trend'" } } }
          }
        }
      ]
    }
  },
  "filters": []
}
```

## 7. Combo Chart

Line + Column combined. Use `Y` for column values and `Y2` for line values.

```json
{
  "visual": {
    "visualType": "lineClusteredColumnComboChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Calendar" } },
                  "Property": "Month"
                }
              },
              "queryRef": "Calendar.Month",
              "active": true
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            }
          ]
        },
        "Y2": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Orders"
                }
              },
              "queryRef": "Sales.Total Orders",
              "active": true
            }
          ]
        }
      }
    }
  }
}
```

## 8. Pie Chart

```json
{
  "visual": {
    "visualType": "pieChart",
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Region"
                }
              },
              "queryRef": "Sales.Region",
              "active": true
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
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
  }
}
```

## 9. Donut Chart

Same as pie chart but with `donutChart` visual type. The center can show a total.

```json
{
  "visual": {
    "visualType": "donutChart",
    "query": {
      "queryState": {
        "Category": { "projections": [{ "field": { "Column": { "Expression": { "SourceRef": { "Entity": "Product" } }, "Property": "Category" } }, "queryRef": "Product.Category", "active": true }] },
        "Y": { "projections": [{ "field": { "Measure": { "Expression": { "SourceRef": { "Entity": "Sales" } }, "Property": "Total Revenue" } }, "queryRef": "Sales.Total Revenue", "active": true }] }
      }
    }
  }
}
```

## 10. Table

Data grid. Each column is a separate projection in the `Values` data role.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "table_detail",
  "position": { "x": 10, "y": 420, "z": 3, "width": 850, "height": 280, "tabOrder": 5 },
  "visual": {
    "visualType": "tableEx",
    "query": {
      "queryState": {
        "Values": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "ProductName"
                }
              },
              "queryRef": "Product.ProductName",
              "active": true
            },
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "Category"
                }
              },
              "queryRef": "Product.Category",
              "active": true
            },
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            },
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Orders"
                }
              },
              "queryRef": "Sales.Total Orders",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {
      "grid": [
        {
          "properties": {
            "gridVertical": { "expr": { "Literal": { "Value": "true" } } }
          }
        }
      ],
      "columnHeaders": [
        {
          "properties": {
            "bold": { "expr": { "Literal": { "Value": "true" } } }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "text": { "expr": { "Literal": { "Value": "'Product Details'" } } }
          }
        }
      ]
    }
  },
  "filters": []
}
```

## 11. Matrix (Pivot Table)

Cross-tab layout with `Rows`, `Columns`, and `Values`.

```json
{
  "visual": {
    "visualType": "pivotTable",
    "query": {
      "queryState": {
        "Rows": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "Category"
                }
              },
              "queryRef": "Product.Category",
              "active": true
            }
          ]
        },
        "Columns": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Calendar" } },
                  "Property": "Year"
                }
              },
              "queryRef": "Calendar.Year",
              "active": true
            }
          ]
        },
        "Values": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
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
  }
}
```

## 12. Slicer

Interactive filter control. The `Values` data role takes the field to filter on.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "slicer_region",
  "position": { "x": 870, "y": 10, "z": 10, "width": 200, "height": 300, "tabOrder": 0 },
  "visual": {
    "visualType": "slicer",
    "query": {
      "queryState": {
        "Values": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Region"
                }
              },
              "queryRef": "Sales.Region",
              "active": true
            }
          ]
        }
      }
    },
    "objects": {
      "data": [
        {
          "properties": {
            "mode": { "expr": { "Literal": { "Value": "'Basic'" } } }
          }
        }
      ],
      "selection": [
        {
          "properties": {
            "selectAllCheckboxEnabled": { "expr": { "Literal": { "Value": "true" } } },
            "singleSelect": { "expr": { "Literal": { "Value": "false" } } }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "text": { "expr": { "Literal": { "Value": "'Region'" } } }
          }
        }
      ]
    }
  },
  "filters": []
}
```

**Slicer modes:**
- `'Basic'` -- List of checkboxes
- `'Dropdown'` -- Dropdown selector
- `'Between'` -- Range slider (for numeric/date fields)

## 13. Shape (Text Box / Title)

Use for page titles, section headers, or decorative elements.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "title_shape",
  "position": { "x": 10, "y": 5, "z": 0, "width": 400, "height": 40, "tabOrder": -1 },
  "visual": {
    "visualType": "shape",
    "objects": {
      "general": [
        {
          "properties": {
            "paragraphs": {
              "expr": {
                "Literal": {
                  "Value": "[{\"textRuns\":[{\"value\":\"Sales Dashboard\",\"textStyle\":{\"fontFamily\":\"Segoe UI Semibold\",\"fontSize\":\"20px\",\"color\":\"#333333\"}}]}]"
                }
              }
            }
          }
        }
      ],
      "line": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "false" } } }
          }
        }
      ],
      "fill": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "false" } } }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "background": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "false" } } }
          }
        }
      ]
    }
  },
  "filters": []
}
```

## 14. Gauge

Progress toward a target.

```json
{
  "visual": {
    "visualType": "gauge",
    "query": {
      "queryState": {
        "Y": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            }
          ]
        },
        "TargetValue": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Revenue Target"
                }
              },
              "queryRef": "Sales.Revenue Target",
              "active": true
            }
          ]
        }
      }
    }
  }
}
```

## 15. Treemap

Hierarchical part-of-whole.

```json
{
  "visual": {
    "visualType": "treemap",
    "query": {
      "queryState": {
        "Group": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Product" } },
                  "Property": "Category"
                }
              },
              "queryRef": "Product.Category",
              "active": true
            }
          ]
        },
        "Values": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
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
  }
}
```

## 16. KPI

KPI with trend indicator.

```json
{
  "visual": {
    "visualType": "kpi",
    "query": {
      "queryState": {
        "Indicator": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Total Revenue"
                }
              },
              "queryRef": "Sales.Total Revenue",
              "active": true
            }
          ]
        },
        "TrendAxis": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": { "SourceRef": { "Entity": "Calendar" } },
                  "Property": "Date"
                }
              },
              "queryRef": "Calendar.Date",
              "active": true
            }
          ]
        },
        "Goal": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Revenue Target"
                }
              },
              "queryRef": "Sales.Revenue Target",
              "active": true
            }
          ]
        }
      }
    }
  }
}
```
