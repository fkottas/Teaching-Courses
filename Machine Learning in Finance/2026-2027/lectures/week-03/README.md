# Week 3 — Data Cleaning and Preprocessing

This is the complete Week 3 package for **Machine Learning in Finance** (NKUA MPhil Economics, 2026–2027).

## Start here

| Resource | Purpose |
|---|---|
| [Lecture presentation](slides/Lecture_03_Data_Cleaning_and_Preprocessing_2026-2027.pptx) | Editable lecture deck with native text, tables, charts, and code examples |
| [Colab notebook](notebooks/lecture_03_data_cleaning_preprocessing.ipynb) | Executable student lab with visible outputs |
| [Local Python script](notebooks/lecture_03_data_cleaning_preprocessing.py) | Same workflow for Spyder or a local environment |
| [Data guide](data/README.md) | Source, access path, observation unit, variables, and modelling roles |
| [Weekly assignment](assignment/README.md) | Required notebook evidence and submission checklist |
| [Mathematics to insert](reference/mathematics_to_insert.md) | Render-safe equations, slide locations, and explanations |

## Learning focus

The lecture follows the supervised-learning route in the syllabus. It covers data-quality auditing, missing values, duplicates, outliers, categorical encoding, numeric scaling, train/test separation, leakage prevention, `ColumnTransformer`, and `Pipeline`. No unsupervised-learning model is used.

## Data rule

The source file is the complete UCI credit-card default table stored once in the course repository as a compressed CSV. The notebook reads that canonical copy; it does not create or rely on a truncated replacement. The controlled missingness example is a small in-memory copy used only to demonstrate a cleaning decision because the source file contains no blank cells.

## Suggested sequence

1. Read the data guide before opening the code.
2. Review the presentation in order: theory first, then code and visible outputs.
3. Run the notebook from the first cell in Google Colab.
4. Compare the output with the interpretation in the presentation.
5. Complete the assignment and keep the fitted preprocessing object with your work.

Release date: 24 October 2026  
Planned teaching slot: Week 3, 15:00–18:00 Greece time; confirm the official programme timetable.

