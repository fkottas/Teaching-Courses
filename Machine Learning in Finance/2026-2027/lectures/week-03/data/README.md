# Week 3 data guide

## Canonical source

The Week 3 notebook reuses the complete course copy of the **Default of Credit Card Clients** dataset from the UCI Machine Learning Repository, dataset 350:

- Source: [UCI Machine Learning Repository — Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
- Course copy: [`lecture-00-01/data/credit/default_of_credit_card_clients.csv.gz`](../../lecture-00-01/data/credit/default_of_credit_card_clients.csv.gz)
- Source format: compressed CSV; 30,000 rows and 25 columns
- Observation unit: one credit-card account record for one borrower
- Target: `default_next_month` (`1` = default next month, `0` = no default)
- Monetary unit: New Taiwan dollars

The source file contains no blank cells and no exact duplicate rows. Week 3 therefore creates controlled in-memory examples for missingness and duplicate detection. The source file itself is never overwritten.

## Variable dictionary

| Variable | Meaning | Role in Week 3 |
|---|---|---|
| `ID` | Borrower identifier | Traceability only; exclude from predictors |
| `LIMIT_BAL` | Credit limit in New Taiwan dollars | Numeric predictor; inspect scale and extreme values |
| `SEX` | Sex code (`1`, `2`) | Categorical predictor |
| `EDUCATION` | Education code supplied by the source | Categorical code; inspect values before encoding |
| `MARRIAGE` | Marital-status code supplied by the source | Categorical code; inspect values before encoding |
| `AGE` | Age in years | Numeric predictor |
| `PAY_0` | September 2005 repayment-status code | Ordinal-like source code; preserve and document meaning |
| `PAY_2`–`PAY_6` | Repayment-status codes for earlier months | Ordinal-like source codes |
| `BILL_AMT1`–`BILL_AMT6` | Bill statement amounts for six months | Numeric financial variables |
| `PAY_AMT1`–`PAY_AMT6` | Previous payment amounts for six months | Numeric financial variables |
| `default_next_month` | Default payment next month | Binary target; never include in `X` |

The teaching pipeline uses a small, explicit predictor block so that the transformation is easy to inspect: `LIMIT_BAL`, `AGE`, `PAY_0`, `BILL_AMT1`, `PAY_AMT1`, `SEX`, `EDUCATION`, and `MARRIAGE`.

## Reproducibility

The Colab notebook reads the raw GitHub URL for the canonical `.csv.gz` file. If internet access is unavailable, download the same file from the course data path and update `DATA_URL` to its local path.

