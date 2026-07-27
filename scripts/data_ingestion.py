import pandas as pd
import os

# Folder containing the datasets
data_folder = "data/raw"

# Get all CSV files
csv_files = sorted([file for file in os.listdir(data_folder) if file.endswith(".csv")])

print("=" * 70)
print("BlueStock Internship - Day 1")
print("Data Ingestion Report")
print("=" * 70)

for file in csv_files:
    file_path = os.path.join(data_folder, file)

    print(f"\nReading: {file}")

    try:
        df = pd.read_csv(file_path)

        print(f"Shape: {df.shape}")

        print("\nColumn Data Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

        print("-" * 70)

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\nAll datasets loaded successfully!")