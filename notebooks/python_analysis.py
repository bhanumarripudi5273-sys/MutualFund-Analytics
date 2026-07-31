# ==========================================
# Python for Data Analysis - Bluestock Internship
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("BLUESTOCK DATA ANALYSIS PROJECT")
print("="*60)

# ------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\nDataset Loaded Successfully!")
print("Shape:", df.shape)

# ------------------------------------------------
# 2. Display Dataset
# ------------------------------------------------

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe(include='all'))

# ------------------------------------------------
# 3. Missing Values
# ------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# ------------------------------------------------
# 4. Remove Duplicate Rows
# ------------------------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)

# ------------------------------------------------
# 5. Data Validation
# ------------------------------------------------

df = df[df["amount_inr"] > 0]

print("\nData Validation Completed")

# ------------------------------------------------
# 6. Convert Date
# ------------------------------------------------

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# ------------------------------------------------
# 7. KPIs
# ------------------------------------------------

print("\n================ KPIs ================\n")

total_transactions = len(df)
print("Total Transactions :", total_transactions)

total_amount = df["amount_inr"].sum()
print("Total Investment Amount :", round(total_amount,2))

average_amount = df["amount_inr"].mean()
print("Average Investment :", round(average_amount,2))

maximum_amount = df["amount_inr"].max()
print("Highest Investment :", round(maximum_amount,2))

minimum_amount = df["amount_inr"].min()
print("Lowest Investment :", round(minimum_amount,2))

unique_investors = df["investor_id"].nunique()
print("Unique Investors :", unique_investors)

# ------------------------------------------------
# 8. Transaction Type Analysis
# ------------------------------------------------

transaction_counts = df["transaction_type"].value_counts()

print("\nTransaction Types")

print(transaction_counts)

# ------------------------------------------------
# 9. KYC Status Analysis
# ------------------------------------------------

print("\nKYC Status")

print(df["kyc_status"].value_counts())

# ------------------------------------------------
# 10. State Wise Transactions
# ------------------------------------------------

state_counts = df["state"].value_counts()

print("\nTop States")

print(state_counts.head())

# ------------------------------------------------
# 11. Save Cleaned Dataset
# ------------------------------------------------

df.to_csv(
    "data/processed/investor_transactions_python_cleaned.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully!")

# ------------------------------------------------
# 12. Visualization 1
# ------------------------------------------------

plt.figure(figsize=(7,5))

transaction_counts.plot(kind="bar")

plt.title("Transaction Type Distribution")

plt.xlabel("Transaction Type")

plt.ylabel("Count")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("reports/transaction_type_bar_chart.png")

plt.show()

# ------------------------------------------------
# 13. Visualization 2
# ------------------------------------------------

plt.figure(figsize=(6,6))

transaction_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Transaction Type Percentage")

plt.tight_layout()

plt.savefig("reports/transaction_type_pie_chart.png")

plt.show()

# ------------------------------------------------
# 14. Visualization 3
# ------------------------------------------------

plt.figure(figsize=(8,5))

state_counts.head(10).plot(kind="bar")

plt.title("Top 10 States by Transactions")

plt.xlabel("State")

plt.ylabel("Transactions")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/top_states_transactions.png")

plt.show()

# ------------------------------------------------
# 15. Basic Statistics
# ------------------------------------------------

print("\n============= BASIC STATISTICS =============")

print("Mean Investment :", round(df["amount_inr"].mean(),2))

print("Median Investment :", round(df["amount_inr"].median(),2))

print("Standard Deviation :", round(df["amount_inr"].std(),2))

print("Variance :", round(df["amount_inr"].var(),2))

# ------------------------------------------------
# 16. Correlation
# ------------------------------------------------

numeric_df = df.select_dtypes(include=np.number)

print("\nCorrelation Matrix")

print(numeric_df.corr())

plt.figure(figsize=(8,6))

plt.imshow(numeric_df.corr(), cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(numeric_df.columns)), numeric_df.columns, rotation=90)

plt.yticks(range(len(numeric_df.columns)), numeric_df.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("reports/correlation_matrix.png")

plt.show()

print("\n=========================================")
print("Python Data Analysis Completed Successfully!")
print("=========================================")