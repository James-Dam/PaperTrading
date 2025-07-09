import unittest
import sys
import os

folder = os.path.abspath('/home/codio/workspace/modules')
sys.path.append(folder)

import api

# API key
_KEY = os.environ.get('FINANCIAL_MODELING_PREP_KEY')


class TestAPI(unittest.TestCase):
    STATEMENT = "Ticker Symbol not found."

    def test_get_last_price(self):
        self.assertNotEqual(api.get_last_price('aapl'), None)

    def test_get_last_price_with_wrong_ticker_symbol(self):
        self.assertEqual(api.get_last_price('hello world'), self.STATEMENT)
        self.assertEqual(api.get_last_price('-1'), self.STATEMENT)

    def test_get_last_price_from_date(self):
        self.assertEqual(api.get_last_price_from_date('aapl', '2025-01-01', 1)
                         [0][0], 250.42)

    def test_get_last_price_from_date_with_wrong_ticker_symbol(self):
        self.assertEqual(api.get_last_price_from_date('hello world',
                         '2025-01-01', 1), self.STATEMENT)

    def test_get_last_price_from_date_with_wrong_timeseries(self):
        self.assertEqual(api.get_last_price_from_date('aapl', '2025-01-01', -1)
                         , 'Timeseries must be greater than 0 or less \
                         than 10.')
        self.assertEqual(api.get_last_price_from_date('aapl', '2025-01-01'
                         , 11), 'Timeseries must be greater than 0 or less \
                         than 10.')

    def test_get_last_price_from_date_length(self):
        self.assertEqual(len(api.get_last_price_from_date('aapl', '2020-01-01'
                         , 10)), 10)
        self.assertEqual(len(api.get_last_price_from_date('aapl', '2020-01-01'
                         , 1)), 1)

    def test_company_lookup(self):
        self.assertEqual(api.company_lookup('roblox'), [('RBLX',
                         'Roblox Corporation')])


if __name__ == '__main__':
    unittest.main()
