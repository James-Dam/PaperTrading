import api
import calculation


def run():
    '''
    Main Program
    '''
    # Print opening dialog
    print('Hello!, welcome to the PaperTrading app, please start by entering a balance')

    # Balance for calculating unrealized profits/losses
    balance = input('Enter starting balance: ')
    if int(balance) < 0:
        return "Balance cannot be below 0."
    if not balance.isnumeric():
        return "Please enter a number."

    # Boolean for while Loop
    statement = True

    # Loop until user enters 0 to quit
    print('Please pick one of the options below!')
    while (statement):
        print('Enter 0: Quit')
        print('Enter 1: View last stock price')
        print('Enter 2: View stock price at certain date')
        print('Enter 3: Lookup company')
        print('Enter 4: Calculate balance from buying & selling stocks')
        user_input = input()

        # If user enters 0, quit
        if user_input == '0':
            print('Goodbye!')
            break

        # Call API functions based on user input
        if user_input == '1':
            # Get user input for Ticker symbol
            ticker_symbol = input("Enter a ticker symbol: ")
            print(api.get_last_price(ticker_symbol))

        elif user_input == '2':
            # Get user input for ticker symbol
            ticker_symbol = input("Enter a ticker smybol: ")

            # Get user input for date
            date = input("Enter the date (YYYY-MM-DD) for which \
                         you wanted the price for: ")

            # Get user input for timeseries
            timeseries = input("Enter timespan from date (1 if just the date above): ")

            # Call and return price
            print(api.get_last_price_from_date(ticker_symbol, date, timeseries))

        elif user_input == '3':
            # Get user input for company
            company_name = input('Enter a company to find ticker symbol: ')
            print(api.company_lookup(company_name))

        # Call calculation function
        elif user_input == '4':
            # Get Ticker symbol
            ticker_symbol = input("Enter ticker symbol: ")

            # Get buying date
            buy_date = input("Enter buying date (YYYY-MM-DD): ")

            # Get selling date
            sell_date = input("Enter selling date (YYYY-MM-DD): ")

            balance = calculation.calculate_trade(balance, ticker_symbol,
                                                  buy_date, sell_date)

            print(f'You now have ${balance[0]} if you bought {ticker_symbol} at {buy_date} and sold at {sell_date}.')
            print(f'Your total net change in balance is {balance[1]}%.')

        # If no numbers listed are pressed, return message
        else:
            print('Please type one of the numbers listed above')
