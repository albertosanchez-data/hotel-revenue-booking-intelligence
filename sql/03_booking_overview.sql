
-- Project: Hotel Revenue & Booking Intelligence
-- File: 03_booking_overview.sql
-- Purpose: Analyze booking volume and cancellation rates.
-- Safety: Read-only queries. Source data remains unchanged.

-- 1. Overall booking and cancellation overview.
SELECT
    COUNT(*) AS total_bookings,

    COUNT(*) FILTER (
        WHERE TRIM("IsCanceled") = '1'
    ) AS canceled_bookings,

    COUNT(*) FILTER (
        WHERE TRIM("IsCanceled") = '0'
    ) AS not_canceled_bookings,

    COUNT(*) FILTER (
        WHERE TRIM("IsCanceled") IS NULL
           OR TRIM("IsCanceled") NOT IN ('0', '1')
    ) AS invalid_or_missing_cancellation_values,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE TRIM("IsCanceled") = '1'
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS cancellation_rate_pct

FROM public.stg_hotel_bookings;


-- 2. Compare booking and cancellation rates by hotel type.
SELECT
    CASE
        WHEN source_file = 'H1.csv' THEN 'Resort Hotel'
        WHEN source_file = 'H2.csv' THEN 'City Hotel'
        ELSE 'Unknown'
    END AS hotel_type,

    COUNT(*) AS total_bookings,

    COUNT(*) FILTER (
        WHERE TRIM("IsCanceled") = '1'
    ) AS canceled_bookings,

    COUNT(*) FILTER (
        WHERE TRIM("IsCanceled") = '0'
    ) AS not_canceled_bookings,

    COUNT(*) FILTER (
        WHERE TRIM("IsCanceled") IS NULL
           OR TRIM("IsCanceled") NOT IN ('0', '1')
    ) AS invalid_or_missing_cancellation_values,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE TRIM("IsCanceled") = '1'
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS cancellation_rate_pct

FROM public.stg_hotel_bookings
GROUP BY source_file
ORDER BY source_file;
