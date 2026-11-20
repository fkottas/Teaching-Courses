# Week 5 quality assessment

Release reviewed for the 25 November 2026 lecture · 15:00–18:00 Greece time (Europe/Athens).

## Scope review

The prior material compressed PCA, K-means, reinforcement learning, NLP, trees, metrics, regularisation, logistic regression, and neural networks into one deck. That structure made the lecture difficult to teach and caused formulas to be introduced without enough explanation.

This release narrows Week 5 to a single route:

1. the modelling question and financial target;
2. machine learning versus econometrics;
3. the three learning families at overview level;
4. generalisation and the train/validation/test boundary;
5. logistic regression from score to probability;
6. likelihood, log-loss, gradient descent, coefficient interpretation, regularisation, calibration, and threshold policy;
7. a reproducible notebook and a focused assignment.

The other methods are assigned to Weeks 6–12 in `next_weeks_plan.md` rather than being repeated in Week 5.

## Structural and visual checks

- 96 slides, including section dividers, teaching examples, code, assessment, and close.
- 16:9 layout.
- 40 native PowerPoint table slides (42 native tables in total, including the PCA-versus-K-means comparison).
- 7 native quantitative chart slides, including the PCA explained-variance chart and the later logistic-regression evaluation charts. The cover is now a professional finance photograph rather than a chart.
- supplied course figures, sourced internet PCA and finance visuals, a black-box/white-box fraud visual, two finance reinforcement-learning loop visuals, the focused bias–variance curve, and rendered equation figures.
- Every slide was rendered to PNG and reviewed through a full montage plus individual checks of the redesigned cover, opening sequence, PCA distinction and mathematics, K-means iteration, RL visuals, workflow, underfitting/overfitting, bias–variance, sigmoid, odds, likelihood, gradient, Elastic Net, worked loss, notebook, and close slides.
- The presentation package validator reported no integrity findings.
- The layout validator reported no geometry findings or warnings.
- No empty image placeholders remain in the rebuilt export.

## Editability note

All explanatory text, code, tables, and charts are native PowerPoint objects. The equations are high-resolution image objects so that PowerPoint and GitHub do not reinterpret broken delimiters or unsupported macros. The authoritative equation source is the accompanying `mathematics.md` file. This makes formula corrections reproducible without editing a damaged presentation package.

## Content cautions

- The credit sample is synthetic and course-sized. It illustrates workflow and should not be treated as a lending model.
- The supplied and internet-sourced figures are credited in speaker notes and `attributions.md`. The full uploaded bias–variance cheat sheet is intentionally not included.
- The illustrative threshold and validation charts are teaching examples. The notebook computes the corresponding quantities from the sample.
- A good validation metric does not establish causality, fairness, profitability, or deployment readiness.
- The slide deck contains completed worked checks; only the final weekly assignment is unsolved by design.
