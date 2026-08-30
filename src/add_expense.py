import csv
import os
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
FILE_NAME = BASE_DIR / "data" / "expenses.csv"


def add_expense():

    print("\n========== ADD EXPENSE ==========")

    # DATE VALIDATION
    while True:
        date = input("Enter Date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    # CATEGORY VALIDATION
    while True:
        category = input("Enter Category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # AMOUNT VALIDATION
    while True:
        try:
            amount = float(input("Enter Amount: "))

            if amount > 0:
                break

            print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # DESCRIPTION VALIDATION
    while True:
        description = input("Enter Description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Date", "Category", "Amount", "Description"]
            )

        writer.writerow(
            [date, category, amount, description]
        )

    print("\nExpense Added Successfully!")