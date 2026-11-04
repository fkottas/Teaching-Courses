# Week 4 mathematics reference

This is the mathematics reference for the single canonical 90-slide deck. The equations below use Unicode symbols and plain text so they remain readable in GitHub, PowerPoint, and Colab without special rendering commands.

## Formula map

| Slide | Concept | Formula or rule |
|---:|---|---|
| 8 | Prediction point | A feature at time t may use only events with event_time ≤ t. |
| 12 | Data-driven event | Eₜ(X) = 𝟙{g(Xₜ, Xₜ₋₁, …) crosses a stated threshold}. |
| 13 | Target-driven event | BRₘ = Bₘ / Nₘ; ΔBRₘ = BRₘ − BRₘ₋₁. |
| 18 | Utilization | utilizationᵢ = BILL_AMT1ᵢ / LIMIT_BALᵢ, when LIMIT_BALᵢ ≠ 0. |
| 20 | Payment capacity | payment_to_billᵢ = total_paid_6mᵢ / total_bill_6mᵢ, when total_bill_6mᵢ ≠ 0. |
| 21 | Frequency and severity | overdue_count₆ₘ = Σₘ₌₁⁶ 𝟙(PAYₘ > 0); max_delay₆ₘ = max(PAY₁, …, PAY₆). |
| 23 | Change | Δxₜ = xₜ − xₜ₋₁. |
| 25 | Lag | lag₁(xₜ) = xₜ₋₁. |
| 26 | Rolling mean | rolling_meanₖ(xₜ) = (1/k) × Σⱼ₌₀ᵏ⁻¹ xₜ₋ⱼ. |
| 27 | Rolling volatility | sₖ(xₜ) = √[(1/(k−1)) × Σⱼ₌₀ᵏ⁻¹ (xₜ₋ⱼ − x̄ₜ,ₖ)²]. |
| 28 | As-of join | Same entity and event_time ≤ prediction_time; choose the latest qualifying event. |
| 29 | Log transformation | log1p(xᵢ) = ln(1 + xᵢ), with xᵢ > −1 for a real-valued natural logarithm. |
| 30 | Signed log | signed_log(x) = sign(x) × ln(1 + |x|). |
| 31 | Standardisation | zᵢ = (xᵢ − μ_train) / σ_train. |
| 35 | Interaction | stress_flagᵢ = high_utilizationᵢ × recent_overdueᵢ. |
| 37 | Quadratic term | x² = x × x. |
| 38 | Binning | bin(x) = j when bⱼ ≤ x < bⱼ₊₁. |
| 42 | Selection objective | S⋆ = arg max over S ⊆ {1, …, p} of CVScore(model(X_S), y). |
| 44 | F-test screen | Fⱼ = MS_between,j / MS_within,j. |
| 45 | Mutual information | MI(X;Y) = ΣₓΣᵧ p(x,y) ln[p(x,y) / (p(x)p(y))]. |
| 46 | Pearson association | r(X,Y) = cov(X,Y) / (σX σY). |
| 47 | Correlation matrix | rₐᵦ = Σᵢ(aᵢ−ā)(bᵢ−b̄) / √[Σᵢ(aᵢ−ā)² Σᵢ(bᵢ−b̄)²]. |
| 48 | Permutation importance | PIⱼ = M_base − M_perm(j). |
| 49 | RFE search | S⋆ = arg maxₖ CVScore(Sₖ), where Sₖ is the retained subset at step k. |
| 50 | RFECV decision | k⋆ = arg maxₖ average_fold_score(k). |
| 51 | Lasso | β̂ = arg min over β { −ℓ(β₀, β) + λΣⱼ|βⱼ| }. |
| 52 | Elastic Net | (β̂₀, β̂) = arg min over (β₀, β) { −ℓ(β₀, β) + λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²] }. |
| 53 | Elastic Net penalty | P(β) = λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²]. |
| 54 | Tree-based selection | Choose feature-threshold pair θ that minimises weighted child impurity. |
| 55 | Stability selection | πⱼ = (1/B)Σᵦ₌₁ᴮ 𝟙(j ∈ Sᵦ). |
| 56 | Leakage-safe route | Fit preprocessing, selection, and model on the training fold; apply the frozen route to validation data. |
| 57 | Cross-validation score | CVScore = (1/Kf)Σᵣ₌₁ᴷᶠ Scoreᵣ. |
| 63 | Numeric distribution | pⱼ,ₘ = count(bin j in month m) / count(non-missing X in month m). |
| 64 | Categorical distribution | pₖ,ₘ = count(category k in month m) / count(non-missing category in month m). |
| 65 | Target rate | BRₘ = Bₘ / Nₘ; SE(BRₘ) ≈ √[BRₘ(1−BRₘ) / Nₘ]. |
| 66 | Target-driven jump | ΔBRₘ = BRₘ − BRₘ₋₁; Relative change = ΔBRₘ / BRₘ₋₁. |
| 67 | PSI | PSIⱼ = (qⱼ − pⱼ) × ln(qⱼ / pⱼ); PSI = Σⱼ PSIⱼ. |
| 69 | PSI code | For a binary target, compare [1−r_reference, r_reference] with [1−r_monitor, r_monitor] after labels mature. |
| 76 | Tree split | G_split = (nL / nt)G(L) + (nR / nt)G(R); choose θ⋆ = arg minθ G_split(θ). |
| 77 | Gini impurity | pₖ|t = (1/nt)Σᵢ∈t 𝟙(yᵢ = k); G(t) = 1 − Σₖ(pₖ|t)². |
| 78 | Worked tree split | ΔG = G(parent) − G_split; candidate B has 0.48 − 0.16 = 0.32. |
| 79 | WOE | GoodShareⱼ = Goodⱼ / Good_total; BadShareⱼ = Badⱼ / Bad_total; WOEⱼ = ln(GoodShareⱼ / BadShareⱼ). |
| 81 | Information Value | IV = Σⱼ (GoodShareⱼ − BadShareⱼ) × WOEⱼ. |
| 82 | Model Gini and IC | Gini_model = 2 × AUC − 1; ICₜ = corr(rank(signalₜ), rank(returnₜ₊₁)). |

