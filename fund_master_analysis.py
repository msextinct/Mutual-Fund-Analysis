import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 70)
print("FUND MASTER ANALYSIS")
print("=" * 70)

print("\nNumber of Schemes:", len(df))

# Unique Fund Houses
print("\nUnique Fund Houses")
print(df["fund_house"].unique())

# Categories
print("\nCategories")
print(df["category"].unique())

# Sub Categories
print("\nSub Categories")
print(df["sub_category"].unique())

# Risk Grades
print("\nRisk Categories")
print(df["risk_category"].unique())

# AMFI Code Summary
print("\nAMFI Code Summary")

print("Minimum Code :", df["amfi_code"].min())
print("Maximum Code :", df["amfi_code"].max())

print("\nFirst 10 AMFI Codes")
print(df["amfi_code"].head(10))

print("\nTotal Unique AMFI Codes")
print(df["amfi_code"].nunique())