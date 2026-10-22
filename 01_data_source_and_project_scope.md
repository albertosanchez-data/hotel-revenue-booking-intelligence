# Hotel Revenue & Booking Intelligence

## 1. Project Overview

This project analyzes hotel booking data to identify booking patterns, cancellation behavior, seasonality, market segment differences, and Average Daily Rate (ADR) trends.

The project uses PostgreSQL and SQL for data validation and analysis, Python for data profiling, and Power BI for interactive reporting.

## 2. Data Source

**Dataset:** Hotel Booking Demand

**Research paper:** Hotel Booking Demand Datasets

**Source:** https://pmc.ncbi.nlm.nih.gov/articles/PMC6297060/

**Files selected:**

- `H1.csv` — Resort Hotel
- `H2.csv` — City Hotel

Both files contain the same 31 source columns in the same order.

## 3. Main Business Questions

1. What percentage of bookings are canceled overall and by hotel type?
2. How does booking volume and cancellation behavior vary by arrival month and year?
3. How is booking lead time associated with cancellation rates?
4. How does ADR vary by hotel type, and which unusual values require investigation?
5. Which market segments account for the most bookings, and how do cancellation rates differ by segment?
6. What data quality issues should be considered when interpreting the results?

## 4. Technology Stack

- PostgreSQL and SQL
- Python
- Power BI
- Visual Studio Code
- CSV files as the original data source

## 5. Data Handling Principles

- Preserve the original source files.
- Profile and validate source data before interpreting analytical results.
- Keep the imported staging data unchanged during read-only analysis.
- Document data quality findings and any cleaning rules or exclusions.
- Do not classify identical-looking rows as invalid duplicates without investigation.
- Treat ADR as a recorded daily rate, not as confirmed revenue collected.
- Investigate unusual ADR values rather than automatically removing them.
- Interpret differences in cancellation rates as associations, not proof of causation.

## 6. Current Project Status

- Project folder structure created.
- Source files `H1.csv` and `H2.csv` stored in the `data` folder.
- Initial source data profiling completed.
- Staging table `public.stg_hotel_bookings` populated in PostgreSQL.
- Imported record counts verified:
  - `H1.csv`: 40,060 records
  - `H2.csv`: 79,330 records
  - Total: 119,390 records
- Eight SQL files reviewed, covering staging verification, booking and cancellation overview, ADR analysis and data quality, monthly trends, lead time, and market segments.
- ADR anomalies identified for investigation, including one negative value and unusually high values.
- Power BI report created with Executive Overview and Cancellation Analysis pages.
- Remaining work: review project documentation, reconcile key Power BI metrics with SQL results, and perform a final project quality check before publication.
