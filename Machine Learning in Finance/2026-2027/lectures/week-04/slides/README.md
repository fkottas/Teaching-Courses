# Week 4 presentation

Download the single current deck:

[Lecture 04 — Feature Engineering for Financial Data](Lecture_04_Feature_Engineering_for_Financial_Data_2026-2027.pptx)

The deck is an editable PowerPoint file. Text, tables, charts, code examples, and speaker notes are native PowerPoint content rather than slide screenshots. The presentation contains 90 slides and is organised as:

- why feature engineering is a financial-information problem;
- observation units, targets, cutoffs, and feature contracts;
- ratios, payment capacity, counts, indicators, transformations, and scaling;
- lags, changes, rolling summaries, recency, and point-in-time joins;
- interactions and nonlinear representations;
- data-driven events versus target-driven events;
- filter, wrapper, embedded, and stability-based feature selection;
- distribution, relationship, and operational feature stability, including the UCI lookback limitation and monthly monitoring plots from an open LendingClub extract;
- monthly fixed-bin distributions for revolving utilisation, monthly categorical shares for grade, and a target default-rate time series with the resolved-loan denominator;
- a worked PSI calculation with bin-level contributions and a clear distinction between variable PSI and delayed target PSI;
- scorecard binning, decision-tree cut points, an official scikit-learn tree-structure figure, WOE, Information Value, Information Coefficient, and the distinct meanings of Gini;
- worked cases using the real UCI credit-default data;
- leakage-safe validation, selection, stability, and documentation;
- the Week 4 assignment and the final model-readiness gate.

## External figure credits

- Decision-tree anatomy: scikit-learn documentation, [Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure).
- Binning, WOE, and IV illustration: MathWorks, [Binning Explorer case study](https://www.mathworks.com/help/risk/binning-explorer-case-study.html).
- Filter statistics: scikit-learn, [F-test versus mutual information](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html).
- Wrapper selection: scikit-learn, [Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html).
- Correlated-feature importance: scikit-learn, [Permutation importance with multicollinear features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html).
- Lasso model selection: scikit-learn, [Lasso model selection](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html).
- Target-driven event context: Board of Governors of the Federal Reserve System, [Delinquency Rate on Credit Card Loans, All Commercial Banks](https://fred.stlouisfed.org/series/DRCCLACBS), retrieved through FRED.

The figures are embedded as image assets in the deck for visual explanation. The surrounding mathematics, tables, plots, and code remain editable native PowerPoint content. The external figures are used only where they clarify an algorithmic or mathematical idea; the course’s financial plots remain native charts from the documented teaching data.

## Quality and editability note

The deck was rebuilt after a full rendered-slide assessment. The selection sequence is now a decision route rather than a list: admissible candidates, filters, redundancy, wrappers, embedded regularisation, and stability. The event section separates `Xₜ` information available at the prediction point from `Yₜ₊₁` labels and later target monitoring. The PSI example exposes every intermediate term and uses separate treatments for explanatory-variable distributions and delayed binary-target monitoring. The tree section includes a numerical split comparison, a native Gini curve, per-bin WOE direction, and per-bin IV contributions.

The presentation uses the unambiguous identity `log1p(xᵢ) = ln(1 + xᵢ)` and explicitly rejects the incorrect expression `log(xᵢ) = xᵢ + 1`. Text, formulas, tables, code, and course-generated charts are native PowerPoint content; external figures are embedded only as credited explanatory visuals.

See the [full visual and teaching redesign assessment](../reference/quality_assessment_redesign.md) and the [editable mathematics reference](../reference/mathematics_to_insert.md).

