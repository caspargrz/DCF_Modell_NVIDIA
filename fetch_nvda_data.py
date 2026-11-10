import pandas as pd
import yfinance as yf


def main():
    ticker_symbol = "NVDA"
    print(f"Ziehe Daten für {ticker_symbol} aus Yahoo Finance...")

    stock = yf.Ticker(ticker_symbol)

    financials = stock.financials
    cashflow = stock.cashflow
    balance_sheet = stock.balance_sheet

    if financials.empty or cashflow.empty or balance_sheet.empty:
        print(
            f"Fehler: Konnte keine Daten für {ticker_symbol} abrufen. Bitte"
            " überprüfe das Tickersymbol oder deine Internetverbindung."
        )
        return

    info = stock.info


    metrics_dict = {
        "Market Cap": info.get("marketCap"),
        "Enterprise Value": info.get("enterpriseValue"),
        "Trailing P/E": info.get("trailingPE"),
        "Forward P/E": info.get("forwardPE"),
        "PEG Ratio": info.get("pegRatio"),
        "Price/Sales": info.get("priceToSalesTrailing12Months"),
        "Price/Book": info.get("priceToBook"),
        "Enterprise Value/Revenue": info.get("enterpriseToRevenue"),
        "Enterprise Value/EBITDA": info.get("enterpriseToEbitda"),
        "Beta": info.get("beta"),
    }


    dcf_key_metrics = pd.DataFrame.from_dict(
        metrics_dict, orient="index", columns=["Value"]
    )

    output_filename = f"{ticker_symbol}_Raw_Data.xlsx"
    print(f"Exportiere Daten nach {output_filename}...")

    with pd.ExcelWriter(output_filename, engine="openpyxl") as writer:
        dcf_key_metrics.to_excel(writer, sheet_name="DCF_Key_Metrics")
        financials.to_excel(writer, sheet_name="Income_Statement")
        balance_sheet.to_excel(writer, sheet_name="Balance_Sheet")
        cashflow.to_excel(writer, sheet_name="Cashflow")

    print(
        f"Erfolgreich abgeschlossen! Datei '{output_filename}' wurde erstellt."
    )


if __name__ == "__main__":
    main()