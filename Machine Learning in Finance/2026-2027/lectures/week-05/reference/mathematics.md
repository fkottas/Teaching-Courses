# Week 5 mathematics reference

This is the mathematics reference for the single canonical 96-slide Week 5 deck. It follows the same convention as the previous lecture: a formula map, plain Unicode equations, a symbol glossary, worked numerical examples, and interpretation rules.

The equations are deliberately written in plain text and Unicode. They do not use LaTeX delimiters, left/right commands, operatorname macros, or Markdown link syntax inside formulas. They therefore remain readable on GitHub, in a downloaded Markdown file, and in Colab.

## Formula map

| Slide | Concept | Formula or rule |
|---:|---|---|
| 4 | Model mapping | f(θ; X) maps available information X to an output using parameters θ. |
| 11 | Predictive objective | f̂ = arg min over f∈F of (1/n_train) × Σᵢ∈train L(yᵢ, f(xᵢ)). |
| 20 | Supervised target | At cutoff t, use Xₜ to predict the later label Yₜ₊ₕ. |
| 25 | PCA score | zₖ = Xwₖ, where wₖ is the loading vector for component k. |
| 28 | PCA explained variance | EVRₖ = λₖ / Σᵣ λᵣ; cumulative EVR(K) = Σₖ₌₁ᴷ EVRₖ. |
| 30 | K-means assignment | Assign observation i to the centroid μₖ with the smallest distance d(xᵢ, μₖ). |
| 30 | K-means centroid | μₖ = (1/nₖ) × Σᵢ assigned to k xᵢ. |
| 31 | K-means objective | Inertia I = Σₖ₌₁ᴷ Σᵢ assigned to k ||xᵢ − μₖ||². |
| 33 | Reinforcement learning value | Q(S,A) = expected discounted reward after taking action A in state S. |
| 33 | Bellman target | Q(S,A) ← R + γ × max over A′ Q(S′,A′). |
| 41 | Information boundary | feature event_time ≤ prediction_time; future information is excluded. |
| 47 | Bias–variance decomposition | Expected squared error = bias² + variance + irreducible noise. |
| 49 | Generic objective | J(θ) = data-fit loss(θ) + penalty(θ). |
| 61 | Logistic score | ηᵢ = β₀ + xᵢᵀβ = β₀ + Σⱼ₌₁ᵖ βⱼxᵢⱼ. |
| 62 | Sigmoid probability | pᵢ = P(Yᵢ = 1 given xᵢ) = 1 / [1 + exp(−ηᵢ)]. |
| 63 | Odds and log-odds | oddsᵢ = pᵢ/(1−pᵢ) = exp(ηᵢ); ln(oddsᵢ) = ηᵢ. |
| 65 | Coefficient interpretation | A one-unit increase in xⱼ multiplies the odds by exp(βⱼ), holding other features fixed. |
| 66 | Threshold rule | ŷᵢ(c) = 1 when pᵢ ≥ c; otherwise ŷᵢ(c) = 0. |
| 67 | Bernoulli likelihood | L(β₀,β) = Πᵢ₌₁ⁿ pᵢʸⁱ × (1−pᵢ)¹⁻ʸⁱ. |
| 68 | Log-likelihood | ℓ(β₀,β) = Σᵢ₌₁ⁿ [yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ)]. |
| 69 | Binary log-loss | J = −(1/n) × Σᵢ₌₁ⁿ [yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ)]. |
| 71 | Logistic gradient | ∇βJ = (1/n) × Xᵀ(p−y); ∂J/∂βⱼ = (1/n) × Σᵢ(pᵢ−yᵢ)xᵢⱼ. |
| 72 | Gradient update | β⁽ᵗ⁺¹⁾ = β⁽ᵗ⁾ − a × ∇βJ(β⁽ᵗ⁾). |
| 77 | Regularised objective | J_regularised = J + penalty; the intercept is excluded from the penalty. |
| 78 | Ridge | J_Ridge = J + λ × Σⱼ₌₁ᵖ βⱼ². |
| 79 | LASSO | J_LASSO = J + λ × Σⱼ₌₁ᵖ abs(βⱼ). |
| 80 | Elastic Net | J_EN = J + λ [α × Σⱼ abs(βⱼ) + (1−α) × (1/2) × Σⱼ βⱼ²]. |
| 81 | Class-weighted loss | Jw = −(1/n) × Σᵢ wᵧᵢ [yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ)]. |

