# Week 4 mathematics reference

The presentation uses editable native text for these equations. This reference uses Unicode/plain text deliberately so the equations remain readable in GitHub and PowerPoint.

## Formula locations in the 90-slide deck

| Slide | Concept | Formula |
|---:|---|---|
| 18 | Utilization | utilizationᵢ = BILL_AMT1ᵢ / LIMIT_BALᵢ, when LIMIT_BALᵢ ≠ 0 |
| 21 | Payment capacity | payment_to_billᵢ = total_paid_6mᵢ / total_bill_6mᵢ, when total_bill_6mᵢ ≠ 0 |
| 27 | Change | Δxₜ = xₜ − xₜ₋₁ |
| 29 | Log transformation | log1p(xᵢ) = ln(1 + xᵢ); `log_limitᵢ = log1p(LIMIT_BALᵢ)` |
| 30 | Signed log | signed_log(x) = sign(x) × ln(1 + |x|) |
| 31 | Standardisation | zᵢ = (xᵢ − μ_train) / σ_train |
| 33 | Lag | lag₁(xₜ) = xₜ₋₁ |
| 34 | Rolling mean | rolling_meanₖ(xₜ) = (1/k) × Σⱼ₌₀ᵏ⁻¹ xₜ₋ⱼ |
| 37 | Recency | months_since_eventₜ = t − last_event_time |
| 38 | As-of join | same entity and event_time ≤ prediction_time |
| 41 | Interaction | interaction(x₁, x₂) = x₁ × x₂ |
| 44 | Quadratic term | x² = x × x |
| 45 | Binning | bin(x) = j when bⱼ ≤ x < bⱼ₊₁ |
| 47 | Conceptual WOE | WOEⱼ = ln(good share in bin j / bad share in bin j) |
| 12 | Target-driven event | BRₜ = Bₜ / Nₜ; ΔBRₜ = BRₜ − BRₜ₋₁ |
| 50 | Selection objective | S* = argmax over S ⊆ {1, …, p} of CVScore(model(X_S), y) |
| 51 | Selection families | Filter asks whether Xⱼ relates to y alone; wrapper asks whether a subset improves a fitted model; embedded selects inside the fitted objective; stability records persistence under resampling. |
| 52 | F-test filter | Fⱼ = MS_between / MS_within; both quantities are calculated for Xⱼ after grouping observations by Y. |
| 53 | Pearson association | rⱼ = cov(Xⱼ, Y) / (σXⱼ σY) |
| 54 | Correlation matrix | rₐᵦ = Σᵢ(aᵢ − ā)(bᵢ − b̄) / √[Σᵢ(aᵢ − ā)² Σᵢ(bᵢ − b̄)²] |
| 55 | Permutation importance | PIⱼ = M_base − M_perm(j) |
| 56 | Mutual information worked example | MI(X;Y) = Σₓ,ᵧ p(x,y) ln[p(x,y) / (p(x)p(y))] = 0.193 nats for the displayed table |
| 57 | Recursive feature elimination | S* = argmaxₖ CVScore(Sₖ); Sₖ is the subset retained at step k; important parameters include cv, scoring, step, and minimum features |
| 58 | Lasso selection | β̂(λ) = argminβ { −ℓ(β) + λΣⱼ|βⱼ| }; C = 1/λ in scikit-learn |
| 59 | Elastic Net | minimize −ℓ(β₀, β) + λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²] |
| 60 | Regularisation strength in scikit-learn | C = 1 / λ |
| 61 | Leakage-safe selection pipeline | Fit preprocessing, selected columns, and model on the training fold; apply the frozen route to validation data |
| 62 | Stability selection | πⱼ = (1 / B) Σᵦ₌₁ᴮ 𝟙(j ∈ Sᵦ); SE(πⱼ) ≈ √[πⱼ(1−πⱼ)/B]; for [1,1,1,1,0], πⱼ = 4/5 = 0.80 |
| 64 | Monthly variable distribution | pⱼ,ₘ = count(bin j in month m) / count(non-missing variable in month m) |
| 65 | Monthly categorical distribution | pₖ,ₘ = count(category k in month m) / count(non-missing category in month m) |
| 66 | Monthly target rate and jump | BRₘ = Bₘ / Nₘ; ΔBRₘ = BRₘ − BRₘ₋₁; SE(BRₘ) ≈ √[BRₘ(1−BRₘ)/Nₘ] |
| 67 | PSI contribution | PSIⱼ = (qⱼ − pⱼ) × ln(qⱼ / pⱼ), and PSI = Σⱼ PSIⱼ |
| 68 | PSI code | The code implements the same bin-level sum with a small epsilon for zero shares |
| 83 | Decision-tree split | G_split(θ) = (n_L(θ) / n_t)G(Lθ) + (n_R(θ) / n_t)G(Rθ); θ* = argminθ G_split(θ) |
| 84 | Gini impurity | pₖ|t = (1 / nₜ) Σᵢ∈t 𝟙(yᵢ = k), and G(t) = 1 − Σₖ(pₖ|t)² |
| 85 | Worked WOE | GoodShareⱼ = Goodⱼ / Good_total; BadShareⱼ = Badⱼ / Bad_total; WOEⱼ = ln(GoodShareⱼ / BadShareⱼ) |
| 86 | Worked Information Value | IV = Σⱼ (GoodShareⱼ − BadShareⱼ) × WOEⱼ |
| 87 | Information Coefficient and model Gini | ICₜ = ρₛ(ŝᵢ,ₜ, rᵢ,ₜ₊₁) = corr(rank(ŝᵢ,ₜ), rank(rᵢ,ₜ₊₁)); Gini_model = 2 × AUC − 1 |

