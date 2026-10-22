# NULL Marker Classification

## 1. Objective

Distinguish empty fields from text NULL markers in selected columns of `H1.csv` and `H2.csv` during source-data profiling.

## 2. Results

| Column   | H1.csv TEXT NULL | H2.csv TEXT NULL |
| -------- | ---------------: | ---------------: |
| Children |                0 |                0 |
| Country  |              464 |               24 |
| Agent    |            8,209 |            8,131 |
| Company  |           36,952 |           75,641 |

No empty fields were found in these four columns according to the initial profiling results.

## 3. Interpretation

- `Children`: no empty or text NULL values were detected in the initial profiling results.
- `Country`: text NULL markers indicate missing country information and require a documented handling rule.
- `Agent`: a missing agent value may represent a booking without a recorded travel agent.
- `Company`: a missing company value may represent a booking without an associated company.

These are possible interpretations, not confirmed explanations for every record.

Text NULL markers must be distinguished from genuinely empty fields and database NULL values. Their treatment should follow documented business rules.

## 4. Data Protection and Processing Status

The original CSV files remain unchanged.

No values were replaced, and no records were deleted as part of this profiling step.

The source data has since been imported into the PostgreSQL staging table `public.stg_hotel_bookings`, containing 119,390 verified records.

The staging table stores the source columns as text for subsequent validation and analysis.

## 5. Follow-up

The initial NULL-marker classification is documented.

The remaining work includes completing the documentation review, reconciling key Power BI metrics with SQL results, and performing a final project quality check.

Any future replacement or exclusion of missing values must be based on documented rules and validated against the intended analytical use.
