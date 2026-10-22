
-- Project: Hotel Revenue & Booking Intelligence
-- File: 08_cancellation_by_market_segment.sql
-- Purpose: Compare bookings and cancellation rates by market segment.
-- Safety: Read-only query. Source data remains unchanged.

WITH prepared_data AS (
    SELECT
        source_file,
        COALESCE(
            NULLIF(TRIM("MarketSegment"), ''),
            'Missing'
        ) AS market_segment,
        TRIM("IsCanceled") AS cancellation_status
    FROM public.stg_hotel_bookings
)
SELECT
    market_segment,

    CASE
        WHEN source_file = 'H1.csv' THEN 'Resort Hotel'
        WHEN source_file = 'H2.csv' THEN 'City Hotel'
        ELSE 'Unknown'
    END AS hotel_type,

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

FROM prepared_data
GROUP BY
    market_segment,
    source_file
ORDER BY
    total_bookings DESC,
    market_segment,
    hotel_type;
