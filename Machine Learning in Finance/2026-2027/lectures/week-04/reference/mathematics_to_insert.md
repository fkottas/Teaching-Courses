# Week 4 mathematics reference

The presentation uses editable native text for these equations. This reference uses Unicode/plain text deliberately so the equations remain readable in GitHub and PowerPoint.

## Formula locations in the 90-slide deck

| Slide | Concept | Formula |
|---:|---|---|
| 18 | Utilization | utilizationᵢ = BILL_AMT1ᵢ / LIMIT_BALᵢ, when LIMIT_BALᵢ ≠ 0 |
| 21 | Payment capacity | payment_to_billᵢ = total_paid_6mᵢ / total_bill_6mᵢ, when total_bill_6mᵢ ≠ 0 |
| 27 | Change | Δxₜ = xₜ − xₜ₋₁ |
| 29 | Log transformation | log_limitᵢ = ln(1 + LIMIT_BALᵢ) |
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
| 59 | Elastic Net | minimize −ℓ(β₀, β) + λ[α‖β‖₁ + (1−α)(1/2)‖β‖₂²] |
| 65 | Lookback utilization | utilizationᵢ,ₜ = BILL_AMTᵢ,ₜ / LIMIT_BALᵢ |
| 67 | PSI contribution | PSIⱼ = (qⱼ − pⱼ) × ln(qⱼ / pⱼ), and PSI = Σⱼ PSIⱼ |
| 68 | PSI code | The code implements the same bin-level sum with a small epsilon for zero shares |
| 83 | Gini impurity | G(t) = 1 − [p₀|t² + p₁|t²] |
| 84 | Worked WOE | WOEⱼ = ln(GoodShareⱼ / BadShareⱼ) |
| 85 | Worked Information Value | IV = Σⱼ (GoodShareⱼ − BadShareⱼ) × WOEⱼ |
| 87 | Model Gini | Gini = 2 × AUC − 1 |

## Worked calculations

### Gini impurity

For a node containing 80% non-defaults and 20% defaults:

G(t) = 1 − (0.80² + 0.20²) = 1 − (0.64 + 0.04) = 0.32

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
