# Lecture 2 mathematics: manual insertion guide

The PPTX deliberately contains no equations. Add the following equations manually as editable PowerPoint equation objects. The slide numbers refer to the final 51-slide Lecture 2 deck.

Use the equation exactly as written. Do not use `\operatorname`, `\left`, or `\right`; the course renderer has rejected those macros or delimiters before. `\mathrm{Cov}` is used instead of `\operatorname{Cov}`.

## Slide 9 — One-period simple return

Insert:

```text
r_t = \frac{P_t-P_{t-1}}{P_{t-1}}
```

Explain:

- `P_t` is the price at the end of the period.
- `P_{t-1}` is the price at the beginning of the period.
- `r_t` is a decimal return. Multiply by 100 only when presenting it as a percentage.

Numerical check for the code on the slide:

```text
P_{t-1}=100, \quad P_t=105
\quad\Longrightarrow\quad
r_t=\frac{105-100}{100}=0.05=5\%
```

The code applies this calculation to every adjacent pair of prices.

## Slide 11 — Weighted portfolio return

Insert:

```text
r_{p,t}=\sum_{j=1}^{m}w_jr_{j,t},
\qquad
\sum_{j=1}^{m}w_j=1
```

Explain:

- `r_{p,t}` is the portfolio return.
- `w_j` is the weight of asset `j`.
- `r_{j,t}` is the return of asset `j`.
- The weights add to one when the portfolio is fully invested.

Numerical check for the code on the slide:

```text
r_{p,t}=0.50(0.08)+0.30(0.03)+0.20(0.01)=0.051=5.10\%
```

The three contributions are `0.040`, `0.009`, and `0.002`.

## Slide 19 — Missingness rate

Insert:

```text
m_j=\frac{1}{n}\sum_{i=1}^{n}I_{ij}
```

Then define the indicator in ordinary text below the equation:

```text
I_{ij}=1 \text{ when } x_{ij} \text{ is missing, and } I_{ij}=0 \text{ otherwise.}
```

Explain:

- `m_j` is the fraction of observations missing in variable `j`.
- `n` is the number of observations.
- `x_{ij}` is the value of variable `j` for observation `i`.

If 5 of 100 observations are missing, then `m_j=5/100=0.05`, or 5%. In the supplied UCI file, the blank-cell rate is zero for all displayed columns. That does not remove the need to interpret coded values.

## Slide 22 — Mean, variance, standard deviation, and IQR

Insert the following three equations:

```text
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
```

```text
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
```

```text
s=\sqrt{s^2}
```

If you refer to the IQR on the slide, also insert:

```text
\mathrm{IQR}=Q_{0.75}-Q_{0.25}
```

Explain:

- `n` is the number of observations.
- `x_i` is observation `i`.
- `\bar{x}` is the arithmetic mean.
- `s^2` is the sample variance and `s` is the sample standard deviation.
- `Q_{0.25}` and `Q_{0.75}` are the first and third quartiles.

Use the mean and standard deviation for general scale and dispersion. Use the median and IQR as well when the variable is strongly right-skewed, as with credit limits and payment amounts.

## Slide 32 — Default rate within a group

Insert:

```text
\hat{p}_g=\frac{1}{n_g}\sum_{i\in g}y_i,
\qquad
y_i\in\{0,1\}
```

Explain:

- `g` identifies a group, such as a credit-limit band.
- `n_g` is the number of borrowers in group `g`.
- `y_i=1` means default and `y_i=0` means no default.
- `\hat{p}_g` is the observed default share in that group.

For the low-limit group, the displayed value is approximately `0.2948`, or 29.48%. This is a descriptive sample comparison. It is not a causal effect of credit limit.

## Slide 34 — Pearson correlation

Insert:

```text
\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}
```

Explain:

- `\rho_{XY}` measures the strength and direction of a linear association.
- `\mathrm{Cov}(X,Y)` is the covariance between `X` and `Y`.
- `\sigma_X` and `\sigma_Y` are the standard deviations of `X` and `Y`.
- The value lies between `-1` and `1` when both standard deviations are positive.

Interpretation:

- A positive value means that larger values of one variable tend to accompany larger values of the other in the sample.
- A value near zero means that linear association is weak. It does not rule out a nonlinear relationship.
- Correlation does not establish causality.

## Slides without equations

Do not add equations to the remaining slides. Slides 31 and 33 use plots, while the other slides focus on Python operations, data definitions, interpretation, or workflow.
