#!/usr/bin/env python3
"""
Create a new PBIR project scaffold with all required files and folders.

Usage:
    python create_pbir_project.py --name "MyProject" --output-dir /path/to/output

This creates the complete folder structure for a PBIR project including:
- .pbip project file
- Report folder with definition.pbir, report.json, version.json, pages.json
- SemanticModel folder with definition.pbism, database.tmdl, model.tmdl, relationships.tmdl
"""

import argparse
import json
import os
import uuid


def generate_id(prefix=""):
    """Generate a unique identifier for pages and visuals."""
    uid = uuid.uuid4().hex[:20]
    return f"{prefix}{uid}" if prefix else uid


def create_directory(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def write_json(path, data):
    """Write a JSON file with proper formatting."""
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def write_text(path, content):
    """Write a text file (for TMDL)."""
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(content)


def create_pbir_project(name, output_dir, pages=None):
    """
    Create a complete PBIR project scaffold.

    Args:
        name: Project name
        output_dir: Where to create the project
        pages: List of dicts with 'name' and 'displayName' keys.
               Defaults to a single "Overview" page.
    """
    if pages is None:
        pages = [{"name": generate_id("page_"), "displayName": "Overview"}]

    project_dir = os.path.join(output_dir, name)
    report_dir = os.path.join(project_dir, f"{name}.Report")
    definition_dir = os.path.join(report_dir, "definition")
    pages_dir = os.path.join(definition_dir, "pages")
    resources_dir = os.path.join(report_dir, "StaticResources", "RegisteredResources")
    model_dir = os.path.join(project_dir, f"{name}.SemanticModel")
    model_def_dir = os.path.join(model_dir, "definition")
    tables_dir = os.path.join(model_def_dir, "tables")

    # Create all directories
    for d in [definition_dir, pages_dir, resources_dir, model_def_dir, tables_dir]:
        create_directory(d)

    # 1. Project file (.pbip)
    write_json(os.path.join(project_dir, f"{name}.pbip"), {
        "version": "1.0",
        "artifacts": [
            {
                "report": {
                    "path": f"{name}.Report"
                }
            }
        ],
        "settings": {
            "enableAutoRecovery": True
        }
    })

    # 2. Report definition.pbir
    write_json(os.path.join(report_dir, "definition.pbir"), {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
        "version": "4.0",
        "datasetReference": {
            "byPath": {
                "path": f"../{name}.SemanticModel"
            }
        }
    })

    # 3. version.json
    write_json(os.path.join(definition_dir, "version.json"), {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
        "version": "1.0.0"
    })

    # 4. report.json
    write_json(os.path.join(definition_dir, "report.json"), {
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
    })

    # 5. pages.json
    pages_metadata = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
        "pages": [{"name": p["name"], "displayName": p["displayName"]} for p in pages],
        "activePageName": pages[0]["name"]
    }
    write_json(os.path.join(pages_dir, "pages.json"), pages_metadata)

    # 6. Create page folders
    for i, page in enumerate(pages):
        page_dir = os.path.join(pages_dir, page["name"])
        visuals_dir = os.path.join(page_dir, "visuals")
        create_directory(visuals_dir)

        write_json(os.path.join(page_dir, "page.json"), {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/1.0.0/schema.json",
            "name": page["name"],
            "displayName": page["displayName"],
            "displayOption": 1,
            "height": 720,
            "width": 1280,
            "ordinal": i,
            "filters": []
        })

    # 7. Semantic model definition.pbism
    write_json(os.path.join(model_dir, "definition.pbism"), {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
        "version": "4.0"
    })

    # 8. database.tmdl
    write_text(os.path.join(model_def_dir, "database.tmdl"),
        f"database {name}\n\tcompatibilityLevel: 1604\n")

    # 9. model.tmdl
    write_text(os.path.join(model_def_dir, "model.tmdl"),
        "model Model\n"
        "\tculture: en-US\n"
        "\tdefaultPowerBIDataSourceVersion: powerBI_V3\n"
        "\tdiscourageImplicitMeasures: true\n"
        "\tsourceQueryCulture: en-US\n")

    # 10. relationships.tmdl (empty scaffold)
    write_text(os.path.join(model_def_dir, "relationships.tmdl"),
        "// Define relationships between tables here\n"
        "// Example:\n"
        "// relationship sales_to_product\n"
        "//\tfromColumn: Sales.ProductKey\n"
        "//\ttoColumn: Product.ProductKey\n")

    # 11. expressions.tmdl (empty scaffold)
    write_text(os.path.join(model_def_dir, "expressions.tmdl"),
        "// Define shared expressions (Power Query parameters) here\n")

    # 12. .gitignore
    write_text(os.path.join(project_dir, ".gitignore"),
        "**/.pbi/localSettings.json\n"
        "**/.pbi/cache.abf\n"
        "**/.pbi/unappliedChanges.json\n")

    print(f"PBIR project created at: {project_dir}")
    print(f"  Report: {report_dir}")
    print(f"  Semantic Model: {model_dir}")
    print(f"  Pages: {len(pages)}")

    return project_dir


def add_visual_to_page(page_dir, visual_name, visual_json):
    """
    Add a visual to an existing page.

    Args:
        page_dir: Path to the page folder (e.g., .../pages/page_abc123/)
        visual_name: Unique name for the visual folder
        visual_json: Complete visual.json content as a dict
    """
    visual_dir = os.path.join(page_dir, "visuals", visual_name)
    create_directory(visual_dir)
    write_json(os.path.join(visual_dir, "visual.json"), visual_json)
    print(f"  Added visual: {visual_name}")


def add_table_tmdl(tables_dir, table_name, tmdl_content):
    """
    Add a table TMDL file to the semantic model.

    Args:
        tables_dir: Path to the tables folder
        table_name: Name of the table (used as filename)
        tmdl_content: Complete TMDL content as a string
    """
    filepath = os.path.join(tables_dir, f"{table_name}.tmdl")
    write_text(filepath, tmdl_content)
    print(f"  Added table: {table_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new PBIR project scaffold")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--pages", nargs="*", default=["Overview"],
                        help="Page display names (default: Overview)")

    args = parser.parse_args()

    pages = [{"name": generate_id("page_"), "displayName": p} for p in args.pages]
    create_pbir_project(args.name, args.output_dir, pages)
