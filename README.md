# Smart Expense Analytics

An end-to-end financial expense analysis project built using Python, Pandas, Matplotlib, and Power BI.

##  Project Overview

Smart Expense Analytics is a Python-based expense management and analytics system designed to transform raw expense transactions into meaningful financial insights.

The application allows users to:

- Add new expense records
- Validate expense inputs
- Store expense data in CSV format
- View and search expense records
- Perform Exploratory Data Analysis (EDA)
- Analyze spending by category
- Analyze monthly spending trends
- Identify potential outliers
- Generate financial reports
- Create data visualizations
- View an interactive Power BI dashboard

The project demonstrates an end-to-end Data Analytics workflow from data collection to business insights.

---

##  Business Objective

The main objective of this project is to understand spending patterns and provide useful financial insights.

The analysis helps answer questions such as:

- How much was spent in total?
- What is the average expense?
- Which category has the highest spending?
- Which months have the highest expenses?
- What are the top 5 expenses?
- Are there any unusual expense transactions?
- How is total spending distributed across categories?

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development and data processing |
| Pandas | Data cleaning, EDA and analysis |
| Matplotlib | Data visualization |
| CSV | Expense data storage |
| Power BI | Interactive dashboard and business reporting |
| GitHub | Version control and project portfolio |

---

##  Project Structure

```text
SmartExpenseAnalytics/
│
├── dashboard/
│   ├── expense_dashboard.png
│   └── Financial Expense Analytics Dashboards.pbix
│
├── data/
│   └── expenses.csv
│
├── src/
│   ├── add_expense.py
│   ├── analytics.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── main.py
│   ├── reports.py
│   ├── view_expense.py
│   └── visualization.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

##  Project Workflow

```text
Expense Data Entry
        ↓
Input Validation
        ↓
CSV Data Storage
        ↓
Data Loading using Pandas
        ↓
Exploratory Data Analysis
        ↓
Expense Analytics
        ↓
Reports & Business Insights
        ↓
Matplotlib Visualizations
        ↓
Power BI Dashboard
        ↓
Financial Decision Support
```

---

#  Python Application

## 1. Add Expense

The application allows users to enter:

- Date
- Category
- Amount
- Description

Input validation is implemented to prevent invalid data.

Validation includes:

- Date must follow YYYY-MM-DD
- Category cannot be empty
- Amount must be greater than zero
- Description cannot be empty

---

## 2. View Expenses

Users can:

- View the first 10 records
- View the last 10 records
- View all records
- Search expenses by category

---

#  Exploratory Data Analysis

The project performs several EDA operations using Pandas.

### Basic EDA

The project checks:

- Dataset shape
- Column names
- Data types
- First few records
- Statistical summary

### Missing Value Analysis

Checks whether any columns contain missing values.

### Duplicate Analysis

Identifies duplicate transaction records.

### Category Analysis

Analyzes:

- Number of categories
- Category frequency
- Total spending by category

### Monthly Analysis

Groups expenses by month to identify spending trends over time.

### Outlier Analysis

The project uses the Interquartile Range (IQR) method to identify potential unusual transactions.

```text
IQR = Q3 - Q1

Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR
```

Transactions outside these limits are considered potential outliers.

---

#  Expense Analytics

The application calculates important financial metrics such as:

- Total Transactions
- Total Expense
- Average Expense
- Highest Expense
- Lowest Expense
- Total Categories

It also performs:

- Category-wise spending analysis
- Monthly spending analysis

---

#  Reports

The project generates reports for:

### Expense Summary

Provides:

- Total transactions
- Total expense
- Average expense

### Top Spending Categories

Ranks categories based on total spending.

### Top 5 Expenses

Identifies the five highest expense transactions.

### Highest Spending Months

Ranks months based on total spending.

### Business Insights

Identifies:

- Highest spending category
- Highest spending amount
- Highest spending month
- Highest monthly spending
- Average transaction value
- Total number of transactions

---

#  Python Visualizations

The project generates three main visualizations using Matplotlib.

### 1. Category-wise Bar Chart

Shows total spending for each category.

### 2. Monthly Expense Trend

Shows how expenses change over time.

### 3. Expense Distribution by Category

Shows the percentage contribution of each category to total spending.

---

#  Power BI Dashboard

The project includes an interactive Power BI dashboard for financial expense analysis.

### Dashboard KPIs

- Average Expense
- Total Transactions
- Total Expenses
- Highest Expense

### Dashboard Visualizations

- Spending by Category
- Top 5 Expenses
- Expense Distribution by Category
- Monthly Expense Trend
- Category Filter
- Year / Quarter Filter

## Dashboard Preview

![Smart Expense Analytics Dashboard](dashboard/expense_dashboard.png)

## Power BI File

The complete Power BI dashboard file is included in:

```text
dashboard/Financial Expense Analytics Dashboards.pbix
```

---

# 💡 Business Insights

The project helps identify:

1. Categories contributing the highest amount of spending.
2. Months with unusually high or low expenses.
3. The largest individual expense transactions.
4. The distribution of total spending across categories.
5. Potential unusual transactions using outlier analysis.

These insights can help users improve budgeting and monitor spending behavior.

---

#  Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Navigate to the Project

```bash
cd SmartExpenseAnalytics
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶ How to Run

Navigate to the `src` directory:

```bash
cd src
```

Run the application:

```bash
python main.py
```

The application displays the main menu:

```text
=======================================================
       SMART EXPENSE ANALYTICS DASHBOARD
=======================================================
1. Add Expense
2. View Expenses
3. EDA
4. Analytics
5. Reports
6. Charts
7. Exit
=======================================================
```

---

#  Skills Demonstrated

This project demonstrates practical knowledge of:

- Python
- Python Functions
- Loops and Conditional Statements
- Exception Handling
- File Handling
- Modular Programming
- Pandas
- DataFrames
- Data Cleaning
- Exploratory Data Analysis
- GroupBy and Aggregation
- DateTime Analysis
- Outlier Detection
- Matplotlib
- Data Visualization
- Power BI
- Business Analysis
- Data Storytelling
- Git and GitHub

---

#  Project Outcome

The project demonstrates an end-to-end Data Analytics workflow:

```text
Raw Data
   ↓
Data Collection
   ↓
Data Validation
   ↓
Data Analysis
   ↓
EDA
   ↓
Visualization
   ↓
Power BI Dashboard
   ↓
Business Insights
```

The final solution converts raw expense transactions into understandable financial information that can support better spending and budgeting decisions.

---

##  Author

**Mahesh Nasarla**

Data Analytics Portfolio Project