import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Convert date column
# -----------------------------
df["date"] = pd.to_datetime(df["date"])

# -----------------------------
# 2. Sort by AMFI code and Date
# -----------------------------
df = df.sort_values(
    by=["amfi_code", "date"]
)

# -----------------------------
# 3. Remove duplicate rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# 4. Forward-fill missing NAV
# -----------------------------
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# -----------------------------
# 5. Keep only valid NAV values
# -----------------------------
df = df[df["nav"] > 0]

# -----------------------------
# 6. Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)

print("Cleaning Completed Successfully!")