## Worked calculations

### Log transformation notation

The notation used in the code is:

log1p(xᵢ) = ln(1 + xᵢ)

It is not `log(xᵢ) = xᵢ + 1`. For a real-valued natural logarithm, xᵢ must be greater than −1. For a non-negative monetary amount, the condition is automatically satisfied. The worked values on Slide 29 are:

log1p(0) = ln(1) = 0

log1p(99) = ln(100) ≈ 4.605

In Python, use `np.log1p(x)`. The transformation compresses the right tail while preserving zero; it changes the scale and therefore the interpretation of a model coefficient.

### Target-driven event and bad-rate jump

Let Bₜ be the number of bad outcomes observed for period t and Nₜ be the eligible target population whose outcome window is mature. The observed bad rate is:

BRₜ = Bₜ / Nₜ

The period-to-period jump is:

ΔBRₜ = BRₜ − BRₜ₋₁

The relative change is:

Relative changeₜ = (BRₜ − BRₜ₋₁) / BRₜ₋₁

For a simple binomial teaching approximation, the standard error is:

SE(BRₜ) ≈ √[BRₜ(1−BRₜ) / Nₜ]

and an approximate 95% interval is BRₜ ± 1.96SE(BRₜ). This approximation is useful for intuition; clustered borrowers, overlapping outcome windows, censoring, and model monitoring policies may require a different uncertainty treatment.

In the LendingClub example on Slide 66, the labelled jump from 2011-11 to 2011-12 is:

BR₍₂₀₁₁₋₁₁₎ = 16.2%,   BR₍₂₀₁₁₋₁₂₎ = 20.7%

ΔBR = 20.7% − 16.2% = 4.5 percentage points

Relative change = 4.5% / 16.2% = 27.5%

The jump is target-driven because the eventual outcome is observed after the loan outcome window. A financial crisis, pandemic, war, energy shock, policy change, or reporting change can define a candidate event window for investigation. A coincident jump is evidence for a monitoring question, not proof of a causal effect.

### Feature selection objective

Let S be a candidate subset of the p available predictors. A useful teaching formulation is:

S* = argmax over S ⊆ {1, …, p} of E_CV[Score(model(X_S), y)]

The expectation is approximated by the average score across validation folds. The constraints still matter: the variables must be available at the prediction point, reproducible, interpretable, and stable enough for the intended use.

### Filter statistics

For an F-test screen, the statistic compares variation between target groups with variation within target groups:

Fⱼ = MS_between,ⱼ / MS_within,ⱼ

Mutual information compares the joint distribution with the product of its marginals:

MI(Xⱼ;Y) = Σₓ,ᵧ p(x,y) ln[p(x,y) / (p(x)p(y))]

For the binary table used on Slide 56, the joint probabilities are 0.40, 0.10, 0.10, and 0.40, while p(X = low) = p(X = high) = p(Y = 0) = p(Y = 1) = 0.50. Therefore:

MI = 2 × 0.40 × ln(0.40 / 0.25) + 2 × 0.10 × ln(0.10 / 0.25) = 0.193 nats

The value is zero when every joint probability equals p(x)p(y). Mutual information detects dependence, not causality.

### Correlation and permutation importance

Pearson correlation is:

rₐᵦ = Σᵢ(aᵢ − ā)(bᵢ − b̄) / √[Σᵢ(aᵢ − ā)² Σᵢ(bᵢ − b̄)²]

For a model-based permutation score, define:

PIⱼ = M_base − M_perm(j)

If the baseline AUC is 0.74 and the AUC after shuffling feature j is 0.70, then PIⱼ = 0.04. With correlated predictors, another feature can preserve the signal after the shuffle, so a small individual PIⱼ does not prove that the feature family is unimportant.

