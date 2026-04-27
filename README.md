# Global Supply Chain & Distribution Data Warehouse

## 📌 Project Overview
This project is an end-to-end Data Engineering and Business Intelligence solution designed to track, analyze, and visualize global supply chain logistics. The architecture bridges backend database computation with a highly interactive, minimalist Tableau frontend, allowing executives to track KPIs, supplier reliability, and fulfillment bottlenecks via a dynamic Current Year (CY) vs. Previous Year (PY) parameter interface.

## 🛠️ Tech Stack & Tools
* **Database Engine:** Oracle SQL Developer
* **Data Modeling:** Star Schema (STG, DIM, FACT tables)
* **Advanced Compute:** CTEs, Window Functions, Materialized Views, PL/SQL
* **Business Intelligence:** Tableau
* **UI/UX Design:** Minimalist 60-30-10 aesthetic, Dual-Axis Sparklines, Executive Dashboarding

## 🏗️ Architecture & Features

### 1. Database-Level Compute
To optimize BI performance, heavy data transformations were pushed down to the database level. 
* **Materialized Views:** Pre-calculates row-level binary logic (e.g., On-Time Delivery status) and time-series aggregates.
* **PL/SQL Automation:** Includes stored procedures to update and refresh the materialized views as new staging data arrives.

### 2. Parameter-Driven BI Dashboard
The Tableau frontend abandons standard filter shelves in favor of complex Calculated Fields driven by a single `Select Year` parameter. This enables:
* **Overlapping CY vs. PY Sparklines:** Dual-axis line charts that instantly compare historical performance without dropping context.
* **Dynamic KPIs:** Real-time percentage variance calculations for Total Logistics Spend, Average Lead Time, Volume Throughput, and Defect Rates.

### 3. Visual Insights
* **The Lead Time Crisis:** A step-line forecast chart tracking shipping delays.
* **Global Fulfillment Heatmap:** Spatial analysis of distribution density.
* **Supplier Reliability Matrix:** A scatter plot mapping defect rates against delivery speed to identify high-risk vendors.

## 💡 Key Technical Challenges Solved
* Resolved complex "Aggregate vs. Non-Aggregate" calculation boundaries in Tableau by nesting conditional logic inside aggregation functions.
* Bypassed Tableau's Order of Operations filter conflicts by engineering custom Level of Detail (LOD) and Boolean internal filters to maintain PY data visibility.
