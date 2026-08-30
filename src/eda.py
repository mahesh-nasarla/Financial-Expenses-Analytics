import pandas as pd

FILE_NAME = "../data/expenses.csv"


def load_data():

    df = pd.read_csv(FILE_NAME)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def basic_eda():

    df = load_data()

    print("\n========== BASIC EDA ==========")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nStatistical Summary:")
    print(df.describe())


def missing_values():

    df = load_data()

    print("\n========== MISSING VALUES ==========")

    print(df.isnull().sum())


def duplicate_analysis():

    df = load_data()

    print("\n========== DUPLICATE ANALYSIS ==========")

    print("Duplicate Records:", df.duplicated().sum())


def category_analysis_eda():

    df = load_data()

    print("\n========== CATEGORY ANALYSIS ==========")

    print("Number of Categories:",
          df["Category"].nunique())

    print("\nCategory Frequency:")

    print(df["Category"].value_counts())

    print("\nCategory-wise Total Spending:")

    category_spending = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print(category_spending)


def monthly_analysis_eda():

    df = load_data()

    df["Month"] = df["Date"].dt.to_period("M")

    monthly_spending = (
        df.groupby("Month")["Amount"]
        .sum()
    )

    print("\n========== MONTHLY ANALYSIS ==========")

    print(monthly_spending)


def outlier_analysis():

    df = load_data()

    Q1 = df["Amount"].quantile(0.25)
    Q3 = df["Amount"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df["Amount"] < lower_limit) |
        (df["Amount"] > upper_limit)
    ]

    print("\n========== OUTLIER ANALYSIS ==========")

    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)

    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)

    print("\nNumber of Outliers:",
          len(outliers))

    print("\nTop Outlier Records:")

    print(
        outliers
        .sort_values("Amount", ascending=False)
        .head(10)
    )


def complete_eda():

    basic_eda()

    missing_values()

    duplicate_analysis()

    category_analysis_eda()

    monthly_analysis_eda()

    outlier_analysis()


if __name__ == "__main__":
    complete_eda()