## Symbol glossary

| Symbol | Meaning | Reading in the Week 5 example |
|---|---|---|
| θ | All fitted model parameters | In logistic regression, θ contains β₀ and β. |
| X | Available input information | The borrower features known at the decision time. |
| f(θ; X) | Fitted mapping from inputs to output | The rule that converts borrower information into a score or probability. |
| i = 1,…,n | Observation index | One borrower snapshot is observation i. |
| j = 1,…,p | Feature index | Feature j may be utilisation or overdue_count. |
| xᵢ | Feature vector for row i | All approved inputs for one borrower snapshot. |
| xᵢⱼ | Value of feature j for row i | The utilisation value for borrower i. |
| yᵢ ∈ {0,1} | Observed binary label | 1 means the defined default event occurred. |
| Yᵢ | Random future outcome | The event before its realised value is known. |
| β₀ | Intercept | Baseline log-odds when the features equal zero after preprocessing. |
| β | Vector of feature coefficients | β = (β₁,…,βₚ). |
| βⱼ | Coefficient for feature j | Effect of one unit of xⱼ on log-odds, conditional on the other features. |
| ηᵢ | Linear score | The quantity passed into the sigmoid. |
| pᵢ | Predicted event probability | A number from 0 to 1. |
| σ(·) | Sigmoid function | σ(η) = 1/[1+exp(−η)]. |
| exp(·) | Exponential function | exp(z) = eᶻ. |
| ln(·) | Natural logarithm | The logarithm used in likelihood and log-loss. |
| L | Likelihood | Probability assigned to all observed labels jointly. |
| ℓ | Log-likelihood | ln(L); maximised when fitting logistic regression. |
| J | Average loss | The quantity minimised by the training algorithm. |
| Xᵀ | Transpose of the feature matrix | Reverses the orientation for the matrix gradient. |
| a | Gradient-descent learning rate | Controls the size of an optimisation step. |
| c | Decision threshold | Converts a probability into a binary action. |
| λ ≥ 0 | Regularisation strength | Larger λ gives a stronger penalty. |
| α ∈ [0,1] | Elastic Net mixture | α = 1 is LASSO; α = 0 is Ridge. |
| w₀, w₁ | Class weights | Relative importance assigned to non-events and events. |
| zₖ | Principal-component score | The value of component k for one row. |
| wₖ | PCA loading vector | The direction used to construct component k. |
| λₖ | PCA eigenvalue | Variance explained by component k. |
| μₖ | K-means centroid | Coordinate-wise mean of cluster k. |
| d(xᵢ, μₖ) | Distance from row i to centroid k | Used for the assignment step. |
| S | Reinforcement-learning state | Current market or portfolio information. |
| A | Reinforcement-learning action | Buy, sell, hold, hedge, or another decision. |
| R | Reward | Outcome received after an action. |
| γ ∈ [0,1] | Discount factor | Weight placed on future rewards. |
| Q(S,A) | State–action value | Expected discounted reward from taking A in S. |

## 1. From a financial question to a prediction objective

The model mapping is:

~~~text
f(θ; X) = output produced by parameters θ from information X
~~~

Supervised learning chooses a function that performs well on the training rows:

~~~text
f̂ = arg min over f∈F of
(1/n_train) × Σᵢ∈train L(yᵢ, f(xᵢ))
~~~

F is the candidate model class, L is the one-row loss, and n_train is the number of training rows. The validation sample is used to compare candidate models and hyperparameters. The final test sample is used only after those choices are frozen.

## 2. PCA: the overview mathematics

PCA starts with centred or standardised features. Let X be the resulting n by p matrix. The sample covariance matrix is:

~~~text
Σ = (1/(n−1)) × XᵀX
~~~

PCA solves the eigenvalue equation:

~~~text
Σwₖ = λₖwₖ
~~~

The component score is:

~~~text
zₖ = Xwₖ
~~~

The explained-variance ratio is:

~~~text
EVRₖ = λₖ / (λ₁ + λ₂ + … + λₚ)
cumulative EVR(K) = EVR₁ + … + EVRₖ
~~~

Numerical example: if the eigenvalues are 4.0, 1.0, and 0.5, total variance is 5.5. Component 1 explains 4.0/5.5 = 72.7%; the first two explain 5.0/5.5 = 90.9%. PCA creates new directions; it does not assign observations to clusters.

