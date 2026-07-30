import pandas as pd
import sqlite3

# Create SQLite database
conn = sqlite3.connect("bluestock_mf.db")

datasets = {
    "nav_history": "data/processed/02_nav_history_cleaned.csv",
    "investor_transactions": "data/processed/08_investor_transactions_cleaned.csv",
    "scheme_performance": "data/processed/07_scheme_performance_cleaned.csv"
}

for table_name, file_path in datasets.items():
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded.")

conn.close()

print("\nSQLite database created successfully!")