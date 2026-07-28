import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

# Total records
print("\nTotal Records:", len(df))

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Unique Fund Houses
print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

# Unique Categories
print("\nUnique Categories:")
print(df["category"].unique())

# Unique Sub Categories
print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

# Unique Risk Categories
print("\nUnique Risk Categories:")
print(df["risk_category"].unique())

# Count of schemes by category
print("\nScheme Count by Category:")
print(df["category"].value_counts())

# Count of schemes by Fund House
print("\nScheme Count by Fund House:")
print(df["fund_house"].value_counts())