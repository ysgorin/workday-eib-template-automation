
# Workday EIB Template Automation

A lightweight Python solution for automating Workday Enterprise Interface Builder (EIB) file generation using Snowflake, Workato, and Excel.

## Overview

Workday EIBs provide a native way to perform bulk data imports, including built-in import processing and results in the Workday interface. However, EIB workflows typically rely on Excel templates populated manually, even when source data is available in Snowflake. Although EIBs can be scheduled to pick up files, generating those files automatically from query output requires additional integration work.

This project bridges that gap by automatically populating an existing EIB Excel template with Snowflake query results, enabling an orchestrated import workflow without building a separate API-based import and job-polling mechanism.

## Architecture

1. **Snowflake:** Query and shape data to match the EIB template's expected schema and column order.
2. **Workato:** Orchestrate the workflow and retrieve the Excel template from FileStorage.
3. **Python:** Use `openpyxl` to populate the existing workbook with CSV query output.
4. **SFTP:** Transfer the completed Excel file.
5. **Workday:** Invoke the EIB integration and rely on native import processing and error reporting.

## Design Approach

The solution separates responsibilities across existing platforms rather than recreating functionality:

- **Snowflake** handles data extraction and shaping.
- **Python** handles the focused task of populating the Excel template.
- **Workato** handles orchestration and file transfer.
- **Workday EIB** handles import processing.

The script uses Python's standard `csv` and `io` modules with `openpyxl`. It loads the existing workbook and writes data to the designated worksheet starting at row 6, following the five standard header rows in Workday EIB templates. It then returns the completed workbook as bytes.

The implementation prioritizes simplicity and maintainability over a standalone framework. Schema alignment is handled by the Snowflake query, while orchestration and import processing remain with the platforms already responsible for them.

## Technology Stack

Python · openpyxl · Snowflake · Workato · Workday EIB · SFTP

## Scope

Designed as a component of a Workato recipe, the script assumes a compatible EIB template and correctly ordered CSV data. The surrounding workflow invokes it only when data is available. Workday remains responsible for import processing and reporting errors.

The result is a practical example of automating an enterprise data workflow by solving the missing integration step without unnecessarily duplicating existing platform capabilities.
