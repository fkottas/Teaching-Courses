# Dataset dictionary

## `finance-charts-apple.csv`

| Column | Meaning used in this course |
|---|---|
| `Date` | Trading date |
| `AAPL.Open` | Apple opening price |
| `AAPL.High` | Apple daily high |
| `AAPL.Low` | Apple daily low |
| `AAPL.Close` | Apple closing price |
| `AAPL.Volume` | Daily trading volume |
| `AAPL.Adjusted` | Adjusted closing price supplied by the source |
| `dn` | Lower chart-band field supplied by the source |
| `mavg` | Moving-average field supplied by the source |
| `up` | Upper chart-band field supplied by the source |
| `direction` | Direction field supplied by the source |

The Week 1 analysis table uses `Date`, `AAPL.Close`, and `AAPL.Volume`. The notebook renames them to `date`, `close`, and `volume` for readability.

## `credit/default_of_credit_card_clients.csv`

This is the CSV version included in the course package of the UCI Default of Credit Card Clients dataset. It contains 30,000 borrower records and 25 columns. The target column is `default payment next month`, with 23,364 observations equal to 0 and 6,636 observations equal to 1 in the supplied file.

The feature columns include credit limit, demographic fields, repayment-status variables, bill amounts, and payment amounts. The lecture uses this table to demonstrate a real credit-risk observation unit, class balance, target definition, and later supervised-learning preparation.

### Credit variable definitions

| Column | Meaning and coding used in this course |
|---|---|
| `ID` | Client identifier. It is retained for traceability and excluded from predictive features. |
| `LIMIT_BAL` | Amount of given credit in New Taiwan dollars, including individual and supplementary credit. |
| `SEX` | Source coding: 1 = male; 2 = female. |
| `EDUCATION` | Source coding: 1 = graduate school; 2 = university; 3 = high school; 4 = others. |
| `MARRIAGE` | Source coding: 1 = married; 2 = single; 3 = others. |
| `AGE` | Age in years. |
| `PAY_0` | Repayment status in September 2005; the source uses 0 for September. |
| `PAY_2` | Repayment status in August 2005. |
| `PAY_3` | Repayment status in July 2005. |
| `PAY_4` | Repayment status in June 2005. |
| `PAY_5` | Repayment status in May 2005. |
| `PAY_6` | Repayment status in April 2005. |
| `BILL_AMT1`–`BILL_AMT6` | Monthly bill statement amounts from September 2005 back to April 2005, in New Taiwan dollars. |
| `PAY_AMT1`–`PAY_AMT6` | Previous payment amounts from September 2005 back to April 2005, in New Taiwan dollars. |
| `default payment next month` | Binary target: 1 = default payment next month; 0 = no default payment next month. |

For `PAY_0`–`PAY_6`, the source describes −1 as paid duly and values 1–9 as payment delay from one month to nine months or more. The supplied file also contains 0 and −2 codes; students must inspect and document these values before recoding them. The official UCI page reports no missing values, but an absence of missing values does not mean that every coded value is automatically valid for a modelling decision.

## Provenance

- Source repository: <https://github.com/plotly/datasets>
- Direct file: <https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv>
- Downloaded for this course package: 2026-10-03
- Observation unit: one daily Apple market observation
- Teaching target in Week 1: none; the lecture is descriptive and prepares the later supervised-learning workflow

## Credit-data provenance

- UCI dataset page: <https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients>
- Official download: <https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip>
- Observation unit: one borrower credit-card account record
- Target: whether the borrower defaulted in the following month
- Citation: Yeh, I. (2009). *Default of Credit Card Clients* [Dataset]. UCI Machine Learning Repository. DOI: <https://doi.org/10.24432/C55S3H>
- Licence: Creative Commons Attribution 4.0 International (CC BY 4.0)
