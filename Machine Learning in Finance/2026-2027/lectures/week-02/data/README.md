# Lecture 2 data guide

The notebook uses the complete 30,000-row UCI Default of Credit Card Clients dataset in compressed CSV form. The course copy is stored at [default_of_credit_card_clients.csv.gz](../../lectures/lecture-00-01/data/credit/default_of_credit_card_clients.csv.gz). This week does not create a second dataset copy.

Source: UCI Machine Learning Repository dataset 350
URL: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
Citation: Yeh (2009), Default of Credit Card Clients, DOI https://doi.org/10.24432/C55S3H
Licence: CC BY 4.0
Observation unit: one borrower credit-card account record
Target: default payment next month, renamed to default_next_month
Monetary unit: New Taiwan dollars

| Variable | Meaning | Use |
|---|---|---|
| ID | Client identifier | Traceability and duplicate checks; not a predictive feature |
| LIMIT_BAL | Given credit limit | Distribution, grouping, and derived ratios |
| AGE | Age in years | Distribution and age bands |
| PAY_0 to PAY_6 | Source-coded repayment status over six months | Code-frequency audit |
| BILL_AMT1 to BILL_AMT6 | Monthly bill statements in New Taiwan dollars | Descriptive statistics and total bill |
| PAY_AMT1 to PAY_AMT6 | Previous payment amounts in New Taiwan dollars | Descriptive statistics and total payment |
| SEX, EDUCATION, MARRIAGE | Source-coded demographic categories | Data dictionary and label join |
| default payment next month | 1 = default, 0 = no default | Target balance and group comparisons |

The supplied file contains 30,000 rows and 25 columns and reports no blank cells. No missing cells does not remove the need to inspect special codes or variable definitions.
