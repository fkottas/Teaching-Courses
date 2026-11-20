# Week 5 mathematics reference

This is the copyable mathematics reference for the 96-slide Week 5 deck. It intentionally uses plain Unicode notation rather than fragile LaTeX commands. GitHub will therefore display the equations as written, without interpreting unmatched delimiters, unsupported macros, or square brackets as links.

## Formula map

| Concept | GitHub-safe formula |
|---|---|
| Prediction objective | f̂ = arg min over f∈F of (1/n_train) × Σᵢ∈train L(yᵢ, f(xᵢ)) |
| Logistic score | ηᵢ = β₀ + xᵢᵀβ = β₀ + Σⱼ₌₁ᵖ βⱼxᵢⱼ |
| Sigmoid probability | pᵢ = P(Yᵢ = 1 \| xᵢ) = 1 / [1 + exp(−ηᵢ)] |
| Odds | oddsᵢ = pᵢ / (1 − pᵢ) = exp(ηᵢ) |
| Log-odds | ln[pᵢ / (1 − pᵢ)] = ηᵢ = β₀ + xᵢᵀβ |
| Likelihood | L(β₀,β) = Πᵢ₌₁ⁿ pᵢʸⁱ (1 − pᵢ)¹⁻ʸⁱ |
| Log-likelihood | ℓ(β₀,β) = Σᵢ₌₁ⁿ [yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ)] |
| Binary log-loss | J(β₀,β) = −(1/n) × Σᵢ₌₁ⁿ [yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ)] |
| Gradient | ∇βJ = (1/n) × Xᵀ(p − y) |
| One-feature gradient | ∂J/∂βⱼ = (1/n) × Σᵢ₌₁ⁿ (pᵢ − yᵢ)xᵢⱼ |
| Gradient update | β⁽ᵗ⁺¹⁾ = β⁽ᵗ⁾ − a × ∇βJ(β⁽ᵗ⁾) |
| Threshold rule | ŷᵢ(c) = 1 if pᵢ ≥ c; otherwise ŷᵢ(c) = 0 |
| Ridge objective | J_Ridge = J + λ × Σⱼ₌₁ᵖ βⱼ² |
| LASSO objective | J_LASSO = J + λ × Σⱼ₌₁ᵖ abs(βⱼ) |
| Elastic Net objective | J_EN = J + λ [ α × Σⱼ₌₁ᵖ abs(βⱼ) + (1−α) × (1/2) × Σⱼ₌₁ᵖ βⱼ² ] |
| Weighted log-loss | J_w = −(1/n) × Σᵢ₌₁ⁿ wᵧᵢ [yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ)] |

## Notation and symbols

| Symbol | Meaning |
|---|---|
| i = 1,…,n | Observation index; n is the number of rows. |
| j = 1,…,p | Feature index; p is the number of input variables. |
| xᵢ | Feature vector for observation i. |
| xᵢⱼ | Value of feature j for observation i. |
| yᵢ ∈ {0,1} | Observed binary label; yᵢ = 1 is the event being modelled. |
| β₀ | Intercept; baseline log-odds before feature contributions. |
| β | Vector of feature coefficients (β₁,…,βₚ). |
| βⱼ | Coefficient for feature j, holding other features fixed. |
| ηᵢ | Linear score before the sigmoid transformation. |
| pᵢ | Predicted probability P(Yᵢ = 1 \| xᵢ), between 0 and 1. |
| σ(·) | Sigmoid function, σ(η) = 1/[1 + exp(−η)]. |
| exp(·) | Exponential function; exp(z) = eᶻ. |
| ln(·) | Natural logarithm. |
| L | Likelihood of the observed labels under the candidate coefficients. |
| ℓ | Log-likelihood; maximised during maximum-likelihood fitting. |
| J | Average loss being minimised. |
| X | Feature matrix; each row is one observation. |
| a | Learning rate in gradient descent. |
| c | Decision threshold applied after probabilities are estimated. |
| λ ≥ 0 | Overall regularisation strength. Larger λ applies a stronger penalty. |
| α ∈ [0,1] | Elastic Net mixture; α = 1 is LASSO and α = 0 is Ridge. |
| w₀, w₁ | Class weights for non-events and events. |
| F | Candidate model class in the prediction objective. |

The intercept β₀ is normally excluded from Ridge, LASSO, and Elastic Net penalties because it calibrates the baseline event rate.

## 1. Prediction objective

Supervised learning chooses a function that performs well on the training sample:

~~~text
f̂ = arg min over f∈F of
(1/n_train) × Σᵢ∈train L(yᵢ, f(xᵢ))
~~~

F is the candidate model class and L is the one-row loss. The training sample fits the rule. Validation estimates generalisation and helps choose hyperparameters. The final test sample is used only after those choices are frozen.

## 2. Logistic score and sigmoid

The score is linear in the input features:

~~~text
ηᵢ = β₀ + xᵢᵀβ
   = β₀ + Σⱼ₌₁ᵖ βⱼxᵢⱼ
~~~

The sigmoid converts every real score into a probability:

~~~text
pᵢ = P(Yᵢ = 1 | xᵢ)
   = 1 / [1 + exp(−ηᵢ)]
~~~

Checks:

- If ηᵢ = 0, then pᵢ = 0.500.
- If ηᵢ increases, pᵢ increases.
- If ηᵢ tends to negative infinity, pᵢ tends to 0.
- If ηᵢ tends to positive infinity, pᵢ tends to 1.

