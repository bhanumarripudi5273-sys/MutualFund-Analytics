import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Convert return columns to numeric
# -----------------------------
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Remove rows with missing returns
# -----------------------------
df = df.dropna(subset=return_cols)

# -----------------------------
# Validate expense ratio
# -----------------------------
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# -----------------------------
# Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Save cleaned dataset
# -----------------------------
import os

output_path = "data/processed/07_scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print("Cleaned Shape:", df.shape)
print("Saved to:", os.path.abspath(output_path))
print("Scheme Performance Cleaning Completed!")