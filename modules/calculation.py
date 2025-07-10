import api


def calculate_trade(balance: float, ticker_symbol: str, buy_date: str, sell_date: str) -> tuple:
    '''
    Calculates new balance when buying and selling a certain stock
    on certain dates
    '''
    # Convert balance from str to float
    balance = float(balance)

    # Collect prices
    buy_price = api.get_last_price_from_date(ticker_symbol, buy_date, 1)[0][0]
    sell_price = api.get_last_price_from_date(ticker_symbol, sell_date, 1)[0][0]

    # Perform calculations
    total_positions = balance / buy_price
    new_balance = total_positions * sell_price
    profit_loss = new_balance - balance
    net_change = ((new_balance - balance) / balance) * 100

    # Convert new balance and net change to rounded decimal places
    new_balance = float(f'{new_balance:.2f}')
    net_change = float(f'{net_change:.2f}')


    # Return new balance as well as net_change in profit/loss
    return (new_balance, net_change)
