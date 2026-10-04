# Machine Learning in Finance: complete 13-week material map

This map follows the syllabus supplied for the 2026–2027 academic year. The course uses supervised learning throughout. The optional Isolation Forest item in the syllabus is omitted from the core route so the course remains focused on supervised prediction.

## Assessment

| Component | Weight |
|---|---:|
| Weekly exercises, including DataCamp practice and Colab notebooks | 20% |
| Capstone project | 40% |
| Final examination | 40% |
| Bonus exercise | up to +10% |

The regular assessment totals 100%. The bonus can raise the maximum course total to 110%.

## Week 1 — Python Foundations I

**Theory:** Google Colab and Jupyter notebooks, variables, data types, operators, conditions, loops, functions, file handling, package use, descriptive statistics, and introductory visualisation.

**Financial application:** Load a public financial dataset, define the observation unit, calculate descriptive statistics, calculate returns, and produce labelled charts.

**Colab examples:** arithmetic and percentage conventions, lists/tuples/dictionaries/sets, indexing and slicing, `if/elif/else`, `for`, `range`, `enumerate`, `zip`, `while`, functions with docstrings, CSV loading, grouping, correlations, and visualisation.

**Weekly exercise:** A reproducible notebook with basic programming tasks, grouped descriptive statistics, two visualisations, and interpretation.

## Week 2 — Python Foundations II: NumPy and Pandas

**Theory:** NumPy arrays, Pandas DataFrames, indexing, filtering, joins, grouping, transformations, missing values, correlations, and exploratory data analysis.

**Financial application:** Explore a real credit-risk table and document distributions, data types, missingness, class balance, and relationships.

**Colab examples:** vectorised operations, boolean masks, `loc` and `iloc`, `merge`, `groupby`, `pivot_table`, `assign`, `value_counts`, missingness tables, correlation matrices, and EDA charts.

**Weekly exercise:** Complete EDA and identify material data-quality issues.

## Week 3 — Data Cleaning and Preprocessing

**Theory:** Missing values, duplicates, outliers, scaling, categorical encoding, preprocessing pipelines, and `ColumnTransformer`.

**Financial application:** Prepare a credit-risk modelling table without leaking information from the validation or test sample.

**Colab examples:** train/test split, numeric and categorical column lists, `SimpleImputer`, `StandardScaler`, `OneHotEncoder`, `Pipeline`, `ColumnTransformer`, and transformed feature names.

**Weekly exercise:** Build a complete preprocessing pipeline and document the data-quality changes.

## Week 4 — Feature Engineering for Financial Data

**Theory:** Feature construction, financial ratios, interaction terms, nonlinear transformations, feature selection, domain knowledge, and leakage prevention.

**Financial application:** Create features for credit-risk and fraud-risk prediction with an explicit time definition.

**Colab examples:** utilisation ratios, log transformations, rolling variables, lagged values, interactions, date features, target timing, and leakage checks. Binning may be discussed conceptually, while WOE/IV scorecard construction remains outside the core course.

**Weekly exercise:** Design and evaluate six to ten predictive variables.

## Week 5 — Logistic Regression for Credit Risk

**Theory:** Binary classification, odds, log-odds, logistic function, likelihood, maximum likelihood estimation, gradient optimisation, class imbalance, class weighting, L1/L2/Elastic-Net regularisation, coefficient interpretation, calibration, and diagnostics.

**Mathematics:**

$$
p_i=P(Y_i=1\mid\mathbf{x}_i)=\sigma(\eta_i)=\frac{1}{1+e^{-\eta_i}},\qquad \eta_i=\beta_0+\mathbf{x}_i^{\top}\boldsymbol{\beta}.
$$

$$
\ell(\boldsymbol{\beta})=\sum_{i=1}^{n}\left[y_i\log(p_i)+(1-y_i)\log(1-p_i)\right].
$$

**Financial application:** Probability of Default modelling.

**Weekly exercise:** Compare regularised logistic models using cross-validation.

## Week 6 — Model Evaluation and Performance Metrics

**Theory:** Confusion matrix, precision, recall, F1, ROC-AUC, PR-AUC, KS, Gini, log-loss, Brier score, lift, gains, and calibration.

**Mathematics:**

$$
\mathrm{LogLoss}=-\frac{1}{n}\sum_{i=1}^{n}\left[y_i\log(p_i)+(1-y_i)\log(1-p_i)\right].
$$

$$
\mathrm{Brier}=\frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)^2,\qquad \mathrm{Gini}=2\,\mathrm{AUC}-1.
$$

