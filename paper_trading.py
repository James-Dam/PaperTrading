import json
import os
import requests

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

data = response.json()
print(data)