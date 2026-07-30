-- ===================================================
-- 1. Top 5 Funds by Highest NAV
-- ===================================================
SELECT amfi_code, MAX(nav) AS highest_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY highest_nav DESC
LIMIT 5;

-- ===================================================
-- 2. Average NAV Per Fund
-- ===================================================
SELECT amfi_code, ROUND(AVG(nav),2) AS average_nav
FROM nav_history
GROUP BY amfi_code;

-- ===================================================
-- 3. Monthly Average NAV
-- ===================================================
SELECT
strftime('%Y-%m',date) AS month,
ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- ===================================================
-- 4. Transaction Count by Type
-- ===================================================
SELECT transaction_type,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

-- ===================================================
-- 5. Total Amount Invested by Transaction Type
-- ===================================================
SELECT transaction_type,
ROUND(SUM(amount_inr),2) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;

-- ===================================================
-- 6. Transactions by State
-- ===================================================
SELECT state,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- ===================================================
-- 7. Funds with Expense Ratio below 1%
-- ===================================================
SELECT amfi_code,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- ===================================================
-- 8. Top Performing Funds (5-Year Return)
-- ===================================================
SELECT amfi_code,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- ===================================================
-- 9. Average Returns
-- ===================================================
SELECT
ROUND(AVG(return_1yr_pct),2) AS avg_1yr,
ROUND(AVG(return_3yr_pct),2) AS avg_3yr,
ROUND(AVG(return_5yr_pct),2) AS avg_5yr
FROM scheme_performance;

-- ===================================================
-- 10. Highest Single Transaction
-- ===================================================
SELECT *
FROM investor_transactions
ORDER BY amount_inr DESC
LIMIT 1;