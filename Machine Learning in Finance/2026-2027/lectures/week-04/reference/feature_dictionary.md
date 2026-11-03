# Week 4 feature dictionary

| Feature | Formula / construction | Unit | Raw inputs | Missing / zero policy | Timing |
|---|---|---|---|---|---|
| `utilization` | `BILL_AMT1 / LIMIT_BAL` | ratio | `BILL_AMT1`, `LIMIT_BAL` | `LIMIT_BAL == 0` becomes missing | Snapshot |
| `total_bill_6m` | `Σ BILL_AMT1:BILL_AMT6` | currency units | six bill fields | sum of available source fields in this teaching table | Lookback through snapshot |
| `total_paid_6m` | `Σ PAY_AMT1:PAY_AMT6` | currency units | six payment fields | sum of available source fields in this teaching table | Lookback through snapshot |
| `payment_to_bill_6m` | `total_paid_6m / total_bill_6m` | ratio | two totals | zero bill total becomes missing | Lookback through snapshot |
| `overdue_count_6m` | `Σ 1(PAY_status > 0)` | count, 0–6 | `PAY_0`, `PAY_2`–`PAY_6` | status fields are required for the count | Lookback |
| `max_delay_6m` | `max(PAY_status)` | ordered status code | six status fields | status-code meaning must be retained | Lookback |
| `recent_overdue` | `1(PAY_0 > 0)` | binary | `PAY_0` | no missing status in the teaching path | Snapshot |
| `high_utilization` | `1(utilization ≥ 0.80)` | binary | `utilization` | missing utilization maps to 0 only after explicit review | Snapshot |
| `stress_flag` | `high_utilization × recent_overdue` | binary | two indicators | components retained for auditability | Snapshot |
| `bill_change_1m` | `BILL_AMT1 − BILL_AMT2` | currency units | two bill fields | source missingness is preserved | Recent change |
| `payment_change_1m` | `PAY_AMT1 − PAY_AMT2` | currency units | two payment fields | source missingness is preserved | Recent change |
| `log_limit` | `log(1 + LIMIT_BAL)` | transformed currency scale | `LIMIT_BAL` | requires non-negative source amount | Snapshot |

The target `default_next_month` is documented but is excluded from every feature formula.

