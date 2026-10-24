# Week 3 assignment — Leakage-safe preprocessing

Submit one reproducible Google Colab notebook one day before the next course meeting. Complete the related DataCamp Python practice as part of the weekly exercise.

## Required notebook evidence

1. Load the complete course dataset and document the UCI source, licence or citation, observation unit, target, and variable meanings.
2. Show shape, dtypes, missingness, duplicate count, unique-ID count, target balance, and coded-category frequencies.
3. Create one controlled missingness example in memory. Explain whether the response is imputation, an indicator, removal, or a combination, and why.
4. Create a duplicate-detection example and explain why an identifier is not automatically evidence that two rows are economically different.
5. Apply one documented outlier flag to a numeric variable. Report the threshold and count before deciding whether any treatment is appropriate.
6. Separate numeric, categorical, identifier, and target columns.
7. Split the data with a fixed random seed and target stratification.
8. Build a `ColumnTransformer` with a numeric `Pipeline` and a categorical `Pipeline`. Use training-only fitting and `handle_unknown="ignore"`.
9. Display transformed shapes and feature names. Explain in plain language how the workflow prevents leakage.

## Submission standard

The notebook must run from top to bottom in a fresh Colab runtime. Keep outputs visible, label every chart, and write short interpretations after the important outputs. Do not upload a private or modified copy of the source data; reference the canonical course file.

