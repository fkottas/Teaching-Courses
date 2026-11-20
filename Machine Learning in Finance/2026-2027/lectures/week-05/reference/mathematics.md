# Week 5 mathematics reference

This file is the text source for the equations used in the Week 5 deck. Every symbol is defined before it is used. The display equations use standard GitHub-compatible LaTeX: delimiters are balanced and only widely supported commands are used.

## Notation

- \(i=1,\ldots,n\) indexes observations.
- \(j=1,\ldots,p\) indexes features.
- \(x_i=(x_{i1},\ldots,x_{ip})^\mathsf{T}\) is the feature vector for observation \(i\).
- \(y_i\in\{0,1\}\) is the observed binary label; \(y_i=1\) is the event being modelled.
- \(\beta_0\) is the intercept and \(\boldsymbol{\beta}=(\beta_1,\ldots,\beta_p)^\mathsf{T}\) contains feature coefficients.
- \(\eta_i\) is the linear score and \(p_i\) is the predicted probability of the event \(Y_i=1\).

## A prediction objective

For a candidate function \(f\) and a one-row loss \(L\), supervised learning chooses a function that performs well on the training sample:

$$
\widehat f \in \arg\min_{f\in\mathcal F}
\frac{1}{n_{\mathrm{train}}}
\sum_{i\in\mathrm{train}} L\bigl(y_i,f(x_i)\bigr).
$$

Here \(\mathcal F\) is the candidate model class, \(n_{\mathrm{train}}\) is the number of training rows, and \(L\) measures the cost of a prediction error. The validation design estimates whether the fitted rule generalises beyond the rows used to fit it.

## Logistic score and sigmoid

The score is linear in the features:

$$
\eta_i=\beta_0+x_i^\mathsf{T}\boldsymbol{\beta}
=\beta_0+\sum_{j=1}^{p}\beta_jx_{ij}.
$$

The sigmoid maps every real score to a number between zero and one:

$$
p_i=\Pr(Y_i=1\mid x_i)
=\sigma(\eta_i)
=\frac{1}{1+\exp(-\eta_i)}.
$$

The score is not yet a probability. The sigmoid is the link that turns the score into a probability:

- if \(\eta_i=0\), then \(p_i=0.5\);
- if \(\eta_i\) increases, \(p_i\) increases;
- as \(\eta_i\to-\infty\), \(p_i\to0\);
- as \(\eta_i\to+\infty\), \(p_i\to1\).

For example, \(\eta=0.40\) gives \(p=1/(1+\exp(-0.40))\approx0.599\). A score of \(-1.10\) gives \(p\approx0.250\).

## Odds and log-odds

The odds compare the event probability with the non-event probability:

$$
\mathrm{odds}_i=\frac{p_i}{1-p_i}=\exp(\eta_i).
$$

Taking the natural logarithm gives the linear log-odds relation:

$$
\log\bigl(\frac{p_i}{1-p_i}\bigr)
=\eta_i
=\beta_0+x_i^\mathsf{T}\boldsymbol{\beta}.
$$

Holding other features fixed, a one-unit increase in \(x_{ij}\) changes the odds by the multiplier \(\exp(\beta_j)\). It does not change the probability by a constant number of percentage points because the sigmoid is nonlinear. If \(\beta_j=0.40\), then \(\exp(0.40)\approx1.49\): the odds are multiplied by about 1.49.

## Likelihood and log-likelihood

For a binary label, the Bernoulli likelihood contribution of row \(i\) can be written in one expression:

$$
\mathcal L(\beta_0,\boldsymbol{\beta})
=\prod_{i=1}^{n}
p_i^{y_i}(1-p_i)^{1-y_i}.
$$

If \(y_i=1\), the contribution is \(p_i\); if \(y_i=0\), the contribution is \(1-p_i\). Under the usual independent-row assumption, the likelihood multiplies the row contributions.

The log-likelihood is easier to optimise:

$$
\ell(\beta_0,\boldsymbol{\beta})
=\sum_{i=1}^{n}
\bigl[
y_i\log(p_i)+(1-y_i)\log(1-p_i)
\bigr].
$$

Maximum likelihood chooses the coefficients that maximise \(\ell\). Equivalently, training minimises the negative average log-likelihood.

## Binary log-loss

The negative average log-likelihood is the binary cross-entropy or log-loss:

$$
J(\beta_0,\boldsymbol{\beta})
=-\frac{1}{n}\sum_{i=1}^{n}
\bigl[
y_i\log(p_i)+(1-y_i)\log(1-p_i)
\bigr].
$$

For one row:

- \(y_i=1\) gives loss \(-\log(p_i)\);
- \(y_i=0\) gives loss \(-\log(1-p_i)\).

