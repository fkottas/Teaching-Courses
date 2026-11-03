# Week 4 lab

Open [`lecture_04_feature_engineering_finance.ipynb`](lecture_04_feature_engineering_finance.ipynb) in Google Colab. The notebook downloads the canonical UCI source when run in Colab, constructs the same features as the lecture, prints key outputs, creates labelled plots, demonstrates an interaction, and shows a training-only threshold example.

The `.py` file contains the same executable logic for students who prefer to inspect or run a plain Python script.

The notebook also plots the real six-step UCI lookback history and calculates variable PSI between the oldest encoded month and the reporting snapshot. It explicitly distinguishes this within-account history from production calendar-period drift.

The monthly monitoring section loads the open LendingClub extract from the public raw URL (or the packaged CSV when running locally). It calculates fixed-bin distributions for `revol_util_pct`, category shares for `grade`, the resolved-loan default-rate time series, and monthly variable PSI. The target is shown as a rate with counts and a denominator, not as a distribution plot. The notebook includes pre-rendered text outputs for the monthly tables; rerun the cells in Colab to regenerate plots and outputs.

