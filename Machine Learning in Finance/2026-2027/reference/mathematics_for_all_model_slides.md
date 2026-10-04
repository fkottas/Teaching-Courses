# Exact mathematics for the supervised-learning model lectures

Use display-math blocks exactly as written below. On GitHub, the `$$` delimiters render the equations as mathematics. On a presentation slide, pair each equation with symbol definitions, one numerical example, and a financial interpretation.

## Logistic regression

$$
p_i=P(Y_i=1\mid\mathbf{x}_i)=\sigma(\eta_i)=\frac{1}{1+e^{-\eta_i}},\qquad
\eta_i=\beta_0+\mathbf{x}_i^{\top}\boldsymbol{\beta}.
$$

## Logistic log-likelihood and log-loss

$$
\ell(\boldsymbol{\beta})=\sum_{i=1}^{n}\left[y_i\log(p_i)+(1-y_i)\log(1-p_i)\right].
$$

$$
\mathrm{LogLoss}=-\frac{1}{n}\sum_{i=1}^{n}\left[y_i\log(p_i)+(1-y_i)\log(1-p_i)\right].
$$

## Elastic-Net regularisation

$$
\min_{\beta_0,\boldsymbol{\beta}}
\{ -\ell(\beta_0,\boldsymbol{\beta})
+\lambda[\alpha\lVert\boldsymbol{\beta}\rVert_1
+(1-\alpha)\frac{1}{2}\lVert\boldsymbol{\beta}\rVert_2^2]\}.
$$

## Decision-tree impurity

$$
G(t)=1-\sum_{k=1}^{K}p_{k\mid t}^{2},\qquad H(t)=-\sum_{k=1}^{K}p_{k\mid t}\log(p_{k\mid t}).
$$

## Cross-validation estimate

$$
\widehat{R}_{\mathrm{CV}}=\frac{1}{K}\sum_{k=1}^{K}\frac{1}{|I_k|}\sum_{i\in I_k}L\left(y_i,\widehat{f}^{(-k)}(\mathbf{x}_i)\right).
$$

## Gradient boosting

$$
F_m(\mathbf{x})=F_{m-1}(\mathbf{x})+\nu h_m(\mathbf{x}),\qquad 0<\nu\le1.
$$

## Support-vector machine

$$
\min_{\mathbf{w},b,\boldsymbol{\xi}}\frac{1}{2}\lVert\mathbf{w}\rVert_2^2+C\sum_{i=1}^{n}\xi_i
$$

subject to

$$
y_i(\mathbf{w}^{\top}\mathbf{x}_i+b)\ge1-\xi_i,\qquad \xi_i\ge0.
$$

## Calibration

$$
\mathrm{ECE}=\sum_{m=1}^{M}\frac{|B_m|}{n}\left|\mathrm{acc}(B_m)-\mathrm{conf}(B_m)\right|.
$$

## Neural-network forward pass

$$
\mathbf{h}^{(1)}=\phi\left(W^{(1)}\mathbf{x}+\mathbf{b}^{(1)}\right),\qquad
\widehat{y}=\sigma\left(W^{(2)}\mathbf{h}^{(1)}+b^{(2)}\right).
$$

## Financial evaluation

$$
W_T=W_0\prod_{t=1}^{T}(1+R_t),\qquad
\mathrm{Sharpe}=\frac{\overline{R}-R_f}{s_R}\sqrt{m}.
$$

State the return frequency, annualisation factor `m`, and risk-free-rate assumption whenever the Sharpe ratio is used.
