# Automated Multi-Ticker DCF Valuation Model

An automated Discounted Cash Flow (DCF) valuation pipeline combining a Python financial data ETL script (`yfinance`, `pandas`, `openpyxl`) with a dynamic Excel valuation model powered by **Power Query** and **`XLOOKUP`**.

Designed for institutional-style equity research, this workflow eliminates manual financial statement entry and enables instant multi-ticker valuation switching (e.g., NVDA, AAPL, TSLA) with standardized Wall Street financial modeling conventions.

---

## Output Preview

### Dynamic DCF Valuation Summary & WACC Build-Up
![DCF Valuation Overview](assets/dcf_valuation_overview.png)

### Historical Financials & FCFF Projection Schedule
![FCFF Model Schedule](assets/fcff_schedule.png)

---

## Key Features

- **Automated Financial Data ETL (Python):** Fetches historical Income Statement, Balance Sheet, Cash Flow Statement, and key market metrics (Share Price, Shares Outstanding, Beta, Market Cap) via `yfinance` and exports clean, structured data tables using `pandas` and `openpyxl`.
- **Zero-Touch Excel Integration (Power Query):** Connects the Excel workbook directly to the Python-generated raw data output, enabling one-click data refreshes without breaking cell references.
- **Dynamic Multi-Ticker Architecture (`XLOOKUP`):** Uses robust `XLOOKUP` formulas to dynamically map historical line items into the valuation engine across different tickers.
- **Full Intrinsic Valuation Engine:**
  - **Unlevered Free Cash Flow (FCFF)** build-up (EBIT, Taxes, D&A, CapEx, Changes in Net Working Capital)
  - **WACC Calculation** (CAPM Cost of Equity, After-Tax Cost of Debt, Capital Structure Weights)
  - **Terminal Value** estimation (Gordon Growth Model & Exit Multiple cross-check)
  - **Implied Share Price & Upside/Downside** bridge from Enterprise Value to Equity Value
- **Institutional Modeling Standards:** Follows clean financial modeling best practices (color-coded inputs vs. formulas, gridline removal, structured assumption blocks, and sensitivity checks).

---

## Tech Stack

- **Data Extraction & ETL:** Python 3.13+, `yfinance`, `pandas`, `openpyxl`
- **Financial Modeling & BI:** Microsoft Excel, Power Query (M), `XLOOKUP`

---

## Project Structure

```text
automated-dcf-valuation/
├── assets/                     # Screenshots of DCF model & valuation outputs
├── fetch_financials.py         # Python ETL script extracting yfinance statements
├── DCF_Valuation_Model.xlsx    # Master Excel DCF model with Power Query & XLOOKUP
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation


# 1. Clone repository & install dependencies
git clone [https://github.com/caspargrz/automated-dcf-valuation.git](https://github.com/caspargrz/automated-dcf-valuation.git)
cd automated-dcf-valuation
pip install yfinance pandas openpyxl

# 2. Extract raw financial data for target ticker(s)
python fetch_financials.py

# 3. Refresh Excel Valuation Model
# Open DCF_Valuation_Model.xlsx -> Data -> Refresh All (Strg + Alt + F5)