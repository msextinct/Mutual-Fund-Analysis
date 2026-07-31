-- 1. Top 5 funds by AUM
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV by month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. Total SIP amount by year
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by state
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense ratio below 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Average 1-Year Return
SELECT AVG(return_1yr_pct) AS avg_return
FROM fact_performance;

-- 7. Top 10 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 8. Average Transaction Amount by Payment Mode
SELECT
    payment_mode,
    AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY payment_mode;

-- 9. Number of Investors by KYC Status
SELECT
    kyc_status,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Average NAV by AMFI Code
SELECT
    amfi_code,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;