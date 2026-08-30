import matplotlib.pyplot as plt
from data_loader import load_data


def category_chart():

    df = load_data()

    category_expense = df.groupby("Category")["Amount"].sum()
    category_expense = category_expense.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))

    category_expense.plot(kind="bar")

    plt.title("Category-wise Expense")
    plt.xlabel("Category")
    plt.ylabel("Total Expense")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def monthly_chart():

    df = load_data()

    df["Month"] = df["Date"].dt.to_period("M")

    monthly_expense = df.groupby("Month")["Amount"].sum()

    plt.figure(figsize=(10, 6))

    monthly_expense.plot(kind="line", marker="o")

    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def category_pie_chart():

    df = load_data()

    category_expense = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 8))

    category_expense.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution by Category")

    plt.ylabel("")

    plt.show()