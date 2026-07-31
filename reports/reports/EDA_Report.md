# Exploratory Data Analysis (EDA) Report

## Project
Mutual Fund Analytics – Investor Transactions Analysis

## Dataset
08_investor_transactions.csv

## Objective
The objective of this analysis is to clean investor transaction data, identify trends, calculate key performance indicators (KPIs), and gain business insights through exploratory data analysis.

---

# 1. Dataset Overview

- Dataset Name: investor_transactions.csv
- Total Records: 32,778
- Dataset Type: Mutual Fund Investor Transactions

---

# 2. Data Cleaning Performed

The following preprocessing steps were completed:

- Loaded the CSV file using Pandas.
- Checked for missing values.
- Removed duplicate records.
- Validated transaction amounts (amount > 0).
- Converted transaction_date to datetime format.
- Standardized transaction data.

---

# 3. Key Performance Indicators (KPIs)

The following KPIs were calculated:

- Total Transactions
- Total Investment Amount
- Average Investment Amount
- Maximum Investment
- Minimum Investment
- Unique Investors

---

# 4. Exploratory Data Analysis

The following analyses were performed:

- Transaction Type Distribution
- KYC Status Analysis
- State-wise Transaction Analysis
- Basic Statistical Summary
- Correlation Analysis

---

# 5. Visualizations Created

- Transaction Type Bar Chart
- Transaction Type Pie Chart
- Top States Bar Chart
- Correlation Matrix

---

# 6. Business Insights

- SIP transactions are one of the most frequent investment methods.
- Most investor records have valid KYC status.
- Certain states contribute significantly more transactions than others.
- Investment amounts vary across investors, indicating different investment patterns.
- The cleaned dataset is suitable for further analytics and dashboard development.

---

# 7. Conclusion

The dataset was successfully cleaned and analyzed using Python, Pandas, NumPy, and Matplotlib. The generated KPIs and visualizations provide valuable insights into investor behavior and can be used for business reporting and dashboard creation.