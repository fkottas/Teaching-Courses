# Mathematics to insert — Week 3

The presentation intentionally keeps equations in this separate reference so that the deck remains editable and the equations can be reviewed before insertion. The blocks below use standard LaTeX without `\operatorname`, `\left`, `\right`, or unmatched delimiters.

## Slide 13 — Missingness rate

Use this equation after the code that creates `missing_rate`:

```math
m_j = \frac{1}{n} \sum_{i=1}^{n} I(x_{ij}\text{ is missing})
```

Here, `m_j` is the missingness rate for variable `j`, `n` is the number of observations, and `I(·)` equals 1 when the stated condition is true and 0 otherwise. The formula describes the audit; it does not decide whether to impute or remove a value.

## Slide 20 — Interquartile range

Use this equation when introducing an outlier rule:

```math
IQR = Q_{0.75} - Q_{0.25}
```

`Q_{0.25}` and `Q_{0.75}` are the first and third quartiles. The interquartile range measures the spread of the central 50% of observations and is less affected by extreme values than the minimum and maximum.

## Slide 22 — IQR fences

If the IQR rule is used in the notebook, insert:

```math
L = Q_{0.25} - 1.5 IQR, \qquad U = Q_{0.75} + 1.5 IQR
```

An observation below `L` or above `U` is flagged by this rule. A flag is a prompt for review, not proof that the observation is invalid. The presentation’s visible `LIMIT_BAL` example uses the 1st and 99th percentiles, so do not label that chart as an IQR rule.

## Slide 32 — Standardisation

Insert the following equation in the scaling concept slide:

```math
z_{ij} = \frac{x_{ij} - \mu_{j,\mathrm{train}}}{\sigma_{j,\mathrm{train}}}
```

For variable `j` and observation `i`, `x_{ij}` is the original value, `\mu_{j,\mathrm{train}}` is the training-sample mean, and `\sigma_{j,\mathrm{train}}` is the training-sample standard deviation. The subscript `train` is essential: the test sample must not determine either parameter.

## Slide 29 — One-hot representation

Use this definition beside the category table:

```math
d_{ik} = I(c_i = k)
```

`d_{ik}` is the indicator for observation `i` belonging to category `k`; it equals 1 when the category matches and 0 otherwise. One-hot encoding avoids treating category labels such as 1, 2, and 3 as equally spaced numerical measurements.

## Slide 39 — Stratified split

Use this compact definition when discussing target proportions:

```math
\widehat{p}_{\mathrm{train}} = \frac{1}{n_{\mathrm{train}}} \sum_{i \in \mathrm{train}} y_i, \qquad
\widehat{p}_{\mathrm{test}} = \frac{1}{n_{\mathrm{test}}} \sum_{i \in \mathrm{test}} y_i
```

With stratification, the two estimated default proportions are designed to be similar. This is a sampling property, not evidence that the model performs well.

## Slide 42 — Pipeline as a composition

Use this equation to explain that preprocessing is an ordered function:

```math
T(x) = T_{\mathrm{cat}}(x_{\mathrm{cat}}) \oplus T_{\mathrm{num}}(x_{\mathrm{num}})
```

`T_num` is the numeric pipeline, `T_cat` is the categorical pipeline, and `⊕` denotes concatenation of the resulting feature blocks. Fitting the two transformations on the training data and reusing them later makes the operation reproducible.

## Final review checklist

- Keep every equation in a math-capable text box or in the lecture reference, not as a screenshot.
- Render each equation before publishing and check subscripts, superscripts, Greek letters, minus signs, and delimiters.
- Do not use `\operatorname`, `\left`, or `\right` in the GitHub math guide because they have caused rendering failures in this repository.
- The mathematical notation must agree with the code: the notebook uses training-only imputation and scaling, and the visible outlier chart uses percentile thresholds.

