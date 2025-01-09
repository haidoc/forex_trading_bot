#
# import os
# import pandas as pd
#
# # Use the absolute file path to the CSV file
# file_path = "C:/Users/haida/PycharmProjects/forex_trading_bot/data/EURUSD.csv"
#
# # Print the current working directory for verification
# print("Current working directory:", os.getcwd())
#
# # Load the data
# try:
#     df = pd.read_csv(file_path)
#     print(f"Data successfully loaded from {file_path}")
#     print(df.head())  # Display the first few rows of the data
# except FileNotFoundError as e:
#     print(f"Error: {e}")

import pandas as pd


def load_data(file_path: str):
    """
    Load market data from a CSV file and standardize the columns for both Haidar and Ismail's formats.
    """
    # Load the data without parsing dates to inspect the content
    df = pd.read_csv(file_path)

    # Check the columns to determine which format the data is in
    print(f"Columns in DataFrame: {df.columns}")
    print(df.head())  # Inspect the first few rows of the data to check the structure

    # If Ismail's data (with extra columns), we need to clean it up
    if 'Tick_volume' in df.columns:
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # Keep only the relevant columns

    # Check if 'Date' is available, otherwise, it's problematic
    if 'Date' not in df.columns:
        raise ValueError("Missing 'Date' column in data")

    print(f"Data loaded successfully from {file_path}")
    return df

# Example usage:
df = load_data('C:/Users/haida/PycharmProjects/forex_trading_bot/data/EURUSD.csv')