### Wrapper and embedded selection

Recursive feature elimination can be written as:

S* = argmaxₖ CVScore(RFEₖ(X), y)

The estimator is fitted repeatedly, the least important variables are removed, and the subset size is chosen by cross-validation. Lasso uses:

β̂(λ) = argminβ { −ℓ(β) + λΣⱼ|βⱼ| }

The L1 penalty can make some coefficients exactly zero. Elastic Net adds an L2 term:

minimize −ℓ(β₀, β) + λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²]

For β = (0.8, 0.7), λ = 0.1, and α = 0.5, ‖β‖₁ = 1.5 and ‖β‖₂² = 1.13. The penalty contribution is:

0.1[0.5(1.5) + 0.5(0.5)(1.13)] = 0.10325

In scikit-learn logistic regression, C = 1 / λ. Therefore a smaller C means stronger regularisation.

### Stability selection

If Sᵦ is the selected set in resample b, the empirical selection frequency is:

πⱼ = (1 / B) Σᵦ₌₁ᴮ 𝟙(j ∈ Sᵦ)

For B = 5 and selection indicators [1, 1, 1, 1, 0], πⱼ = 4/5 = 0.80. This is persistence under the stated resampling design. Correlated variables can exchange places, so group-level stability should also be reported.

### Gini impurity

For a node t, define the class share explicitly:

pₖ|t = (1 / nₜ) Σᵢ∈t 𝟙(yᵢ = k)

For two classes, the node impurity is:

G(t) = 1 − Σₖ₌₀¹(pₖ|t)² = 1 − [(p₀|t)² + (p₁|t)²]

For a node containing 80% non-defaults and 20% defaults:

G(t) = 1 − (0.80² + 0.20²) = 1 − (0.64 + 0.04) = 0.32

For a candidate split θ into left and right children:

G_split(θ) = (n_L(θ) / nₜ)G(Lθ) + (n_R(θ) / nₜ)G(Rθ)

The tree selects the candidate with the largest impurity reduction, equivalently:

θ* = argminθ G_split(θ)

ΔG(θ) = G(t) − G_split(θ)

This is a decision-tree split criterion. It is not the model Gini derived from AUC.

### WOE

Use Good = non-default and Bad = default. For the illustrative bin A in the deck:

GoodShare_A = 8,000 / 23,364 = 0.3424

BadShare_A = 500 / 6,636 = 0.0753

WOE_A = ln(0.3424 / 0.0753) = 1.5139

Positive WOE under this convention means that the bin contains a larger share of goods than bads.

### Information Value

The contribution from the same illustrative bin is:

IV_A = (0.3424 − 0.0753) × 1.5139 = 0.4043

The deck adds the contributions from all approved bins. The illustrative two-bin total is 0.4953.

### Information Coefficient

For a cross-sectional financial forecast, let ŝᵢ,ₜ be the signal for asset i at time t and rᵢ,ₜ₊₁ be its realised next-period return. A common information coefficient is Spearman rank correlation:

ICₜ = ρₛ(ŝᵢ,ₜ, rᵢ,ₜ₊₁)

ICₜ = corr(rank(ŝᵢ,ₜ), rank(rᵢ,ₜ₊₁))

The subscript t matters: IC is usually calculated separately for each date and then summarised across dates. Information Coefficient is not Information Value, and neither is the same as tree Gini impurity.

### PSI

For one utilization bin with reference share pⱼ = 0.40 and monitoring share qⱼ = 0.32:

PSIⱼ = (0.32 − 0.40) × ln(0.32 / 0.40) = 0.0179

The total PSI is the sum of the contributions for every fixed bin. Record the reference sample, monitoring window, bin edges, and sample sizes.

## Important distinctions

- Gini impurity measures class mixing inside one tree node.
- Model Gini is the discrimination summary Gini = 2 × AUC − 1.
- Information Value is target-driven, binned, and univariate. It is not incremental model performance and it does not prove causality.
- WOE and IV must be fitted inside the training sample or training fold, including any smoothing and bin merging.
- A decision tree proposes candidate cut points; the analyst and governance process review, merge, constrain, and approve the final bins.
- Variable PSI monitors input distributions and can be calculated before labels arrive. Target PSI monitors outcome prevalence and is available only after the target window closes.
- The UCI six-step plots are within-account lookback profiles. They show how encoded historical inputs change from t−5 to t; they are not evidence of calendar-period production drift.
- For a numeric input, monthly PSI compares fixed-bin shares. For a categorical input, compare category shares with a fixed category universe and an explicit missing/unseen policy.
- For a target, show the monthly default-rate time series DRₘ = Dₘ / Nₘ with event counts and the eligible denominator. Do not present a 0/1 target as a variable-distribution chart.
