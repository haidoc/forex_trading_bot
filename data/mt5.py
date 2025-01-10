# import MetaTrader5 as mt5
#
# account = 52103207  # Your account number (integer)
# password = "1MsTz@B48J2LaB"  # Your password (string)
# server = "ICMarketsSC-Demo"  # Your broker's server (string)

import MetaTrader5 as mt5

# Initialize the MetaTrader5 connection
if not mt5.initialize():
    print("MetaTrader5 initialization failed")
    mt5.shutdown()
else:
    print("MetaTrader5 initialized successfully")

# Define order type using correct constant
order_type = mt5.ORDER_TYPE_BUY  # Correct way to reference buy order type

# Now, place an order (buy order)
symbol = "EURUSD"
lot_size = 1.0
price = mt5.symbol_info_tick(symbol).ask  # Getting current ask price
slippage = 10
stop_loss = price - 0.0010
take_profit = price + 0.0010

# Prepare the order request
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot_size,
    "type": order_type,
    "price": price,
    "slippage": slippage,
    "stoploss": stop_loss,
    "takeprofit": take_profit,
    "deviation": 20,
    "magic": 234000,
    "comment": "Test Buy Order",
    "type_filling": mt5.ORDER_FILLING_IOC,
    "type_time": mt5.ORDER_TIME_GTC
}

# Place a buy order
order_result = mt5.order_send(request)

# Check if the order was placed successfully
if order_result is not None:
    if order_result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"Order placed successfully: {order_result}")
    else:
        print(f"Failed to place order. Error code: {order_result.retcode}")
        print(f"Error details: {mt5.last_error()}")
else:
    print("Order send failed. Error: ", mt5.last_error())

# Shutdown MT5 connection
mt5.shutdown()