import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

# Get unique AMFI codes
master_codes = set(fund_master["amfi_code"])
history_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = master_codes - history_codes

print(f"\nTotal Fund Master Codes : {len(master_codes)}")
print(f"Total NAV History Codes : {len(history_codes)}")

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in NAV History.")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)

print("\nValidation Completed.")