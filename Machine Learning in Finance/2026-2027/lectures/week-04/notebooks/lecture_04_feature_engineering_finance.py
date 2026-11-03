# %% [markdown]
# Machine Learning in Finance — Week 4
# # Feature Engineering for Financial Data
#
# This Colab-first lab uses the real UCI Default of Credit Card Clients data. The objective is to construct financial predictors whose meaning, timing, units, and data-quality policies are explicit.
#
# **Rule:** a feature must be available at the prediction point. The future target is used for descriptive evaluation only, never to define the features.
#
#

# %%
import io
import zipfile
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 60)
pd.set_option('display.float_format', lambda value: f'{value:,.4f}')
plt.style.use('seaborn-v0_8-whitegrid')

SOURCE_URL = 'https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip'
LOCAL_XLS = '/workspace/scratch/ba5b2241db61/week4_build/data/default_of_credit_card_clients.xls'

def load_credit_data():
    """Load the canonical UCI file; use the local path only for the prepared package QA."""
    if Path(LOCAL_XLS).exists():
        frame = pd.read_excel(LOCAL_XLS, header=1)
    else:
        archive = urllib.request.urlopen(SOURCE_URL).read()
        with zipfile.ZipFile(io.BytesIO(archive)) as zf:
            xls_name = next(name for name in zf.namelist() if name.lower().endswith('.xls'))
            frame = pd.read_excel(io.BytesIO(zf.read(xls_name)), header=1)
    return frame.rename(columns={'default payment next month': 'default_next_month'})

credit = load_credit_data()
print(f'Rows: {len(credit):,}; columns: {credit.shape[1]}')
print(f'Default rate: {credit.default_next_month.mean():.2%}')
credit.head(3)


# %% [markdown]
# # 1. Audit the observation unit and the information boundary
#
# One row represents one client at the reporting snapshot. 'default_next_month' is the following-month outcome. It is not an input feature. The six bill, payment, and repayment-status fields are treated as the available lookback history at the snapshot.
#
#

# %%
print('Duplicate IDs:', int(credit.ID.duplicated().sum()))
print('Missing cells:', int(credit.isna().sum().sum()))
print('Target counts:')
print(credit['default_next_month'].value_counts().sort_index())
print('\nStatus ranges:')
print(credit[['PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']].agg(['min', 'max']).T)


# %% [markdown]
# # 2. Construct interpretable features
#
# The code keeps raw columns and appends derived columns. A ratio is not automatically “better” than a level: it expresses a different financial question. The denominator policy is part of the feature definition.
#
#

# %%
status_cols = ['PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']
bill_cols = [f'BILL_AMT{i}' for i in range(1, 7)]
payment_cols = [f'PAY_AMT{i}' for i in range(1, 7)]

credit['utilization'] = credit['BILL_AMT1'].div(credit['LIMIT_BAL'].replace(0, np.nan))
credit['total_bill_6m'] = credit[bill_cols].sum(axis=1)
credit['total_paid_6m'] = credit[payment_cols].sum(axis=1)
credit['payment_to_bill_6m'] = credit['total_paid_6m'].div(
    credit['total_bill_6m'].replace(0, np.nan)
)
credit['overdue_count_6m'] = (credit[status_cols] > 0).sum(axis=1)
credit['max_delay_6m'] = credit[status_cols].max(axis=1)
credit['recent_overdue'] = (credit['PAY_0'] > 0).astype(int)
credit['high_utilization'] = (credit['utilization'] >= 0.80).astype(int)
credit['stress_flag'] = credit['high_utilization'] * credit['recent_overdue']
credit['bill_change_1m'] = credit['BILL_AMT1'] - credit['BILL_AMT2']
credit['payment_change_1m'] = credit['PAY_AMT1'] - credit['PAY_AMT2']
credit['log_limit'] = np.log1p(credit['LIMIT_BAL'])

derived = ['utilization', 'total_bill_6m', 'total_paid_6m', 'payment_to_bill_6m',
           'overdue_count_6m', 'max_delay_6m', 'recent_overdue',
           'high_utilization', 'stress_flag', 'bill_change_1m',
           'payment_change_1m', 'log_limit']
credit[derived].head()


# %% [markdown]
# # 3. Descriptive statistics with denominators
#
# Rates without counts can be misleading. Always show the number of accounts behind a rate, and avoid reading a grouped difference as a causal effect.
#
#