## 3. K-means: distance, centroid, and objective

For two rows P and Q with two features, Euclidean distance is:

~~~text
d₂(P,Q) = √[(x₁Q−x₁P)² + (x₂Q−x₂P)²]
~~~

For p features:

~~~text
d₂(xᵢ, μₖ) = √[Σⱼ₌₁ᵖ (xᵢⱼ−μₖⱼ)²]
~~~

One K-means iteration has two calculations:

~~~text
Assignment: assign i to cluster k with the smallest d₂(xᵢ, μₖ)
Update:      μₖ = (1/nₖ) × Σᵢ assigned to k xᵢ
~~~

Worked centroid update: if cluster 1 contains (2,4) and (4,8), its new centroid is ((2+4)/2, (4+8)/2) = (3,6). The centroid moves because it is replaced by the mean of the rows currently assigned to the cluster.

The within-cluster objective is:

~~~text
I = Σₖ₌₁ᴷ Σᵢ assigned to k ||xᵢ−μₖ||²
~~~

The objective decreases as K increases, so K cannot be chosen only by the lowest inertia. Use an elbow, silhouette, stability, and financial interpretation together.

## 4. Reinforcement learning: value and update

Reinforcement learning uses states, actions, rewards, and a policy. The value of taking action A in state S is:

~~~text
Q(S,A) = expected discounted total reward after taking A in S
~~~

The one-step temporal-difference target is:

~~~text
target = R + γ × max over A′ Q(S′,A′)
Q_new(S,A) = Q_old(S,A) + a × [target − Q_old(S,A)]
~~~

Here a is the learning rate for the Q update and γ discounts future rewards. Do not confuse a reinforcement-learning action A with the gradient-descent learning rate a; the context is different.

Numerical example: Q_old = 0.80, R = 0.20, γ = 0.90, and max Q(S′,A′) = 0.90. The target is 0.20 + 0.90×0.90 = 1.01. With a = 0.05:

~~~text
Q_new = 0.80 + 0.05 × (1.01−0.80)
      = 0.8105
~~~

## 5. Bias, variance, underfitting, and overfitting

For a new observation, expected squared prediction error can be decomposed as:

~~~text
Expected error = Bias² + Variance + irreducible noise
~~~

Bias is systematic error from a model that is too rigid or omits repeatable structure. Variance is sensitivity to the particular training sample. Irreducible noise is uncertainty that no model can remove.

- Underfitting: high bias, usually low variance; both training and validation errors remain high.
- Overfitting: low training error but high validation or test error; the model has learned noise or sample-specific detail.
- Increasing complexity normally reduces bias but can increase variance.
- Validation selects a complexity or regularisation level; the test sample estimates final generalisation.

## 6. Logistic score and sigmoid

The score is linear in the features:

~~~text
ηᵢ = β₀ + xᵢᵀβ
   = β₀ + Σⱼ₌₁ᵖ βⱼxᵢⱼ
~~~

The sigmoid maps the score into the interval from 0 to 1:

~~~text
pᵢ = P(Yᵢ = 1 given xᵢ)
   = 1 / [1 + exp(−ηᵢ)]
~~~

Checks:

- η = 0 gives p = 0.500.
- η = 0.40 gives p = 1/[1+exp(−0.40)] ≈ 0.599.
- η = −1.10 gives p ≈ 0.250.

## 7. Odds and coefficient interpretation

The odds and log-odds are:

~~~text
oddsᵢ = pᵢ/(1−pᵢ) = exp(ηᵢ)
ln[oddsᵢ] = ln[pᵢ/(1−pᵢ)] = ηᵢ
~~~

If βⱼ = 0.40:

~~~text
odds multiplier = exp(βⱼ) = exp(0.40) ≈ 1.49
~~~

Holding other features fixed, a one-unit increase in xⱼ multiplies the odds by 1.49. It does not increase probability by 49 percentage points. The probability effect depends on the starting probability because the sigmoid is nonlinear.

## 8. Likelihood, log-likelihood, and log-loss

The Bernoulli likelihood is:

~~~text
L(β₀,β) = Πᵢ₌₁ⁿ pᵢʸⁱ × (1−pᵢ)¹⁻ʸⁱ
~~~

