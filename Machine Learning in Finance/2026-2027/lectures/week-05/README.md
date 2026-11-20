# Week 5 — Introduction to Machine Learning and Logistic Regression

**Machine Learning in Finance · 2026–2027**  
**Teaching date:** 25 November 2026 · 15:00–18:00 Greece time (Europe/Athens)  
**Release:** Published 20 November 2026

This week has one coherent purpose: introduce the machine-learning vocabulary, compare prediction-led modelling with theory-led econometrics, and develop logistic regression as the first transparent probability model. PCA, clustering, and reinforcement learning appear as a clear conceptual map with finance examples; their full mathematical treatment, together with trees, boosting, alternative classifiers, explainability, and neural networks, is reserved for later weeks.

## Package contents

| Item | Purpose |
| --- | --- |
| slides/Lecture_05_Introduction_to_Machine_Learning_and_Logistic_Regression_2026-2027.pptx | 96-slide editable PowerPoint deck |
| notebooks/lecture_05_introduction_to_machine_learning_and_logistic_regression_finance.ipynb | Runnable Colab lab for the financial question, logistic probability, likelihood, regularisation, calibration, and threshold policy |
| reference/mathematics.md | Corrected formulas with symbol definitions, worked numerical examples, and GitHub-safe notation |
| reference/quality_assessment.md | Scope and quality review of this release |
| reference/attributions.md | Figure and source credits |
| reference/next_weeks_plan.md | Week-by-week route from Week 5 through Week 12 |
| reference/web_figures | Supporting visuals used in the deck |
| data/credit_ml_sample.csv | Synthetic/course-sized credit sample used by the notebook |
| assignment/README.md | Week 5 student assignment |

## Teaching route

1. Start with a financial decision and define the future target.
2. Distinguish econometric inference from predictive generalisation.
3. Introduce supervised, unsupervised, and reinforcement learning at the correct level.
4. Protect the train, validation, and test boundaries.
5. Derive the logistic score, sigmoid, odds, likelihood, log-loss, gradient, and regularisation objectives.
6. Fit and inspect a probability model before selecting a decision threshold.

## Mathematics policy

The deck uses high-resolution rendered equation figures for stable mathematical typography in PowerPoint and GitHub. The formulas remain visually sharp and the surrounding slide text, tables, charts, and code remain editable. The authoritative source formulas are kept in reference/mathematics.md so future corrections can be made without repairing a damaged presentation package.

The formulas avoid unsupported macros and unmatched delimiters. The Elastic Net objective is written with an explicit sum over coefficients and excludes the intercept from the penalty:

$$
J_{\mathrm{EN}}(\beta_0,\boldsymbol{\beta})
=J(\beta_0,\boldsymbol{\beta})
+\lambda[
\alpha\sum_{j=1}^{p}\lvert\beta_j\rvert
+(1-\alpha)\frac{1}{2}\sum_{j=1}^{p}\beta_j^2
].
$$

## Student workflow

Open the week page, download the editable PPTX if you want to annotate it, open the notebook in Colab or Jupyter, run it from top to bottom, read the mathematics reference, and submit only the final assignment work. The sample is synthetic and is for teaching the modelling workflow, not for lending decisions.

## Status

Week 5 is published as a complete package. The deck includes completed worked checks; only the final weekly assignment is intentionally unsolved. The later-week plan is included for structure, but each later deck will be delivered separately so it can be reviewed before the next one is built.
