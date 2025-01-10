import pandas as pd

def generate_signals(df):
    df["Buy_Signal"] = (df["RSI"] < 40) & (df["MACD"] > df["MACD_Signal"]) & (df["Close"] < df["BB_Lower"])
    df["Sell_Signal"] = (df["RSI"] > 60) & (df["MACD"] < df["MACD_Signal"]) & (df["Close"] > df["BB_Upper"])
    return df

# Debugging block (use this only when running the script standalone)
if __name__ == "__main__":
    try:
        # Load sample data for testing
        file_path = "C:/Users/haida/PycharmProjects/forex_trading_bot/data/EURUSD.csv"
        df = pd.read_csv(file_path)

        # Assuming `add_indicators` is defined in `indicators_setup.py`
        from src.indicators.indicators_setup import add_indicators

        df = add_indicators(df)
        df = generate_signals(df)

        # Print debug output for the last 10 rows
        print(df[["RSI", "MACD", "MACD_Signal", "BB_Upper", "BB_Lower", "Buy_Signal", "Sell_Signal"]].tail(10))

    except Exception as e:
        print(f"Error: {e}")
















































