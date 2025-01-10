import pandas as pd
import numpy as np


def add_indicators(df):
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)

    # RSI
    df['RSI'] = calculate_rsi(df['Close'], 14)

    # Bollinger Bands
    df['BB_Upper'], df['BB_Lower'] = calculate_bollinger_bands(df['Close'], 20)

    # ATR
    df['ATR'] = calculate_atr(df, 14)

    # MACD
    df['MACD'], df['MACD_Signal'] = calculate_macd(df['Close'])

    return df


def calculate_rsi(series, period):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def calculate_bollinger_bands(series, window):
    sma = series.rolling(window).mean()
    std = series.rolling(window).std()
    upper_band = sma + 2 * std
    lower_band = sma - 2 * std
    return upper_band, lower_band


def calculate_atr(df, period):
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def calculate_macd(series):
    fast_ema = series.ewm(span=12, adjust=False).mean()
    slow_ema = series.ewm(span=26, adjust=False).mean()
    macd = fast_ema - slow_ema
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal
