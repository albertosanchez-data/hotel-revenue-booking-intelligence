# Missing Values Profile

## 1. Objective

Identify missing or NULL-like values in `H1.csv` and `H2.csv` during initial source-data profiling.

## 2. Method

Python was used to count empty strings and the following case-insensitive markers after trimming surrounding whitespace:

- `NULL`
- `NA`
- `N/A`
- `NONE`
- `NAN`

This is an initial profiling rule, not a final data-cleaning policy.

## 3. Results

| Column   | H1.csv Missing | H1.csv % | H2.csv Missing | H2.csv % |
| -------- | -------------: | -------: | -------------: | -------: |
| Children |              0 |    0.00% |              4 |    0.01% |
| Country  |            464 |    1.16% |             24 |    0.03% |
| Agent    |          8,209 |   20.49% |          8,131 |   10.25% |
| Company  |         36,952 |   92.24% |         75,641 |   95.35% |

## 4. Initial Interpretation

- `Children`: investigate the four missing values in `H2.csv`.
- `Country`: consider the missing country information when conducting country-based analysis.
- `Agent`: missing values may reflect bookings without a recorded agent.
- `Company`: the high missing proportion may reflect bookings without an associated company.

These interpretations require validation against the dataset definitions and business context.

## 5. Data Protection and Processing Status

The original CSV files remain unchanged.

No missing values were replaced, and no records were deleted as part of this profiling step.

The source data has since been imported into the PostgreSQL staging table `public.stg_hotel_bookings`, containing 119,390 records.

The staging table preserves the source fields as text for subsequent validation and analysis.

## 6. Follow-up

Missing-value classifications and literal NULL-like markers were investigated in the source-data profiling process.

Before any future cleaning or exclusion, document the relevant field definitions, business rules, and expected analytical impact. Do not assume that every missing value should be replaced or that every NULL-like marker has the same meaning.