Numerical example: if η = 0.40, then p = 1/[1 + exp(−0.40)] ≈ 0.599. If η = −1.10, then p ≈ 0.250.

## 3. Odds and coefficient interpretation

Odds compare the event probability with the non-event probability:

~~~text
oddsᵢ = pᵢ / (1 − pᵢ) = exp(ηᵢ)
ln[ pᵢ / (1 − pᵢ) ] = ηᵢ
~~~

Holding all other features fixed, a one-unit increase in xᵢⱼ multiplies the odds by exp(βⱼ). It does not add a constant number of percentage points to pᵢ because the sigmoid is nonlinear.

If βⱼ = 0.40:

~~~text
exp(βⱼ) = exp(0.40) ≈ 1.49
~~~

The odds are multiplied by approximately 1.49, or increase by approximately 49%. The probability change depends on the starting probability.

## 4. Likelihood and log-likelihood

For a binary label, the likelihood multiplies the probability assigned to the observed outcome in every row:

~~~text
L(β₀,β) = Πᵢ₌₁ⁿ pᵢʸⁱ (1 − pᵢ)¹⁻ʸⁱ
~~~

If yᵢ = 1, the row contribution is pᵢ. If yᵢ = 0, the row contribution is 1 − pᵢ. Taking logs turns the product into a sum:

~~~text
ℓ(β₀,β) = Σᵢ₌₁ⁿ [ yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ) ]
~~~

Maximum likelihood chooses the coefficients that maximise ℓ. Equivalently, logistic training minimises the negative average log-likelihood.

## 5. Binary log-loss

The objective being minimised is:

~~~text
J(β₀,β) = −(1/n) × Σᵢ₌₁ⁿ
           [ yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ) ]
~~~

For one row:

- when yᵢ = 1, loss = −ln(pᵢ);
- when yᵢ = 0, loss = −ln(1−pᵢ).

Example for a positive event:

~~~text
If y = 1 and p = 0.90: loss = −ln(0.90) ≈ 0.105
If y = 1 and p = 0.10: loss = −ln(0.10) ≈ 2.303
~~~

A confident mistake therefore receives a much larger loss than a cautious prediction.

## 6. Gradient descent

Let X be the feature matrix, p the vector of predicted probabilities, and y the vector of observed labels. The gradient of the unregularised average log-loss is:

~~~text
∇βJ = (1/n) × Xᵀ(p − y)
~~~

For one feature j:

~~~text
∂J/∂βⱼ = (1/n) × Σᵢ₌₁ⁿ (pᵢ − yᵢ)xᵢⱼ
~~~

With learning rate a > 0:

~~~text
β⁽ᵗ⁺¹⁾ = β⁽ᵗ⁾ − a × ∇βJ(β⁽ᵗ⁾)
~~~

If a gradient component is positive, increasing that coefficient currently increases the loss, so the update reduces the coefficient. The learning rate is a hyperparameter, not a fitted coefficient.

## 7. Threshold and decision policy

The model estimates pᵢ first. A separate policy converts the probability into an action:

~~~text
ŷᵢ(c) = 1  if pᵢ ≥ c
       = 0  if pᵢ < c
~~~

Changing c does not refit β₀ or β. It changes positive decisions, false positives, false negatives, approval volume, and review volume. The threshold must follow an explicit cost, capacity, or governance rule.

## 8. Ridge, LASSO, and Elastic Net

Let J(β₀,β) be the unpenalised logistic loss. The three objectives are:

~~~text
J_Ridge = J(β₀,β) + λ × Σⱼ₌₁ᵖ βⱼ²

J_LASSO = J(β₀,β) + λ × Σⱼ₌₁ᵖ |βⱼ|

J_EN = J(β₀,β)
       + λ [ α × Σⱼ₌₁ᵖ |βⱼ|
             + (1−α) × (1/2) × Σⱼ₌₁ᵖ βⱼ² ]
~~~

Interpretation:

- Ridge uses the squared L2 penalty. It shrinks large coefficients smoothly and usually keeps correlated variables together.
- LASSO uses the absolute L1 penalty. It can make some coefficients exactly zero, so it can perform feature selection.
- Elastic Net combines both. The L1 part encourages sparsity; the L2 part stabilises correlated predictors.
- λ controls the total strength of regularisation.
- α controls the mixture between L1 and L2.
- β₀ is excluded from all three penalties.

### Elastic Net numerical example

Let β = (0.8, 0.7), λ = 0.10, and α = 0.50:

~~~text
L1 part       = |0.8| + |0.7| = 1.50
Squared L2    = 0.8² + 0.7² = 1.13
Penalty       = 0.10 × [0.50×1.50 + 0.50×(1/2)×1.13]
               = 0.10325
~~~

The penalty is added to the unpenalised loss. It is not a separate probability or a separate data column.

## 9. Class-weighted loss

When an event and a non-event have different decision costs, the fitted objective can weight their contributions:

~~~text
J_w = −(1/n) × Σᵢ₌₁ⁿ wᵧᵢ
      [ yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ) ]
~~~

w₀ weights non-events and w₁ weights events. Class weighting changes the fitted coefficients. Threshold selection changes the decision rule after fitting. They are different interventions.

## Interpretation boundary

A logistic coefficient is a conditional association inside the fitted model. It is not automatically a causal effect, a stable population relationship, a fair decision rule, or a guarantee of profitability. Those claims require separate design, monitoring, and governance evidence.
