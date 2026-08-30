from data_loader import load_data


def show_basic_analytics():

    df = load_data()

    print("\n========== EXPENSE ANALYTICS ==========")

    total_transactions = len(df)
    total_expense = df["Amount"].sum()
    average_expense = df["Amount"].mean()
    highest_expense = df["Amount"].max()
    lowest_expense = df["Amount"].min()
    total_categories = df["Category"].nunique()

    print(f"Total Transactions : {total_transactions}")
    print(f"Total Expense      : ₹{total_expense:,.2f}")
    print(f"Average Expense    : ₹{average_expense:,.2f}")
    print(f"Highest Expense    : ₹{highest_expense:,.2f}")
    print(f"Lowest Expense     : ₹{lowest_expense:,.2f}")
    print(f"Total Categories   : {total_categories}")


def category_analysis():

    df = load_data()

    print("\n========== CATEGORY-WISE EXPENSE ==========")

    result = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print(result)


def monthly_analysis():

    df = load_data()

    df["Month"] = df["Date"].dt.to_period("M")

    result = (
        df.groupby("Month")["Amount"]
        .sum()
        .sort_index()
    )

    print("\n========== MONTHLY EXPENSE ==========")

    print(result)