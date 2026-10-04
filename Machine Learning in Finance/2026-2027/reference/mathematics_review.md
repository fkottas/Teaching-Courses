# Mathematics reference — Lecture 0 + Lecture 1

This page uses GitHub-compatible display mathematics. Each equation is followed by the meaning of its symbols and a financial interpretation.

| Slide | Topic | Where to study |
|---:|---|---|
| 71 | Arithmetic mean | [Equation and interpretation](#slide-71--arithmetic-mean) |
| 72 | Median | [Equation and interpretation](#slide-72--median) |
| 73 | Sample variance and standard deviation | [Equation and interpretation](#slide-73--sample-variance-and-standard-deviation) |
| 74 | Z-score | [Equation and interpretation](#slide-74--z-score) |
| 75 | Simple and log returns | [Equation and interpretation](#slide-75--simple-and-log-returns) |
| 78 | Correlation | [Equation and interpretation](#slide-78--correlation) |

## Slide 71 — Arithmetic mean

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
$$

Here, $x_i$ is observation $i$ and $n$ is the number of observations. Every observation receives equal weight. For a financial price sample, the mean summarises the centre of the observed prices; it does not describe every trading day.

## Slide 72 — Median

First order the observations from smallest to largest.

$$
\tilde{x}=
\begin{cases}
x_{\left(\frac{n+1}{2}\right)}, & n\text{ odd},\\
\frac{x_{\left(\frac{n}{2}\right)}+x_{\left(\frac{n}{2}+1\right)}}{2}, & n\text{ even}.
\end{cases}
$$

The median is the middle ordered observation. When $n$ is even, it is the average of the two middle observations. It is often more representative than the mean when financial values are skewed or contain extreme observations.

## Slide 73 — Sample variance and standard deviation

$$
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2,
\qquad
s=\sqrt{s^2}
$$

The sample variance measures squared dispersion around the sample mean, and the standard deviation returns the measure to the original units.

## Slide 74 — Z-score

$$
z_i=\frac{x_i-\bar{x}}{s}
$$

The z-score measures how many sample standard deviations observation $i$ lies above or below the sample mean.

## Slide 75 — Simple and log returns

$$
R_t=\frac{P_t-P_{t-1}}{P_{t-1}},
\qquad
r_t=\ln\left(\frac{P_t}{P_{t-1}}\right)
$$

$P_t$ is the price at time $t$. $R_t$ is the simple return, while $r_t$ is the continuously compounded log return. The code must state which return definition is being used.

## Slide 78 — Correlation

$$
\mathrm{Corr}(X,Y)=\frac{\mathrm{Cov}(X,Y)}{s_Xs_Y}
$$

Correlation is unit-free and measures linear co-movement. It lies between $-1$ and $1$ when both standard deviations are positive. A high correlation is descriptive and does not establish causality.

## Presentation integrity note

Slides 71 and 72 retain the rendered equations. The unwanted background on the arithmetic-mean slide was removed without deleting the equation, and the median expression contains no extra closing parenthesis.