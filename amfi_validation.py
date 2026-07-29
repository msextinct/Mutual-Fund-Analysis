import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

# Unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("\nTotal AMFI codes in Fund Master :", len(master_codes))
print("Total AMFI codes in NAV History :", len(nav_codes))

# Find missing codes
missing_codes = master_codes - nav_codes

print("\nChecking validation...")

if len(missing_codes) == 0:
    print("SUCCESS: Every AMFI code in fund_master exists in nav_history.")
else:
    print(" Missing AMFI Codes:")
    print(sorted(missing_codes))

# Summary
print("\n" + "=" * 70)
print("DATA QUALITY SUMMARY")
print("=" * 70)

print(f"Fund Master Records : {len(fund_master)}")
print(f"NAV History Records : {len(nav_history)}")

print(f"Unique AMFI Codes : {len(master_codes)}")

print(f"Missing Codes : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\nOverall Status : PASS ")
else:
    print("\nOverall Status : FAILED ")