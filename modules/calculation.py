import api

def calculate_trade(balance: float, ticker_symbol: str, buy_date: str, sell_date: str) -> float:
    '''
    Calculates new balance when buying and selling a certain stock on certain dates
    '''
    # Collect prices
    buy_price = api.get_last_price_from_date(ticker_symbol, buy_date, 1)[0][0]
    sell_price = api.get_last_price_from_date(ticker_symbol, sell_date, 1)[0][0]

    # Perform calculations
    total_positions = float(balance) / buy_price
    net_change = (sell_price / buy_price) * 100

    # Calculate and return new balance
    new_balance = (buy_price + (buy_price * net_change)) * total_positions
    return new_balance