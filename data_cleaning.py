import pandas as pd
import os

# ======================================================
# Day 2 - Data Cleaning
# ======================================================

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

print("=" * 80)
print("DAY 2 - DATA CLEANING STARTED")
print("=" * 80)

# ------------------------------------------------------
# 1. NAV HISTORY
# ------------------------------------------------------

print("\nCleaning nav_history.csv...")

nav = pd.read_csv(f"{RAW_FOLDER}/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

# Sort
nav = nav.sort_values(["amfi_code", "date"])

# Forward fill NAV for each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
nav = nav.drop_duplicates()

# Keep only valid NAV
nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED_FOLDER}/02_nav_history_cleaned.csv",
    index=False
)

print("✓ NAV History cleaned")

# ------------------------------------------------------
# 2. INVESTOR TRANSACTIONS
# ------------------------------------------------------

print("\nCleaning investor_transactions.csv...")

txn = pd.read_csv(f"{RAW_FOLDER}/08_investor_transactions.csv")

# Standardize transaction types
txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

txn["transaction_type"] = txn["transaction_type"].replace(mapping)

# Convert dates
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

# Keep positive amounts
txn = txn[txn["amount_inr"] > 0]

# Valid KYC values
valid_kyc = ["Verified", "Pending", "Rejected"]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn = txn.drop_duplicates()

txn.to_csv(
    f"{PROCESSED_FOLDER}/08_investor_transactions_cleaned.csv",
    index=False
)

print("✓ Investor Transactions cleaned")

# ------------------------------------------------------
# 3. SCHEME PERFORMANCE
# ------------------------------------------------------

print("\nCleaning scheme_performance.csv...")

perf = pd.read_csv(f"{RAW_FOLDER}/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

expense = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

perf = perf[
    (expense >= 0.1) &
    (expense <= 2.5)
]

perf = perf.drop_duplicates()

perf.to_csv(
    f"{PROCESSED_FOLDER}/07_scheme_performance_cleaned.csv",
    index=False
)

print("✓ Scheme Performance cleaned")

# ------------------------------------------------------
# 4. Copy Remaining Datasets
# ------------------------------------------------------

remaining = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in remaining:

    df = pd.read_csv(f"{RAW_FOLDER}/{file}")

    df = df.drop_duplicates()

    output = file.replace(".csv", "_cleaned.csv")

    df.to_csv(
        f"{PROCESSED_FOLDER}/{output}",
        index=False
    )

print("\n✓ Remaining datasets cleaned")

print("\n" + "=" * 80)
print("ALL DATASETS CLEANED SUCCESSFULLY")
print("=" * 80)