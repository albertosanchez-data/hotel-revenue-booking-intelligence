
-- Project: Hotel Revenue & Booking Intelligence
-- File: 06_monthly_booking_trends.sql
-- Purpose: Analyze booking volume and cancellations by arrival year and month.
-- Safety: Read-only query. Source data remains unchanged.

WITH prepared_data AS (
    SELECT
        source_file,
        TRIM("ArrivalDateYear") AS arrival_year_text,
        TRIM("ArrivalDateMonth") AS arrival_month,
        TRIM("IsCanceled") AS cancellation_status
    FROM public.stg_hotel_bookings
),
validated_data AS (
    SELECT
        source_file,
        arrival_month,
        CASE
            WHEN arrival_year_text ~ '^[0-9]{4}$'
            THEN arrival_year_text::INTEGER
            ELSE NULL
        END AS arrival_year,
        cancellation_status
    FROM prepared_data
)
SELECT
    arrival_year,
    arrival_month,

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
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS cancellation_rate_pct

FROM validated_data
GROUP BY
    arrival_year,
    arrival_month,
    source_file
ORDER BY
    arrival_year NULLS LAST,
    CASE TRIM(arrival_month)
        WHEN 'January' THEN 1
        WHEN 'February' THEN 2
        WHEN 'March' THEN 3
        WHEN 'April' THEN 4
        WHEN 'May' THEN 5
        WHEN 'June' THEN 6
        WHEN 'July' THEN 7
        WHEN 'August' THEN 8
        WHEN 'September' THEN 9
        WHEN 'October' THEN 10
        WHEN 'November' THEN 11
        WHEN 'December' THEN 12
        ELSE 13
    END,
    source_file;
