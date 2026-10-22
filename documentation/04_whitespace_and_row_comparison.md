# Whitespace Investigation and Row Comparison

## 1. Objective

Investigate leading and trailing spaces in `H1.csv` and `H2.csv` and determine whether trimming changes the number of distinct complete-row patterns.

## 2. Method

Python was used to inspect raw CSV values and compare complete rows before and after applying `strip()` to each field.

The transformation was performed in memory only.

Original CSV files were not modified.

## 3. Results

| Metric                                            | H1.csv | H2.csv |
| ------------------------------------------------- | -----: | -----: |
| Original rows                                     | 40,060 | 79,330 |
| Distinct raw row patterns                         | 33,968 | 53,428 |
| Distinct patterns after trimming                  | 33,968 | 53,428 |
| Patterns appearing more than once before trimming |  2,325 |  5,846 |
| Patterns appearing more than once after trimming  |  2,325 |  5,846 |

## 4. Observations

- Leading spaces were detected in `IsRepeatedGuest`, `Agent`, and `Company`.
- Trailing spaces were detected in `Meal`, `ReservedRoomType`, `AssignedRoomType`, and `DepositType`.
- Example values changed in representation after trimming.
- The number of distinct complete-row patterns remained unchanged in both files.
- The number of repeated row patterns also remained unchanged.

## 5. Interpretation

Trimming leading and trailing spaces did not change the complete-row pattern counts in these files.

This does not establish that every field is valid or that all data-cleaning issues have been resolved.

The literal text value `NULL` must be distinguished from an actual missing value when preparing data for analysis or database loading.

## 6. Data Protection and Processing Status

The original CSV files remain unchanged.

The whitespace comparison was performed in memory. No records were deleted, and no cleaned CSV files were created by this investigation.

The original source data has since been imported into the PostgreSQL staging table `public.stg_hotel_bookings`, containing 119,390 verified records.

## 7. Follow-up

Whitespace, repeated-row patterns, and missing-value representations were investigated in the source-data profiling process.

The PostgreSQL staging data and SQL analysis scripts have also been reviewed. Remaining work includes reviewing the documentation, reconciling key Power BI metrics with SQL results, and performing a final project quality check.
