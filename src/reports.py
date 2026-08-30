from data_loader import load_data


def expense_summary():
    df = load_data()

    print("\n========== EXPENSE SUMMARY ==========")
    print("Total Transactions:", len(df))
    print("Total Expense:", df["Amount"].sum())
    print("Average Expense:", df["Amount"].mean())


def top_categories():
    df = load_data()

    result = df.groupby("Category")["Amount"].sum()
    result = result.sort_values(ascending=False)

    print("\n========== TOP SPENDING CATEGORIES ==========")
    print(result)


def highest_expense():
    df = load_data()

    result = df.sort_values(
        by="Amount",
        ascending=False
    ).head(5)

    print("\n========== TOP 5 EXPENSES ==========")
    print(result)


def highest_spending_month():
    df = load_data()

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    result = df.groupby("Month")["Amount"].sum()
    result = result.sort_values(ascending=False)

    print("\n========== HIGHEST SPENDING MONTHS ==========")
    print(result.head(5))


def business_insights():
    df = load_data()

    df["Date"] = pd.to_datetime(df["Date"])

    category_data = df.groupby("Category")["Amount"].sum()

    monthly_data = (
        df.groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
    )

    highest_category = category_data.idxmax()
    highest_month = monthly_data.idxmax()

    print("\n========== BUSINESS INSIGHTS ==========")

    print("Highest Spending Category:", highest_category)
    print("Highest Spending Amount:", category_data.max())

    print("Highest Spending Month:", highest_month)
    print("Highest Monthly Amount:", monthly_data.max())

    print("Average Transaction:", df["Amount"].mean())

    print("Total Transactions:", len(df))