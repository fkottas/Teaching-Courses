# Week 4 assignment — documented financial features

## Deadline

Submit one executed Colab notebook **one day before the next course meeting**. The notebook must run from a clean runtime using the canonical UCI download path.

## Required work

1. Load the complete UCI Default of Credit Card Clients dataset and state the observation unit, target, prediction point, and target horizon.
2. Audit data types, duplicates, missing values, zero denominators, target balance, and status-code ranges.
3. Construct at least:
   - one level feature;
   - one ratio feature;
   - one count or severity feature;
   - one change feature;
   - one transformed monetary feature;
   - one interaction feature.
4. Produce at least three labelled plots or grouped summaries. Include counts in every rate comparison.
5. Create a feature dictionary with feature name, formula, raw inputs, unit, timing, missingness policy, and financial interpretation.
6. Demonstrate one leakage failure in a small controlled example and explain why it is invalid.
7. Write a short interpretation for every selected feature. Separate association from causality.

## Analytical questions

- Why is `payment_to_bill_6m` not interchangeable with `utilization`?
- What information is lost when a continuous variable is replaced by a binary flag?
- Why must a rolling feature be computed within the entity and in time order?
- When would a maximum be more appropriate than a count?
- Which feature definitions would change if the prediction point moved one month earlier?

## Grading emphasis

The quality of the explanation matters as much as the code. A feature with a correct Python expression but an unclear timing rule, missingness policy, or unit is incomplete. Do not use the target to define, tune, bin, clip, or select a feature before the validation route.

