# Exploratory Data Analysis (EDA) Report

## Project
Mutual Fund Analytics – Investor Transactions Analysis

## Dataset
08_investor_transactions.csv

## Objective
The objective of this analysis is to clean investor transaction data, identify trends, calculate key performance indicators (KPIs), and generate business insights through exploratory data analysis. The cleaned dataset is prepared for SQL analysis, Power BI dashboards, and further business intelligence reporting.

---

# 1. Dataset Overview

- **Dataset Name:** 08_investor_transactions.csv
- **Dataset Type:** Mutual Fund Investor Transactions
- **Total Records:** 32,778
- **Purpose:** Analyze investor transactions, investment patterns, KYC status, and regional distribution of investments.

---

# 2. Data Cleaning Performed

The following preprocessing steps were completed using Python and Pandas:

- Loaded the CSV dataset.
- Checked for missing values in all columns.
- Removed duplicate records.
- Converted `transaction_date` into datetime format.
- Standardized transaction type values.
- Validated investment amounts (`amount_inr > 0`).
- Verified KYC status values.
- Ensured data consistency before analysis.

---

# 3. Key Performance Indicators (KPIs)

The following KPIs were calculated:

- Total Transactions
- Total Investment Amount
- Average Investment Amount
- Maximum Investment Amount
- Minimum Investment Amount
- Total Unique Investors

These KPIs provide an overall understanding of investor activity and business performance.

---

# 4. Exploratory Data Analysis

The following analyses were performed:

- Transaction Type Distribution
- KYC Status Analysis
- State-wise Investment Analysis
- Basic Statistical Analysis
- Correlation Analysis
- Investment Trend Analysis

These analyses help identify investment behavior, customer distribution, and business trends.

---

# 5. Outlier Detection

Outlier detection was performed on the `amount_inr` column to identify unusually high or low investment values.

### Observations

- No invalid negative investment amounts were found.
- A few high-value investment transactions were identified.
- These transactions were retained because they may represent genuine large investments.
- Statistical summaries and distribution analysis were used to inspect potential outliers.

---

# 6. Basic Statistics

The following statistical measures were calculated:

- Mean Investment Amount
- Median Investment Amount
- Mode of Transaction Type
- Standard Deviation of Investment Amount
- Minimum Investment Amount
- Maximum Investment Amount

These statistics provide insights into the central tendency and variability of investor transactions.

---

# 7. Correlation Analysis

Correlation analysis was performed on numerical columns to understand relationships between variables.

### Findings

- Numerical columns showed weak to moderate correlations.
- Correlation analysis helps identify dependencies between investment-related variables.
- A correlation matrix was generated for visualization.

---

# 8. Trend Analysis

Trend analysis was performed using transaction dates.

### Observations

- Investment activity varied across different months.
- Some periods recorded higher transaction volumes than others.
- Monthly trends help understand investor behavior over time.

---

# 9. Visualizations Created

The following visualizations were generated using Matplotlib:

- Transaction Type Bar Chart
- Transaction Type Pie Chart
- Top States by Transactions
- Correlation Matrix

These charts provide a visual representation of investor activity and business performance.

---

# 10. Business Insights

The analysis produced the following key insights:

- SIP transactions are one of the most frequently used investment methods.
- Most investors have completed KYC verification.
- Certain states contribute significantly more investment transactions than others.
- Investment amounts vary across investors, indicating diverse investment patterns.
- The cleaned dataset is suitable for SQL analysis, Power BI dashboards, and advanced analytics.

---

# 11. Conclusion

The investor transactions dataset was successfully cleaned, validated, and analyzed using Python, Pandas, NumPy, and Matplotlib. Missing values, duplicate records, data validation checks, outlier detection, correlation analysis, and trend analysis were completed successfully. Key performance indicators and business insights were generated, and multiple visualizations were created. The processed dataset is now ready for SQL querying, Power BI dashboard development, and future predictive analytics projects.