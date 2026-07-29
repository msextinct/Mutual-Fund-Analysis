import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# ---------------------------------------------
# Required Mutual Fund Scheme Codes
# ---------------------------------------------

schemes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 70)
print("LIVE NAV FETCH STARTED")
print("=" * 70)

for scheme_name, scheme_code in schemes.items():

    print(f"\nFetching {scheme_name} ({scheme_code})...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            # Basic Scheme Information
            meta = data.get("meta", {})

            print("Scheme Name :", meta.get("scheme_name"))
            print("Fund House  :", meta.get("fund_house"))
            print("Scheme Code :", scheme_code)

            # NAV History
            nav_history = pd.DataFrame(data["data"])

            filename = f"data/raw/{scheme_name}_NAV.csv"

            nav_history.to_csv(filename, index=False)

            print(f"Saved -> {filename}")

        else:

            print(f"Failed ({response.status_code})")

    except Exception as e:

        print("Error:", e)

print("\n" + "=" * 70)
print("ALL LIVE NAV FILES SAVED")
print("=" * 70)