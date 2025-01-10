def backtest(data):
    initial_balance = 10000
    balance = initial_balance
    position = None

    for index, row in data.iterrows():
        if row["Buy_Signal"] and position is None:
            position = row["Close"]
            print(f"Buy at {position:.2f}")
        elif row["Sell_Signal"] and position is not None:
            profit = row["Close"] - position
            balance += profit
            print(f"Sell at {row['Close']:.2f}")
            position = None

    return balance








































