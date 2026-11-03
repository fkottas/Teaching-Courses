# Week 4 data guide

## Canonical source

The teaching data are derived from the **Default of Credit Card Clients** dataset in the UCI Machine Learning Repository:

- UCI dataset page: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- Archive used by the notebook: https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip
- Dataset DOI: 10.24432/C55S3H
- Original study: Yeh, I.-C. (2009), “Modeling credit card customer default by logistic regression.”

The complete source data contain 30,000 client observations and 25 columns, including the target `default_next_month`. The notebook downloads the source archive directly in Colab. The file `credit_feature_engineering_sample.csv` contains the first 1,000 rows after the same documented feature construction and is provided for quick inspection and repository navigation.

## Observation unit and target

- **Observation unit:** one credit-card client at the reporting snapshot.
- **Target:** `default_next_month`, where 1 means default on payment in the following month and 0 means no default in the following month.
- **Prediction point used in this lecture:** the reporting snapshot, before the following-month outcome is observed.
- **Important limitation:** the published UCI table is a cross-sectional teaching dataset with a six-month history encoded in columns. It is not a full event-level production history. The lecture uses it to teach feature construction and timing discipline, not to claim production-grade credit-risk performance.

## Raw variables

| Field | Meaning | Type / unit | Timing role |
|---|---|---|---|
| `ID` | Client identifier | integer | Entity key; never a predictive measurement by itself |
| `LIMIT_BAL` | Amount of given credit | monetary amount in the source data | Available at snapshot |
| `SEX` | Recorded sex code | categorical code | Available at snapshot; interpret cautiously |
| `EDUCATION` | Education code | categorical code | Available at snapshot |
| `MARRIAGE` | Marital-status code | categorical code | Available at snapshot |
| `AGE` | Client age | years | Available at snapshot |
| `PAY_0` | Most recent repayment-status code | ordered status code | Snapshot history; the source names the most recent month `PAY_0` |
| `PAY_2`–`PAY_6` | Earlier repayment-status codes | ordered status codes | Lookback history |
| `BILL_AMT1`–`BILL_AMT6` | Bill statement amounts | monetary amounts | Snapshot and six-month lookback |
| `PAY_AMT1`–`PAY_AMT6` | Previous payment amounts | monetary amounts | Snapshot and six-month lookback |
| `default_next_month` | Default-payment outcome in the next month | binary target | Future outcome; never use as an input feature |

The source includes `PAY_0` and then `PAY_2` through `PAY_6`; the absence of `PAY_1` is a property of the published column naming and is preserved rather than silently invented.

## Derived variables used in the lecture

| Field | Definition | Interpretation | Safety rule |
|---|---|---|---|
| `utilization` | `BILL_AMT1 / LIMIT_BAL` | Current billed balance relative to credit limit | Zero limits become missing; retain a denominator flag |
| `total_bill_6m` | Sum of `BILL_AMT1`–`BILL_AMT6` | Six-month billed amount | Only the lookback fields are aggregated |
| `total_paid_6m` | Sum of `PAY_AMT1`–`PAY_AMT6` | Six-month recorded payments | Do not add future payments |
| `payment_to_bill_6m` | `total_paid_6m / total_bill_6m` | Payment relative to billed amount | Zero billed amount becomes missing |
| `overdue_count_6m` | Count of `PAY_* > 0` across six status fields | Frequency of overdue status | Status-code meaning must be documented |
| `max_delay_6m` | Maximum of the six status fields | Worst recorded status code | Valid only because the code is ordered in the source convention |
| `recent_overdue` | `1(PAY_0 > 0)` | Whether the most recent status is overdue | Uses the snapshot status only |
| `high_utilization` | `1(utilization ≥ 0.80)` | Whether billed balance reaches 80% of limit | Threshold is a teaching rule; validate it in modelling |
| `stress_flag` | `high_utilization × recent_overdue` | Joint high-use and recent-overdue state | Keep both component fields as well |
| `bill_change_1m` | `BILL_AMT1 − BILL_AMT2` | Recent change in billed amount | Direction is retained |
| `payment_change_1m` | `PAY_AMT1 − PAY_AMT2` | Recent change in payment amount | Direction is retained |
| `log_limit` | `log(1 + LIMIT_BAL)` | Compressed credit-limit scale | Transformation is fit/applied without using the target |

The file `feature_correlation_matrix.json` contains the pairwise correlation matrix for the selected engineered variables used in the correlation and cluster slides. It is calculated from the complete UCI source after the documented feature construction.

## Data-quality checks required in the lab

Check column types, duplicate IDs, missing values, zero denominators, infinite ratios, negative or impossible amounts, status-code ranges, target balance, and the number of rows affected by every policy. A feature should not be considered complete until its data-quality policy is written down.

The file lookback_stability_summary.json contains the six encoded lookback-period summaries used in the presentation: mean bill amount, mean payment amount, mean utilization, and the share of accounts with a positive repayment-status code for t−5 through t. It is calculated from the real UCI source. These are within-account lookback profiles, not calendar-period population drift, because the UCI file does not provide observation dates or later monitoring cohorts.

