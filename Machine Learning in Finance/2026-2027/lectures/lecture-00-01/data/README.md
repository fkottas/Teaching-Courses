# Lecture 0–1 data guide

This folder documents the open data used in Lecture 0–1 and reused in later lectures.

## Default of Credit Card Clients

| Item | Information |
|---|---|
| Dataset | Default of Credit Card Clients |
| Source | [UCI Machine Learning Repository, dataset 350](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) |
| Citation | Yeh, I. (2009), *Default of Credit Card Clients*, DOI [10.24432/C55S3H](https://doi.org/10.24432/C55S3H) |
| Licence | CC BY 4.0 |
| Observation unit | One borrower credit-card account record |
| Size | 30,000 observations and 25 columns |
| Target | Default payment next month: 1 = default, 0 = no default |
| Monetary unit | New Taiwan dollars |

The validated course copy is stored as [default_of_credit_card_clients.csv.gz](credit/default_of_credit_card_clients.csv.gz). It is a compressed CSV containing the complete 30,000-row dataset. The notebook reads it with pandas using compression="gzip".

The earlier truncated CSV copy was removed. Students should use the compressed file above or the official UCI source.

## Variable documentation

Use the [data dictionary](data_dictionary.md) before interpreting any variable. In particular, the repayment-status variables use source codes and should not be treated as ordinary continuous measurements without explanation.

## Reproducible loading

The following pattern loads the course copy from raw GitHub:

    import pandas as pd

    DATA_URL = "https://raw.githubusercontent.com/fkottas/Teaching-Courses/main/Machine%20Learning%20in%20Finance/2026-2027/lectures/lecture-00-01/data/credit/default_of_credit_card_clients.csv.gz"
    credit = pd.read_csv(DATA_URL, compression="gzip")

Always record the source, access date, observation unit, target definition, and any transformation in your notebook.
