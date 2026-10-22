# Repeated Rows Investigation

## 1. Objective

Investigate exact repeated rows in `H1.csv` and `H2.csv` without modifying the source files.

## 2. Method

Python was used to read the CSV files and count complete rows using `Counter`.

Two rows were considered identical when all 31 raw column values matched exactly.

## 3. Results

| Metric                            | H1.csv | H2.csv |
| --------------------------------- | -----: | -----: |
| Original data rows                | 40,060 | 79,330 |
| Distinct row patterns             | 33,968 | 53,428 |
| Patterns appearing more than once |  2,325 |  5,846 |
| Rows beyond the first occurrence  |  6,092 | 25,902 |

Total original rows: 119,390.

Total repeated occurrences beyond the first occurrence: 31,994.

## 4. Observations

- Both files contain exact repeated rows.
- Some row patterns occur many times.
- The most frequent examples examined have `IsCanceled = 1`.
- The dataset does not include an explicit unique reservation identifier among the 31 inspected columns.
- Some values contain leading or trailing spaces.

## 5. Interpretation and Limitations

Exact repeated rows are not automatically invalid duplicates.

Different reservations may share the same recorded attributes. The available columns do not establish whether every repeated row represents an accidental duplicate.

Whitespace may also affect exact comparisons. The results describe exact matches in the raw source values, not confirmed duplicate reservations.

Further investigation is required before deciding how repeated rows should be handled.

## 6. Data Protection and Processing Status

The investigation script reads the original CSV files without modifying them.

The source CSV files remain unchanged.

The data has since been imported into the PostgreSQL staging table `public.stg_hotel_bookings`, where 119,390 records were verified.

The staging data has been analyzed using read-only SQL queries. No records were deleted as part of this repeated-row investigation.

## 7. Follow-up

Whitespace differences and missing-value patterns were investigated in subsequent profiling documentation.

The repeated-row findings should remain documented as a data quality observation. Any future deduplication decision must be supported by an explicit business rule and validation.
