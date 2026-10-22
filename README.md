# Hotel Revenue & Booking Intelligence

## Project Overview

Hotel Revenue & Booking Intelligence is an end-to-end data analytics project focused on hotel booking behavior, cancellation patterns, Average Daily Rate (ADR), and data quality.

The project combines PostgreSQL, SQL, Python, pandas, and Power BI to transform hotel booking data into validated analytical insights and an interactive business intelligence report.

The goal is to demonstrate how data profiling, SQL analysis, metric validation, and dashboard development can support evidence-based business decisions.

## Business Objectives

- Analyze booking volume and cancellation patterns.
- Compare booking behavior between City Hotel and Resort Hotel.
- Evaluate cancellation rates by market segment and lead-time group.
- Explore monthly booking and cancellation trends.
- Compare Average Daily Rate (ADR) between hotel types.
- Examine operational indicators such as special requests and booking changes.
- Identify data quality issues before using metrics for business interpretation.
- Present key performance indicators through an executive dashboard.

## Dataset

The project uses two hotel booking CSV files:

- `H1.csv` — Resort Hotel
- `H2.csv` — City Hotel

**Total records: 119,390 hotel bookings**

| Hotel Type | Booking Records |
|---|---:|
| Resort Hotel | 40,060 |
| City Hotel | 79,330 |
| **Total** | **119,390** |

The dataset includes hotel type, cancellation status, arrival dates, lead time, Average Daily Rate (ADR), market segment, special requests, booking changes, and other booking attributes.

The original source CSV files were preserved during the data quality investigation.

## Tools & Technologies

- **PostgreSQL** — Relational data storage and querying.
- **SQL** — Data validation, aggregation, and analytical queries.
- **Python** — Source data profiling and data quality investigation.
- **pandas** — Data inspection and processing.
- **Power BI Desktop** — Interactive dashboards and business intelligence.
- **GitHub** — Version control, project publication, and documentation.

## Power BI Report

The Power BI report contains two analytical pages.

### 1. Executive Overview

Provides a high-level summary of booking performance through key performance indicators and visualizations.

**Key Performance Indicators**

- Total Bookings
- Canceled Bookings
- Not Canceled Bookings
- Cancellation Rate
- Average ADR
- Average Lead Time
- Total Special Requests
- Total Booking Changes

**Visual Analysis**

- Cancellation rate by hotel type.
- Booking status by hotel type.
- Cancellation rate by lead-time group.

### 2. Cancellation Analysis

Examines cancellation patterns and differences across hotel booking categories.

**Visual Analysis**

- Cancellation Rate by Market Segment
- Cancellation Rate by Month
- Average Daily Rate by Hotel Type

The report's key metrics were reconciled against PostgreSQL analytical results.

## Key Analytical Findings

### Booking and Cancellation Performance

- Total booking records: 119,390.
- Canceled bookings: 44,224.
- Overall cancellation rate: 37.04%.
- Resort Hotel cancellation rate: 27.76%.
- City Hotel cancellation rate: 41.73%.

City Hotel has a higher observed cancellation rate than Resort Hotel, with a difference of 13.97 percentage points.

### Lead-Time Analysis

Cancellation rates increase across longer lead-time groups, particularly for City Hotel. This relationship identifies a useful area for further investigation, but it does not establish that lead time causes cancellations.

### Market Segment Analysis

Cancellation rates differ substantially by market segment.

- City Hotel — Groups: 68.86% cancellation rate.
- Resort Hotel — Groups: 42.39% cancellation rate.
- City Hotel — Direct: 17.33% cancellation rate.
- Resort Hotel — Direct: 13.48% cancellation rate.
- City Hotel — Online TA: 37.40% cancellation rate.
- Resort Hotel — Online TA: 35.24% cancellation rate.

Group bookings at City Hotel have a particularly high observed cancellation rate, while direct bookings have lower rates in both hotel types. These findings describe associations and do not establish the causes of cancellations.

### Monthly Booking Trends

August has the highest booking volume for both hotel types in the analyzed dataset. Monthly cancellation patterns were reviewed with year and month identified in the Power BI visual tooltip.

### Average Daily Rate (ADR)

- Resort Hotel average ADR: 94.95.
- City Hotel average ADR: 105.30.
- Resort Hotel minimum ADR: -6.38.
- City Hotel maximum ADR: 5,400.

The dataset contains negative, zero, and unusually high ADR values that require investigation before financial interpretation. The currency is not specified in the source dataset.

**Important:** ADR represents an average daily booking rate. It should not be interpreted as total hotel revenue.

## Data Quality and Validation

The project includes source data profiling and investigations into repeated rows, whitespace, missing values, null markers, and data types.

Key data quality practices include:

- Preserving the original source CSV files.
- Investigating repeated rows without automatically deleting them.
- Profiling missing values and potential null markers.
- Examining whitespace and row-level differences.
- Identifying unusual ADR values for further review.
- Validating analytical booking counts and cancellation rates against PostgreSQL results.
- Documenting limitations before interpreting metrics for business decisions.

Data quality findings are documented separately to support transparency and reproducibility.

## Project Structure

```text
Hotel_Revenue_Booking_Intelligence/
├── data/
├── sql/
├── python/
├── powerbi/
├── reports/
├── documentation/
├── Hotel_Revenue_Booking_Intelligence.pbix
└── README.md
```

**Folder contents**

- `data/` — Original source CSV files, maintained locally.
- `sql/` — SQL scripts for validation and analytical queries.
- `python/` — Python scripts for source data profiling and data quality investigation.
- `powerbi/` — Local Power BI project files.
- `reports/` — Initial SQL findings and analytical reporting.
- `documentation/` — Project scope, source profile, data quality investigations, and data dictionary.
- `Hotel_Revenue_Booking_Intelligence.pbix` — Published Power BI report.

The source CSV files are not included in the public repository.

## Current Project Status

- PostgreSQL staging table loaded with 119,390 hotel booking records.
- SQL validation completed for booking counts, cancellation rates, monthly trends, lead-time groups, market segments, and ADR data quality.
- Python source data profiling scripts published.
- Data quality investigations documented.
- Power BI report completed with two analytical pages: Executive Overview and Cancellation Analysis.
- Executive KPIs reconciled against PostgreSQL results.
- Cancellation metrics reviewed by hotel type, lead-time group, and market segment.
- Repository documentation and analytical findings published.

## Project Documentation

The supporting documentation includes the project scope, initial data profile, repeated row investigation, whitespace and row comparison, missing value profiling, null marker classification, and data dictionary.

[**View the project documentation folder**](https://github.com/albertosanchez-data/hotel-revenue-booking-intelligence/tree/main/documentation)

[**View the SQL findings report**](https://github.com/albertosanchez-data/hotel-revenue-booking-intelligence/blob/main/reports/initial_sql_findings.md)

## Professional Skills Demonstrated

- Data analysis and business intelligence.
- SQL and relational database workflows.
- PostgreSQL data validation and analytical querying.
- Python-based data profiling and quality investigation.
- KPI definition, reconciliation, and interpretation.
- Power BI dashboard development.
- Business-oriented analytical communication.
- Technical documentation and version control.

## Author

**Alberto Sanchez**

Data Analyst | Data Quality | SQL | PostgreSQL | Power BI | Excel | Business Intelligence

- **GitHub:** https://github.com/albertosanchez-data
- **LinkedIn:** https://www.linkedin.com/in/alberto-sanchez-data/

---

*This project is part of my data analytics portfolio and demonstrates an end-to-end approach to hotel booking analysis and business intelligence using PostgreSQL, SQL, Python, and Power BI.*