## Feature-selection symbol glossary

The feature-selection slides use the same symbols repeatedly. Read this table before reading the equations; no symbol is intended to be a placeholder without a definition.

| Symbol | Meaning | Concrete reading in the credit example |
|---|---|---|
| `j` | Feature index | `j = 3` means the third candidate column. |
| `p` | Number of candidate features | If the table has 20 admissible columns, `p = 20`. |
| `Xⱼ` | Column j of the design matrix | The utilisation column can be one `Xⱼ`. |
| `X_S` | Design matrix restricted to subset S | If `S = {utilisation, overdue_count}`, `X_S` has those two columns. |
| `y` | Observed target label | `y = 1` for the defined default event and `y = 0` otherwise. |
| `S` | Candidate set of retained columns | A possible model input list, not the final answer. |
| `S⋆` | Selected subset after the stated rule | The subset chosen by validated performance plus governance constraints. |
| `CVScore` | Cross-validated score for a candidate subset | Mean ROC-AUC across the stated folds. |
| `Fⱼ` | Univariate F-test score for feature j | Between-group variation divided by within-group variation. |
| `MS_between,j` | Between-target-group mean square for feature j | How far the good and bad group means are separated. |
| `MS_within,j` | Within-group mean square for feature j | Residual variation inside the good and bad groups. |
| `p(x,y)` | Joint probability in mutual information | Share of rows in one X category and one Y category. |
| `p(x)`, `p(y)` | Marginal probabilities | Row and column shares obtained from the joint table. |
| `ln` | Natural logarithm | `ln(0.40 / 0.25)` is the log contribution in the worked cell. |
| `r(X,Y)` | Pearson correlation | Linear association between one feature and the target. |
| `cov(X,Y)` | Covariance | Average product of deviations from the two means. |
| `σX`, `σY` | Standard deviations | The scale terms that standardise covariance in `r`. |
| `M_base` | Validation metric before shuffling | Example: AUC = 0.74 with all columns unchanged. |
| `M_perm,j` | Same metric after shuffling column j | Example: AUC = 0.70 after shuffling utilisation. |
| `PIⱼ` | Permutation importance for feature j | `0.74 − 0.70 = 0.04` in that worked example. |
| `k` | Number of retained features | `k = 8` means the candidate subset contains eight columns. |
| `Sₖ` | Subset containing k retained features | The subset evaluated at a particular RFE step. |
| `Kf` | Number of cross-validation folds | `Kf = 5` for five stratified folds. |
| `r` | Fold index | `r = 1, …, Kf`; it is not Pearson correlation here. |
| `Scoreᵣ,ₖ` | Score on fold r with k retained features | ROC-AUC for that fold and subset size. |
| `β₀` | Model intercept | Baseline log-odds before adding feature contributions. |
| `βⱼ` | Coefficient for feature j | The fitted contribution of column j on the model scale. |
| `β` | Vector of all feature coefficients | `β = (β₁, …, βₚ)`. |
| `ℓ(β₀,β)` | Log-likelihood | Fit term for the observed labels; larger is better before penalisation. |
| `λ` | Total regularisation strength | Larger λ puts more weight on the penalty. |
| `α` | L1 share in Elastic Net | `α = 1` is Lasso; `α = 0` is Ridge. |
| `‖β‖₁` | L1 norm, `Σⱼ|βⱼ|` | Sum of coefficient magnitudes; it can produce exact zeros. |
| `‖β‖₂²` | Squared L2 norm, `Σⱼβⱼ²` | Sum of squared coefficients; it shrinks large values smoothly. |
| `θ = (j,t)` | Candidate tree split | Feature j and threshold t, such as `utilisation ≤ 0.80`. |
| `G_split(θ)` | Weighted child impurity for split θ | The class mixing after the candidate split. |
| `πⱼ` | Selection frequency for feature j | Selected in 42 of 50 resamples gives `πⱼ = 0.84`. |
| `B` | Number of resamples | `B = 50` in the illustrative stability plot. |
| `b` | Resample index | `b = 1, …, B`. |
| `S_b` | Selected subset in resample b | The feature list chosen from one bootstrap or subsample. |
| `𝟙(·)` | Indicator function | Equals 1 when the condition is true and 0 otherwise. |

