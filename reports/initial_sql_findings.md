# Hotel Revenue & Booking Intelligence

## Initial SQL Findings

### 1. Dataset overview

- Total booking records: 119,390
- Resort Hotel records: 40,060
- City Hotel records: 79,330
- Cancellation rate overall: 37.04%
- Canceled bookings: 44,224

### 2. Cancellation performance by hotel

- Resort Hotel cancellation rate: 27.76% (11,122 bookings)
- City Hotel cancellation rate: 41.73% (33,102 bookings)
- Difference: 13.97 percentage points

City Hotel has a substantially higher cancellation rate than Resort Hotel. Further analysis is needed to investigate possible relationships with lead time, market segment, and distribution channel.

### 3. Average Daily Rate (ADR)

- Resort Hotel average ADR: 94.95
- City Hotel average ADR: 105.30
- Resort Hotel minimum ADR: -6.38
- City Hotel minimum ADR: 0
- Resort Hotel maximum ADR: 508
- City Hotel maximum ADR: 5,400

City Hotel has a higher average recorded ADR. Negative, zero, and unusually high ADR values should be investigated before using them for financial decisions. The currency is not specified in the source dataset.

### 4. Monthly booking trends

- August has the highest booking volume for both hotel types.
- Resort Hotel: 4,894 bookings in August and 4,573 in July.
- City Hotel: 8,983 bookings in August.
- City Hotel has a higher monthly cancellation rate than Resort Hotel in every month.
- The highest monthly cancellation rate is 46.32% for City Hotel in April and 33.45% for Resort Hotel in August.

### 5. Data quality considerations

- The original source CSV files were preserved.
- Repeated rows were not automatically deleted.
- ADR values should be investigated before excluding any records.
- Cancellation rates describe booking records and should not be interpreted as realized revenue.

### 6. Next analytical steps

1. Analyze cancellation rate by lead time.
2. Compare cancellation rates by market segment and distribution channel.
3. Examine ADR and booking patterns by month.
4. Prepare validated measures for Excel and Power BI.

### 7. Cancellation rates by market segment

- Online TA is the largest segment by booking volume in both hotels.
- City Hotel — Groups: 13,975 bookings, 9,623 cancellations, 68.86% cancellation rate.
- Resort Hotel — Groups: 5,836 bookings, 2,474 cancellations, 42.39% cancellation rate.
- City Hotel — Direct: 6,093 bookings, 1,056 cancellations, 17.33% cancellation rate.
- Resort Hotel — Direct: 6,513 bookings, 878 cancellations, 13.48% cancellation rate.
- City Hotel — Online TA: 38,748 bookings, 14,491 cancellations, 37.40% cancellation rate.
- Resort Hotel — Online TA: 17,729 bookings, 6,248 cancellations, 35.24% cancellation rate.

**Business interpretation:** Group bookings at City Hotel show a particularly high cancellation rate and deserve further investigation. Direct bookings have lower cancellation rates in both hotel types. These are observed associations and do not establish the causes of cancellations.

The `Undefined` segment in City Hotel contains only two records, so its 100% cancellation rate should not be generalized.

### 8. Overall project conclusions

1. City Hotel accounts for more bookings and has a higher overall cancellation rate than Resort Hotel.
2. August is the busiest arrival month for both hotels in this dataset.
3. Cancellation rates increase across longer lead-time groups, especially for City Hotel.
4. Cancellation performance differs substantially by market segment.
5. ADR includes unusual values that require validation before financial interpretation.
6. The staging dataset has been preserved; repeated rows and unusual values have not been automatically deleted.

### 9. Recommended dashboard KPIs

- Total bookings
- Canceled bookings
- Cancellation rate
- Average Daily Rate (ADR)
- Bookings by hotel type and arrival month
- Cancellation rate by lead-time group
- Cancellation rate by market segment
