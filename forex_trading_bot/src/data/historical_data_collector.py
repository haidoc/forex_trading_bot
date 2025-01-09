import yfinance as yf
import pandas as pd
import os


def fetch_historical_data(symbol="EURUSD=X", start_date="2020-01-01", end_date="2025-01-01", interval="1d"):
    """
    Fetch historical data from Yahoo Finance.

    :param symbol: The symbol for the asset (EURUSD=X for EUR/USD forex pair)
    :param start_date: Start date for historical data
    :param end_date: End date for historical data
    :param interval: Interval for the data (1d, 1h, 1m, etc.)
    :return: DataFrame containing the historical data
    """
    try:
        print(f"Fetching historical data for {symbol} from {start_date} to {end_date} with {interval} interval.")
        df = yf.download(symbol, start=start_date, end=end_date, interval=interval)

        # Ensure the DataFrame has the required columns and set Date as index
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date is in datetime format
        df.set_index('Date', inplace=True)

        print(f"Data fetched successfully for {symbol}")
        print(df.head())  # Display the first few rows
        return df

    except Exception as e:
        print(f"Failed to fetch historical data for {symbol}. Error: {e}")
        return None


def save_to_csv(df, file_path="C:/Users/haida/PycharmProjects/forex_trading_bot/data/EURUSD.csv"):
    """
    Save the DataFrame to CSV.
    :param df: The DataFrame to save
    :param file_path: Path to save the CSV file
    """
    if df is not None:
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False)
        else:
            df.to_csv(file_path)
        print(f"Data saved to {file_path}")


def main():
    symbol = "EURUSD=X"  # EUR/USD forex pair symbol on Yahoo Finance
    start_date = "2020-01-01"
    end_date = "2025-01-01"
    interval = "1d"  # daily data

    # Fetch historical data from Yahoo Finance
    df = fetch_historical_data(symbol, start_date, end_date, interval)

    # Save the data to CSV
    save_to_csv(df)


if __name__ == "__main__":
    main()