### Three equations read from left to right

1. **Wrapper search:** `S⋆ = arg max over S CVScore(model(X_S), y)` means “try an admissible subset S, validate the resulting model, and keep the subset with the largest valid score.”
2. **Permutation importance:** `PIⱼ = M_base − M_perm,j` means “measure how much the validation metric falls when only feature j is made uninformative by shuffling.”
3. **Stability frequency:** `πⱼ = (1/B)Σᵦ 𝟙(j ∈ S_b)` means “count how often feature j is selected and divide by the number of resamples.”

The equations are written as plain Unicode text rather than fragile LaTeX commands. The reference avoids unsupported delimiter commands, custom macros, and unclosed formula pairs.

## Interpretation rules

1. A ratio is undefined when its denominator is zero. The code must record the policy: missing value, separate indicator, or an approved fallback.
2. A lag and a rolling statistic must be constructed after sorting by entity and time. The window must not reach into the future.
3. Scaling parameters, imputation values, cut points, target encodings, WOE, and IV are fitted on training data or inside a training fold.
4. F-test, Pearson correlation, mutual information, WOE, and IV are association or screening tools. None establishes causality.
5. Tree Gini impurity measures class mixing inside a node. Model Gini is derived from AUC. They are not interchangeable.
6. PSI is a distribution-drift statistic. For an explanatory variable, use fixed value bins or fixed categories. For a target, wait for mature labels and show the target-rate time series with denominators.

## Worked mathematics

### Mutual information

The displayed table has joint probabilities 0.40, 0.10, 0.10, and 0.40. Each marginal is 0.50. Therefore:

MI = 2 × 0.40 × ln(0.40 / 0.25) + 2 × 0.10 × ln(0.10 / 0.25)

