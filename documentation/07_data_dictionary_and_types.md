# Data Dictionary and PostgreSQL Type Plan

## 1. Objective

Document the 31 source columns shared by `H1.csv` and `H2.csv`, their proposed analytical data types, and the validation requirements for future analysis.

This document distinguishes the proposed analytical types from the actual PostgreSQL staging schema.

## 2. Current PostgreSQL Staging Schema

The source data has already been imported into:

`public.stg_hotel_bookings`

Verified row counts:

- `H1.csv` (Resort Hotel): 40,060 rows
- `H2.csv` (City Hotel): 79,330 rows
- Total: 119,390 rows

The staging table contains 32 columns: `source_file` plus the 31 original source columns. The `source_file` column is `VARCHAR` and `NOT NULL`; the 31 original source columns are stored as text and are nullable.

The staging table preserves the source values for validation and analysis. The proposed types below have not been applied as a replacement schema.

## 3. Proposed Analytical Data Types

| Column                      | Proposed PostgreSQL Type               | Validation Required                                                    |
| --------------------------- | -------------------------------------- | ---------------------------------------------------------------------- |
| IsCanceled                  | SMALLINT                               | Confirm values are 0 or 1                                              |
| LeadTime                    | INTEGER                                | Confirm non-negative values                                            |
| ArrivalDateYear             | SMALLINT                               | Validate year values                                                   |
| ArrivalDateMonth            | VARCHAR(15)                            | Validate month names and whitespace                                    |
| ArrivalDateWeekNumber       | SMALLINT                               | Validate week range                                                    |
| ArrivalDateDayOfMonth       | SMALLINT                               | Validate day range                                                     |
| StaysInWeekendNights        | INTEGER                                | Confirm non-negative values                                            |
| StaysInWeekNights           | INTEGER                                | Confirm non-negative values                                            |
| Adults                      | INTEGER                                | Validate guest counts                                                  |
| Children                    | INTEGER, subject to validation         | Inspect source values and missing-value patterns                       |
| Babies                      | INTEGER                                | Validate guest counts                                                  |
| Meal                        | VARCHAR(20)                            | Validate categories and whitespace                                     |
| Country                     | VARCHAR(10), subject to validation     | Review country codes, missing markers, and actual values               |
| MarketSegment               | VARCHAR(30)                            | Validate categories and whitespace                                     |
| DistributionChannel         | VARCHAR(30)                            | Validate categories and whitespace                                     |
| IsRepeatedGuest             | SMALLINT                               | Confirm values are 0 or 1                                              |
| PreviousCancellations       | INTEGER                                | Confirm non-negative values                                            |
| PreviousBookingsNotCanceled | INTEGER                                | Confirm non-negative values                                            |
| ReservedRoomType            | VARCHAR(10)                            | Validate categories and whitespace                                     |
| AssignedRoomType            | VARCHAR(10)                            | Validate categories and whitespace                                     |
| BookingChanges              | INTEGER                                | Confirm non-negative values                                            |
| DepositType                 | VARCHAR(30)                            | Validate categories and whitespace                                     |
| Agent                       | TEXT or VARCHAR, subject to validation | Preserve identifier values and review missing markers                  |
| Company                     | TEXT or VARCHAR, subject to validation | Preserve identifier values and review missing markers                  |
| DaysInWaitingList           | INTEGER                                | Confirm non-negative values                                            |
| CustomerType                | VARCHAR(30)                            | Validate categories and whitespace                                     |
| ADR                         | NUMERIC(12,2), subject to validation   | Validate numeric conversion, precision, outliers, and business meaning |
| RequiredCarParkingSpaces    | INTEGER                                | Validate counts                                                        |
| TotalOfSpecialRequests      | INTEGER                                | Validate counts                                                        |
| ReservationStatus           | VARCHAR(30)                            | Validate categories and whitespace                                     |
| ReservationStatusDate       | DATE                                   | Validate date format and invalid dates                                 |

These are proposed analytical types, not enforced constraints. Final choices must reflect the actual source values and analytical requirements. In particular, `Agent` and `Company` should be treated as identifiers rather than assumed numeric measures.

## 4. Import and Data-Quality Principles

- Preserve the original `H1.csv` and `H2.csv` files.
- Do not delete repeated rows automatically.
- Do not replace text NULL markers or missing values without documented handling rules.
- Validate source values before enforcing final data types or constraints.
- Keep accepted and rejected records traceable if future transformation rules exclude any rows.
- Preserve `source_file` to identify the origin of each record.
- Investigate unusual ADR values instead of automatically removing them.
- Distinguish the Average Daily Rate (ADR) field from confirmed realized revenue.
- Document any future transformations and reconcile their results with the original row counts.

## 5. Current Status

- Source profiling has been completed for the two CSV files.
- Repeated-row patterns, whitespace, missing-value patterns, and text NULL markers have been investigated.
- The staging table has been loaded and its 119,390 records verified.
- The analytical SQL scripts have been reviewed.
- The final analytical schema and any future type conversions remain subject to validation.
- The Power BI report still requires reconciliation of key metrics against SQL results.

## 6. Next Steps

1. Complete the documentation review.
2. Reconcile key Power BI metrics with

## 8. Power BI Validation Status

**Status: Completed**

The Power BI report was reviewed against the PostgreSQL results.

### Executive Overview

The following metrics were validated:

- Total bookings: 119,390
- Canceled bookings: 44,224
- Not canceled bookings: 75,166
- Cancellation rate: 37.04%
- Total special requests: 68,215

### Cancellation Analysis

The following elements were reviewed:

- Cancellation rate by hotel type.
- Cancellation rate by lead-time range.
- Cancellation rate by market segment.
- Monthly cancellation trend, with year and month visible in the tooltip.
- Average Daily Rate (ADR) visual.
- Visual layout and readability.

The validated cancellation rates match the PostgreSQL query results. The Aviation market segment has no Resort Hotel records in the reviewed SQL results.

### Remaining Data Quality Considerations

- Negative and zero ADR values remain documented as data-quality observations.
- High ADR values remain documented as potential outliers.
- These values must not be removed without further business justification.

### Current Project Status

The staging data load, SQL validation, and Power BI metric reconciliation have been completed.

The next phase is final project quality assurance, documentation consistency, and repository review.
