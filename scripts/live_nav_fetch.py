import requests
import pandas as pd
import os

# Folder to save NAV files
output_folder = "data/raw"

# AMFI Scheme Codes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 60)
print("Fetching Live NAV Data")
print("=" * 60)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for fund_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            json_data = response.json()

            if "data" in json_data:
                df = pd.DataFrame(json_data["data"])

                filename = f"{fund_name}_NAV.csv"
                filepath = os.path.join(output_folder, filename)

                df.to_csv(filepath, index=False)

                print(f"✅ {filename} saved successfully")
            else:
                print(f"❌ No NAV data found for {fund_name}")

        else:
            print(f"❌ Failed to fetch {fund_name} (Status Code: {response.status_code})")

    except Exception as e:
        print(f"❌ Error fetching {fund_name}")
        print(e)

print("=" * 60)
print("Live NAV Download Completed!")