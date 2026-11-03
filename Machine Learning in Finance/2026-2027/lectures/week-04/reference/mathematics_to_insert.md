# Week 4 mathematics reference

The formulas below use editable Unicode and plain text. They do not use `\\left`, `\\right`, `\\operatorname`, or unsupported Markdown macros.

## Formula locations in the 90-slide deck

| Slide | Concept | Formula |
|---:|---|---|
| 20 | Utilization | `utilizationᵢ = BILL_AMT1ᵢ / LIMIT_BALᵢ`, when `LIMIT_BALᵢ ≠ 0` |
| 23 | Payment capacity | `payment_to_billᵢ = total_paid_6mᵢ / total_bill_6mᵢ`, when `total_bill_6mᵢ ≠ 0` |
| 29 | Change | `Δxₜ = xₜ − xₜ₋₁` |
| 31 | Log transformation | `log_limitᵢ = ln(1 + LIMIT_BALᵢ)` |
| 32 | Signed log | `signed_log(x) = sign(x) × ln(1 + |x|)` |
| 33 | Standardisation | `zᵢ = (xᵢ − μ_train) / σ_train` |
| 34 | Binning and ranks | `bin(x) = j` when `bⱼ ≤ x < bⱼ₊₁` |
| 36 | Lag | `lag₁(xₜ) = xₜ₋₁` |
| 37 | Rolling mean | `rolling_meanₖ(xₜ) = (1/k) × Σⱼ₌₀ᵏ⁻¹ xₜ₋ⱼ` |
| 41 | Recency | `months_since_eventₜ = t − last_event_time` |
| 42 | As-of join | `same entity + event_time ≤ prediction_time` |
| 45 | Interaction | `interaction(x₁, x₂) = x₁ × x₂` |
| 48 | Quadratic term | `x² = x × x` |
| 49 | Binning | `bin(x) = j` when `bⱼ ≤ x < bⱼ₊₁` |
| 51 | Weight of Evidence | `WOEⱼ = ln((non-default share in bin j) / (default share in bin j))` |
| 60 | Elastic Net | `minimize  −ℓ(β₀, β) + λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²]` |
| 66 | Population Stability Index | `PSI = Σⱼ (monitoringⱼ − referenceⱼ) × ln(monitoringⱼ / referenceⱼ)` |
| 83 | Gini impurity | `G(t) = 1 − Σₖ (pₖ|t)²` |
| 85 | Information Value | `IV = Σⱼ (% non-defaultsⱼ − % defaultsⱼ) × WOEⱼ` |
| 86 | Model Gini | `Gini = 2 × AUC − 1` |

## Important distinctions

- **Gini impurity** is a decision-tree split criterion. It measures how mixed the classes are inside one node.
- **Model Gini** is a discrimination measure derived from the model AUC: `2 × AUC − 1`.
- **Information Value** is a target-driven, binned, univariate separation measure. It is not incremental model performance and it does not prove causality.
- **WOE and IV are target-driven transformations.** Fit bins, WOE values, smoothing, and IV calculations inside the training sample or training fold.
- **Decision-tree binning proposes cut points.** The analyst and risk-governance process review, merge, constrain, and approve the final bins using sample size, monotonicity, stability, missingness, and operational meaning.

