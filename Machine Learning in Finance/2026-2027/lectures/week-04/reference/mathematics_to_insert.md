# Week 4 mathematics reference

The formulas below use editable Unicode and plain text. They do not use `\\left`, `\\right`, `\\operatorname`, or unsupported Markdown macros.

## Formula locations in the 90-slide deck

| Slide | Concept | Formula |
|---:|---|---|
| 18 | Ratio feature | `utilizationᵢ = BILL_AMT1ᵢ / LIMIT_BALᵢ`, when `LIMIT_BALᵢ ≠ 0` |
| 21 | Payment capacity | `payment_to_billᵢ = total_paid_6mᵢ / total_bill_6mᵢ`, when `total_bill_6mᵢ ≠ 0` |
| 27 | Change | `Δxₜ = xₜ − xₜ₋₁` |
| 29 | Log transformation | `log_limitᵢ = ln(1 + LIMIT_BALᵢ)` |
| 30 | Signed log | `signed_log(x) = sign(x) × ln(1 + |x|)` |
| 31 | Standardisation | `zᵢ = (xᵢ − μ_train) / σ_train` |
| 33 | Lag | `lag₁(xₜ) = xₜ₋₁` |
| 34 | Rolling mean | `rolling_meanₖ(xₜ) = (1/k) × Σⱼ₌₀ᵏ⁻¹ xₜ₋ⱼ` |
| 37 | Recency | `months_since_eventₜ = t − last_event_time` |
| 38 | As-of join | `same entity + event_time ≤ prediction_time` |
| 41 | Interaction | `interaction(x₁, x₂) = x₁ × x₂` |
| 44 | Quadratic term | `x² = x × x` |
| 45 | Binning | `bin(x) = j` when `bⱼ ≤ x < bⱼ₊₁` |
| 47 | Conceptual WOE | `WOEⱼ = ln((non-default share in bin j) / (default share in bin j))` |
| 59 | Elastic Net | `minimize  −ℓ(β₀, β) + λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²]` |
| 66 | Generic PSI | `PSI = Σⱼ (monitoringⱼ − referenceⱼ) × ln(monitoringⱼ / referenceⱼ)` |
| 67 | Variable PSI | `PSI_X = Σⱼ (pⱼ^monitor − pⱼ^reference) × ln(pⱼ^monitor / pⱼ^reference)` |
| 68 | Target PSI | `PSI_Y = Σₖ∈{0,1} (pₖ^monitor − pₖ^reference) × ln(pₖ^monitor / pₖ^reference)` |
| 84 | Gini impurity | `G(t) = 1 − Σₖ (pₖ|t)²` |
| 86 | Information Value | `IV = Σⱼ (% non-defaultsⱼ − % defaultsⱼ) × WOEⱼ` |
| 87 | Model Gini | `Gini = 2 × AUC − 1` |

## Important distinctions

- **Gini impurity** is a decision-tree split criterion. It measures how mixed the classes are inside one node.
- **Model Gini** is a discrimination measure derived from model AUC: `2 × AUC − 1`.
- **Information Value** is a target-driven, binned, univariate separation measure. It is not incremental model performance and it does not prove causality.
- **WOE and IV are target-driven transformations.** Fit bins, WOE values, smoothing, and IV calculations inside the training sample or training fold.
- **Decision-tree binning proposes cut points.** The analyst and risk-governance process review, merge, constrain, and approve the final bins using sample size, monotonicity, stability, missingness, and operational meaning.
- **Variable PSI** monitors input distributions and can be calculated before labels arrive. **Target PSI** monitors outcome prevalence and is available only after the target window closes.

