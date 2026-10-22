
-- Project: Hotel Revenue & Booking Intelligence
-- File: 07_cancellation_by_lead_time.sql
-- Purpose: Analyze cancellation rates by booking lead time.
-- Safety: Read-only query. Source data remains unchanged.

WITH prepared_data AS (
    SELECT
        source_file,
        NULLIF(TRIM("LeadTime"), '') AS lead_time_text,
        TRIM("IsCanceled") AS cancellation_status
    FROM public.stg_hotel_bookings
),
validated_data AS (
    SELECT
        source_file,
        cancellation_status,
        CASE
            WHEN lead_time_text ~ '^[0-9]+$'
            THEN lead_time_text::INTEGER
            ELSE NULL
        END AS lead_time_days
    FROM prepared_data
),
grouped_data AS (
    SELECT
        CASE
            WHEN lead_time_days BETWEEN 0 AND 7 THEN '0-7 days'
            WHEN lead_time_days BETWEEN 8 AND 30 THEN '8-30 days'
            WHEN lead_time_days BETWEEN 31 AND 90 THEN '31-90 days'
            WHEN lead_time_days BETWEEN 91 AND 180 THEN '91-180 days'
            WHEN lead_time_days > 180 THEN '181+ days'
            ELSE 'Missing or invalid'
        END AS lead_time_group,

        CASE
            WHEN source_file = 'H1.csv' THEN 'Resort Hotel'
            WHEN source_file = 'H2.csv' THEN 'City Hotel'
            ELSE 'Unknown'
        END AS hotel_type,

        cancellation_status,

        CASE
            WHEN lead_time_days BETWEEN 0 AND 7 THEN 1
            WHEN lead_time_days BETWEEN 8 AND 30 THEN 2
            WHEN lead_time_days BETWEEN 31 AND 90 THEN 3
            WHEN lead_time_days BETWEEN 91 AND 180 THEN 4
            WHEN lead_time_days > 180 THEN 5
            ELSE 6
        END AS sort_order

    FROM validated_data
)
SELECT
    lead_time_group,
    hotel_type,

    COUNT(*) AS total_bookings,

    COUNT(*) FILTER (
        WHERE cancellation_status = '1'
    ) AS canceled_bookings,

    COUNT(*) FILTER (
        WHERE cancellation_status = '0'
    ) AS not_canceled_bookings,

    COUNT(*) FILTER (
        WHERE cancellation_status IS NULL
           OR cancellation_status NOT IN ('0', '1')
    ) AS invalid_or_missing_cancellation_values,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE cancellation_status = '1'
        ) / NULLIF(
            COUNT(*) FILTER (
                WHERE cancellation_status IN ('0', '1')
            ),
            0
        ),
        2
    ) AS cancellation_rate_pct

FROM grouped_data
GROUP BY
    lead_time_group,
    hotel_type,
    sort_order
ORDER BY
    sort_order,
    hotel_type;
