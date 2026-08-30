import pandas as pd

FILE_NAME = "../data/expenses.csv"


def view_expenses():

    try:
        df = pd.read_csv(FILE_NAME)

        while True:

            print("\n========== VIEW EXPENSES ==========")
            print("1. View First 10 Records")
            print("2. View Last 10 Records")
            print("3. View All Records")
            print("4. Search by Category")
            print("5. Back")

            choice = input("Enter Choice: ")

            if choice == "1":
                print(df.head(10))

            elif choice == "2":
                print(df.tail(10))

            elif choice == "3":
                print(df)

            elif choice == "4":

                category = input("Enter Category: ")

                result = df[df["Category"].str.lower() == category.lower()]

                if result.empty:
                    print("No Records Found")

                else:
                    print(result)

            elif choice == "5":
                break

            else:
                print("Invalid Choice")

    except FileNotFoundError:
        print("Expense file not found.")