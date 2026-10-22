
-- Project: Hotel Revenue & Booking Intelligence
-- File: 04_revenue_analysis.sql
-- Purpose: Analyze average daily rate (ADR) by hotel type.
-- ADR is the recorded daily rate, not total realized revenue.
-- Safety: Read-only query. Source data remains unchanged.

WITH prepared_data AS (
    SELECT
        source_file,
        NULLIF(TRIM("ADR"), '') AS adr_text
    FROM public.stg_hotel_bookings
),
validated_data AS (
    SELECT
        source_file,
        adr_text,
        CASE
            WHEN adr_text ~ '^[+-]?[0-9]+([.][0-9]+)?$'
            THEN adr_text::NUMERIC
            ELSE NULL
        END AS adr_value
    FROM prepared_data
)
SELECT
    CASE
        WHEN source_file = 'H1.csv' THEN 'Resort Hotel'
        WHEN source_file = 'H2.csv' THEN 'City Hotel'
        ELSE 'Unknown'
    END AS hotel_type,

    COUNT(*) AS total_bookings,

    COUNT(adr_value) AS valid_adr_records,

    COUNT(*) FILTER (
        WHERE adr_text IS NULL
    ) AS missing_adr_records,

    COUNT(*) FILTER (
        WHERE adr_text IS NOT NULL
          AND adr_value IS NULL
    ) AS invalid_adr_records,

    ROUND(AVG(adr_value), 2) AS average_daily_rate,

    ROUND(MIN(adr_value), 2) AS minimum_daily_rate,

    ROUND(MAX(adr_value), 2) AS maximum_daily_rate

FROM validated_data
GROUP BY source_file
ORDER BY source_file;
