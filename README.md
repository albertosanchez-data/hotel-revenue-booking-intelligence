
# Hotel Revenue & Booking Intelligence

## Project Overview

Hotel Revenue & Booking Intelligence is a data analytics project focused on hotel booking behavior, cancellation patterns, and daily rate analysis.

The project combines PostgreSQL, SQL, Python, and Power BI to organize booking data and develop an interactive business intelligence report that supports data-driven decision-making.

## Business Objectives

- Analyze booking volume and cancellation patterns.
- Compare booking behavior between City Hotel and Resort Hotel.
- Evaluate cancellation rates across market segments and lead-time groups.
- Explore monthly cancellation patterns.
- Compare average daily rates by hotel type.
- Monitor operational indicators such as special requests and booking changes.
- Present key performance indicators through an executive dashboard.

## Dataset

The project uses hotel booking data from two source files:

- `H1.csv` — Resort Hotel
- `H2.csv` — City Hotel

**Total records:** 119,390 hotel bookings.

The dataset includes booking information such as hotel type, cancellation status, arrival dates, lead time, average daily rate (ADR), market segment, special requests, and booking changes.

## Tools & Technologies

- **PostgreSQL** — Data storage and querying.
- **SQL** — Data exploration and analytical queries.
- **Python** — Source data profiling and data analysis.
- **pandas** — Data inspection and processing.
- **Power BI Desktop** — Data visualization and business intelligence.
- **GitHub** — Project documentation and version control.

## Power BI Report

The report contains two analytical pages.

### 1. Executive Overview

Provides a high-level view of booking performance through key performance indicators and visualizations.

Key indicators include:

- Total Bookings
- Canceled Bookings
- Not Canceled Bookings
- Cancellation Rate
- Average ADR
- Average Lead Time
- Total Special Requests
- Total Booking Changes

Visual analysis includes cancellation rates by hotel type, booking status by hotel type, and cancellation rate by lead time.

### 2. Cancellation Analysis

Explores cancellation patterns and rate differences through three visualizations:

- Cancellation Rate by Market Segment
- Cancellation Rate by Month
- Average Daily Rate by Hotel Type

## Key Analytical Areas

### Booking Performance
Measures total booking volume and compares canceled versus non-canceled reservations.

### Cancellation Analysis
Examines cancellation behavior by hotel type, market segment, month, and lead time.

### Rate Analysis
Uses Average Daily Rate (ADR) to compare daily booking rates between hotel types.

**Note:** ADR represents the average daily rate, not total hotel revenue.

### Operational Indicators
Tracks special requests and booking changes to provide additional context about booking behavior.

## Project Structure

```text
Hotel_Revenue_Booking_Intelligence/
├── data/
├── sql/
├── python/
├── powerbi/
├── reports/
├── documentation/
└── README.md
```

## Current Project Status

- PostgreSQL staging table loaded with 119,390 hotel booking records.
- SQL validation completed for booking counts, cancellation rates, monthly trends, lead-time groups, market segments, and ADR data quality.
- Power BI report completed with two analytical pages: Executive Overview and Cancellation Analysis.
- Executive KPIs reconciled against PostgreSQL results.
- Cancellation rates validated by hotel type, lead-time range, and market segment.
- Monthly cancellation analysis reviewed with year and month identified in the visual tooltip.
- Data-quality observations documented, including negative, zero, and unusually high ADR values.
- Final Power BI metric reconciliation completed.
- Repository documentation and final publication review remain in progress.
- - **Project Documentation:** [View the documentation folder](documentation/)

## Professional Skills Demonstrated

- Data analysis and business intelligence
- SQL and relational database workflows
- Python-based data profiling
- KPI definition and interpretation
- Data visualization and dashboard development
- Analytical communication and project documentation

## Author

**Alberto Sanchez**

Data Analyst | Data Quality | SQL | PostgreSQL | Power BI | Excel | Business Intelligence

- **GitHub:** https://github.com/albertosanchez-data
- **LinkedIn:** https://www.linkedin.com/in/alberto-sanchez-data/

---

*This project is part of my data analytics portfolio and demonstrates an end-to-end approach to hotel booking analysis and business intelligence.*
