# Week 4 presentation — high-quality rebuild assessment

## Scope

This assessment covers the complete 90-slide Week 4 deck after a rendered-slide review. The review focused on visual hierarchy, mathematical readability, editable PowerPoint structure, data provenance, and the teaching sequences that had generated repeated correction requests: feature selection, data-driven versus target-driven events, PSI, decision-tree binning, Gini impurity, WOE, Information Value, and Information Coefficient.

## Findings from the previous version

1. The deck was structurally editable, but the repeated rounded pastel cards made the presentation feel like a worksheet rather than a professional lecture.
2. Several difficult concepts were compressed into small side panels. Students who study from the slides at home needed the question, formula, numerical substitution, interpretation, and limitation in a clearer order.
3. Feature selection was introduced as a four-item list without enough distinction between the question answered by a filter, wrapper, embedded, or stability method.
4. Data-driven events and target-driven events were described, but their different clocks and their relation to the prediction point were not visually explicit enough.
5. PSI had a formula and a short table, but not every numerical term was visible. The redesigned worked example now shows pⱼ, qⱼ, qⱼ − pⱼ, ln(qⱼ / pⱼ), PSIⱼ, and the contribution plot.
6. The scorecard section needed to show who proposes bins, who approves them, and how a candidate split is evaluated numerically. The redesigned tree example compares two candidate cuts using the parent Gini, weighted child Gini, and impurity reduction.
7. WOE and IV needed per-bin interpretation. The redesigned slides identify positive and negative WOE, show the GoodShare and BadShare values, calculate each IV contribution, and state the zero-count control.
8. The logarithm example needed unambiguous notation. The deck now uses `log1p(xᵢ) = ln(1 + xᵢ)` and explicitly rejects the false identity `log(xᵢ) = xᵢ + 1`.

## Redesign decisions

- The title slide is unchanged.
- The body deck now uses square editorial panels, a restrained navy/teal/gold/coral palette, stronger whitespace, and a consistent left-hand section marker.
- Native PowerPoint text, tables, charts, and code are used for the course’s own material. Difficult equations are high-resolution typeset visuals so that symbols render consistently; the same equations remain available as copyable Unicode notation in the mathematics reference.
- Official or primary-source figures are embedded only where they clarify an algorithm or mathematical idea: scikit-learn for feature-selection, permutation-importance, tree, Lasso, and Elastic Net coefficient-path examples; MathWorks for the WOE/IV illustration; FRED for credit-delinquency context.
- The financial charts generated for the course remain native charts. Source, denominator, and teaching limitation are recorded in the slide notes and the package README.

## Teaching sequences rebuilt

### Events and timing — Slides 11–15

The sequence now starts with two parallel clocks. `Xₜ` is available at the prediction point; `Yₜ₊₁` is observed only after the outcome window. A data-driven event is demonstrated as a current utilization threshold crossing. A target-driven event is demonstrated as a later bad-rate movement, with the denominator and event-window caveat shown next to the FRED figure.

### Feature selection — Slides 41–58

The sequence now follows a decision route:

1. define the admissible candidate set;
2. screen relationships with transparent filter statistics;
3. identify redundancy and interpret correlated groups;
4. compare subsets with wrapper methods;
5. select inside the fitted objective with Lasso or Elastic Net;
6. report persistence with resampling-based stability selection.

Each family has its own question, output, parameter choices, and limitation. Selection is explicitly kept inside the validation pipeline.

### Stability and PSI — Slides 59–72

The deck separates numeric-bin distributions, categorical shares, target-rate time series, relationship stability, and operational stability. The target slide uses a connected line with a labelled point for every month and keeps the denominator beside the jump. The PSI code shows both fixed-bin variable monitoring and delayed two-category target monitoring.

### Binning, Gini, WOE, and IV — Slides 73–83

The decision-tree section now includes:

- an official tree-anatomy figure;
- a parent with 6 good and 4 bad observations;
- candidate cut A with weighted Gini 0.40 and gain 0.08;
- candidate cut B with weighted Gini 0.16 and gain 0.32;
- the Gini curve, including the 50/50 maximum;
- per-bin WOE direction and zero-count handling;
- per-bin IV contributions and a contribution chart;
- a final distinction between Information Value, model Gini, tree Gini impurity, and Information Coefficient.

## Numerical checks used in the deck

- Target-rate jump: 16.2% → 20.7% = +4.5 percentage points and +27.5% relative change.
- PSI worked example: contributions 0.0178, 0.0050, 0.0019, and 0.0036; total approximately 0.0283 using unrounded logarithms.
- Tree split: parent Gini 0.48; candidate B weighted child Gini 0.16; gain 0.32.
- WOE: bin A `ln(0.3424 / 0.0753) = +1.5139`; bin B `ln(0.6576 / 0.9247) = −0.3408`.
- IV: contributions 0.4043 and 0.0910; illustrative total 0.4953.

## Quality gates

The final generated deck was checked as follows:

- 90 slides rendered and inspected as a full montage and as focused slides.
- `node --check` passed for the build source.
- PowerPoint package integrity: passed, 0 findings.
- Layout and heading/bullet geometry: passed, 0 findings and 0 warnings.
- Native charts: 13 charts validated; native quantitative-chart gate passed.
- Native tables: 39 tables present; arithmetic check passed for the worked IV table.
- First-party artifact-tool import: passed, 90 slides.
- Approved fonts: Arial and Courier New only.
- Mathematics-reference scan: clean; the GitHub reference uses readable Unicode/plain text and does not require unsupported LaTeX control sequences or environments. The deck’s equation images were rendered separately and visually inspected on the feature-selection, regularisation, PSI, Gini, WOE, and IV slides.

## Evidence and limitations

The UCI Default of Credit Card Clients file is used for feature-construction examples and does not provide a complete calendar-time production panel. The LendingClub extract is used for transparent monthly monitoring mechanics, not as a one-month-forward Probability of Default dataset. A target-rate movement around a crisis, pandemic, war, energy shock, or reporting change is an event window to investigate; it is not proof of a causal effect.

## Figure and method sources

- [scikit-learn feature selection guide](https://scikit-learn.org/stable/modules/feature_selection.html)
- [scikit-learn F-test versus mutual information](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html)
- [scikit-learn RFECV](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)
- [scikit-learn decision-tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure)
- [scikit-learn correlated-feature permutation importance](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
- [scikit-learn Lasso model selection](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)
- [scikit-learn Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
- [MathWorks Binning Explorer case study](https://www.mathworks.com/help/risk/binning-explorer-case-study.html)
- [FRED credit-card delinquency series](https://fred.stlouisfed.org/series/DRCCLACBS)
- [ECB PSI guidance](https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.supervisory_guidance_on_the_validation_of_aml_and_cft_risk_assessment_models.en.pdf)
