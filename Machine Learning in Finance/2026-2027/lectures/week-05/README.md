# Machine Learning in Finance — Week 5

## Introduction to Machine Learning and Logistic Regression

**Academic year:** 2026–2027  
**Programme:** MPhil in Economics, National and Kapodistrian University of Athens  
**Course mode:** English; supervised learning throughout  
**Teaching date:** 25 November 2026 · 15:00–18:00 Greece time (Europe/Athens)  
**Release:** Published 20 November 2026

This week introduces the machine-learning vocabulary, compares prediction-led modelling with theory-led econometrics, and develops logistic regression as the first transparent probability model. PCA, clustering, and reinforcement learning are included only as an overview; their detailed mathematics and applications belong to later weeks.

## Start here

| Resource | Purpose | Link |
|---|---|---|
| Lecture presentation | 96-slide editable deck with theory, mathematics, finance examples, plots, code, and completed worked checks | [Open the PPTX](slides/Lecture_05_Introduction_to_Machine_Learning_and_Logistic_Regression_2026-2027.pptx) |
| Colab notebook | Runnable laboratory for target definition, logistic probability, likelihood, log-loss, regularisation, calibration, and threshold policy | [Open the notebook](notebooks/lecture_05_introduction_to_machine_learning_and_logistic_regression_finance.ipynb) |
| Dataset | Synthetic course-sized borrower sample used by the notebook | [Download the CSV](data/credit_ml_sample.csv) |
| Data guide | Observation unit, target, limitations, and reproducibility instructions | [Read the data guide](data/README.md) |
| Mathematics reference | GitHub-safe equations, symbol definitions, and numerical examples | [Read the mathematics reference](reference/mathematics.md) |
| Figure credits | Sources for the supporting visuals used in the deck | [Open the figure credits](reference/attributions.md) |
| Quality assessment | Scope, layout, editability, and validation checks | [Read the assessment](reference/quality_assessment.md) |
| Next-weeks route | The planned separation of Weeks 6–12 | [Open the course route](reference/next_weeks_plan.md) |
| Weekly assignment | The only intentionally unsolved component | [Read the assignment](assignment/README.md) |

## Learning route

1. Define a financial decision, one observation, the future target, the outcome horizon, and the information cutoff.
2. Distinguish econometric inference from predictive generalisation.
3. Introduce supervised, unsupervised, and reinforcement learning at overview level.
4. Protect the training, validation, and test boundaries.
5. Derive the logistic score, sigmoid, odds, likelihood, log-loss, gradient, and regularisation objectives.
6. Fit and inspect a probability model before selecting a decision threshold.

## Data and reproducibility

The sample is synthetic and course-sized. It is supplied so that the notebook runs without an external download. It illustrates the modelling workflow and must not be used for lending decisions.

The notebook expects the CSV at data/credit_ml_sample.csv when opened from the package root. Run the cells from top to bottom and keep the outputs. The deck contains completed worked examples; the assignment is the only unsolved exercise.

## Mathematics and editability

The PowerPoint equations are embedded as high-resolution typeset visuals so that PowerPoint does not reinterpret fragile Markdown delimiters. The copyable reference deliberately uses plain Unicode notation rather than LaTeX commands. This prevents the GitHub rendering problems previously caused by unmatched delimiters and unsupported macros.

The Elastic Net objective in the reference is:

~~~text
J_EN(β₀, β) = J(β₀, β) + λ [ α Σⱼ |βⱼ| + (1−α)(1/2) Σⱼ βⱼ² ]
~~~

The intercept β₀ is excluded from the penalty.

## Student workflow

Open the presentation, run the notebook, read the data guide and mathematics reference, and then complete the assignment. Do not use the final test labels to choose a penalty, model, or decision threshold.

## Scope boundary

Trees, financial performance metrics, cross-validation, boosting, alternative classifiers, explainability, monitoring, and neural networks are assigned to later weeks. They are not repeated here as full technical treatments.
