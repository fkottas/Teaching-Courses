# Week 4 mathematics reference

These formulas are written in plain Unicode notation so that they remain readable in GitHub, Markdown, Colab, and editable presentation text. They are not LaTeX macros and do not require `\\left`, `\\right`, `\\operatorname`, or a separate equation renderer.

## Slide locations

| Presentation slide | Concept | Formula to use |
|---:|---|---|
| 23 | Ratio feature | `utilisationᵢ = BILL_AMT1ᵢ / LIMIT_BALᵢ`, when `LIMIT_BALᵢ ≠ 0` |
| 27 | Payment capacity | `payment_to_billᵢ = total_paid_6mᵢ / total_bill_6mᵢ`, when `total_bill_6mᵢ ≠ 0` |
| 31 | Count feature | `overdue_countᵢ = Σₘ 1(PAY_statusᵢₘ > 0)` |
| 32 | Maximum severity | `max_delayᵢ = maxₘ(PAY_statusᵢₘ)` |
| 33 | Indicator | `high_utilizationᵢ = 1` if `utilizationᵢ ≥ 0.80`; otherwise `0` |
| 34 | Log transform | `log_limitᵢ = ln(1 + LIMIT_BALᵢ)` |
| 35 | Signed log | `signed_log(x) = sign(x) × ln(1 + |x|)` |
| 36 | Clipping | `utilisation_clippedᵢ = min(utilisationᵢ, 1.5)` |
| 37 | Standardisation | `zᵢ = (xᵢ − μ_train) / σ_train` |
| 38 | Min–max scaling | `x_scaledᵢ = (xᵢ − min_train) / (max_train − min_train)` |
| 39 | Percentile rank | `rank_i = rank(xᵢ) / number of valid reference observations` |
| 42 | Lag | `lag₁(xₜ) = xₜ₋₁` |
| 43 | Difference | `Δxₜ = xₜ − xₜ₋₁` |
| 44 | Growth / return | `growthₜ = (xₜ − xₜ₋₁) / xₜ₋₁`, when `xₜ₋₁ ≠ 0` |
| 45 | Rolling mean | `rolling_meanₖ(xₜ) = (1/k) × Σⱼ₌₀ᵏ⁻¹ xₜ₋ⱼ` |
| 46 | Rolling volatility | `rolling_stdₖ(xₜ) = standard deviation of {xₜ, xₜ₋₁, …, xₜ₋ₖ₊₁}` |
| 47 | Rolling maximum | `rolling_maxₖ(xₜ) = max{xₜ, xₜ₋₁, …, xₜ₋ₖ₊₁}` |
| 48 | Recency | `months_since_eventₜ = t − last_event_time` |
| 50 | As-of join | `same entity + event_time ≤ prediction_time` |
| 53 | Interaction | `interaction(x₁, x₂) = x₁ × x₂` |
| 54 | Combined state | `stress_flagᵢ = high_utilizationᵢ × recent_overdueᵢ` |
| 58 | Polynomial term | `x² = x × x` |
| 59 | Binning | `bin(x) = j` when `bⱼ ≤ x < bⱼ₊₁` |
| 63 | Train-only threshold | `threshold = quantile({xᵢ : i ∈ training rows}, q)` |
| 66 | Feature selection | `split → fit construction → select in training fold → evaluate on held-out fold` |

## Interpretation rules

- Ratios are dimensionless but can be unstable when the denominator is zero or close to zero.
- A count measures frequency; a maximum measures severity; a lag or difference measures movement; a rolling statistic measures recent history.
- Training-only parameters are part of the fitted transformation. They must not be estimated from validation or test rows.
- A formula defines a feature, but the feature is not valid until the raw fields, timing, missingness policy, and unit are documented.

