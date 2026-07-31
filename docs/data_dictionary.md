# Data Dictionary

## 1. fund_master

| Column        | Data Type | Description                    |
| ------------- | --------- | ------------------------------ |
| amfi_code     | Integer   | Unique AMFI scheme code        |
| scheme_name   | Text      | Name of the mutual fund scheme |
| fund_house    | Text      | Mutual fund company            |
| category      | Text      | Fund category                  |
| sub_category  | Text      | Fund sub-category              |
| risk_category | Text      | Risk level                     |

---

## 2. nav_history

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | Integer   | AMFI scheme code |
| date      | Date      | NAV date         |
| nav       | Decimal   | Net Asset Value  |

---

## 3. aum_by_fund_house

| Column         | Data Type | Description              |
| -------------- | --------- | ------------------------ |
| date           | Date      | Reporting date           |
| fund_house     | Text      | Asset Management Company |
| aum_lakh_crore | Decimal   | AUM in lakh crore        |
| aum_crore      | Decimal   | AUM in crore             |
| num_schemes    | Integer   | Number of schemes        |

---

## 4. investor_transactions

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Investor identifier        |
| transaction_date   | Date      | Date of transaction        |
| amfi_code          | Integer   | Fund scheme code           |
| transaction_type   | Text      | SIP, Lumpsum or Redemption |
| amount_inr         | Decimal   | Transaction amount         |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | City classification        |
| age_group          | Text      | Investor age group         |
| gender             | Text      | Gender                     |
| annual_income_lakh | Decimal   | Annual income              |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |

---

## Source

All datasets were provided as part of the Mutual Fund Analytics Capstone Project and cleaned using Python (Pandas). SQLite was used for database storage and SQL analysis.
