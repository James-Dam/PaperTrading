import json
import os
import pandas as pd
import requests
import sqlalchemy as db

# Url of Financial Modeling Prep API
url = 'https://financialmodelingprep.com/stable/search-symbol?'

# API key
KEY = os.environ.get('FINANCIAL_MODELING_PREP_KEY')

# Test GET request of Financial Modeling Prep
params = {
  'query': 'AAPL',
  'apikey': KEY
}

response = requests.get(url, params=params)

# Turn json data into dict
data = response.json()
# Turn dict into DataFrame
data = pd.DataFrame.from_dict(data)

# Create engine object
engine = db.create_engine('sqlite:///stocks.db')
# Send SQLtable from data
dataframe_name.to_sql('stocks', con=engine, if_exists='replace', index=False)

# Print data and table
print(data)
with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM stocks;")).fetchall()
  print(pd.DataFrame(query_result))