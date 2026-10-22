
-- Project: Hotel Revenue & Booking Intelligence
-- File: 01_verify_staging_table.sql
-- Purpose: Verify the staging table and imported source data.
-- Safety: Read-only queries. No data is inserted, updated, or deleted.

-- 1. Confirm the active database and schema.
SELECT
    current_database() AS database_name,
    current_schema() AS schema_name;

-- 2. Confirm the total number of imported records.
SELECT
    COUNT(*) AS total_rows
FROM public.stg_hotel_bookings;

-- 3. Validate record counts by source file.
SELECT
    source_file,
    COUNT(*) AS total_rows
FROM public.stg_hotel_bookings
GROUP BY source_file
ORDER BY source_file;

-- 4. Review the staging table structure.
SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'stg_hotel_bookings'
ORDER BY ordinal_position;
