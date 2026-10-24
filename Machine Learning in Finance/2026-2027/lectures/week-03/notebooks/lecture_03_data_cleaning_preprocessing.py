"""Week 3 — data cleaning and leakage-safe preprocessing.

Run in Spyder or a local Python environment. The Colab notebook contains the
same workflow with explanatory markdown and visible outputs.
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_URL = (
    "https://raw.githubusercontent.com/fkottas/Teaching-Courses/main/"
    "Machine%20Learning%20in%20Finance/2026-2027/lectures/lecture-00-01/"
    "data/credit/default_of_credit_card_clients.csv.gz"
)


def make_encoder():
    """Support current scikit-learn and older Colab releases."""
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


def main():
    credit = pd.read_csv(DATA_URL, compression="gzip")
    credit = credit.rename(columns={
        "default payment next month": "default_next_month",
    })
    print("shape:", credit.shape)
    print(credit.head(3))

    audit = pd.DataFrame(
        {
            "dtype": credit.dtypes.astype(str),
            "missing": credit.isna().sum(),
            "unique": credit.nunique(),
        }
    )
    print("\naudit:")
    print(audit.head(10))
    print("exact duplicate rows:", int(credit.duplicated().sum()))
    print("unique IDs:", int(credit["ID"].nunique()))
    print("target counts:")
    print(credit["default_next_month"].value_counts().sort_index())

    # Controlled example: the source file has no blank cells.
    demo = credit[["LIMIT_BAL", "AGE", "EDUCATION", "MARRIAGE"]].head(8).copy()
    demo.loc[[1, 4], "AGE"] = np.nan
    demo.loc[[2], "EDUCATION"] = np.nan
    missing_rate = demo.isna().mean()
    demo["AGE_was_missing"] = demo["AGE"].isna().astype(int)
    demo["AGE"] = demo["AGE"].fillna(demo["AGE"].median())
    print("\ncontrolled missingness rate:")
    print(missing_rate)
    print(demo[["AGE", "AGE_was_missing"]])

    # Controlled duplicate example.
    duplicate_demo = pd.concat([credit.head(5), credit.head(1)], ignore_index=True)
    print("\ncontrolled duplicate count:", int(duplicate_demo.duplicated().sum()))

    # Worked case A: imputation plus an indicator.
    case_a = pd.DataFrame(
        {
            "borrower": ["A", "B", "C", "D", "E"],
            "income": [42000.0, np.nan, 58000.0, np.nan, 72000.0],
        }
    )
    case_a["income_was_missing"] = case_a["income"].isna().astype(int)
    median_income = case_a["income"].median()
    case_a["income"] = case_a["income"].fillna(median_income)
    print("\nworked case A median income:", median_income)
    print(case_a.to_string(index=False))

    # Worked case B: exact row and repeated identifier checks.
    transactions = pd.DataFrame(
        {
            "transaction_id": [101, 102, 102, 103],
            "amount": [120, 75, 75, 240],
            "merchant": ["A", "B", "B", "C"],
        }
    )
    print("\nworked case B exact rows:", int(transactions.duplicated().sum()))
    print("worked case B repeated IDs:", int(transactions["transaction_id"].duplicated().sum()))

    # Worked case C: an IQR flag creates a review list.
    payments = pd.DataFrame({"amount": [800, 950, 1100, 1300, 1500, 1600, 180000]})
    q1 = payments["amount"].quantile(0.25)
    q3 = payments["amount"].quantile(0.75)
    upper_fence = q3 + 1.5 * (q3 - q1)
    payments["outlier_flag"] = payments["amount"] > upper_fence
    print("\nworked case C upper fence:", upper_fence)
    print("worked case C flagged rows:", int(payments["outlier_flag"].sum()))

    # Worked case D: an unseen category is handled without changing the layout.
    encoder = make_encoder()
    encoder.fit(pd.DataFrame({"channel": ["branch", "web"]}))
    print("\nworked case D feature names:", encoder.get_feature_names_out().tolist())
    print("worked case D mobile:", encoder.transform(pd.DataFrame({"channel": ["mobile"]})).tolist())

    # Worked case E: fitting on all rows leaks future information.
    train_demo = np.array([10.0, 20.0, 30.0])
    test_demo = np.array([1000.0])
    print("\nworked case E full-sample mean:", np.concatenate([train_demo, test_demo]).mean())
    print("worked case E training-only mean:", train_demo.mean())

    # Documented percentile flag: flag for review; do not delete automatically.
    lower, upper = credit["LIMIT_BAL"].quantile([0.01, 0.99])
    limit_flag = ~credit["LIMIT_BAL"].between(lower, upper)
    print("\nLIMIT_BAL 1%-99% thresholds:", lower, upper)
    print("flagged rows:", int(limit_flag.sum()))

    num_cols = ["LIMIT_BAL", "AGE", "PAY_0", "BILL_AMT1", "PAY_AMT1"]
    cat_cols = ["SEX", "EDUCATION", "MARRIAGE"]
    X = credit[num_cols + cat_cols]
    y = credit["default_next_month"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    numeric_pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]
    )
    categorical_pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", make_encoder()),
        ]
    )
    preprocessor = ColumnTransformer(
        [
            ("num", numeric_pipe, num_cols),
            ("cat", categorical_pipe, cat_cols),
        ]
    )
    X_train_ready = preprocessor.fit_transform(X_train)
    X_test_ready = preprocessor.transform(X_test)
    print("\ntransformed shapes:", X_train_ready.shape, X_test_ready.shape)
    print("feature names:")
    print(preprocessor.get_feature_names_out().tolist())
    print("training target rate:", y_train.mean())
    print("test target rate:", y_test.mean())


if __name__ == "__main__":
    main()

