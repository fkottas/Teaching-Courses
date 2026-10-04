# Lecture 0 and Lecture 1

## Course orientation and Python foundations

**Lecture date:** 14 October 2026  
**Time:** 15:00–18:00 Greece time (Europe/Athens)  
**Course:** Machine Learning in Finance · MPhil in Economics · NKUA  
**Language:** English

This presentation introduces the 13-week course structure and begins the official Week 1 material. The notebook uses the public Apple price and volume dataset and a real credit-risk dataset from the UCI Machine Learning Repository.

## Student files

| Resource | Link |
|---|---|
| Latest editable PowerPoint | [Download the PPTX](slides/Lecture_00_01_Course_Orientation_and_Python_Foundations_2026-2027_EDITABLE_SAVE_SAFE_FINAL.pptx) |
| Google Colab notebook | [Open the Colab notebook](notebooks/lecture_00_01_colab.ipynb) |
| Weekly assignment | [Read the assignment](assignment/README.md) |
| Apple financial data | [Open the CSV](data/finance-charts-apple.csv) |
| Credit-risk data dictionary | [Read the data dictionary](data/data_dictionary.md) |

GitHub does not preview PowerPoint slides directly in the browser. Download the PPTX to open, edit, or present it.

## Assessment reminder

The official weighting is 20% weekly exercises, 40% capstone project, and 40% final examination, with a bonus exercise worth up to 10%.

## Open dataset

Source repository: <https://github.com/plotly/datasets>

Direct CSV: <https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv>

The file contains 506 daily observations and 12 columns. The lecture uses the date, Apple closing price, and Apple trading volume columns. The remaining source columns stay in the file so the source data remain intact.

## Credit-risk dataset

Source: <https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients>

Official download: <https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip>

The included CSV contains 30,000 borrower records, 23 explanatory variables, an identifier, and the target `default payment next month`. The presentation and `data/data_dictionary.md` explain every column, its unit, its coding, and its role in the supervised-learning workflow.

## Running the notebook

Open the notebook in Google Colab and run the cells from top to bottom. The notebook downloads the public CSV directly, so it also runs when opened without cloning the repository. A local copy is included in `data/` for traceability and repository navigation.
