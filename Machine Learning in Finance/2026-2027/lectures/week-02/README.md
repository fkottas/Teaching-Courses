# Week 2 — NumPy, Pandas, and exploratory data analysis

**Course:** Machine Learning in Finance · MPhil in Economics  
**Teaching date:** 21 October 2026 · 15:00–18:00 Greece time (Europe/Athens)  
**Release date:** 15 October 2026  
**Status:** Published

Week 2 builds the data-handling skills required before supervised-learning models. The lecture uses the complete UCI Default of Credit Card Clients dataset and keeps the data source, variable definitions, code, outputs, and assignment together in one student route.

## Start here

| Resource | Purpose |
|---|---|
| [Lecture 2 presentation](slides/Lecture_02_Python_Foundations_II_NumPy_Pandas_EDA_2026-2027.pptx) | Editable lecture slides |
| [Executed Colab notebook](notebooks/lecture_02_numpy_pandas_eda.ipynb) | Worked examples with visible outputs |
| [Spyder/local Python script](notebooks/lecture_02_numpy_pandas_eda.py) | Local version of the notebook code |
| [Dataset and variable guide](data/README.md) | Source, licence, observation unit, target, variables, and limitations |
| [Complete dataset](../../lectures/lecture-00-01/data/credit/default_of_credit_card_clients.csv.gz) | Compressed 30,000-row UCI dataset used by the notebook |
| [Mathematics reference](reference/mathematics_to_insert.md) | Rendered equations, notation, numerical checks, and slide locations |
| [Weekly assignment](assignment/README.md) | Required analysis and submission instructions |

## Learning objectives

By the end of this lecture, you should be able to:

- represent financial observations with NumPy arrays;
- load, inspect, filter, transform, and join Pandas DataFrames;
- distinguish identifiers, features, coded categories, and the binary target;
- calculate missingness, descriptive statistics, grouped default rates, and correlations;
- produce labelled plots and explain what they show;
- identify data-quality limitations before fitting a supervised-learning model.

## Lecture route

1. **NumPy:** arrays, shapes, indexing, vectorised returns, portfolio weights, and missing numeric values.
2. **Pandas:** loading the credit table, checking dimensions, data types, unique identifiers, and target balance.
3. **Descriptive statistics:** count, mean, standard deviation, quartiles, minimum, maximum, and IQR.
4. **Grouped analysis:** credit-limit bands, borrower counts, median age, and observed default rates.
5. **Data operations:** labels, joins, derived variables, and transformations.
6. **Visual evidence:** target balance, credit-limit versus bill amount, and correlation analysis.
7. **Interpretation:** descriptive association, data limitations, and what must be checked before modelling.

## Data and reproducibility

The notebook reads the complete compressed dataset from the course repository through a raw GitHub URL. The file contains 30,000 observations and 25 columns, including the identifier, 23 explanatory variables, and the default-payment target. Run the notebook from top to bottom so that every table and plot is regenerated.

The dataset originates from the UCI Machine Learning Repository, dataset 350, and is licensed under CC BY 4.0. Read the data guide before interpreting any coded variable.

## Submission

Submit the completed Colab notebook one day before the next course meeting, on 20 October 2026. Keep code outputs visible and place a short interpretation beside every important table or plot. Complete the associated DataCamp Python practice.

## Mathematics

The PowerPoint remains editable and the equations are provided separately. Use the mathematics reference for the exact equation, definitions, numerical check, and slide number. The equations are rendered as GitHub mathematics rather than displayed as raw LaTeX text.

## Quality checklist

Before submission, confirm that:

- the notebook runs from the first cell to the last cell;
- the source and licence are stated;
- the observation unit and target coding are explained;
- the dataset shape is 30,000 rows by 25 columns;
- missingness and duplicate rows are checked;
- every plot has a title, axis labels, and an interpretation;
- no causal conclusion is drawn from a descriptive correlation or group comparison.
