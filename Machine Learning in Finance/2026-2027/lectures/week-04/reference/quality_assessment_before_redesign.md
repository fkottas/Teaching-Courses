# Week 4 presentation — detailed assessment before redesign

Date: 4 November 2026  
Scope: editable PowerPoint deck for Lecture 4, slides 50–70 and the transformation notation used earlier in the deck.

## Assessment method

The deck was checked at four levels:

1. **Teaching logic:** whether a student who has not taken a previous machine-learning course can follow the question, method, calculation, and financial interpretation.
2. **Mathematical communication:** whether the notation is large enough to read, whether every symbol is defined, whether the equation is dimensionally and conceptually correct, and whether a numerical substitution follows it.
3. **Visual hierarchy:** whether the main plot or idea is visually dominant, whether the slide has one clear reading path, and whether repeated cards or dense tables compete with the message.
4. **Editability and evidence:** whether equations, text, tables, charts, and code remain native/editable PowerPoint content and whether external figures are credited.

## Findings

### 1. Feature-selection sequence (slides 50–62)

- The selection objective on slide 50 is correct in spirit but is presented as an abstract optimisation statement before the student has a concrete decision to make. The notation is not accompanied by a small candidate-feature example or an explanation of what changes when the subset changes.
- Slide 51 compresses **filter, wrapper, embedded, and stability** methods into one four-column table. This makes the formula, the tuning parameters, and the numerical example compete for the same visual space. A student cannot easily tell which quantity is calculated from the data, which quantity is a model hyperparameter, and which quantity is an output.
- The formulas are rendered as inline text inside table cells or rounded callouts. They are editable, but they are not presented as mathematics: there is no separation between the equation, symbol definitions, units, and worked substitution.
- The sequence does not consistently answer four questions for each method: **What does it calculate? What parameter controls it? What does the numerical result mean? What can go wrong in financial data?**
- Filter methods need a sharper distinction between a univariate screen and incremental predictive value. Mutual information also needs a clean probability-table calculation; otherwise the student sees a formula without a route to the number.
- Correlation and permutation importance need a clearer treatment of correlated predictors: permuting one variable in a correlated cluster can understate the importance of the whole information set.
- Wrapper methods need a direct explanation of the search path and of why the validation score must be nested inside the search. The current RFECV figure is useful, but the surrounding explanation is too dense.
- Lasso and Elastic Net need a parameter map. In particular, the deck must distinguish `lambda` from scikit-learn’s `C`, explain that `C = 1 / lambda` under the stated convention, and show what `alpha` or `l1_ratio` changes. A single dense penalty equation is not enough.
- Stability selection needs a clean frequency plot or frequency table, followed by the definition of selection frequency and a worked count. The approximation for its standard error must be labelled as a teaching approximation, not as a universal probability that a feature is “true.”

### 2. Mathematical presentation

- Several equations use Unicode approximations inside prose-like blocks rather than a consistent mathematical layout. This is the main readability failure.
- Every mathematical slide should use the following order: **equation → symbols → one numerical substitution → financial interpretation → limitation**.
- The equations must remain native text so they can be edited, but the layout should make them visually behave like equations: larger type, generous line spacing, one equation per area, and no multi-line equation hidden inside a dense table.
- The transformation notation must not suggest that a logarithm equals an addition. The correct notation for the transformation used in code is:

  `log1p(xᵢ) = ln(1 + xᵢ)`, for `xᵢ > −1`.

  It is not `log(xᵢ) = xᵢ + 1`. For non-negative monetary data, `x = 0` maps to `0`, while `x = 99` maps to `ln(100) ≈ 4.605`. The code is `np.log1p(x)`.

### 3. Slide 66 — monthly target rate

- The line chart is the correct analytical object, and the dots and labels are useful. However, the chart is forced to share the slide with two stacked callouts, so the reader must alternate between the plot, the formula, and the jump calculation.
- The target-rate formula, standard-error approximation, denominator, and event interpretation need a single, deliberate reading path.
- The slide should give the chart most of the canvas, annotate the December jump directly, and place a clean mathematical strip below the chart. The count and denominator should sit next to the highlighted jump rather than in a separate card.
- The text must explicitly say that the target rate is observed after labels mature and is not a current model input. That is the key target-driven-event lesson.

### 4. Slide 70 — target monitoring

- The current slide repeats the rounded-box timeline style used elsewhere. The repeated boxes are visually heavy and do not show the operational distinction between input monitoring and target monitoring.
- The replacement should use a flat, two-lane monitoring timeline: one lane for an input variable that can be monitored at receipt and one lane for a target rate that becomes available only after the outcome window. A vertical “label maturity” boundary should make the delay visually explicit.
- The slide should include a small worked example: input distribution in January, target rate in February after the label window, and the corresponding action. This is more useful than four generic labels.

## Redesign decision

The affected section will be rebuilt rather than patched. The new version will:

- use one visual question per slide;
- separate equations from symbol definitions and examples;
- use official scikit-learn figures only where they clarify a method, with source credit;
- use native editable charts, tables, equations, and code for the teaching content;
- make the four selection families comparable through a clean decision map, then teach each family with its own formula and worked example;
- redesign slide 66 as a chart-led target-event slide;
- redesign slide 70 as a two-lane input-versus-target monitoring slide;
- replace ambiguous logarithm notation with `log1p(xᵢ) = ln(1 + xᵢ)` and explain the domain and interpretation.

The slide count will remain 90. Existing slide numbers will be preserved so the instructor’s references remain stable.
