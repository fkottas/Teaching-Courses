# Lecture 2 mathematics

This page contains the equations for the final Lecture 2 deck. The equations are written as GitHub display mathematics, so they should render as proper formulas on the page.

The PowerPoint deck intentionally contains no equation objects. Add these equations manually to the corresponding slides as editable PowerPoint equations.

Compatibility rule: the formulas use standard fractions, superscripts, subscripts, and delimiters only. Covariance is written with the conventional notation Cov inside the formula.

## Slide 9 — One-period simple return

A simple return compares the price change with the price at the beginning of the period.

```math
r_t = \frac{P_t-P_{t-1}}{P_{t-1}}
```

Here, $P_t$ is the price at the end of the period, $P_{t-1}$ is the price at the beginning, and $r_t$ is the decimal return. Multiply by $100$ only when reporting the return as a percentage.

For the numerical example on the slide:

```math
P_{t-1}=100,\qquad P_t=105
```

```math
r_t=\frac{105-100}{100}=0.05=5\%
```

The code applies the same calculation to every adjacent pair of prices.

## Slide 11 — Weighted portfolio return

For a fully invested portfolio, the return is the weighted sum of the asset returns.

```math
r_{p,t}=\sum_{j=1}^{m}w_jr_{j,t},
\qquad
\sum_{j=1}^{m}w_j=1
```

Here, $r_{p,t}$ is the portfolio return, $w_j$ is the weight of asset $j$, and $r_{j,t}$ is the return of asset $j$. The weights add to one when all available capital is allocated to the assets.

For the numerical example on the slide:

```math
r_{p,t}
=
0.50(0.08)+0.30(0.03)+0.20(0.01)
=
0.051
=
5.10\%
```

The three asset contributions are $0.040$, $0.009$, and $0.002$.

## Slide 19 — Missingness rate

For variable $j$, the missingness rate is the fraction of observations for which that variable is missing.

```math
m_j=\frac{1}{n}\sum_{i=1}^{n}I_{ij}
```

The indicator $I_{ij}$ equals $1$ when $x_{ij}$ is missing and equals $0$ otherwise. Here, $n$ is the number of observations and $x_{ij}$ is the value of variable $j$ for observation $i$.

If 5 of 100 observations are missing:

```math
m_j=\frac{5}{100}=0.05=5\%
```

In the supplied UCI file, the blank-cell rate is zero for the displayed columns. This does not remove the need to interpret coded values and check whether a value is substantively missing.

## Slide 22 — Mean, variance, standard deviation, and IQR

The arithmetic mean is the average of the observed values.

```math
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
```

The sample variance measures average squared distance from the sample mean.

```math
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
```

The sample standard deviation is the square root of the sample variance.

```math
s=\sqrt{s^2}
```

The interquartile range measures the width of the middle 50% of the observations.

```math
\mathrm{IQR}=Q_{0.75}-Q_{0.25}
```

Here, $n$ is the number of observations, $x_i$ is observation $i$, $\bar{x}$ is the sample mean, $s^2$ is the sample variance, and $s$ is the sample standard deviation. The values $Q_{0.25}$ and $Q_{0.75}$ are the first and third quartiles.

Use the mean and standard deviation to describe general scale and dispersion. Also report the median and IQR when a variable is strongly right-skewed, as often happens with credit limits and payment amounts.

## Slide 32 — Default rate within a group

For group $g$, the observed default rate is the number of defaults divided by the number of observations in that group.

```math
\hat{p}_g=\frac{1}{n_g}\sum_{i\in g}y_i,
\qquad
y_i\in\{0,1\}
```

The index $g$ identifies a group, such as a credit-limit band. The value $n_g$ is the number of borrowers in that group. The indicator $y_i$ equals $1$ for default and $0$ for no default. The quantity $\hat{p}_g$ is the observed default share.

For the low-limit group in the slide:

```math
\hat{p}_g\approx 0.2948=29.48\%
```

This is a descriptive sample comparison. It is not a causal effect of credit limit.

## Slide 34 — Pearson correlation

Pearson correlation standardises covariance by the two standard deviations.

```math
\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}
```

Here, $\rho_{XY}$ measures the strength and direction of a linear association, $\mathrm{Cov}(X,Y)$ is the covariance between $X$ and $Y$, and $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$.

When both standard deviations are positive:

```math
-1\leq \rho_{XY}\leq 1
```

A positive value means that larger values of one variable tend to accompany larger values of the other in the sample. A value near zero means that linear association is weak; it does not rule out a nonlinear relationship. Correlation does not establish causality.

## Slides without equations

Do not add equations to the remaining slides. Slides 31 and 33 are visual analysis slides, and the other slides focus on Python operations, data definitions, interpretation, or workflow.

## PowerPoint insertion checklist

1. Open the editable Lecture 2 PowerPoint.
2. Go to the slide number listed above.
3. Insert an editable equation object, not a screenshot.
4. Paste the corresponding formula from this page.
5. Check subscripts, superscripts, fractions, Greek letters, and the percent sign.
6. Keep the explanatory text next to the equation so the notation is defined for students.
