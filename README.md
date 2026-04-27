# Full-Stack Global Supply Chain Data Platform & Warehouse

## 📌 Project Overview
This project demonstrates a complete, end-to-end data engineering and business intelligence platform. It covers the entire data lifecycle: synthetic data generation, multi-source ingestion, complex Python ETL pipelining into an Oracle Data Warehouse, advanced SQL compute, and a highly interactive executive Tableau dashboard.

## 🛠️ Tech Stack & Tools
* **Data Generation:** Python (`Faker`, `pandas`)
* **Storage & Databases:** PostgreSQL, CSV, XLSX, Oracle SQL Developer
* **ETL Engine:** Python (Database connectors & data manipulation)
* **Advanced DB Compute:** CTEs, Window Functions, Materialized Views, PL/SQL
* **Business Intelligence:** Tableau (Dual-axis, parameter-driven logic)

## 🏗️ Architecture & Pipeline Lifecycle

### 1. Synthetic Data Generation
* Leveraged the Python **Faker** library to generate massive, realistic supply chain datasets.
* Dispersed the generated data across three distinct sources to simulate a fragmented enterprise environment: a local **PostgreSQL** instance, flat **CSV** files, and formatted **Excel (XLSX)** spreadsheets.

### 2. Python ETL Pipelining
* Engineered a centralized Python ETL script that automated connections to PostgreSQL, local CSVs, and Excel files.
* Extracted the isolated datasets, performed light schema mappings, and established a bridge to load and append the unified data straight into an **Oracle Database**.

### 3. Data Warehousing & Cleaning (Oracle)
* Built out a complete Star Schema including Staging (**STG**), Dimension (**DIM**), and Fact (**FACT**) tables.
* Audited data types, executed schema modifications for type safety, and ran various data quality validation scripts before production use.

### 4. Advanced DB Compute Layer
* Migrated heavy business operations to the database to preserve frontend dashboard performance.
* Utilized **Common Table Expressions (CTEs)** and complex **Window Functions** (`SUM OVER`) to handle rolling cost calculations.
* Compiled a high-performance **Materialized View** and programmed a **PL/SQL Procedure** to handle scheduled data refreshes automatically.

### 5. Parameter-Driven Tableau Dashboard
* Built a high-end, visual dashboard using advanced calculated fields to bypass Tableau filter limitations.
* Engineered a custom `Select Year` parameter to force Current Year (CY) and Previous Year (PY) sparklines to perfectly overlap.
* Maintained a strict, high-contrast visual hierarchy optimal for executive analysis.