**Financial application:** Compare models under different decision thresholds and assess whether predicted probabilities are usable.

**Weekly exercise:** Build a reusable evaluation toolkit.

## Week 7 — Decision Trees and Random Forests

**Theory:** CART, recursive partitioning, Gini impurity, entropy, pruning, bootstrap aggregation, random feature selection, feature importance, partial dependence, and tuning.

**Mathematics:**

$$
G(t)=1-\sum_{k=1}^{K}p_{k\mid t}^{2},\qquad H(t)=-\sum_{k=1}^{K}p_{k\mid t}\log(p_{k\mid t}).
$$

**Financial application:** Credit-risk prediction using nonlinear interactions.

**Weekly exercise:** Optimise a Random Forest and compare it with logistic regression.

## Week 8 — Model Validation and Generalisation

**Theory:** Overfitting, underfitting, training/validation/test methodology, stratified K-fold cross-validation, nested cross-validation, learning curves, validation curves, and early stopping.

**Financial application:** Design a validation scheme that respects the time structure and avoids leakage.

**Colab examples:** `StratifiedKFold`, `cross_validate`, `GridSearchCV`, learning curves, validation curves, threshold selection, and time-aware holdout discussion.

**Weekly exercise:** Diagnose learning behaviour and generalisation.

## Week 9 — Gradient Boosting Methods

**Theory:** Gradient Boosting, XGBoost, LightGBM, CatBoost, additive modelling, regularisation, hyperparameter optimisation, early stopping, feature importance, and comparison.

**Mathematics:**

$$
F_m(\mathbf{x})=F_{m-1}(\mathbf{x})+\nu h_m(\mathbf{x}),\qquad 0<\nu\le1.
$$

where the new learner \(h_m\) approximates the negative gradient of the loss with respect to the current model predictions.

**Financial application:** Advanced credit scoring and fraud-risk classification.

**Weekly exercise:** Optimise a boosting model using a controlled search.

## Week 10 — Alternative Machine-Learning Algorithms

**Theory:** Support Vector Machines, k-nearest neighbours, kernel methods, distance metrics, Naive Bayes, probabilistic classifiers, and stacking.

**Mathematics:**

$$
\min_{\mathbf{w},b,\boldsymbol{\xi}}\frac{1}{2}\lVert\mathbf{w}\rVert_2^2+C\sum_{i=1}^{n}\xi_i\quad\text{subject to}\quad y_i(\mathbf{w}^{\top}\mathbf{x}_i+b)\ge1-\xi_i,\quad \xi_i\ge0.
$$

**Financial application:** Benchmark complementary classifiers and justify their suitability.

**Weekly exercise:** Evaluate one alternative classifier against the established baseline.

## Week 11 — Model Calibration and Explainable AI

**Theory:** Calibration, Platt scaling, isotonic regression, reliability diagrams, SHAP values, global explanations, local explanations, and model documentation.

**Mathematics:**

$$
\mathrm{ECE}=\sum_{m=1}^{M}\frac{|B_m|}{n}\left|\mathrm{acc}(B_m)-\mathrm{conf}(B_m)\right|.
$$

**Financial application:** Explain and calibrate a Probability of Default model.

**Weekly exercise:** Produce a calibrated model, SHAP analysis, and concise model card.

## Week 12 — Introduction to Neural Networks

**Theory:** Artificial neural networks, multilayer perceptrons, activation functions, backpropagation, dropout, regularisation, early stopping, and calibration.

**Mathematics:**

$$
\mathbf{h}^{(1)}=\phi\left(W^{(1)}\mathbf{x}+\mathbf{b}^{(1)}\right),\qquad \widehat{y}=\sigma\left(W^{(2)}\mathbf{h}^{(1)}+b^{(2)}\right).
$$

**Financial application:** Credit-risk or fraud-risk prediction using an MLP, compared with the best traditional model.

**Exercise:** Optional comparison of the neural network with the strongest traditional model.

## Week 13 — Capstone Project

The final week completes material that could not be finished earlier and hosts project presentations. The project integrates data acquisition, preprocessing, EDA, feature engineering, baseline and advanced supervised models, validation, hyperparameter optimisation, calibration, performance metrics, SHAP explanations, limitations, and practical implications.

**Deliverables:** Complete Python notebook, technical report, supporting code and documentation, and a 10-minute presentation.

**Project routes:** Credit-risk prediction, fraud-risk prediction, stock prediction, or portfolio management supported by supervised forecasts. The project may be individual or completed by a team of two.