MI ≈ 0.193 nats.

The value is zero when the joint distribution equals the product of the marginals. Mutual information measures dependence, not causality.

### Elastic Net calculation

For β = (0.8, 0.7), λ = 0.1, and α = 0.5:

‖β‖₁ = |0.8| + |0.7| = 1.50

‖β‖₂² = 0.8² + 0.7² = 1.13

P(β) = 0.1[0.5(1.50) + 0.5(0.5)(1.13)] = 0.10325.

The L1 part encourages sparsity. The L2 part stabilises coefficients when predictors are correlated. The statement C = 1 / λ is the inverse-strength convention used in the teaching deck; the exact numerical mapping depends on the estimator’s loss scaling.

### Target-driven jump

For the resolved-loan teaching extract:

BR₍₂₀₁₁₋₁₁₎ = 335 / 2,062 = 16.2%

BR₍₂₀₁₁₋₁₂₎ = 423 / 2,042 = 20.7%

ΔBR = 20.7% − 16.2% = 4.5 percentage points

Relative change = 4.5% / 16.2% = 27.5%.

This is a target-driven monitoring event because the eventual outcome is observed after the outcome window. A crisis, pandemic, war, energy shock, policy change, or reporting change can define a hypothesis window; a coincident jump is not proof of a causal effect.

### PSI numerical example

For a reference share pⱼ = 0.40 and monitoring share qⱼ = 0.32:

PSIⱼ = (0.32 − 0.40) × ln(0.32 / 0.40) ≈ 0.0178.

The four-bin example on Slide 68 is:

| Bin | pⱼ | qⱼ | qⱼ − pⱼ | ln(qⱼ / pⱼ) | PSIⱼ |
|---|---:|---:|---:|---:|---:|
| 0–25% | 0.40 | 0.32 | −0.08 | −0.2231 | 0.0178 |
| 25–50% | 0.30 | 0.34 | +0.04 | +0.1252 | 0.0050 |
| 50–75% | 0.20 | 0.22 | +0.02 | +0.0953 | 0.0019 |
| ≥75% | 0.10 | 0.12 | +0.02 | +0.1823 | 0.0036 |
| Total | 1.00 | 1.00 |  |  | 0.0283 |

Both factors in the first contribution are negative, so the contribution is positive. Use unrounded logarithms in code and state the reference period, monitoring period, fixed bins, and sample sizes.

### Gini impurity and tree split

For a node containing 60% good and 40% bad:

G(parent) = 1 − (0.60² + 0.40²) = 0.48.

Candidate A has child impurities 0.32 and 0.48, so:

G_split(A) = 0.5 × 0.32 + 0.5 × 0.48 = 0.40

ΔG(A) = 0.48 − 0.40 = 0.08.

Candidate B has child impurities 0.00 and 0.32, so:

G_split(B) = 0.5 × 0.00 + 0.5 × 0.32 = 0.16

ΔG(B) = 0.48 − 0.16 = 0.32.

Candidate B gives the larger training-sample reduction. It still requires minimum-size, missing-value, monotonicity, stability, leakage, and governance checks.

### WOE and Information Value

Under the course convention Good = non-default and Bad = default, the illustrative bin A has:

GoodShare_A = 8,000 / 23,364 = 0.3424

BadShare_A = 500 / 6,636 = 0.0753

WOE_A = ln(0.3424 / 0.0753) = +1.5139

IV_A = (0.3424 − 0.0753) × 1.5139 = 0.4043.

The second bin contributes 0.0910, so the illustrative total IV is 0.4953. Positive WOE means that the bin contains a larger share of all goods than of all bads under this convention. If a bin has zero good or bad share, WOE is undefined; merge bins or apply a documented smoothing policy.

### Information Coefficient

For asset i at date t, let signalᵢ,ₜ be the forecast and returnᵢ,ₜ₊₁ the next-period return:

ICₜ = corr(rank(signalᵢ,ₜ), rank(returnᵢ,ₜ₊₁)).

Calculate it by date, then summarise across dates. Information Coefficient is not Information Value, and neither is tree Gini impurity.
