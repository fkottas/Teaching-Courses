# Machine Learning in Finance — Week 4

## Feature Engineering for Financial Data

**Academic year:** 2026–2027  
**Programme:** MPhil in Economics, National and Kapodistrian University of Athens  
**Course mode:** English; supervised learning throughout  
**Week focus:** Turn raw financial fields into interpretable, leakage-safe predictors.

## Start here

| Resource | Purpose | Link |
|---|---|---|
| Lecture presentation | 90-slide editable lecture deck with theory, worked cases, plots, code, scorecard methods, and analytical speaker notes | [Open the PPTX](slides/Lecture_04_Feature_Engineering_for_Financial_Data_2026-2027.pptx) |
| Colab notebook | Reproducible feature-engineering lab using the real UCI credit-default data | [Open the notebook](notebooks/lecture_04_feature_engineering_finance.ipynb) |
| Python script | Same lab as a plain `.py` file for inspection or local execution | [Open the script](notebooks/lecture_04_feature_engineering_finance.py) |
| Dataset guide | Source, observation unit, target, raw fields, derived fields, and limitations | [Read the data guide](data/README.md) |
| Lookback stability summary | Real UCI six-step input-history summaries used for the time-series plots | [Open JSON](data/lookback_stability_summary.json) |
| Monthly monitoring summary | Monthly fixed-bin distributions, category shares, default-rate series, and variable PSI from the resolved LendingClub extract | [Open JSON](data/monthly_monitoring_summary.json) |
| External figures | Sourced visuals for filter statistics, RFE, correlated-feature importance, Lasso, tree anatomy, and scorecard binning | [Open figure credits](slides/README.md) |
| Derived teaching sample | 1,000 rows derived from the complete UCI data; useful for quick inspection | [Download CSV](data/credit_feature_engineering_sample.csv) |
| Feature dictionary | Compact field-by-field definition for the derived sample | [Read the dictionary](reference/feature_dictionary.md) |
| Mathematics reference | Editable, plain-text formulas and the slide locations where they belong | [Read the mathematics reference](reference/mathematics_to_insert.md) |
| Weekly assignment | Submission requirements and analytical questions | [Read the assignment](assignment/README.md) |

## Learning route

1. Define the observation unit, target, prediction horizon, and information cutoff.
2. Translate a financial mechanism into a feature definition.
3. Construct ratios, counts, indicators, transformations, changes, rolling summaries, and interactions.
4. Check zero denominators, missing values, tails, and temporal ordering.
5. Separate descriptive association from causal interpretation.
6. Select variables with filter, wrapper, embedded, and stability-based methods inside the validation route.
7. Monitor numeric-bin distributions, categorical shares, and target default-rate time series as different objects.
8. Document every feature so that another analyst can reproduce it.

## Dataset and reproducibility

The notebook uses the **Default of Credit Card Clients** dataset from the UCI Machine Learning Repository. The target is whether the client defaulted on payment in the following month. The complete source file is downloaded by the notebook from the canonical UCI archive; the small CSV in this folder is a derived teaching sample and is not a replacement for the source data.

The sample contains the raw identifying, demographic, credit-limit, bill, payment, repayment-status, and target fields needed for the examples, plus the engineered features developed in the lecture. The data guide records the source, licence, target timing, and limitations.

The monthly monitoring section uses a public LendingClub loan extract mirrored at [akshayr89/Lending-Club---Exploratory-Data-Analysis](https://github.com/akshayr89/Lending-Club---Exploratory-Data-Analysis/blob/master/loan.csv). It filters to `Fully Paid` and `Charged Off` loans, then plots fixed-bin shares for `revol_util`, category shares for `grade`, and an eventual resolved-loan default-rate time series by `issue_d`. This is a transparent monitoring-mechanics example, not a one-month-forward PD estimate.

## What to submit

Submit one executed Colab notebook one day before the next course meeting. It must include the code, outputs, plots, feature dictionary, and a short interpretation for each selected feature. Do not claim that a descriptive relationship is causal.

## Important boundary

This week is about representation, not model competition. Do not select features using the full target-labelled dataset before a later validation step. Features that depend on training percentiles, scaling parameters, imputation values, or target information must be fitted inside the training route.

