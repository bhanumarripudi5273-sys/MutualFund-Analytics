import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Convert transaction_date
# -----------------------------
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# -----------------------------
# Standardize transaction_type
# -----------------------------
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# -----------------------------
# Keep only valid transaction types
# -----------------------------
valid_types = ["Sip", "Lumpsum", "Redemption"]

df = df[df["transaction_type"].isin(valid_types)]

# -----------------------------
# Validate amount > 0
# -----------------------------
df = df[df["amount_inr"] > 0]

# -----------------------------
# Standardize KYC Status
# -----------------------------
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending", "Rejected"]

df = df[df["kyc_status"].isin(valid_kyc)]

# -----------------------------
# Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Investor Transactions Cleaning Completed!")