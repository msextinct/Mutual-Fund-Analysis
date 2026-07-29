import pandas as pd
import os

DATA_FOLDER = "data/raw"

# Get all CSV files
csv_files = sorted([file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")])

print("=" * 80)
print("DATA INGESTION STARTED")
print("=" * 80)

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 80)
    print(f"Dataset : {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(file_path)

        print("\nShape")
        print(df.shape)

   
        print("\nData Types")
        print(df.dtypes)

      
        print("\nFirst 5 Rows")
        print(df.head())

       
        print("\nMissing Values")
        print(df.isnull().sum())

       
        duplicate_rows = df.duplicated().sum()
        print("\nDuplicate Rows:", duplicate_rows)

 
        total_missing = df.isnull().sum().sum()

        print("\nData Quality Summary")
        print("-" * 40)

        if total_missing == 0:
            print("✓ No missing values found.")
        else:
            print(f"⚠ Missing values : {total_missing}")

        if duplicate_rows == 0:
            print("✓ No duplicate rows found.")
        else:
            print(f"⚠ Duplicate rows : {duplicate_rows}")

        
        print("\nNumeric Summary")
        print(df.describe())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\n" + "=" * 80)
print("ALL DATASETS LOADED SUCCESSFULLY")
print("=" * 80)