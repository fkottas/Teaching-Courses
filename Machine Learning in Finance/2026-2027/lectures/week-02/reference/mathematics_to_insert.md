# Mathematics to insert manually: Lecture 2

The PPTX intentionally contains no mathematics. Insert the following as editable PowerPoint equation objects. The slide numbers below match the final 51-slide deck.

| Slide | Equation to insert | What to explain below it |
|---:|---|---|
| 9 | `r_t = \frac{P_t-P_{t-1}}{P_{t-1}}` | `P_t` is the observed price at time `t`; the result is a decimal return for one period. Explain that the code uses the same formula for every adjacent pair of prices. |
| 11 | `r_{p,t}=\sum_{j=1}^{m}w_jr_{j,t}, \qquad \sum_{j=1}^{m}w_j=1` | `w_j` is the portfolio weight and `r_{j,t}` is asset `j`'s return. In the slide example the weights are 0.50, 0.30, and 0.20, so the portfolio return is 0.051 = 5.10%. |
| 19 | `m_j=\frac{1}{n}\sum_{i=1}^{n}I_{ij}, \qquad I_{ij}=\begin{cases}1,&\text{if }x_{ij}\text{ is missing}\\0,&\text{otherwise}\end{cases}` | `m_j` is the missingness rate for variable `j`. In the supplied UCI file every `m_j` is zero, but valid-looking codes still require interpretation. |
| 22 | `\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i, \qquad s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2, \qquad s=\sqrt{s^2}` | Define `n`, `x_i`, `\bar{x}`, `s^2`, and `s`. Explain why the median and IQR are also needed for the right-skewed credit-limit and payment variables. |
| 32 | `\hat{p}_g=\frac{1}{n_g}\sum_{i\in g}y_i, \qquad y_i\in\{0,1\}` | `g` is a credit-limit group, `n_g` is the number of borrowers in that group, and `\hat{p}_g` is the observed default share. It is a descriptive comparison, not a causal estimate. |
| 34 | `\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}` | `\rho_{XY}` is Pearson correlation, `\mathrm{Cov}(X,Y)` is covariance, and `\sigma_X,\sigma_Y` are standard deviations. Explain that correlation is a screening tool and does not establish causality or capture every nonlinear relationship. |

Do not add equations to the other slides. Use `\mathrm{Cov}` rather than `\operatorname{Cov}`; the latter is deliberately avoided because the course renderer has rejected `\operatorname` macros before. Keep all braces and delimiters balanced when entering the equations.