If \(y_i=1\) and \(p_i=0.90\), the contribution is \(-\log(0.90)\approx0.105\). If \(y_i=1\) and \(p_i=0.10\), the contribution is \(-\log(0.10)\approx2.303\). A confident mistake is therefore much more costly than a cautious mistake.

## Gradient and gradient descent

Let \(X\) be the feature matrix, \(\mathbf p\) the vector of predicted probabilities, and \(\mathbf y\) the label vector. For the unregularised average log-loss, the gradient with respect to the feature coefficients is:

$$
\nabla_{\boldsymbol{\beta}}J
=\frac{1}{n}X^\mathsf{T}(\mathbf p-\mathbf y).
$$

For one feature \(j\):

$$
\frac{\partial J}{\partial\beta_j}
=\frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)x_{ij}.
$$

With learning rate \(a>0\), one gradient step is:

$$
\boldsymbol{\beta}^{(t+1)}
=\boldsymbol{\beta}^{(t)}
-a\nabla_{\boldsymbol{\beta}}J\bigl(\boldsymbol{\beta}^{(t)}\bigr).
$$

If a gradient component is positive, increasing that coefficient currently increases the loss, so the update reduces the coefficient. The learning rate controls step size; it is a hyperparameter, not a fitted coefficient.

## Threshold and decision policy

The model first estimates \(p_i\). A policy then converts it to a binary decision at threshold \(c\):

$$
\widehat y_i(c)=
\begin{cases}
1,&\text{if }p_i\ge c,\\
0,&\text{if }p_i<c.
\end{cases}
$$

Changing \(c\) does not refit \(\beta_0\) or \(\boldsymbol{\beta}\). It changes the number of positive decisions, false positives, false negatives, approval volume, and review volume. The threshold should follow an explicit cost, capacity, or governance rule.

## Ridge, LASSO, and Elastic Net

Let \(J(\beta_0,\boldsymbol{\beta})\) denote the unpenalised logistic loss. The intercept is normally excluded from the penalty because it calibrates the baseline event rate.

Ridge (\(L_2\)) adds a squared-coefficient penalty:

$$
J_{\mathrm{ridge}}(\beta_0,\boldsymbol{\beta})
=J(\beta_0,\boldsymbol{\beta})
+\lambda\sum_{j=1}^{p}\beta_j^2.
$$

LASSO (\(L_1\)) adds an absolute-coefficient penalty:

$$
J_{\mathrm{lasso}}(\beta_0,\boldsymbol{\beta})
=J(\beta_0,\boldsymbol{\beta})
+\lambda\sum_{j=1}^{p}\lvert\beta_j\rvert.
$$

Elastic Net combines both penalties:

$$
J_{\mathrm{EN}}(\beta_0,\boldsymbol{\beta})
=J(\beta_0,\boldsymbol{\beta})
+\lambda\bigl[
\alpha\sum_{j=1}^{p}\lvert\beta_j\rvert
+(1-\alpha)\frac{1}{2}\sum_{j=1}^{p}\beta_j^2
+\bigr].
$$

Here \(\lambda\ge0\) controls overall penalty strength and \(\alpha\in[0,1]\) controls the mixture. With this convention, \(\alpha=1\) is LASSO and \(\alpha=0\) is Ridge up to the conventional factor of \(1/2\). Ridge usually shrinks correlated coefficients without making them exactly zero. LASSO can set some coefficients exactly to zero, but its selected set can be unstable when predictors are highly correlated. Elastic Net can preserve groups of correlated variables while still removing weak variables.

## Class-weighted loss

If events and non-events have different decision costs, a weighted loss can be used:

$$
J_w(\beta_0,\boldsymbol{\beta})
=-\frac{1}{n}\sum_{i=1}^{n}w_{y_i}
\bigl[
y_i\log(p_i)+(1-y_i)\log(1-p_i)
\bigr].
$$

Here \(w_0\) weights non-events and \(w_1\) weights events. Class weighting changes the fitted coefficients. Threshold selection changes the decision rule after fitting. They are different interventions.

## Worked coefficient example

Suppose \(\beta_j=0.40\). Then:

$$
\exp(\beta_j)=\exp(0.40)\approx1.49.
$$

Holding other features fixed, a one-unit increase in \(x_j\) multiplies the odds by approximately 1.49, or increases the odds by approximately 49%. The probability change depends on the starting score. At \(p=0.10\), the same odds multiplier gives a different percentage-point change than at \(p=0.50\).

## Interpretation boundary

The logistic coefficient describes a conditional association inside the fitted model. It is not automatically a causal effect, a stable population relationship, or a guarantee of fairness or profitability. Those claims require separate design, monitoring, and governance evidence.
