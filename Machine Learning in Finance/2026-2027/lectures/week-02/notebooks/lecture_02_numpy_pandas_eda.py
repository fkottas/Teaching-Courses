"""Lecture 2: NumPy, Pandas, and EDA."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
DATA_URL = 'https://raw.githubusercontent.com/fkottas/Teaching-Courses/main/Machine%20Learning%20in%20Finance/2026-2027/lectures/lecture-00-01/data/credit/default_of_credit_card_clients.csv.gz'
credit = pd.read_csv(DATA_URL, compression='gzip').rename(columns={"default payment next month": "default_next_month"})
print(credit.shape)
print(credit.isna().sum().sum())
print(credit["default_next_month"].value_counts())
credit["limit_band"] = pd.cut(credit["LIMIT_BAL"], bins=[-np.inf, 100000, 300000, np.inf], labels=["low", "medium", "high"])
by_band = credit.groupby("limit_band", observed=False).agg(borrowers=("ID", "size"), default_rate=("default_next_month", "mean"), median_age=("AGE", "median")).round(4)
print(by_band)
by_band["default_rate"].plot(kind="bar", color="#2D9DB0")
plt.title("Default rate by credit-limit band")
plt.ylabel("Share of borrowers")
plt.tight_layout()
plt.show()
