# Datasets and Provenance

Every dataset used in a lecture must be present in this repository or downloaded by a documented API/code cell. Students should not have to guess which file a slide refers to.

## Lecture 0–1 datasets

| Dataset | Use | Source and documentation |
|---|---|---|
| `finance-charts-apple.csv` | Apple closing price, volume, descriptive statistics and plots | [Plotly datasets](https://github.com/plotly/datasets) |
| `default_of_credit_card_clients.csv` | Introductory supervised credit-risk example | [UCI Machine Learning Repository, dataset 350](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) |
| `default of credit card clients.xls` | Original UCI workbook supplied with the converted CSV | UCI dataset 350; see the data dictionary |

The complete definitions, units, coding, target variable and licence/provenance notes are in the [Lecture 0–1 data dictionary](../lectures/lecture-00-01/data/data_dictionary.md).

## Student rule

Do not rename variables silently. If you transform a variable, record the transformation in the notebook and explain whether it is a predictor, target, identifier, date, or derived feature.