When yᵢ = 1, the contribution is pᵢ. When yᵢ = 0, the contribution is 1−pᵢ. Taking the natural logarithm changes a product into a sum:

~~~text
ℓ(β₀,β) = Σᵢ₌₁ⁿ [ yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ) ]
~~~

Training minimises the negative average log-likelihood:

~~~text
J(β₀,β) = −(1/n) × Σᵢ₌₁ⁿ
           [ yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ) ]
~~~

For one positive event:

~~~text
y = 1, p = 0.90: loss = −ln(0.90) ≈ 0.105
y = 1, p = 0.10: loss = −ln(0.10) ≈ 2.303
~~~

A confident mistake is therefore punished much more heavily than a cautious mistake.

## 9. Gradient descent

Let X be the feature matrix, p the predicted-probability vector, and y the observed-label vector. The gradient is:

~~~text
∇βJ = (1/n) × Xᵀ(p−y)
∂J/∂βⱼ = (1/n) × Σᵢ₌₁ⁿ (pᵢ−yᵢ)xᵢⱼ
~~~

The update is:

~~~text
β⁽ᵗ⁺¹⁾ = β⁽ᵗ⁾ − a × ∇βJ(β⁽ᵗ⁾)
~~~

If the gradient component is positive, increasing that coefficient currently raises the loss, so the update reduces the coefficient. The learning rate controls the step size and is selected as a hyperparameter.

## 10. Threshold and decision policy

The model produces pᵢ first. The policy then applies a threshold c:

~~~text
ŷᵢ(c) = 1 when pᵢ ≥ c
       = 0 when pᵢ < c
~~~

Changing c does not refit β. It changes false positives, false negatives, approval volume, and review volume. A threshold must be justified by error costs, capacity, regulation, or another governance rule.

## 11. Ridge, LASSO, and Elastic Net

Let J(β₀,β) be the unpenalised logistic loss. The intercept β₀ is excluded from the penalty.

~~~text
Ridge:
J_Ridge = J(β₀,β) + λ × Σⱼ₌₁ᵖ βⱼ²

LASSO:
J_LASSO = J(β₀,β) + λ × Σⱼ₌₁ᵖ abs(βⱼ)

Elastic Net:
J_EN = J(β₀,β)
       + λ [ α × Σⱼ₌₁ᵖ abs(βⱼ)
             + (1−α) × (1/2) × Σⱼ₌₁ᵖ βⱼ² ]
~~~

Interpretation:

- Ridge is the L2 penalty. It shrinks large coefficients smoothly and normally retains all variables.
- LASSO is the L1 penalty. It can set coefficients exactly to zero, so it can perform feature selection.
- Elastic Net combines L1 sparsity with L2 stability for correlated predictors.
- λ controls overall penalty strength.
- α controls the mixture: α = 1 is LASSO and α = 0 is Ridge.

### Elastic Net numerical example

Let β = (0.8, 0.7), λ = 0.10, and α = 0.50:

~~~text
L1 part    = abs(0.8) + abs(0.7) = 1.50
Squared L2 = 0.8² + 0.7² = 1.13

Penalty = 0.10 × [0.50×1.50 + 0.50×(1/2)×1.13]
        = 0.10325
~~~

This penalty is added to the data-fit loss. It is not a probability and it is not a new feature.

## 12. Class-weighted loss

If the event and non-event have different decision costs, use:

~~~text
Jw = −(1/n) × Σᵢ₌₁ⁿ wᵧᵢ
     [ yᵢ ln(pᵢ) + (1−yᵢ) ln(1−pᵢ) ]
~~~

w₀ weights non-events and w₁ weights events. Class weighting changes the fitted coefficients. Threshold selection changes the decision rule after fitting. They are different interventions.

## Interpretation rules

1. A probability model and a decision threshold are separate objects.
2. A coefficient is interpreted on the log-odds scale first; convert it to an odds multiplier with exp(βⱼ).
3. Logistic probability is bounded by the sigmoid; an unrestricted linear probability is not.
4. Likelihood multiplies the probabilities assigned to the observed labels; log-likelihood turns the product into a sum.
5. Regularisation is part of the objective and must be selected inside the validation design.
6. The intercept is excluded from Ridge, LASSO, and Elastic Net penalties.
7. PCA creates directions; K-means creates groups; reinforcement learning learns values from sequential rewards.
8. A good validation score does not establish causality, fairness, profitability, or deployment readiness.
