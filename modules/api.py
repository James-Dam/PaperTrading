import json
import os
import pandas as pd
import requests
import sqlalchemy as db

# Create engine for database
engine = db.create_engine('sqlite:///stocks.db')

# API key
_KEY = os.environ.get('FINANCIAL_MODELING_PREP_KEY')


def get_last_price(ticker_symbol: str) -> int:
    '''
    Given a ticker symbol, find current price. If ticker symbol not found, return error message.
    '''
    # Url of Financial Modeling Prep API
    url = f'https://financialmodelingprep.com/api/v3/stock/full/real-time-price/{ticker_symbol}?'

    # Test GET request of Financial Modeling Prep
    params = {
    'apikey': _KEY
    }

    response = requests.get(url, params=params)

    # Error handling
    try: 
        # Turn data into json format and convert to DataFrame
        data = response.json()
        data = pd.DataFrame.from_dict(data)
        
        # Send SQLtable from data
        data.to_sql('real_time_prices', con=engine, if_exists='replace', index=False)

        # Print data and table
        print(data)

        with engine.connect() as connection:
            query_result = connection.execute(db.text("SELECT lastSalePrice FROM real_time_prices;")).fetchall()
            print(pd.DataFrame(query_result))

        return query_result[0][0]

    except Exception:
        return "Ticker Symbol not found."


def get_last_price_from_date(ticker_symbol: str, date: str, timeseries: int) -> int:
    '''
    Given a ticker symbol, date, and timeseries, return historical data. If ticker symbol not found, return error message.
    '''
    # Check if timeseries > 0
    if int(timeseries) < 1:
        return "Timeseries must be greater than 0"

    # Url of Financial Modeling Prep API
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker_symbol}?'

    # Test GET request of Financial Modeling Prep
    params = {
    'apikey': _KEY,
    'to': date,
    'timeseries': timeseries
    }

    response = requests.get(url, params=params)

    # Error handling
    try:
        # Turn data into json format and convert to DataFrame
        data = response.json()
        data = pd.DataFrame.from_dict(data['historical'])

        # Send SQLtable from data
        data.to_sql('price_from_date', con=engine, if_exists='replace', index=False)

        # Print data and table
        print(data)

        with engine.connect() as connection:
            query_result = connection.execute(db.text("SELECT close FROM price_from_date;")).fetchall()
            print(pd.DataFrame(query_result))
        
        return query_result
    
    except Exception:
        return "Ticker Symbol not found."


def company_lookup(name: str) -> list:
    '''
    Given a company look, look up and return list of results to user
    '''
    # Url of Financial Modeling Prep API
    url = f'https://financialmodelingprep.com/stable/search-name?'

    # Test GET request of Financial Modeling Prep
    params = {
    'apikey': _KEY,
    'query': name,
    'limit': 10
    }

    response = requests.get(url, params=params)

    # Error handling
    try:
        # Turn data into json format and convert to DataFrame
        data = response.json()
        data = pd.DataFrame.from_dict(data)

        # Send SQLtable from data
        data.to_sql('company_info', con=engine, if_exists='replace', index=False)

        # Print data and table
        print(data)

        with engine.connect() as connection:
            query_result = connection.execute(db.text("SELECT symbol, name FROM company_info;")).fetchall()
            print(pd.DataFrame(query_result))
        
        return query_result
    
    except Exception:
        return "No such company found."

    