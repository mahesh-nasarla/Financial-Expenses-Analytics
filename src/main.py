from add_expense import add_expense
from view_expense import view_expenses

from analytics import (
    show_basic_analytics,
    category_analysis,
    monthly_analysis
)

from reports import (
    expense_summary,
    top_categories,
    highest_expense,
    highest_spending_month,
    business_insights
)

from visualization import (
    category_chart,
    monthly_chart,
    category_pie_chart
)
from eda import (
    basic_eda,
    missing_values,
    duplicate_analysis,
    category_analysis_eda,
    monthly_analysis_eda,
    outlier_analysis,
    complete_eda
)


def menu():

    while True:

        print("\n" + "=" * 55)
        print("       SMART EXPENSE ANALYTICS DASHBOARD")
        print("=" * 55)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. EDA")
        print("4. Analytics")
        print("5. Reports")
        print("6. Charts")
        print("7.Exit")

        print("=" * 55)

        choice = input("Enter your choice (1-7): ")

        # ADD EXPENSE
        if choice == "1":

            add_expense()

        # VIEW EXPENSES
        elif choice == "2":

            view_expenses()

        elif choice == "3":

            while True:

                print("\n========== EXPLORATORY DATA ANALYSIS ==========")
                print("1. Basic EDA")
                print("2. Missing Values")
                print("3. Duplicate Analysis")
                print("4. Category Analysis")
                print("5. Monthly Analysis")
                print("6. Outlier Analysis")
                print("7. Complete EDA")
                print("8. Back")

                eda_choice = input("Enter Choice: ")

                if eda_choice == "1":
                    basic_eda()

                elif eda_choice == "2":
                    missing_values()

                elif eda_choice == "3":
                    duplicate_analysis()

                elif eda_choice == "4":
                    category_analysis_eda()

                elif eda_choice == "5":
                    monthly_analysis_eda()

                elif eda_choice == "6":
                    outlier_analysis()

                elif eda_choice == "7":
                    complete_eda()

                elif eda_choice == "8":
                    break

                else:
                    print("Invalid Choice")

        # ANALYTICS
        elif choice == "4":

            while True:

                print("\n========== ANALYTICS ==========")
                print("1. Basic Analytics")
                print("2. Category Analysis")
                print("3. Monthly Analysis")
                print("4. Back")

                analytics_choice = input("Enter Choice: ")

                if analytics_choice == "1":
                    show_basic_analytics()

                elif analytics_choice == "2":
                    category_analysis()

                elif analytics_choice == "3":
                    monthly_analysis()

                elif analytics_choice == "4":
                    break

                else:
                    print("Invalid Choice")

        # REPORTS
        elif choice == "5":

            while True:

                print("\n========== REPORTS ==========")
                print("1. Expense Summary")
                print("2. Top Spending Categories")
                print("3. Top 5 Expenses")
                print("4. Highest Spending Months")
                print("5. Business Insights")
                print("6. Back")

                report_choice = input("Enter Choice: ")

                if report_choice == "1":
                    expense_summary()

                elif report_choice == "2":
                    top_categories()

                elif report_choice == "3":
                    highest_expense()

                elif report_choice == "4":
                    highest_spending_month()

                elif report_choice == "5":
                    business_insights()

                elif report_choice == "6":
                    break

                else:
                    print("Invalid Choice")

        # CHARTS
        elif choice == "6":

            while True:

                print("\n========== CHARTS ==========")
                print("1. Category-wise Bar Chart")
                print("2. Monthly Expense Line Chart")
                print("3. Category Expense Pie Chart")
                print("4. Back")

                chart_choice = input("Enter Choice: ")

                if chart_choice == "1":
                    category_chart()

                elif chart_choice == "2":
                    monthly_chart()

                elif chart_choice == "3":
                    category_pie_chart()

                elif chart_choice == "4":
                    break

                else:
                    print("Invalid Choice")

        # EXIT
        elif choice == "7":

            print("\nThank you for using Smart Expense Analytics Dashboard!")

            break

        else:

            print("\nInvalid choice! Please enter 1-7.")


if __name__ == "__main__":
    menu()