
-- Project: Hotel Revenue & Booking Intelligence
-- File: 05_adr_data_quality.sql
-- Purpose: Investigate unusual ADR values.
-- Safety: Read-only query. No records are changed or removed.

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

    COUNT(*) FILTER (
        WHERE adr_text IS NULL
    ) AS missing_adr_rows,

    COUNT(*) FILTER (
        WHERE adr_text IS NOT NULL
          AND adr_value IS NULL
    ) AS invalid_adr_rows,

    COUNT(*) FILTER (
        WHERE adr_value < 0
    ) AS negative_adr_rows,

    COUNT(*) FILTER (
        WHERE adr_value = 0
    ) AS zero_adr_rows,

    COUNT(*) FILTER (
        WHERE adr_value > 500
    ) AS adr_above_500_rows,

    COUNT(*) FILTER (
        WHERE adr_value > 1000
    ) AS adr_above_1000_rows

FROM validated_data
GROUP BY source_file
ORDER BY source_file;
