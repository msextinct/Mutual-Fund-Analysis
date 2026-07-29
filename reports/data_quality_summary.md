# Day 1 – Data Quality Summary

## Overview

A total of 10 CSV datasets were successfully loaded and explored using Python and Pandas.

## Dataset Summary

- Total datasets loaded: 10
- Fund Master records: 40
- NAV History records: 46,000
- Unique AMFI codes: 40

## Data Quality Checks

### Missing Values

- All datasets contain complete data except:
  - `04_monthly_sip_inflows.csv`
    - `yoy_growth_pct` has 12 missing values.

### Duplicate Records

- No duplicate rows were found in any dataset.

### AMFI Code Validation

- Every AMFI code in `fund_master.csv` exists in `nav_history.csv`.
- Validation Status: PASS

## Conclusion

The datasets are suitable for further analysis. Only minor missing values were found in the Year-over-Year Growth column of the monthly SIP inflows dataset. No duplicate records or missing AMFI mappings were detected.
