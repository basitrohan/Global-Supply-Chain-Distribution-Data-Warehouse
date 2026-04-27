CREATE MATERIALIZED VIEW MV_LOGISTICS_PERFORMANCE
BUILD IMMEDIATE
REFRESH COMPLETE ON DEMAND
AS
WITH Shipment_Logic AS (
    SELECT 
        SHIPMENT_ID,
        SHIP_DATE,
        DELIVERY_DATE,
        QUANTITY,
        SHIPPING_COST,
        -- Calculate lead time (Difference between dates)
        -- In Oracle, subtracting two dates gives you the number of days
        CAST(DELIVERY_DATE - SHIP_DATE AS INT) as ACTUAL_LEAD_TIME,
        -- We'll assume a standard 7-day target for the "On-Time" logic 
        -- since a target column isn't in your fact table
        CASE 
            WHEN (DELIVERY_DATE - SHIP_DATE) <= 7 THEN 1 
            ELSE 0 
        END AS IS_ON_TIME
    FROM FACT_SHIPMENTS
)
SELECT 
    SHIPMENT_ID,
    SHIP_DATE,
    TRUNC(SHIP_DATE, 'MM') as SHIP_MONTH,
    EXTRACT(YEAR FROM SHIP_DATE) as SHIP_YEAR,
    QUANTITY,
    SHIPPING_COST,
    ACTUAL_LEAD_TIME,
    IS_ON_TIME,
    -- Advanced Window Function for running total
    SUM(SHIPPING_COST) OVER (PARTITION BY EXTRACT(YEAR FROM SHIP_DATE) ORDER BY SHIP_DATE) as RUNNING_TOTAL_COST
FROM Shipment_Logic;


--...........................

CREATE OR REPLACE PROCEDURE REFRESH_LOGISTICS_DATA AS
BEGIN
    -- This command tells Oracle to recalculate the Materialized View
    DBMS_MVIEW.REFRESH('MV_LOGISTICS_PERFORMANCE');
    
    DBMS_OUTPUT.PUT_LINE('Success: Logistics Materialized View has been refreshed.');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: Refresh failed. Check source tables.');
END;
/

BEGIN
   REFRESH_LOGISTICS_DATA;
END;
/

--..................................

-- This query demonstrates the logic currently powering your Materialized View
WITH Shipment_Logic AS (
    -- PART A: THE CTE 
    -- Purpose: Row-level transformations and data cleaning
    SELECT 
        SHIPMENT_ID,
        SHIP_DATE,
        DELIVERY_DATE,
        SHIPPING_COST,
        -- Calculate lead time directly in the DB
        CAST(DELIVERY_DATE - SHIP_DATE AS INT) as ACTUAL_LEAD_TIME,
        -- Binary performance logic: 1 if within 7 days, else 0
        CASE 
            WHEN (DELIVERY_DATE - SHIP_DATE) <= 7 THEN 1 
            ELSE 0 
        END AS IS_ON_TIME
    FROM FACT_SHIPMENTS
)
-- PART B: WINDOW FUNCTIONS & FINAL SELECTION
-- Purpose: Time-series analysis and partitioning
SELECT 
    SHIPMENT_ID,
    SHIP_DATE,
    ACTUAL_LEAD_TIME,
    IS_ON_TIME,
    SHIPPING_COST,
    -- The Window Function: 
    -- 1. PARTITION BY: Resets the sum every new year
    -- 2. ORDER BY: Ensures the sum adds up day-by-day (Running Total)
    SUM(SHIPPING_COST) OVER (
        PARTITION BY EXTRACT(YEAR FROM SHIP_DATE) 
        ORDER BY SHIP_DATE
    ) as RUNNING_TOTAL_COST
FROM Shipment_Logic
ORDER BY SHIP_DATE DESC
fetch first 10 rows only;
