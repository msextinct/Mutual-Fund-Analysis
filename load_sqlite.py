import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# Day 2 - Load Cleaned Data into SQLite
# ==========================================

DATABASE_NAME = "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DATABASE_NAME}")

print("=" * 80)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 80)

datasets = {
    "dim_fund": "data/processed/01_fund_master_cleaned.csv",
    "fact_nav": "data/processed/02_nav_history_cleaned.csv",
    "fact_aum": "data/processed/03_aum_by_fund_house_cleaned.csv",
    "monthly_sip_inflows": "data/processed/04_monthly_sip_inflows_cleaned.csv",
    "category_inflows": "data/processed/05_category_inflows_cleaned.csv",
    "industry_folio_count": "data/processed/06_industry_folio_count_cleaned.csv",
    "fact_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "fact_transactions": "data/processed/08_investor_transactions_cleaned.csv",
    "portfolio_holdings": "data/processed/09_portfolio_holdings_cleaned.csv",
    "benchmark_indices": "data/processed/10_benchmark_indices_cleaned.csv"
}

for table_name, file_path in datasets.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✓ Loaded {len(df)} rows")

print("\n" + "=" * 80)
print("VERIFYING ROW COUNTS")
print("=" * 80)

for table_name in datasets.keys():

    count = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM {table_name}",
        engine
    )

    print(f"{table_name:<25} {count.iloc[0,0]} rows")

print("\n" + "=" * 80)
print("SQLITE DATABASE CREATED SUCCESSFULLY")
print("=" * 80)