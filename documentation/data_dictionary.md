# Mutual Fund Analytics Data Dictionary

## 1. nav_history

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## 2. investor_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | INTEGER | Transaction ID |
| investor_id | INTEGER | Investor ID |
| amfi_code | INTEGER | Mutual Fund Scheme Code |
| transaction_date | DATE | Date of Transaction |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Investment Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| investor_age | INTEGER | Investor Age |
| gender | TEXT | Investor Gender |
| investment_mode | TEXT | Online / Offline |
| kyc_status | TEXT | Verified / Pending / Rejected |
| advisor_code | TEXT | Advisor Identifier |

---

## 3. scheme_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Mutual Fund Scheme Code |
| return_1yr_pct | REAL | One-Year Return (%) |
| return_3yr_pct | REAL | Three-Year Return (%) |
| return_5yr_pct | REAL | Five-Year Return (%) |
| sharpe_ratio | REAL | Risk-adjusted Return |
| alpha | REAL | Excess Return |
| beta | REAL | Volatility Measure |
| expense_ratio_pct | REAL | Expense Ratio (%) |