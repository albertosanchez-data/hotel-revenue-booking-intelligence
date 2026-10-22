# Initial Data Profile

## 1. Project

Hotel Revenue & Booking Intelligence

## 2. Source Files

- `H1.csv` — Resort Hotel
- `H2.csv` — City Hotel
- Columns per file: 31

## 3. Structural Validation

| Validation                                 | H1.csv | H2.csv |
| ------------------------------------------ | -----: | -----: |
| Data rows                                  | 40,060 | 79,330 |
| Columns                                    |     31 |     31 |
| Rows with unexpected column counts         |      0 |      0 |
| Exact repeated rows after first occurrence |  6,092 | 25,902 |

Total original rows: 119,390.

Exact repeated rows were identified during initial profiling. These counts describe repeated row content and do not, by themselves, establish that the records are invalid.

## 4. Missing or NULL-Like Values

| Column   | H1.csv | H2.csv |
| -------- | -----: | -----: |
| Children |      0 |      4 |
| Country  |    464 |     24 |
| Agent    |  8,209 |  8,131 |
| Company  | 36,952 | 75,641 |

These figures are from the initial source-data profiling. Missing-value definitions and classifications are documented separately.

## 5. Initial Findings

- Both files have the same 31 column names in the same order.
- No rows with unexpected column counts were detected.
- Exact repeated rows were identified and investigated in subsequent profiling.
- Missing values in Agent and Company may be legitimate, depending on booking circumstances.
- Missing values in Children and Country require context before deciding how to handle them.

## 6. Important Data Quality Principles

- Exact repeated rows are not automatically invalid duplicates.
- Missing values must be handled according to documented business rules.
- Initial profiling findings should be distinguished from later analysis and validation results.
- The original source CSV files must remain unchanged.

## 7. Current Status

- Initial structural profiling completed using Python.
- Source row counts verified in PostgreSQL staging:
  - `H1.csv`: 40,060 rows
  - `H2.csv`: 79,330 rows
  - Total: 119,390 rows
- The staging table and SQL analysis scripts have been reviewed.
- Further documentation review and reconciliation of Power BI metrics remain pending.

Original CSV files remain unchanged. The initial repeated-row counts do not imply that records were deleted.
