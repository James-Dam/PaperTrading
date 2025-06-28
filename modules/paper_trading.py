import json
import os
import pandas as pd
import requests
import sqlalchemy as db

def run():
    # Get user input for stock ticker symbol
    user_symbol = input("Enter a ticker symbol: ")

    # Url of Financial Modeling Prep API
    url = f'https://financialmodelingprep.com/api/v3/stock/full/real-time-price/{user_symbol}?'

    # API key
    KEY = os.environ.get('FINANCIAL_MODELING_PREP_KEY')

    # Test GET request of Financial Modeling Prep
    params = {
    'apikey': KEY
    }

    response = requests.get(url, params=params)

    data = response.json()
    data = pd.DataFrame.from_dict(data)

    engine = db.create_engine('sqlite:///stocks.db')
    # Send SQLtable from data
    data.to_sql('stocks', con=engine, if_exists='replace', index=False)

    # Print data and table
    print(data)

    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT lastSalePrice FROM stocks;")).fetchall()
        print(pd.DataFrame(query_result))
