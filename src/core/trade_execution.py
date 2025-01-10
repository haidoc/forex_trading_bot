# trade_execution.py

import pandas as pd


def execute_trade(df, account_balance, risk_per_trade=0.02):
    # Calculate Position Size
    atr = df['ATR'].iloc[-1]
    position_size = (account_balance * risk_per_trade) / atr

    # Dummy Trade Execution
    print(f"Executing Trade - Position Size: {position_size}")

    # Deduct Fees
    account_balance -= 10  # Dummy fee

    return account_balance