# %%
summary = credit[derived].describe().T[['count', 'mean', 'std', 'min', '50%', 'max']]
summary


# %%
util_bins = [-np.inf, .25, .50, .80, 1.00, np.inf]
util_labels = ['0–25%', '25–50%', '50–80%', '80–100%', '>100%']
credit['utilization_band'] = pd.cut(credit['utilization'], bins=util_bins, labels=util_labels)
utilization_result = credit.groupby('utilization_band', observed=False)['default_next_month'].agg(
    accounts='size', default_rate='mean'
)
utilization_result['default_rate'] = utilization_result['default_rate'].map(lambda value: f'{value:.2%}')
utilization_result


# %% [markdown]
# # 4. Visualise the engineered variables
#
# The first plot asks whether utilisation bands separate observed default rates. The second asks whether a payment-to-bill ratio has a simple monotonic pattern. These are diagnostic plots, not proof of causation or a replacement for out-of-sample evaluation.
#
#

# %%
fig, axes = plt.subplots(1, 2, figsize=(14, 4.5))
utilization_result['default_rate_numeric'] = credit.groupby('utilization_band', observed=False)['default_next_month'].mean()
axes[0].bar(utilization_result.index.astype(str), utilization_result['default_rate_numeric'], color='#159A9C')
axes[0].set_title('Observed default rate by utilisation band')
axes[0].set_ylabel('Default rate')
axes[0].tick_params(axis='x', rotation=25)

pay_bins = [-np.inf, .05, .10, .25, .50, 1.00, np.inf]
pay_labels = ['0–5%', '5–10%', '10–25%', '25–50%', '50–100%', '>100%']
credit['payment_to_bill_band'] = pd.cut(credit['payment_to_bill_6m'], bins=pay_bins, labels=pay_labels)
payment_result = credit.groupby('payment_to_bill_band', observed=False)['default_next_month'].agg(
    accounts='size', default_rate='mean'
)
axes[1].bar(payment_result.index.astype(str), payment_result['default_rate'], color='#D49B32')
axes[1].set_title('Observed default rate by payment-to-bill band')
axes[1].set_ylabel('Default rate')
axes[1].tick_params(axis='x', rotation=25)
plt.tight_layout()
plt.show()


# %% [markdown]
# # 5. Interaction: a combined financial state
#
# An interaction preserves a joint condition. Keep the component variables because the combined state should not hide whether the signal came from utilisation, recency, or both.
#
#

# %%
interaction_result = credit.groupby(['high_utilization', 'recent_overdue'])['default_next_month'].agg(
    accounts='size', default_rate='mean'
).reset_index()
interaction_result['default_rate'] = interaction_result['default_rate'].map(lambda value: f'{value:.2%}')
interaction_result


# %% [markdown]
# # 6. Leakage demonstration
#
# This toy example shows why a random full-sample quantile is not the correct threshold when the threshold is meant to be learned from training data. The safe threshold is estimated from training rows and then applied unchanged to held-out rows.
#
#

# %%
split = int(len(credit) * 0.80)
train = credit.iloc[:split].copy()
test = credit.iloc[split:].copy()
safe_threshold = train['LIMIT_BAL'].quantile(.95)
full_sample_threshold = credit['LIMIT_BAL'].quantile(.95)
print(f'Training-only 95th percentile: {safe_threshold:,.0f}')
print(f'Full-sample 95th percentile:    {full_sample_threshold:,.0f}')
print('The safe threshold is fitted on training rows only.')


# %% [markdown]
# # 7. Export a small derived teaching sample
#
# The repository sample is only for quick inspection. For analysis, use the complete canonical source downloaded above.
#
#

# %%
sample_columns = ['ID', 'LIMIT_BAL', 'PAY_0', 'BILL_AMT1', 'BILL_AMT2',
                  'PAY_AMT1', 'PAY_AMT2', 'default_next_month'] + derived
sample = credit[sample_columns].head(1000)
output_path = Path('credit_feature_engineering_sample.csv')
sample.to_csv(output_path, index=False)
print(f'Wrote {len(sample):,} rows to {output_path}')


# %% [markdown]
# # Submission checklist
#
# - State the observation unit, target, prediction point, and horizon.
# - Document every feature formula, unit, raw input, timing rule, and missingness policy.
# - Show counts with grouped rates.
# - Include at least three plots or grouped summaries.
# - Explain one leakage risk and one safe implementation.
# - Interpret associations carefully; do not claim causality from these descriptive tables.
#
#
